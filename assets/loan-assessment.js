/* AI Car Loan Application Assessment, Phase 1 (static, no backend).
   Spec: Fina audit rulebook v1.0 (22 Oct 2026). Pre-screen only, never an approval. */
(function(){
'use strict';
/* =====================================================================
   CONFIG: ALL THRESHOLDS ARE ASSUMPTIONS PENDING BANK CONFIRMATION.
   [V] = verified in rulebook §2.2 research, [U] = UNVERIFIED (rulebook §9).
   Edit here only; nothing else in this file hard-codes a threshold.
   ===================================================================== */
var CFG={
  ASSUMPTIONS_PENDING_BANK_CONFIRMATION:true,
  version:'rulebook-1.0/phase1',
  consent_version:'dpa-consent-draft-2026-10-22',
  aff:{pass:0.30,review:0.35},              // AFF-01 [V for RCBC 30%; review band U]
  dti:{pass:0.40,review:0.50},              // DTI-01 [U]
  income_min_household:30000,               // INC-01 lowest bank min (BPI/PSBank) [V]
  bank_min_income:{BPI:30000,PSBank:30000,Metrobank:40000,'Security Bank':40000,EastWest:40000,BDO:50000}, // [V]
  metrobank_min_loan:350000,                // LOAN-01 [V]
  age:{min:18,pass_min:21,pass_max:60,max_at_maturity:65},  // AGE-01 [U]
  ten_employed:{pass_regular_yrs:2,pass_permanent_yrs:1,fail_below_yrs:0.5}, // TEN-01 [U general, V RCBC]
  ten_business:{pass_yrs:3,review_profitable_yrs:2},        // TEN-02 [V]
  ten_freelancer:{pass_yrs:2,fail_below_yrs:1},             // [U] not in rulebook, dealer assumption
  dp:{pass_pct:20,review_pct:15},           // DP-01 [V]; dealer promo DP accepted as pass (rulebook "unless promo DP")
  promo_dp_passes:true,
  rf07_min_stay_rented_yrs:0.5,             // RF-07 [U]
  max_term:60,                              // [V BPI/Metrobank]
  promo_term_months:60,                     // promo table term [U for Destinator/L300]
  /* ESTIMATED bank add-on rates (whole-term, standard/in-arrears, brand-new, private use), PENDING CONFIRMATION.
     Median of BPI, Metrobank, PSBank, RCBC, Security Bank, EastWest public rate pages (Oct 2026); see /workspace/loanapp/rates_research.md.
     Monthly = amount_financed x (1 + addon[term]) / months. Excludes insurance, chattel mortgage, LTO and fees (dealer all-in promos include them).
     Not shown to clients as rates (rulebook §0/§2.1): only used for labelled estimates. */
  est_addon_rates:{12:0.0552,24:0.1144,36:0.1737,48:0.2413,60:0.3026},
  est_rates_status:'ESTIMATE - pending bank/dealer confirmation',
  calc_min_dp_pct:20, calc_max_dp_pct:80,   // banks' usual min DP 20% [V BPI 15%/Metrobank 20%]; max for slider
  fit_max_ratio:0.35                        // "fits income" = monthly <= 35% of income (AFF-01 review ceiling)
};
/* Messenger: ONE config value. Page username per Mark.
   Fallback (page ID): 'https://m.me/504759566043148' */
var MESSENGER_URL='https://m.me/MitsubishiRDC';
var CALL_TEL='tel:09542911201';
/* Crisp live chat (Fina + Richard). Loaded only after Data Privacy consent. Page-only embed. */
var CRISP_WEBSITE_ID='ca443e7b-7d1e-4819-87d3-59b97b4fa8c8';
function crispLoad(){if(window.__crispLoaded)return;window.__crispLoaded=true;window.$crisp=window.$crisp||[];window.CRISP_WEBSITE_ID=CRISP_WEBSITE_ID;
  var d=document.createElement('script');d.src='https://client.crisp.chat/l.js';d.async=1;document.head.appendChild(d)}
function cp(){try{window.$crisp=window.$crisp||[];window.$crisp.push([].slice.call(arguments))}catch(_){}}
var BANNED=/\b(approved|aprobado|sure na|guaranteed|suzuki)\b/ig;
function safe(s){return String(s).replace(BANNED,'pre-qualified')}   // §2.4 banned-word filter

var $=function(i){return document.getElementById(i)};
var U=JSON.parse($('la-units').textContent);
function crispSync(){if(!window.__crispLoaded)return;
  cp('set','user:nickname',[A.name]);if(A.mobile)cp('set','user:phone',[A.mobile]);if(A.email)cp('set','user:email',[A.email]);
  var d=[['language',A.lang],['source','loan-assessment']];if(A.leadId)d.push(['lead_id',A.leadId]);
  if(A.assessment){d.push(['result',A.assessment.result])}if(A.unit)d.push(['unit',A.unit.n]);
  if(A.rec)d.push(['recommended',A.rec.primary.label+' | '+Math.round(A.rec.primary.mo)+'/mo']);if(A.dp_capacity)d.push(['dp_capacity',String(A.dp_capacity==='custom'?A.dp_custom:A.dp_capacity)]);if(A.preferred_term)d.push(['preferred_term',String(A.preferred_term)]);if(A.target_monthly)d.push(['target_monthly',String(A.target_monthly==='custom'?A.target_custom:A.target_monthly)]);
  if(A.plan)d.push(['plan',A.plan.type+' | DP '+A.plan.dp+' ('+A.plan.dp_pct+'%) | '+A.plan.term_months+' mo | '+A.plan.monthly+'/mo']);
  if(A.docs){d.push(['docs_ready',A.docs.ready]);d.push(['docs_lacking',A.docs.lacking]);d.push(['missing_items',A.docs.missing.join('; ').slice(0,500)])}
  if(A.employment_type)d.push(['employment_type',A.employment_type]);if(A.length_of_stay_months!=null)d.push(['residence_months',String(A.length_of_stay_months)]);if(A.years_in_employment!=null)d.push(['job_tenure_years',String(A.years_in_employment)]);
  cp('set','session:data',[d]);var sg=['loan_assessment','loan-assessment'];if(A.assessment)sg.push(A.assessment.result.toLowerCase().replace(/_/g,'-'));cp('set','session:segments',[sg])}
function finaMsg(){var u=A.unit,x=A.assessment,L={PRE_QUALIFIED:'Pre-qualified',NEEDS_REVIEW:'Needs Review',NOT_YET_QUALIFIED:'Not yet qualified'};
  var parts=[T('Hi Fina! Ako si ','Hi Fina! I am ')+A.name+'.'];
  if(u)parts.push('Unit: '+u.n+'.');if(x)parts.push(T('Resulta ng assessment: ','Assessment result: ')+L[x.result]+'.');
  if(!A.plan&&A.rec)parts.push(T('Rekomendado: ','Recommended: ')+A.rec.primary.label+', ~'+peso(A.rec.primary.mo)+'/mo.');
  if(A.plan)parts.push(T('Napiling plan: ','Chosen plan: ')+(A.plan.type==='promo'?'promo':'custom')+', DP '+peso(A.plan.dp)+', '+A.plan.term_months+' mo, ~'+peso(A.plan.monthly)+'/mo.');
  if(A.docs)parts.push('Documents: '+A.docs.ready+' ready / '+A.docs.lacking+T(' kulang',' lacking')+(A.docs.missing.length?' ('+A.docs.missing.join(', ')+').':'.'));
  parts.push(T('Pwede mo ba akong tulungan sa requirements?','Can you help me with the requirements?'));if(A.leadId)parts.push('Ref: '+A.leadId);return parts.join(' ')}
function finaGreet(){var m=A.docs&&A.docs.missing.length?A.docs.missing.join(', '):'';
  return m?T('Hi '+A.name+'! Ako si Fina. Nakita ko na ang assessment mo at kulang pa ang: '+m+'. May tanong ka ba bago tayo tumuloy sa official application?','Hi '+A.name+'! I\'m Fina. I\'ve seen your assessment and you still need: '+m+'. Any questions before we proceed to the official application?')
   :T('Hi '+A.name+'! Ako si Fina. Nakita ko na ang assessment mo at kumpleto ka na sa documents. May tanong ka ba bago tayo tumuloy sa official application?','Hi '+A.name+'! I\'m Fina. I\'ve seen your assessment and your documents are complete. Any questions before we proceed to the official application?')}
function openFina(){crispLoad();crispSync();cp('do','chat:open');var g=finaGreet();if(A.finaShown!==g){A.finaShown=g;cp('do','message:show',['text',safe(g)])}
  ga('chat_open',{provider:'crisp'})}
function finaBtn(){return '<button type="button" class="btn la-fina" data-fina="1">💬 '+T('Magtanong pa sa aming live chat','Ask more questions to our live chat')+'</button>'}
function T(t,e){return A.lang==='en'?e:t}
var A={lang:'tl'},log=$('la-log'),started=false,stepN=1;
function peso(n){return '₱'+Math.round(n).toLocaleString('en-PH')}
function esc(s){return String(s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
/* Meta Pixel: NO credit/income/assessment-result fields in payloads (Meta restricted-data policy). Only unit name / contact method / Phase-2 ref. */
function px(ev,p){try{if(typeof window.fbq==='function'){if(ev==='StartAssessment'||ev==='SubmitApplication')window.fbq('trackCustom',ev,p||{});else window.fbq('track',ev,p||{})}}catch(_){}}
function ga(ev,p){try{if(typeof window.gtag==='function')window.gtag('event',ev,p||{})}catch(_){}}
/* Phase 2 stub: call after the backend returns an MP-XXXXX ref. Not fired in Phase 1. */
window.LoanApp={submitApplication:function(ref){if(!/^MP-[A-HJKMNP-Z2-9]{5}$/i.test(ref))return false;px('SubmitApplication',{ref_no:ref.toUpperCase()});ga('submit_application',{ref_no:ref.toUpperCase()});return true},CFG:CFG};

function prog(n){stepN=n;document.querySelectorAll('.la-steps li').forEach(function(li,i){li.className=i<n-1?'done':i===n-1?'on':'';li.querySelector('.n').textContent=i<n-1?'✓':String(i+1);if(i===n-1)li.setAttribute('aria-current','step');else li.removeAttribute('aria-current')})}
function bot(html){var d=document.createElement('div');d.className='la-b bot';d.innerHTML='<span class="la-av" aria-hidden="true">R</span><div class="la-bu">'+html+'</div>';log.appendChild(d);return d}
function me(t){var d=document.createElement('div');d.className='la-b me';d.innerHTML='<div class="la-bu">'+esc(t)+'</div>';log.appendChild(d);return d}
function scroll(el){setTimeout(function(){el.scrollIntoView({behavior:'smooth',block:'end'})},40)}

/* ---------- Step 1: contact + consent ---------- */
function setLang(l){A.lang=l;document.documentElement.setAttribute('data-lang',l);try{localStorage.setItem('la_lang',l)}catch(_){}}
try{var sl=localStorage.getItem('la_lang');if(sl==='en'||sl==='tl')setLang(sl)}catch(_){}
document.querySelectorAll('[data-setlang]').forEach(function(b){b.addEventListener('click',function(){setLang(b.dataset.setlang)})});
document.querySelectorAll('[data-start]').forEach(function(btn){btn.addEventListener('click',function(){setLang(btn.dataset.start);
  $('la-intro').hidden=true;$('la-s1').hidden=false;prog(1);
  if(!started){started=true;px('StartAssessment',{});ga('start_assessment',{})}
  $('la-name').focus();
})});
$('la-f1').addEventListener('submit',function(ev){ev.preventDefault();
  var nm=$('la-name').value.trim(),mob=$('la-mobile').value.replace(/[\s()-]/g,''),em=$('la-email').value.trim();
  var bad=[Lead.err('la-name',nm.length<2),Lead.err('la-mobile',!/^(09\d{9}|\+639\d{9})$/.test(mob)),Lead.err('la-email',!!em&&!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(em)),Lead.err('la-consent',!$('la-consent').checked)];
  if(bad.some(Boolean))return;
  A.name=nm;A.mobile=mob;A.email=em;A.privacy_consent={accepted:true,timestamp:new Date().toISOString(),version:CFG.consent_version};
  $('la-s1').hidden=true;$('la-chat').hidden=false;prog(2);crispLoad();crispSync();
  bot(T('Salamat, <b>'+esc(nm.split(' ')[0])+'</b>! Ilang tanong lang tungkol sa income at trabaho mo. Mga 2 minuto lang ito.','Thanks, <b>'+esc(nm.split(' ')[0])+'</b>! Just a few questions about your income and work. This takes about 2 minutes.'));
  next(0);
});

/* ---------- Step 2/3: question engine (rulebook §1 order, scoring subset) ---------- */
var EMP=[['employed','Employed'],['business_owner','Business owner'],['ofw','OFW'],['seafarer','Seafarer'],['freelancer','Freelancer / VA'],['pensioner','Pensioner'],['other','Iba pa','Other']];
function isOFW(){return A.employment_type==='ofw'||A.employment_type==='seafarer'}
var Q=[
 {id:'purpose',q:['Para saan gagamitin ang sasakyan?','What will you use the vehicle for?'],t:'c',o:[['personal','Personal / family','Personal / family'],['business','Business','Business'],['tnvs','Grab / TNVS','Grab / TNVS'],['other','Iba pa','Other']]},
 {id:'dob',q:['Kailan ang birthday mo?','What is your date of birth?'],t:'date'},
 {id:'civil_status',q:['Civil status?','Civil status?'],t:'c',o:[['single','Single','Single'],['married','Married','Married'],['widowed','Widowed','Widowed'],['separated','Separated','Separated']]},
 {id:'residential_status',q:['Owned, rented, o nakatira sa family ang bahay?','Is your home owned, rented, or with family?'],t:'c',o:[['owned','Owned','Owned'],['mortgaged','Mortgaged / hinuhulugan','Mortgaged'],['rented','Rented','Rented'],['living_with_relatives','Kasama ang family','Living with family'],['company_provided','Company-provided','Company-provided']]},
 {id:'length_of_stay_years',q:['Gaano ka na katagal nakatira diyan?','How long have you lived there?'],t:'ym'},
 {id:'employment_type',q:['Ano ang source of income mo?','What is your source of income?'],t:'c',o:EMP},
 {id:'years_in_employment',q:function(){return A.employment_type==='business_owner'?T('Gaano na katagal ang negosyo mo?','How long have you had your business?'):isOFW()?T('Gaano ka na katagal nagtatrabaho abroad / sa barko?','How long have you worked abroad / at sea?'):T('Gaano ka na katagal sa trabaho mo ngayon?','How long have you been at your current job?')},t:'ym',show:function(){return A.employment_type!=='pensioner'}},
 {id:'employment_status',q:['Permanent, probationary, o contractual ka?','Are you permanent, probationary, or contractual?'],t:'c',o:[['permanent','Permanent / regular','Permanent / regular'],['probationary','Probationary','Probationary'],['contractual','Contractual','Contractual']],show:function(){return A.employment_type==='employed'}},
 {id:'biz_profitable',q:['Kumikita (profitable) ba ang negosyo sa huling 2 taon, may ITR o FS?','Has the business been profitable for the last 2 years, with ITR or FS?'],t:'c',o:[['yes','Oo','Yes'],['no','Hindi pa / walang ITR','Not yet / no ITR']],show:function(){return A.employment_type==='business_owner'}},
 {id:'ofw_contract',q:['May active contract ka ba ngayon?','Do you have an active contract now?'],t:'c',o:[['yes','Oo'],['no','Wala pa']],show:isOFW},
 {id:'ofw_remit',q:['May 3–6 months remittance proof ka ba?','Do you have 3–6 months of remittance proof?'],t:'c',o:[['yes','Oo'],['no','Wala pa']],show:isOFW},
 {id:'ofw_aif',q:['May magiging attorney-in-fact (AIF) ka ba dito sa PH, na pwedeng pirmahan ng SPA?','Do you have an attorney-in-fact (AIF) in the PH who can be named in an SPA?'],t:'c',o:[['yes','Oo, meron','Yes'],['maybe','Hahanap pa','Still looking'],['no','Wala talaga','No']],show:isOFW},
 {id:'gross_monthly_income',q:['Magkano ang gross monthly income mo? (₱)','What is your gross monthly income? (₱)'],t:'n',min:0,max:100000000,step:500},
 {id:'other_household_income',q:['May iba pang income sa household (hal. spouse)? Magkano kada buwan? Ilagay ang 0 kung wala.','Any other household income (e.g. spouse)? How much per month? Enter 0 if none.'],t:'n',min:0,max:100000000,step:500},
 {id:'existing_monthly_obligations',q:['May binabayaran ka bang loans ngayon (housing, car, personal, credit card minimum)? Magkano lahat kada buwan? 0 kung wala.','Are you paying any loans now (housing, car, personal, credit card minimum)? Total per month? 0 if none.'],t:'n',min:0,max:100000000,step:500},
 {id:'co_borrower',q:['May co-borrower o co-maker ka ba? (hal. spouse o kamag-anak na may income)','Do you have a co-borrower or co-maker? (e.g. spouse or relative with income)'],t:'c',o:[['yes','Oo, meron','Yes'],['no','Wala','No']]},
 {id:'co_income',q:['Magkano ang gross monthly income ng co-maker? (₱)','What is the co-maker\'s gross monthly income? (₱)'],t:'n',min:0,max:100000000,step:500,show:function(){return A.co_borrower==='yes'}},
 {id:'registered_owner',q:['Kanino ipapangalan ang unit?','Whose name will the unit be registered under?'],t:'c',o:[['self','Sa akin','Mine'],['other','Sa ibang tao','Someone else']]},
 {id:'preferred_bank',q:['May preferred bank ka ba?','Do you have a preferred bank?'],t:'c',o:[['no_preference','Wala, kayo na bahala','No preference'],['MMPF','Mitsubishi Motors Finance PH'],['BPI','BPI'],['BDO','BDO'],['Metrobank','Metrobank'],['Security Bank','Security Bank'],['PSBank','PSBank'],['RCBC','RCBC'],['EastWest','EastWest']]},
 {id:'dp_capacity',q:['Magkano ang kaya mong ilabas na DP (down payment)?','How much down payment (DP) can you put up?'],t:'c',o:[['zero','Zero DP','Zero DP'],['upto100k','Hanggang ₱100K','Up to ₱100K'],['100k_250k','₱100K–₱250K','₱100K–₱250K'],['250k_500k','₱250K–₱500K','₱250K–₱500K'],['40pct','40% o higit pa ng presyo','40% or more of the price'],['custom','Ilalagay ko ang eksaktong halaga','I\'ll type the exact amount']]},
 {id:'dp_custom',q:['Magkano ang DP na kaya mo? (₱)','How much DP can you put up? (₱)'],t:'n',min:0,max:100000000,step:1000,show:function(){return A.dp_capacity==='custom'}},
 {id:'preferred_term',q:['Ilang taon mo gustong bayaran?','How many years do you want to pay?'],t:'c',sub:1,o:[[12,'1 taon · 12 buwan','1 yr · 12 mo'],[24,'2 taon · 24 buwan','2 yrs · 24 mo'],[36,'3 taon · 36 buwan','3 yrs · 36 mo'],[48,'4 taon · 48 buwan','4 yrs · 48 mo'],[60,'5 taon · 60 buwan','5 yrs · 60 mo'],['unsure','Hindi pa sigurado','Not sure yet']]},
 {id:'target_monthly',q:['May target ka bang monthly?','Do you have a target monthly payment?'],t:'c',o:[['lt15k','Hanggang ₱15K','Up to ₱15K'],['15k_25k','₱15K–₱25K','₱15K–₱25K'],['25k_35k','₱25K–₱35K','₱25K–₱35K'],['35k_up','₱35K pataas','₱35K and up'],['custom','Ilalagay ko ang halaga','I\'ll type an amount'],['none','Wala','None']]},
 {id:'target_custom',q:['Magkano ang target monthly mo? (₱)','What is your target monthly? (₱)'],t:'n',min:1000,max:10000000,step:500,show:function(){return A.target_monthly==='custom'}},
 {id:'source_of_sale',q:['Last na: paano mo kami nahanap?','Last one: how did you find us?'],t:'c',o:[['facebook','Facebook','Facebook'],['google','Google','Google'],['referral','Referral','Referral'],['walk_in','Walk-in','Walk-in'],['other','Iba pa','Other']]}
];
/* Unit/plan steps join the same linear flow so Back/Edit work everywhere */
function modelsList(){var m=[];U.forEach(function(u){if(m.indexOf(u.model)<0)m.push(u.model)});return m}
Q.push(
 {id:'_model',unit:true,q:['Ayos! Ngayon, piliin natin ang unit. Ang DP at monthly ay galing sa promo ngayong buwan. Anong Mitsubishi model ang gusto mo?','Great! Now let\'s pick your unit. DP and monthly figures are from this month\'s promo. Which Mitsubishi model do you want?'],t:'c',o:function(){return modelsList().map(function(m){return [m,m]})}},
 {id:'_variant',unit:true,q:['Anong variant?','Which variant?'],t:'c',o:function(){return U.filter(function(u){return u.model===A._model}).map(function(u){return [u.id,u.n+' · SRP '+peso(u.price)]})}},
 {id:'_color',unit:true,q:['Anong color ang gusto mo? (subject sa availability)','Which color do you prefer? (subject to availability)'],t:'c',o:function(){var u=U.filter(function(x){return x.id===A._variant})[0];return ((u&&u.colors&&u.colors.length)?u.colors:COLORS).map(function(c){return [c[0],c[1]?c[0]+' (+'+peso(c[1])+')':c[0]]}).concat([['undecided','Bahala na / undecided','Undecided']])}}
);
var COLORS=[];
var hist=[],cur=null;  /* hist: [{i,nodes}] answered steps; cur: open question {i,node} */
function clearAns(id){delete A[id];delete A['_prev_'+id];if(id==='_variant'){delete A.unit;delete A.rec}}
function next(i){while(i<Q.length&&Q[i].show&&!Q[i].show())i++;if(i>=Q.length){cur=null;result();return}ask(i)}
function popTo(k){if(cur){cur.node.remove();cur=null}while(hist.length>k){var h=hist.pop();h.nodes.forEach(function(n){n.remove()});clearAns(Q[h.i].id)}}
function goBack(){if(!hist.length)return;var i=hist[hist.length-1].i;popTo(hist.length-1);ask(i)}
function editAt(k){var i=hist[k].i;popTo(k);ask(i)}
function ask(i){
  var q=Q[i];prog(q.unit?3:2);
  var qt=typeof q.q==='function'?q.q():Array.isArray(q.q)?T(q.q[0],q.q[1]):q.q,b=bot(esc(qt)),bu=b.querySelector('.la-bu'),w=document.createElement('div');w.className='la-in';cur={i:i,node:b};
  function done(label){w.remove();var bk=bu.querySelector('.la-back');if(bk)bk.remove();var m=me(label);var k=hist.length;hist.push({i:i,nodes:[b,m]});
    m.classList.add('la-edit');m.title=T('Palitan','Edit');m.querySelector('.la-bu').insertAdjacentHTML('beforeend',' <span class="la-pen">✎ '+T('Palitan','Edit')+'</span>');
    m.onclick=function(){editAt(k)};cur=null;next(i+1)}
  if(q.t==='c'){var opts=typeof q.o==='function'?q.o():q.o;opts.forEach(function(o){var x=document.createElement('button');x.type='button';x.className='chip';var lb=A.lang==='en'&&o[2]?o[2]:o[1];if(q.sub&&lb.indexOf(' · ')>0){var pr=lb.split(' · ');x.innerHTML=esc(pr[0])+' <span class="small" style="opacity:.7">'+esc(pr[1])+'</span>';lb=pr[0]}else x.textContent=lb;
     x.onclick=function(){if(w.dataset.busy)return;w.dataset.busy='1';x.classList.add('sel');w.querySelectorAll('.chip').forEach(function(c){if(c!==x)c.disabled=true});
       setTimeout(function(){A[q.id]=o[0];if(q.id==='_variant'){A.unit=U.filter(function(u){return u.id===o[0]})[0];A.rec=recPlans();A._opt=A.rec.promoIdx}done(lb)},250)};w.appendChild(x)})}
  else if(q.t==='ym'){/* tenure: Years chips + Months chips, live label; stored as years (total months / 12) */
    var YS=[[0,'0'],[1,'1'],[2,'2'],[3,'3'],[4,'4'],[5,'5'],[6,'6–10'],[10,'10+']],sy=null,sm=0;
    var lab=document.createElement('p');lab.className='la-ymlab';lab.style.cssText='font-weight:700;margin:6px 0';
    function ylab(y){var t=YS.filter(function(z){return z[0]===y})[0][1];return t+(A.lang==='en'?(t==='1'?' yr':' yrs'):' taon')}
    function txt(){if(sy===null)return T('Piliin ang taon','Choose years');return ylab(sy)+(sy<6&&sm?T(' at ',' and ')+sm+(A.lang==='en'?(sm===1?' month':' months'):' buwan'):'')}
    var yl=document.createElement('p');yl.className='small';yl.style.margin='0 0 4px';yl.textContent=T('Taon','Years');
    var yr=document.createElement('div');yr.className='la-in';var ml=document.createElement('p');ml.className='small';ml.style.margin='8px 0 4px';ml.textContent=T('Dagdag na buwan','Plus months');
    var mr=document.createElement('div');mr.className='la-in';
    var ok2=document.createElement('button');ok2.type='button';ok2.className='btn sm';ok2.textContent='OK';ok2.disabled=true;
    function paint(){yr.querySelectorAll('.chip').forEach(function(c){c.classList.toggle('on',+c.dataset.y===sy)});mr.querySelectorAll('.chip').forEach(function(c){c.classList.toggle('on',+c.dataset.m===sm)});
      var show=sy!==null&&sy<6;ml.hidden=mr.hidden=!show;lab.textContent=txt();ok2.disabled=sy===null}
    YS.forEach(function(z){var c=document.createElement('button');c.type='button';c.className='chip';c.dataset.y=z[0];c.textContent=z[1];c.onclick=function(){sy=z[0];if(sy>=6)sm=0;paint()};yr.appendChild(c)});
    for(var mi=0;mi<12;mi++)(function(m){var c=document.createElement('button');c.type='button';c.className='chip';c.dataset.m=m;c.textContent=m;c.onclick=function(){sm=m;paint()};mr.appendChild(c)})(mi);
    ok2.onclick=function(){var tm=sy*12+(sy<6?sm:0);A[q.id]=tm/12;A[q.id.replace('_years','')+'_months']=tm;done(txt())};
    [yl,yr,ml,mr,lab,ok2].forEach(function(e){w.appendChild(e)});w.style.display='block';paint()}
  else{var inp=document.createElement('input');inp.type=q.t==='date'?'date':'number';inp.inputMode=q.t==='n'?'decimal':'';
    if(q.t==='n'){inp.min=q.min;inp.max=q.max;inp.step=q.step}else{inp.max=new Date().toISOString().slice(0,10)}
    if(A['_prev_'+q.id]!==undefined)inp.value=A['_prev_'+q.id];
    inp.setAttribute('aria-label',qt);var ok=document.createElement('button');ok.type='button';ok.className='btn sm';ok.textContent='OK';
    var er=document.createElement('p');er.className='er';er.hidden=true;er.textContent=q.t==='date'?T('Pakilagay ang tamang petsa.','Please enter a valid date.'):T('Pakilagay ang tamang numero.','Please enter a valid number.');
    var go=function(){var v=inp.value;if(q.t==='n'){var n=parseFloat(v);if(isNaN(n)||n<q.min||n>q.max){er.hidden=false;return}A[q.id]=n;A['_prev_'+q.id]=v;done(/income|oblig|_custom/.test(q.id)?peso(n):String(n))}
      else{if(!v||new Date(v)>new Date()){er.hidden=false;return}A[q.id]=v;A['_prev_'+q.id]=v;done(new Date(v+'T00:00').toLocaleDateString(A.lang==='en'?'en-PH':'en-PH',{year:'numeric',month:'long',day:'numeric'}))}};
    ok.onclick=go;inp.onkeydown=function(e){if(e.key==='Enter'){e.preventDefault();go()}};w.appendChild(inp);w.appendChild(ok);w.appendChild(er);setTimeout(function(){inp.focus({preventScroll:true})},60)}
  bu.appendChild(w);
  if(hist.length){var bk=document.createElement('button');bk.type='button';bk.className='la-back';bk.textContent='← '+T('Bumalik','Back');bk.onclick=goBack;bu.appendChild(bk)}
  scroll(b);
}
/* ---------- Interactive computation + recommendation panel (estimates only) ---------- */
var TERMS=[12,24,36,48,60];
/* Add-on rate for any term: known 12-month steps from CFG; in-between terms (18/30/42/54) interpolated linearly. ESTIMATE. */
function addon(n){var r=CFG.est_addon_rates;if(r[n]!=null)return r[n];var lo=Math.floor(n/12)*12,hi=lo+12;return r[lo]+(r[hi]-r[lo])*(n-lo)/12}
function estMo(fin,n){return fin*(1+addon(n))/n}
var MTERMS=[12,18,24,30,36,42,48,54,60];
function yrTxt(n){var y=n/12;return A.lang==='en'?y+(y===1?' yr':' yrs'):y+' taon'}
function moTxt(n){return n+(A.lang==='en'?' mo':' buwan')}
function termTxt(n){return n%12===0?yrTxt(n)+' ('+moTxt(n)+')':moTxt(n)+' ('+yrTxt(n)+')'}
/* Plan recommendation from the Step 2 answers (dp_capacity, preferred_term, target_monthly).
   Rule: if the client can pay a big DP but a lower-DP all-in promo already fits, recommend the promo first (keeps cash; insurance/LTO/freebies included). ASSUMPTION thresholds in CFG. */
CFG.rec_big_dp_gap=50000;   // [A] extra cash vs promo DP that counts as "big DP" for the promo-first reason
function capDP(P){var c={zero:0,upto100k:100000,'100k_250k':250000,'250k_500k':500000,'40pct':P*0.4,custom:A.dp_custom||0}[A.dp_capacity];return Math.min(c==null?P*0.2:c,P*0.9)}
function tgtMo(){return {lt15k:15000,'15k_25k':25000,'25k_35k':35000,custom:A.target_custom||null}[A.target_monthly]||null}
function incTot(){return (A.gross_monthly_income||0)+(A.co_borrower==='yes'?(A.co_income||0):0)}
function recPlans(){var u=A.unit,P=u.price,inc=incTot(),cap=capDP(P),tgt=tgtMo(),n=A.preferred_term==='unsure'||!A.preferred_term?60:+A.preferred_term;
  var lim=Math.min(tgt||Infinity,inc?inc*CFG.fit_max_ratio:Infinity);
  var pr=u.opts.map(function(o,i){return {kind:'promo',i:i,dp:o.dp,n:CFG.promo_term_months,mo:o.mo,label:(o.dp?peso(o.dp)+' DP':'Zero DP')+' promo (all-in)'}});
  var inCap=pr.filter(function(o){return o.dp<=cap+1});if(!inCap.length)inCap=[pr.slice().sort(function(a,b){return a.dp-b.dp})[0]];
  var ok=inCap.filter(function(o){return o.mo<=lim}).sort(function(a,b){return a.dp-b.dp});
  var promo=ok[0]||inCap.slice().sort(function(a,b){return a.mo-b.mo})[0];
  var mn=P*CFG.calc_min_dp_pct/100,cdp=Math.max(cap,mn),cust=null;
  if(cdp<P*0.9){cust={kind:'custom',dp:Math.round(cdp),n:n,mo:estMo(P-cdp,n),label:Math.round(cdp/P*100)+'% DP · '+yrTxt(n)+' (bank estimate)'}}
  var primary=promo,alt=cust,why;
  var promoFits=promo.mo<=lim,custFits=cust&&cust.mo<=lim;
  if(!promoFits&&custFits){primary=cust;alt=promo;why=T('Mas pasok sa target monthly mo at sa income mo. Estimate lang ito; hindi pa kasama ang insurance, LTO at fees.','Fits your target monthly and income better. Estimate only; insurance, LTO and fees are not yet included.')}
  else if(cap-promo.dp>=CFG.rec_big_dp_gap){why=T('Mas praktikal: may matitira kang cash (mga '+peso(cap-promo.dp)+') at all-in na ang promo (kasama na ang insurance, LTO at freebies).','More practical: you keep cash (about '+peso(cap-promo.dp)+') and the promo is all-in (insurance, LTO and freebies included).')}
  else why=T('Pasok sa DP na kaya mo at all-in na ang promo (kasama na ang insurance, LTO at freebies).','Fits the DP you can put up, and the promo is all-in (insurance, LTO and freebies included).');
  if(primary.kind==='promo'&&n!==CFG.promo_term_months)why+=T(' Ang promo ay '+yrTxt(CFG.promo_term_months)+'; ang alternative ay naka-compute sa '+yrTxt(n)+' na gusto mo.',' The promo runs '+yrTxt(CFG.promo_term_months)+'; the alternative uses your preferred '+yrTxt(n)+'.');
  if(primary.kind==='promo'&&!promoFits)why+=T(' Medyo mabigat pa ito sa target o income mo; tingnan ang options sa baba.',' This is still above your target or income limit; see the options below.');
  return {primary:primary,alt:alt===primary?null:alt,why:why,promoIdx:promo.i,cap:cap,term:n,tgt:tgt}}
var pickPlan=null;
function initCalc(S,res){
  var u=A.unit,P=u.price,inc=(A.gross_monthly_income||0)+(A.co_borrower==='yes'?(A.co_income||0):0),box=$('la-calc'),st={dp:A.rec&&A.rec.alt&&A.rec.alt.kind==='custom'?A.rec.alt.dp:A.rec&&A.rec.primary.kind==='custom'?A.rec.primary.dp:Math.round(P*0.2),n:A.rec?A.rec.term:60};
  var promos=u.opts.map(function(o){return {kind:'promo',dp:o.dp,n:CFG.promo_term_months,mo:o.mo,label:(o.dp?peso(o.dp)+' DP':'Zero DP')+' promo (all-in)'}});
  function yrs(n){var y=n/12;return y+(A.lang==='en'?(y>1?' years':' year'):' taon')}
  function opt(dp,n){return {kind:'custom',dp:dp,n:n,mo:estMo(P-dp,n),label:Math.round(dp/P*100)+'% DP · '+yrs(n)}}
  function tot(o){return o.dp+o.mo*o.n}
  function fit(o){return inc>0&&o.mo/inc<=CFG.fit_max_ratio}
  function ratio(o){return inc>0?(o.mo/inc*100).toFixed(1)+'%':'—'}
  function fitTxt(o){if(!inc)return '';var x=o.mo/inc;return x<=CFG.aff.pass?'<span class="la-fit ok">'+T('Pasok sa income (≤30%)','Fits your income (≤30%)')+'</span>':x<=CFG.fit_max_ratio?'<span class="la-fit mid">'+T('Medyo mabigat (30–35%)','A bit tight (30–35%)')+'</span>':'<span class="la-fit no">'+T('Lampas sa 35% ng income','Over 35% of income')+'</span>'}
  box.innerHTML=safe('<div class="la-calcbox"><h2 class="h3">'+T('Compute at i-compare ang options','Compute and compare options')+'</h2>'+
   '<div class="la-tabs"><button type="button" class="chip on" data-mode="dp">'+T('Piliin ang DP at term','Choose DP and term')+'</button><button type="button" class="chip" data-mode="tg">Target monthly</button></div>'+
   '<div id="la-m-dp"><p class="fl">Down payment</p><div class="la-in" id="la-dpchips">'+[20,30,40,50].map(function(x){return '<button type="button" class="chip" data-dpp="'+x+'">'+x+'%</button>'}).join('')+'</div>'+
   '<input type="range" id="la-dpr" min="'+CFG.calc_min_dp_pct+'" max="'+CFG.calc_max_dp_pct+'" step="1" value="20" aria-label="DP %"><div class="la-in"><label for="la-dpa" class="small">'+T('O i-type ang eksaktong DP (₱)','Or type the exact DP (₱)')+'</label><input type="number" id="la-dpa" inputmode="numeric" min="0" step="1000"></div><p class="er" id="la-dpw" hidden></p>'+
   '<p class="fl">Term <span class="la-tabs" style="display:inline-flex;gap:6px;margin-left:8px;vertical-align:middle"><button type="button" class="chip on" data-tu="y" style="padding:4px 12px;min-height:0">'+T('Taon','Years')+'</button><button type="button" class="chip" data-tu="m" style="padding:4px 12px;min-height:0">'+T('Buwan','Months')+'</button></span></p><div class="la-in" id="la-terms"></div>'+
   '<dl class="la-sum" id="la-cres"></dl></div>'+
   '<div id="la-m-tg" hidden><div class="la-in"><label for="la-tgt" class="small">'+T('Magkano ang gusto mong monthly? (₱)','What monthly do you want? (₱)')+'</label><input type="number" id="la-tgt" inputmode="numeric" min="0" step="500"></div><table class="la-tbl" id="la-tgres"></table></div>'+
   '<div id="la-best"></div>'+
   '<h3 class="h3" style="margin-top:16px">'+T('Halimbawang computation','Sample computation')+'</h3><p class="small" style="margin:0 0 8px">'+T('Halimbawa: '+esc(u.n)+' — magkano ang monthly depende sa DP at taon','Example: '+esc(u.n)+' — your monthly depending on DP and years')+'</p><table class="la-tbl la-sample"><thead><tr><th>'+T('Taon','Years')+'</th><th>20% DP<br><span class="small">'+peso(P*0.2)+'</span></th><th>40% DP<br><span class="small">'+peso(P*0.4)+'</span></th></tr></thead><tbody>'+
     TERMS.map(function(n){return '<tr><td><b>'+yrTxt(n)+'</b></td><td><b style="font-size:1.2em">'+peso(estMo(P*0.8,n))+'</b></td><td><b style="font-size:1.2em">'+peso(estMo(P*0.6,n))+'</b></td></tr>'}).join('')+'</tbody></table>'+
   '<p class="muted small">'+T('Estimate lang ito, subject sa bank evaluation. Ang final na rate at halaga ay manggagaling sa bank o dealer. Ang custom computation ay hindi pa kasama ang insurance, chattel mortgage, LTO at fees; ang dealer promo ay all-in.','Estimates only, subject to bank evaluation. Final rates and amounts come from the bank or dealer. Custom computations exclude insurance, chattel mortgage, LTO and fees; dealer promos are all-in.')+'</p>'+
   '<p class="la-ok" id="la-planok" hidden></p></div>');
  function mark(){box.querySelectorAll('[data-dpp]').forEach(function(b){b.classList.toggle('on',Math.abs(st.dp-Math.round(P*b.dataset.dpp/100))<1)});box.querySelectorAll('[data-n]').forEach(function(b){b.classList.toggle('on',+b.dataset.n===st.n)})}
  var LIST=[];
  function card(o,i,hl){return '<button type="button" class="la-opt'+(hl?' hl':'')+'" data-pick="'+i+'"><b>'+esc(o.label)+'</b><span>'+peso(o.mo)+'/mo × '+termTxt(o.n)+' · DP '+peso(o.dp)+'</span><span>Total '+peso(tot(o))+' · '+ratio(o)+' '+T('ng income','of income')+'</span>'+fitTxt(o)+'<em>'+T('Piliin ito','Choose this')+'</em></button>'}
  function best(cur){
    var better=promos.filter(function(p){var same=opt(p.dp,p.n);return p.mo<same.mo-1||tot(p)<tot(cur)-1||(fit(p)&&!fit(cur))});
    var pool=[];[20,30,40,50].forEach(function(x){TERMS.forEach(function(n){pool.push(opt(Math.round(P*x/100),n))})});pool.push(cur);
    var top=promos.concat(pool).filter(fit).sort(function(a,b){return tot(a)-tot(b)});
    var seen={},t3=[];top.forEach(function(o){var k=o.kind+Math.round(o.dp)+'-'+o.n;if(!seen[k]&&t3.length<3){seen[k]=1;t3.push(o)}});
    LIST=better.concat(t3);var h='';
    if(better.length)h+='<div class="la-promo"><p><b>💡 '+T('Mas makakatipid ka sa promo','You can save more with the promo')+'</b><br><span class="small">'+T('Mas mababa ang monthly o total kumpara sa custom computation sa parehong DP, at all-in pa.','Lower monthly or total cost than a custom computation at the same DP, and it is all-in.')+'</span></p>'+better.map(function(o,i){return card(o,i,true)}).join('')+'</div>';
    h+='<p class="fl" style="margin-top:12px"><b>'+T('Top 3 options na pasok sa income mo (≤35%), pinakamura sa total','Top 3 options that fit your income (≤35%), lowest total cost first')+'</b></p>';
    h+=t3.length?t3.map(function(o,i){return card(o,better.length+i,false)}).join(''):'<p>'+T('Wala pang option na pasok sa 35% ng income. Subukan ang mas mataas na DP, co-maker, o ibang unit.','No option fits 35% of your income yet. Try a higher DP, a co-maker, or another unit.')+'</p>';
    h+='<p class="small"><button type="button" class="la-link" data-pick="cur">'+T('Piliin ang sarili kong computation','Choose my own computation')+' ('+esc(cur.label)+')</button></p>';
    $('la-best').innerHTML=safe(h);LIST.cur=cur;
    $('la-best').querySelectorAll('[data-pick]').forEach(function(b){b.onclick=function(){choose(b.dataset.pick==='cur'?LIST.cur:LIST[+b.dataset.pick])}})}
  function calc(){var o=opt(st.dp,st.n);mark();
    $('la-cres').innerHTML=safe('<div><dt>Amount financed</dt><dd>'+peso(P-st.dp)+'</dd></div><div><dt>Monthly (estimate)</dt><dd>'+peso(o.mo)+'</dd></div><div><dt>'+T('Total cost (DP + lahat ng monthly)','Total cost (DP + all monthlies)')+'</dt><dd>'+peso(tot(o))+'</dd></div><div><dt>Monthly vs income</dt><dd>'+ratio(o)+' '+fitTxt(o)+'</dd></div>');
    best(o)}
  function choose(o){A.plan={dp:Math.round(o.dp),dp_pct:+(o.dp/P*100).toFixed(1),term_months:o.n,monthly:Math.round(o.mo),total_cost:Math.round(tot(o)),type:o.kind,ratio:inc?+(o.mo/inc).toFixed(4):null};
    $('la-planok').hidden=false;$('la-planok').textContent=T('✓ Napili: ','✓ Selected: ')+o.label+' · '+peso(o.mo)+'/mo × '+termTxt(o.n)+'. '+T('Ime-message ka ni Richard para i-confirm sa bank o dealer.','Richard will message you to confirm with the bank or dealer.');
    crispSync();
    ga('select_plan',{plan_type:o.kind,term_months:o.n,unit:u.n,result:res});
    var L=Lead.base('loan_plan_select');L.name=A.name;L.mobile=A.mobile;L.chosenUnit=u.n;L.unitParam=u.id;L.language=A.lang;L.dpPreference=peso(A.plan.dp)+' DP ('+A.plan.dp_pct+'%)';
    L.planType=o.kind;L.planDp=A.plan.dp;L.planDpPct=A.plan.dp_pct;L.planTerm=o.n;L.planMonthly=A.plan.monthly;L.planTotal=A.plan.total_cost;
    L.timeline='Plan: '+o.kind+' '+A.plan.dp_pct+'% DP, '+o.n+' mo, '+peso(o.mo)+'/mo';L.usage='Selected plan ('+o.kind+'): DP '+peso(A.plan.dp)+', '+o.n+' mo, monthly '+peso(o.mo)+' (estimate), total '+peso(tot(o))+' | Language: '+A.lang;
    L.dp_capacity=A.dp_capacity;L.preferred_term=A.preferred_term;L.target_monthly=A.target_monthly==='custom'?A.target_custom:A.target_monthly;
    Lead.send(L);var rk=$('la-recok');if(rk){rk.hidden=false;rk.textContent=$('la-planok').textContent}}
  pickPlan=choose;
  box.querySelectorAll('[data-dpp]').forEach(function(b){b.onclick=function(){st.dp=Math.round(P*b.dataset.dpp/100);$('la-dpr').value=b.dataset.dpp;$('la-dpa').value='';$('la-dpw').hidden=true;calc()}});
  $('la-dpr').oninput=function(){st.dp=Math.round(P*this.value/100);$('la-dpa').value='';$('la-dpw').hidden=true;calc()};
  $('la-dpa').oninput=function(){var v=parseFloat(this.value),w=$('la-dpw');if(isNaN(v)||v<0)return;if(v>=P){w.hidden=false;w.textContent=T('Mas mataas sa presyo ang DP.','DP is higher than the price.');return}
    w.hidden=v>=P*CFG.calc_min_dp_pct/100;w.textContent=T('Karaniwang minimum ng bank ay '+CFG.calc_min_dp_pct+'% DP ('+peso(P*CFG.calc_min_dp_pct/100)+'). Pwede pa ring i-compute, pero mas malaki ang chance na hindi pumasa.','Banks usually require at least '+CFG.calc_min_dp_pct+'% DP ('+peso(P*CFG.calc_min_dp_pct/100)+'). We can still compute it, but it may not pass.');st.dp=v;calc()};
  function terms(unit){var L=unit==='m'?MTERMS:TERMS;$('la-terms').innerHTML=safe(L.map(function(n){return '<button type="button" class="chip" data-n="'+n+'">'+(unit==='m'?'<b>'+n+'</b> <span class="small">'+T('buwan','mo')+'</span>':yrTxt(n)+'<br><span class="small" style="opacity:.7">'+moTxt(n)+'</span>')+'</button>'}).join(''));
    box.querySelectorAll('[data-tu]').forEach(function(b){b.classList.toggle('on',b.dataset.tu===unit)});
    $('la-terms').querySelectorAll('[data-n]').forEach(function(b){b.onclick=function(){st.n=+b.dataset.n;calc()}});mark()}
  box.querySelectorAll('[data-tu]').forEach(function(b){b.onclick=function(){terms(b.dataset.tu)}});terms(st.n%12?'m':'y');
  box.querySelectorAll('[data-mode]').forEach(function(b){b.onclick=function(){box.querySelectorAll('[data-mode]').forEach(function(x){x.classList.toggle('on',x===b)});$('la-m-dp').hidden=b.dataset.mode!=='dp';$('la-m-tg').hidden=b.dataset.mode!=='tg'}});
  $('la-tgt').oninput=function(){var t=parseFloat(this.value);if(isNaN(t)||t<=0){$('la-tgres').innerHTML='';return}
    var mn=P*CFG.calc_min_dp_pct/100;
    $('la-tgres').innerHTML=safe('<thead><tr><th>'+T('Taon','Years')+'</th><th>'+T('Kailangang DP','DP needed')+'</th></tr></thead><tbody>'+TERMS.map(function(n){var dp=P-t*n/(1+addon(n));
      var cell=dp>=P*0.9?'<span class="la-fit no">'+T('Hindi kaya sa term na ito','Not possible on this term')+'</span>':dp<=mn?peso(mn)+' ('+CFG.calc_min_dp_pct+'% min) · ~'+peso(estMo(P-mn,n))+'/mo':peso(Math.ceil(dp/1000)*1000)+' ('+Math.round(dp/P*100)+'%)';return '<tr><td><b>'+yrTxt(n)+'</b> <span class="small">('+moTxt(n)+')</span></td><td>'+cell+'</td></tr>'}).join('')+'</tbody>')};
  calc();
}

/* ---------- Step 4: scoring (rulebook §2.3/§2.4) ---------- */
function age(d,at){var b=new Date(d+'T00:00'),a=at.getFullYear()-b.getFullYear();var m=at.getMonth()-b.getMonth();if(m<0||(m===0&&at.getDate()<b.getDate()))a--;return a}
function assess(){
  var u=A.unit,o=u.opts[A._opt],term=CFG.promo_term_months,R=[],flags=[],fixable=[];
  var gross=A.gross_monthly_income,hh=gross+(A.other_household_income||0),co=A.co_borrower==='yes'?(A.co_income||0):0,inc=gross+co;
  var amort=o.mo,fin=u.price-o.dp,dpPct=u.price?o.dp/u.price*100:0;
  function r(id,out,note){R.push({rule_id:id,outcome:out,note:note})}
  var aff=inc?amort/inc:9;r('AFF-01',aff<=CFG.aff.pass?'pass':aff<=CFG.aff.review?'review':'fail','Amortization '+(aff*100).toFixed(1)+'% ng income');
  var hhAll=hh+co;r('INC-01',hhAll>=CFG.income_min_household?'pass':aff<=CFG.aff.pass?'review':'fail','Household income '+peso(hhAll));
  var dti=inc?(amort+(A.existing_monthly_obligations||0))/inc:9;r('DTI-01',dti<=CFG.dti.pass?'pass':dti<=CFG.dti.review?'review':'fail','DTI '+(dti*100).toFixed(1)+'%');
  var et=A.employment_type,y=A.years_in_employment||0;
  if(et==='employed'){var TE=CFG.ten_employed;r('TEN-01',(y>=TE.pass_regular_yrs&&A.employment_status==='permanent')||(A.employment_status==='permanent'&&y>=TE.pass_permanent_yrs)?'pass':y<TE.fail_below_yrs?'fail':'review',y+' yrs, '+A.employment_status)}
  else if(et==='business_owner'){var B=CFG.ten_business;r('TEN-02',y>=B.pass_yrs?'pass':(y>=B.review_profitable_yrs&&A.biz_profitable==='yes')?'review':'fail',y+' yrs')}
  else if(isOFW()){r('TEN-03',A.ofw_aif==='no'?'fail':(A.ofw_contract==='yes'&&A.ofw_remit==='yes'&&A.ofw_aif==='yes')?'pass':'review','contract '+A.ofw_contract+', remittance '+A.ofw_remit+', AIF '+A.ofw_aif)}
  else if(et==='freelancer'||et==='other'){var F=CFG.ten_freelancer;r('TEN-F',y>=F.pass_yrs?'pass':y<F.fail_below_yrs?'fail':'review',y+' yrs [dealer assumption]')}
  var now=new Date(),ag=age(A.dob,now),mat=new Date(now);mat.setMonth(mat.getMonth()+term);var agm=age(A.dob,mat),G=CFG.age;
  r('AGE-01',ag<G.min||ag>G.max_at_maturity?'fail':agm>G.max_at_maturity?'review':(ag<G.pass_min||ag>G.pass_max)?'review':'pass','Age '+ag+', '+agm+' sa maturity');
  r('DP-01',dpPct>=CFG.dp.pass_pct?'pass':(CFG.promo_dp_passes?'pass':dpPct>=CFG.dp.review_pct?'review':'fail'),'DP '+dpPct.toFixed(1)+'%'+(dpPct<CFG.dp.pass_pct?' (dealer promo DP)':''));
  if(fin<CFG.metrobank_min_loan)r('LOAN-01','review','Amount financed '+peso(fin)+': hindi pasok sa Metrobank');
  if(A.purpose==='tnvs')r('PUR-01','review','TNVS: hindi pasok sa Metrobank');
  if(A.residential_status==='rented'&&A.length_of_stay_years<CFG.rf07_min_stay_rented_yrs)flags.push('RF-07');
  if(A.registered_owner==='other')flags.push('RF-08');
  /* eligible banks */
  var banks=[],ex={};if(fin<CFG.metrobank_min_loan||A.purpose==='tnvs'||(et==='business_owner'&&y<3))ex.Metrobank=1;if(dpPct<20)ex.Metrobank=1;
  if(isOFW()&&co===0){ex['Security Bank']=1;if(A.civil_status==='married')ex.EastWest=1}
  Object.keys(CFG.bank_min_income).forEach(function(k){if(!ex[k]&&hhAll>=CFG.bank_min_income[k])banks.push(k)});
  if(aff<=CFG.aff.pass)banks.push('RCBC');banks.unshift('Mitsubishi Motors Finance PH');
  /* outcome (§2.4). Assumption: a Fail that §3 can fix (higher DP / cheaper unit / co-maker) shows as Needs Review. */
  var fails=R.filter(function(x){return x.outcome==='fail'}),revs=R.filter(function(x){return x.outcome==='review'});
  var hardFail=fails.some(function(x){return ['AGE-01','TEN-01','TEN-02','TEN-03','TEN-F'].indexOf(x.rule_id)>=0});
  var res=hardFail?'NOT_YET_QUALIFIED':fails.length||revs.length||flags.length?'NEEDS_REVIEW':'PRE_QUALIFIED';
  /* recommendations (§3) */
  var rec=[],target=CFG.aff.pass*inc;
  if(res!=='PRE_QUALIFIED'){
    if(amort>target){var two=u.opts.length>1,a0=u.opts[0],a1=u.opts[u.opts.length-1];
      if(two&&a1.dp!==a0.dp){var slope=(a0.mo-a1.mo)/(a1.dp-a0.dp),need=a0.dp+(a0.mo-target)/slope;
        if(need<u.price*0.9)rec.push(T('Mas mataas na DP: mga '+peso(Math.ceil(need/1000)*1000)+' DP para bumaba ang monthly sa ~'+peso(target)+' (30% ng income). Estimate lang ito, subject sa bank computation.','Higher DP: about '+peso(Math.ceil(need/1000)*1000)+' DP to bring the monthly down to ~'+peso(target)+' (30% of income). This is an estimate only, subject to bank computation.'))}
      else rec.push(T('Mas mataas na DP: ipapa-compute namin sa bank kung magkano ang DP para bumaba ang monthly sa ~'+peso(target)+'.','Higher DP: we will ask the bank to compute the DP needed to bring the monthly down to ~'+peso(target)+'.'))}
    if(term<CFG.max_term)rec.push(T('Mas mahabang term: ','Longer term: ')+CFG.max_term+' months.');
    if(amort>target){var ch=U.filter(function(x){return x.id!==u.id&&Math.min.apply(null,x.opts.map(function(p){return p.mo}))<=target}).sort(function(a,b){return Math.min.apply(null,b.opts.map(function(p){return p.mo}))-Math.min.apply(null,a.opts.map(function(p){return p.mo}))})[0];
      rec.push(ch?T('Mas abot-kayang unit: ','More affordable unit: ')+ch.n+' (from '+peso(Math.min.apply(null,ch.opts.map(function(p){return p.mo})))+'/mo).':T('Mas abot-kayang unit: L300 o Mirage G4, ipapa-quote namin ang pinakabagong promo.','More affordable unit: L300 or Mirage G4; we will quote the latest promo.'))}
    if(co===0&&(amort>target||isOFW()||dti>CFG.dti.pass))rec.push(T('Mag-add ng co-maker: spouse o kamag-anak na may income','Add a co-maker: a spouse or relative with income')+(isOFW()?T(' (kailangan ng PH co-maker sa Security Bank; spouse co-maker sa EastWest kung married).',' (Security Bank requires a PH co-maker; EastWest requires a spouse co-maker if married).'):'.'));
    if(hardFail)rec.push(T('Pwede tayong mag-try ulit after ma-build ang income o tenure. Pwede ka naming i-follow up in 3–6 months kung gusto mo.','We can try again once your income or tenure builds up. We can follow up in 3–6 months if you like.'));
    if(flags.indexOf('RF-08')>=0)rec.push(T('Kung sa ibang tao ipapangalan ang unit, siya ang dapat mag-apply bilang borrower. Pag-usapan natin.','If the unit will be in someone else\'s name, that person should apply as the borrower. Let\'s talk.'));
  }
  return {result:res,affordability_ratio:+aff.toFixed(4),dti_ratio:+dti.toFixed(4),rule_results:R,red_flags:flags,eligible_banks:banks,recommendations:rec.slice(0,3),_amort:amort,_fin:fin,_dp:o.dp,_term:term,_dpPct:dpPct};
}
function reqs(){var REQ={common:[T('2 valid government IDs (hindi expired)','2 valid government IDs (unexpired)'),T('Proof of billing (hindi lalampas ng 3 months)','Proof of billing (not older than 3 months)'),'Data Privacy consent'],
 employed:['COE with compensation','Latest 3 months payslips','ITR / BIR 2316'],
 business_owner:['DTI / SEC registration','Mayor\'s permit','3–6 months bank statements','Audited FS / ITR'],
 ofw:['Employment contract','3–6 months remittance proof',T('IDs ng AIF + SPA','AIF\'s IDs + SPA')],
 freelancer:['PayPal / Wise statements','Client contracts','6 months bank statements'],
 comaker:[T('Co-maker: 2 IDs + sariling income documents','Co-maker: 2 IDs + own income documents')]};
REQ.seafarer=REQ.ofw;REQ.pensioner=['Pension statement / proof of pension'];REQ.other=[T('Proof of income (ipapaalam namin kung ano)','Proof of income (we will tell you which)')];return REQ}
var EMPL={employed:'Employed',business_owner:'Business owner',ofw:'OFW',seafarer:'Seafarer',freelancer:'Freelancer / VA',pensioner:'Pensioner',other:'other income type'};
var LBL={PRE_QUALIFIED:'Pre-qualified',NEEDS_REVIEW:'Needs Review',NOT_YET_QUALIFIED:'Not yet qualified'};
function msgr(res){var ref=('loan-assessment-'+res.toLowerCase().replace(/_/g,'-')+'-'+A.unit.id).replace(/[^a-z0-9-]/gi,'').slice(0,240);return MESSENGER_URL+'?ref='+encodeURIComponent(ref)}
function contactBtns(res){return '<div class="la-cta">'+finaBtn()+'<a class="btn la-msg" href="'+msgr(res)+'" rel="noopener" data-c="messenger">💬 '+T('Makipag-usap sa tao sa Messenger','Talk to a person on Messenger')+'</a><a class="btn ghost dk" href="'+CALL_TEL+'" data-c="call">📞 '+T('Tumawag','Call')+': 0954 291 1201</a></div>'}
function bindContact(el,res){el.addEventListener('click',function(e){var f=e.target.closest&&e.target.closest('[data-fina]');if(f){e.preventDefault();px('Contact',{method:'crisp_chat',content_name:A.unit.n});ga('contact',{method:'crisp_chat',result:res});openFina()}});el.querySelectorAll('[data-c]').forEach(function(a){a.addEventListener('click',function(){px('Contact',{method:a.dataset.c,content_name:A.unit.n});ga('contact',{method:a.dataset.c,result:res})})})}
function recHtml(){var r=A.rec,inc=incTot();if(!r)return '';
  function c(o,k,main){var tot=o.dp+o.mo*o.n;return '<div class="la-opt'+(main?' hl':'')+'"><b>'+(main?'⭐ '+T('Rekomendado','Recommended')+': ':T('Alternative','Alternative')+': ')+esc(o.label)+'</b><span style="font-size:1.25em"><b>'+peso(o.mo)+'</b>/mo × '+termTxt(o.n)+'</span><span>DP '+(o.dp?peso(o.dp):'₱0')+' · Total '+peso(tot)+(inc?' · '+(o.mo/inc*100).toFixed(1)+'% '+T('ng income','of income'):'')+'</span>'+(o.kind==='custom'?'<span class="small muted">'+T('Hindi pa kasama ang insurance, LTO at fees.','Excludes insurance, LTO and fees.')+'</span>':'')+'<button type="button" class="btn sm'+(main?'':' ghost dk')+'" data-rec="'+k+'">'+T('Piliin ito','Choose this')+'</button></div>'}
  return '<div class="la-recbox"><h2 class="h3">'+T('Ang rekomendasyon namin','Our recommendation')+'</h2>'+c(r.primary,'p',1)+'<p class="la-why">💡 '+esc(r.why)+'</p>'+(r.alt?c(r.alt,'a',0):'')+'<p class="la-ok" id="la-recok" hidden></p></div>'}
function result(){
  var S=assess(),u=A.unit,first=A.name.split(' ')[0],res=S.result;A.assessment=S;prog(4);
  first=esc(first);var head=A.lang==='en'?{PRE_QUALIFIED:'Good news, '+first+'! Based on the initial assessment, you are <b>Pre-qualified</b> for the '+esc(u.n)+'. This is not yet a bank approval; the final decision is still the bank\'s. Next step: get your requirements ready.',
   NEEDS_REVIEW:'Hi '+first+', we still need to review a few details of your assessment for the '+esc(u.n)+'. Richard, your sales consultant, will call or message you.',
   NOT_YET_QUALIFIED:'Hi '+first+', thanks for your interest! For now, your profile does not meet the requirements yet. But we have options, see below. Would you like to try one?'}[res]:{PRE_QUALIFIED:'Good news, '+first+'! Base sa initial assessment, <b>Pre-qualified</b> ka para sa '+esc(u.n)+'. Hindi pa ito bank approval. Ang final decision ay sa bank pa rin. Next step: i-ready ang requirements.',
   NEEDS_REVIEW:'Hi '+first+', kailangan pa naming i-review ang ilang details ng assessment mo para sa '+esc(u.n)+'. Tatawagan o ime-message ka ni Richard, ang sales consultant mo.',
   NOT_YET_QUALIFIED:'Hi '+first+', salamat sa interest! Sa ngayon, hindi pa pasok ang profile sa requirements. Pero may options tayo, tingnan sa baba. Gusto mo bang i-try natin ang isa dito?'}[res];
  var REQ=reqs(),et=A.employment_type,req=REQ.common.concat(REQ[et]||[]).concat(A.co_borrower==='yes'||S.recommendations.join().indexOf('co-maker')>=0?REQ.comaker:[]);
  $('la-chat').hidden=true;var R=$('la-res');R.hidden=false;
  R.innerHTML=safe('<div class="la-card res-'+res.toLowerCase()+'"><p class="kick">'+T('Resulta ng assessment','Assessment result')+'</p><p class="la-badge">'+LBL[res]+'</p><p>'+head+'</p>'+
   recHtml()+'<details class="la-adj"><summary>⚙️ '+T('I-adjust ang computation (optional)','Adjust the computation (optional)')+'</summary><div id="la-calc"></div></details><dl class="la-sum"><div><dt>Documents</dt><dd id="la-docsum">'+T('I-check sa Step 5','Check in Step 5')+'</dd></div><div><dt>Unit</dt><dd>'+esc(u.n)+' · '+esc(A._color==='undecided'?T('Bahala na','Undecided'):A._color)+'</dd></div><div><dt>SRP / promo price</dt><dd>'+peso(u.price)+'</dd></div><div><dt>Down payment</dt><dd>'+(S._dp?peso(S._dp):'Zero DP')+'</dd></div><div><dt>Monthly (promo, '+yrTxt(S._term)+')</dt><dd>'+peso(S._amort)+'</dd></div><div><dt>Monthly vs income</dt><dd>'+(S.affordability_ratio*100).toFixed(1)+'%</dd></div></dl>'+
   (S.recommendations.length?'<h2 class="h3">'+T('Mga options para pumasa','Options to qualify')+'</h2><ol class="la-rec">'+S.recommendations.map(function(x){return '<li>'+esc(x)+'</li>'}).join('')+'</ol>':'')+
   '<h2 class="h3">'+T('Banks na pwedeng i-try','Banks you can try')+'</h2><p>'+S.eligible_banks.map(esc).join(' · ')+'</p><p class="muted">'+T('Subject to bank evaluation. Hindi kami nagbibigay ng interest rate; ang bank ang magko-compute.','Subject to bank evaluation. We do not quote interest rates; the bank computes them.')+'</p>'+
   '<div id="la-docbox"><h2 class="h3">Step 5: Requirements checklist</h2><p>'+T('Base sa checklist ni Fina para sa '+esc(EMPL[et]||et)+'. I-tick ang mga documents na <b>meron ka na</b>. Wala pang upload dito.','Based on Fina\'s checklist for '+esc(EMPL[et]||et)+'. Tick the documents you <b>already have</b>. No uploads here yet.')+'</p><ul class="la-docs">'+req.map(function(x,i){return '<li><span>'+esc(x)+'</span><label><input type="checkbox" data-doc="'+i+'"'+(x.indexOf('Data Privacy')===0?' checked':'')+'> '+T('Meron na ako','I have this')+'</label></li>'}).join('')+'</ul><p class="la-cnt" id="la-cnt"></p><button class="btn" type="button" id="la-docsave">'+T('I-save ang checklist','Save checklist')+'</button><p id="la-docerr" class="er" hidden>'+T('Hindi na-save. Pakisubukan ulit.','Not saved. Please try again.')+'</p><div id="la-docres" hidden></div></div>'+
   '<div class="la-cta la-final"><p class="small">'+T('May tanong pa? Si Fina ng aming live chat ang tutulong sa iyo papunta sa official application form.','Any questions? Fina from our live chat will guide you to the official application form.')+'</p>'+finaBtn()+'</div>'+
   '<p class="muted small">'+T('Initial pre-screening lang ito base sa sagot mo, hindi bank approval. Lahat ng figures ay subject sa bank evaluation at promo validity (','This is an initial pre-screening based on your answers, not a bank approval. All figures are subject to bank evaluation and promo validity (')+esc($('la-note').textContent)+').</p></div>');
  bindContact(R,res);window.scrollTo(0,0);initCalc(S,res);
  R.querySelectorAll('[data-rec]').forEach(function(b){b.onclick=function(){pickPlan(b.dataset.rec==='p'?A.rec.primary:A.rec.alt)}});
  /* lead capture: existing pipeline (Apps Script webhook via /assets/lead.js, honeypot + Turnstile) */
  var L=Lead.base('loan_assessment');L.name=A.name;L.mobile=A.mobile;L.chosenUnit=u.n;L.unitParam=u.id;L.dpPreference=S._dp?peso(S._dp)+' DP':'Zero DP';
  L.employment=et;L.seg=isOFW()?'ofw_abroad':'local';L.income=A.gross_monthly_income;L.timeline='Assessment: '+LBL[res];
  L.usage=['Result: '+LBL[res],'Monthly '+peso(S._amort)+' ('+(S.affordability_ratio*100).toFixed(1)+'% AFF, '+(S.dti_ratio*100).toFixed(1)+'% DTI)','Color: '+A._color,'Purpose: '+A.purpose,A.email?'Email: '+A.email:'','Rules: '+S.rule_results.map(function(x){return x.rule_id+'='+x.outcome}).join(','),S.red_flags.length?'Flags: '+S.red_flags.join(','):'','Banks: '+S.eligible_banks.join('/'),'Pref bank: '+A.preferred_bank,'Source: '+A.source_of_sale,'Consent: '+A.privacy_consent.version+' '+A.privacy_consent.timestamp].filter(Boolean).join(' | ');
  L.residence_months=A.length_of_stay_months;L.tenure_months=A.years_in_employment!=null?Math.round(A.years_in_employment*12):'';L.language=A.lang;L.dp_capacity=A.dp_capacity==='custom'?A.dp_custom:A.dp_capacity;L.preferred_term=A.preferred_term;L.target_monthly=A.target_monthly==='custom'?A.target_custom:A.target_monthly;L.recommended=A.rec?A.rec.primary.kind+' | DP '+A.rec.primary.dp+' | '+A.rec.primary.n+' mo | '+Math.round(A.rec.primary.mo)+'/mo':'';
  L.usage+=' | DP capacity: '+L.dp_capacity+' | Pref term: '+L.preferred_term+' | Target monthly: '+L.target_monthly+' | Recommended: '+L.recommended+' | Language: '+A.lang;L.docsTotal=req.length;L.docsReady=0;L.docsLacking=req.length;L.assessment=JSON.stringify({result:res,affordability_ratio:S.affordability_ratio,dti_ratio:S.dti_ratio,rule_results:S.rule_results,red_flags:S.red_flags,eligible_banks:S.eligible_banks,recommendations:S.recommendations});
  A.leadId=L.leadId;crispSync();
  Lead.send(L).then(function(){if(!Lead.skipped()){px('Lead',{content_name:u.n});ga('generate_lead',{form:'loan_assessment',unit:u.n,result:res,value:0,currency:'PHP'})}});
  /* Step 5: documents client already has (no uploads) */
  var boxes=R.querySelectorAll('[data-doc]');function cnt(){var r=0;boxes.forEach(function(b){if(b.checked)r++});$('la-cnt').textContent=r+' ready / '+(req.length-r)+T(' kulang',' lacking');return r}
  boxes.forEach(function(b){b.addEventListener('change',cnt)});cnt();
  $('la-docsave').addEventListener('click',function(){var btn=this,r=cnt(),lack=[];boxes.forEach(function(b){if(!b.checked)lack.push(req[+b.dataset.doc])});prog(5);
    $('la-docsum').textContent=r+' ready / '+lack.length+T(' kulang',' lacking');
    $('la-docres').innerHTML=safe(lack.length?'<div class="la-lack"><p><b>'+T('Kulang pa','Still lacking')+' ('+lack.length+'):</b></p><ul>'+lack.map(function(x){return '<li>'+esc(x)+'</li>'}).join('')+'</ul><p>'+T('Okay lang yan! Tutulungan ka nina Fina at Richard kung paano at saan makukuha ang mga ito, at ano ang pwedeng ipalit kung wala ka pa. I-tap lang ang live chat button sa baba.','That\'s okay! Fina and Richard will help you with how and where to get these, and what alternatives you can use. Just tap the live chat button below.')+'</p></div>':'<p class="la-ok">'+T('Wow, kumpleto ka na sa '+r+' documents! Ihanda lang ang malinaw na kopya. Tutulungan ka nina Fina at Richard sa next step.','Great, you have all '+r+' documents! Just prepare clear copies. Fina and Richard will help you with the next step.')+'</p>');
    $('la-docres').hidden=false;A.docs={ready:r,lacking:lack.length,missing:lack};crispSync();
    var D=Lead.base('loan_docs_checklist');D.leadId=L.leadId;D.name=A.name;D.mobile=A.mobile;D.chosenUnit=u.n;D.employment=et;D.docsReady=r;D.docsLacking=lack.length;D.docsTotal=req.length;D.language=A.lang;
    D.timeline='Docs: '+r+' ready / '+lack.length+' kulang ('+LBL[res]+')';D.usage='Docs ready '+r+'/'+req.length+(lack.length?' | Kulang: '+lack.join('; '):'');
    btn.disabled=true;btn.textContent=T('Sine-send...','Sending...');Lead.send(D).then(function(ok){if(ok===false)throw 0;btn.disabled=false;btn.textContent=T('✓ Na-save · I-update ang checklist','✓ Saved · Update checklist');$('la-docerr').hidden=true;px('Contact',{method:'crisp_chat',content_name:u.n});ga('contact',{method:'crisp_chat',result:res,trigger:'checklist_save'});openFina()}).catch(function(){btn.disabled=false;btn.textContent=T('I-save ang checklist','Save checklist');$('la-docerr').hidden=false});ga('docs_checklist',{ready:r,lacking:lack.length,result:res})});
}
document.addEventListener('DOMContentLoaded',function(){try{AS.init($('la-f1'))}catch(_){}});
})();
