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
  if(A.plan)d.push(['plan',A.plan.type+' | DP '+A.plan.dp+' ('+A.plan.dp_pct+'%) | '+A.plan.term_months+' mo | '+A.plan.monthly+'/mo']);
  if(A.docs){d.push(['docs_ready',A.docs.ready]);d.push(['docs_lacking',A.docs.lacking]);d.push(['missing_items',A.docs.missing.join('; ').slice(0,500)])}
  cp('set','session:data',[d]);var sg=['loan-assessment'];if(A.assessment)sg.push(A.assessment.result.toLowerCase().replace(/_/g,'-'));cp('set','session:segments',[sg])}
function finaMsg(){var u=A.unit,x=A.assessment,L={PRE_QUALIFIED:'Pre-qualified',NEEDS_REVIEW:'Needs Review',NOT_YET_QUALIFIED:'Not yet qualified'};
  var parts=[T('Hi Fina! Ako si ','Hi Fina! I am ')+A.name+'.'];
  if(u)parts.push('Unit: '+u.n+'.');if(x)parts.push(T('Resulta ng assessment: ','Assessment result: ')+L[x.result]+'.');
  if(A.plan)parts.push(T('Napiling plan: ','Chosen plan: ')+(A.plan.type==='promo'?'promo':'custom')+', DP '+peso(A.plan.dp)+', '+A.plan.term_months+' mo, ~'+peso(A.plan.monthly)+'/mo.');
  if(A.docs)parts.push('Documents: '+A.docs.ready+' ready / '+A.docs.lacking+T(' kulang',' lacking')+(A.docs.missing.length?' ('+A.docs.missing.join(', ')+').':'.'));
  parts.push(T('Pwede mo ba akong tulungan sa requirements?','Can you help me with the requirements?'));if(A.leadId)parts.push('Ref: '+A.leadId);return parts.join(' ')}
function openFina(){crispLoad();crispSync();cp('do','chat:open');if(!A.finaSent){A.finaSent=true;cp('do','message:send',['text',finaMsg()])}
  ga('chat_open',{provider:'crisp'})}
function finaBtn(){return '<button type="button" class="btn la-fina" data-fina="1">🤖 '+T('Chat kay Fina ngayon','Chat with Fina now')+'</button>'}
function T(t,e){return A.lang==='en'?e:t}
var A={lang:'tl'},log=$('la-log'),started=false,stepN=1;
function peso(n){return '₱'+Math.round(n).toLocaleString('en-PH')}
function esc(s){return String(s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
/* Meta Pixel: NO credit/income/assessment-result fields in payloads (Meta restricted-data policy). Only unit name / contact method / Phase-2 ref. */
function px(ev,p){try{if(typeof window.fbq==='function'){if(ev==='StartAssessment'||ev==='SubmitApplication')window.fbq('trackCustom',ev,p||{});else window.fbq('track',ev,p||{})}}catch(_){}}
function ga(ev,p){try{if(typeof window.gtag==='function')window.gtag('event',ev,p||{})}catch(_){}}
/* Phase 2 stub: call after the backend returns an MP-XXXXX ref. Not fired in Phase 1. */
window.LoanApp={submitApplication:function(ref){if(!/^MP-[A-HJKMNP-Z2-9]{5}$/i.test(ref))return false;px('SubmitApplication',{ref_no:ref.toUpperCase()});ga('submit_application',{ref_no:ref.toUpperCase()});return true},CFG:CFG};

function prog(n){stepN=n;document.querySelectorAll('.la-steps li').forEach(function(li,i){li.className=i<n?'on':''})}
function bot(html){var d=document.createElement('div');d.className='la-b bot';d.innerHTML='<span class="la-av" aria-hidden="true">R</span><div class="la-bu">'+html+'</div>';log.appendChild(d);return d}
function me(t){var d=document.createElement('div');d.className='la-b me';d.innerHTML='<div class="la-bu">'+esc(t)+'</div>';log.appendChild(d)}
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
 {id:'length_of_stay_years',q:['Gaano ka na katagal diyan? (taon, hal. 0.5 kung 6 months)','How long have you lived there? (years, e.g. 0.5 for 6 months)'],t:'n',min:0,max:80,step:0.5},
 {id:'employment_type',q:['Ano ang source of income mo?','What is your source of income?'],t:'c',o:EMP},
 {id:'years_in_employment',q:['Ilang taon ka na sa trabaho o negosyo na ito? (hal. 0.5 kung 6 months)','How many years in this job or business? (e.g. 0.5 for 6 months)'],t:'n',min:0,max:60,step:0.5,show:function(){return A.employment_type!=='pensioner'}},
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
 {id:'source_of_sale',q:['Last na: paano mo kami nahanap?','Last one: how did you find us?'],t:'c',o:[['facebook','Facebook','Facebook'],['google','Google','Google'],['referral','Referral','Referral'],['walk_in','Walk-in','Walk-in'],['other','Iba pa','Other']]}
];
function next(i){while(i<Q.length&&Q[i].show&&!Q[i].show())i++;if(i>=Q.length){unitStep();return}ask(Q[i],function(){next(i+1)})}
function ask(q,done){
  var qt=Array.isArray(q.q)?T(q.q[0],q.q[1]):q.q,b=bot(esc(qt)),bu=b.querySelector('.la-bu'),w=document.createElement('div');w.className='la-in';
  if(q.t==='c'){q.o.forEach(function(o){var x=document.createElement('button');x.type='button';x.className='chip';var lb=A.lang==='en'&&o[2]?o[2]:o[1];x.textContent=lb;
     x.onclick=function(){A[q.id]=o[0];w.remove();me(lb);done()};w.appendChild(x)})}
  else{var inp=document.createElement('input');inp.type=q.t==='date'?'date':'number';inp.inputMode=q.t==='n'?'decimal':'';
    if(q.t==='n'){inp.min=q.min;inp.max=q.max;inp.step=q.step}else{var t=new Date();inp.max=t.toISOString().slice(0,10)}
    inp.setAttribute('aria-label',qt);var ok=document.createElement('button');ok.type='button';ok.className='btn sm';ok.textContent='OK';
    var er=document.createElement('p');er.className='er';er.hidden=true;er.textContent=q.t==='date'?T('Pakilagay ang tamang petsa.','Please enter a valid date.'):T('Pakilagay ang tamang numero.','Please enter a valid number.');
    var go=function(){var v=inp.value;if(q.t==='n'){var n=parseFloat(v);if(isNaN(n)||n<q.min||n>q.max){er.hidden=false;return}A[q.id]=n;w.remove();me(q.id.indexOf('income')>=0||q.id.indexOf('oblig')>=0?peso(n):String(n))}
      else{if(!v||new Date(v)>new Date()){er.hidden=false;return}A[q.id]=v;w.remove();me(new Date(v+'T00:00').toLocaleDateString('en-PH',{year:'numeric',month:'long',day:'numeric'}))}done()};
    ok.onclick=go;inp.onkeydown=function(e){if(e.key==='Enter'){e.preventDefault();go()}};w.appendChild(inp);w.appendChild(ok);w.appendChild(er);setTimeout(function(){inp.focus({preventScroll:true})},60)}
  bu.appendChild(w);scroll(b);
}
var COLORS=['White Pearl','Silver','Graphite Gray','Black','Red'];
function unitStep(){prog(3);
  bot(T('Ayos! Ngayon, piliin natin ang <b>unit</b>. Ang DP at monthly ay galing sa promo ngayong buwan.','Great! Now let\'s pick your <b>unit</b>. DP and monthly figures are from this month\'s promo.'));
  var models=[];U.forEach(function(u){if(models.indexOf(u.model)<0)models.push(u.model)});
  ask({id:'_model',q:['Anong Mitsubishi model ang gusto mo?','Which Mitsubishi model do you want?'],t:'c',o:models.map(function(m){return [m,m]})},function(){
    var vs=U.filter(function(u){return u.model===A._model});
    ask({id:'_variant',q:['Anong variant?','Which variant?'],t:'c',o:vs.map(function(u){return [u.id,u.n+' · SRP '+peso(u.price)]})},function(){
      var u=U.filter(function(x){return x.id===A._variant})[0];A.unit=u;
      ask({id:'_opt',q:T('Anong promo ang kaya mo? (All-in, ','Which promo fits you? (All-in, ')+CFG.promo_term_months+' months)',t:'c',o:u.opts.map(function(o,i){return [i,(o.dp?peso(o.dp)+' DP':'Zero DP')+' · '+peso(o.mo)+'/mo']})},function(){
        ask({id:'_color',q:['Anong color ang gusto mo? (subject sa availability)','Which color do you prefer? (subject to availability)'],t:'c',o:COLORS.map(function(c){return [c,c]}).concat([['undecided','Bahala na / undecided','Undecided']])},function(){result()})})})});
}

/* ---------- Interactive computation + recommendation panel (estimates only) ---------- */
var TERMS=[12,24,36,48,60];
function estMo(fin,n){return fin*(1+CFG.est_addon_rates[n])/n}
function initCalc(S,res){
  var u=A.unit,P=u.price,inc=(A.gross_monthly_income||0)+(A.co_borrower==='yes'?(A.co_income||0):0),box=$('la-calc'),st={dp:Math.round(P*0.2),n:60};
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
   '<p class="fl">Term</p><div class="la-in" id="la-terms">'+TERMS.map(function(n){return '<button type="button" class="chip" data-n="'+n+'">'+yrs(n)+'</button>'}).join('')+'</div>'+
   '<dl class="la-sum" id="la-cres"></dl></div>'+
   '<div id="la-m-tg" hidden><div class="la-in"><label for="la-tgt" class="small">'+T('Magkano ang gusto mong monthly? (₱)','What monthly do you want? (₱)')+'</label><input type="number" id="la-tgt" inputmode="numeric" min="0" step="500"></div><table class="la-tbl" id="la-tgres"></table></div>'+
   '<div id="la-best"></div>'+
   '<h3 class="h3" style="margin-top:16px">'+T('Halimbawang computation','Sample computation')+': '+esc(u.n)+'</h3><table class="la-tbl"><thead><tr><th>Term</th><th>20% DP ('+peso(P*0.2)+')</th><th>40% DP ('+peso(P*0.4)+')</th></tr></thead><tbody>'+
     TERMS.map(function(n){return '<tr><td>'+n+' mo</td><td>'+peso(estMo(P*0.8,n))+'/mo</td><td>'+peso(estMo(P*0.6,n))+'/mo</td></tr>'}).join('')+'</tbody></table>'+
   '<p class="muted small">'+T('Estimate lang ito, subject sa bank evaluation. Ang final na rate at halaga ay manggagaling sa bank o dealer. Ang custom computation ay hindi pa kasama ang insurance, chattel mortgage, LTO at fees; ang dealer promo ay all-in.','Estimates only, subject to bank evaluation. Final rates and amounts come from the bank or dealer. Custom computations exclude insurance, chattel mortgage, LTO and fees; dealer promos are all-in.')+'</p>'+
   '<p class="la-ok" id="la-planok" hidden></p></div>');
  function mark(){box.querySelectorAll('[data-dpp]').forEach(function(b){b.classList.toggle('on',Math.abs(st.dp-Math.round(P*b.dataset.dpp/100))<1)});box.querySelectorAll('[data-n]').forEach(function(b){b.classList.toggle('on',+b.dataset.n===st.n)})}
  var LIST=[];
  function card(o,i,hl){return '<button type="button" class="la-opt'+(hl?' hl':'')+'" data-pick="'+i+'"><b>'+esc(o.label)+'</b><span>'+peso(o.mo)+'/mo × '+o.n+' · DP '+peso(o.dp)+'</span><span>Total '+peso(tot(o))+' · '+ratio(o)+' '+T('ng income','of income')+'</span>'+fitTxt(o)+'<em>'+T('Piliin ito','Choose this')+'</em></button>'}
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
    $('la-planok').hidden=false;$('la-planok').textContent=T('✓ Napili: ','✓ Selected: ')+o.label+' · '+peso(o.mo)+'/mo × '+o.n+'. '+T('Ime-message ka ni Richard para i-confirm sa bank o dealer.','Richard will message you to confirm with the bank or dealer.');
    crispSync();$('la-planok').scrollIntoView({block:'center',behavior:'smooth'});
    ga('select_plan',{plan_type:o.kind,term_months:o.n,unit:u.n,result:res});
    var L=Lead.base('loan_plan_select');L.name=A.name;L.mobile=A.mobile;L.chosenUnit=u.n;L.unitParam=u.id;L.language=A.lang;L.dpPreference=peso(A.plan.dp)+' DP ('+A.plan.dp_pct+'%)';
    L.planType=o.kind;L.planDp=A.plan.dp;L.planDpPct=A.plan.dp_pct;L.planTerm=o.n;L.planMonthly=A.plan.monthly;L.planTotal=A.plan.total_cost;
    L.timeline='Plan: '+o.kind+' '+A.plan.dp_pct+'% DP, '+o.n+' mo, '+peso(o.mo)+'/mo';L.usage='Selected plan ('+o.kind+'): DP '+peso(A.plan.dp)+', '+o.n+' mo, monthly '+peso(o.mo)+' (estimate), total '+peso(tot(o))+' | Language: '+A.lang;
    Lead.send(L)}
  box.querySelectorAll('[data-dpp]').forEach(function(b){b.onclick=function(){st.dp=Math.round(P*b.dataset.dpp/100);$('la-dpr').value=b.dataset.dpp;$('la-dpa').value='';$('la-dpw').hidden=true;calc()}});
  $('la-dpr').oninput=function(){st.dp=Math.round(P*this.value/100);$('la-dpa').value='';$('la-dpw').hidden=true;calc()};
  $('la-dpa').oninput=function(){var v=parseFloat(this.value),w=$('la-dpw');if(isNaN(v)||v<0)return;if(v>=P){w.hidden=false;w.textContent=T('Mas mataas sa presyo ang DP.','DP is higher than the price.');return}
    w.hidden=v>=P*CFG.calc_min_dp_pct/100;w.textContent=T('Karaniwang minimum ng bank ay '+CFG.calc_min_dp_pct+'% DP ('+peso(P*CFG.calc_min_dp_pct/100)+'). Pwede pa ring i-compute, pero mas malaki ang chance na hindi pumasa.','Banks usually require at least '+CFG.calc_min_dp_pct+'% DP ('+peso(P*CFG.calc_min_dp_pct/100)+'). We can still compute it, but it may not pass.');st.dp=v;calc()};
  box.querySelectorAll('[data-n]').forEach(function(b){b.onclick=function(){st.n=+b.dataset.n;calc()}});
  box.querySelectorAll('[data-mode]').forEach(function(b){b.onclick=function(){box.querySelectorAll('[data-mode]').forEach(function(x){x.classList.toggle('on',x===b)});$('la-m-dp').hidden=b.dataset.mode!=='dp';$('la-m-tg').hidden=b.dataset.mode!=='tg'}});
  $('la-tgt').oninput=function(){var t=parseFloat(this.value);if(isNaN(t)||t<=0){$('la-tgres').innerHTML='';return}
    var mn=P*CFG.calc_min_dp_pct/100;
    $('la-tgres').innerHTML=safe('<thead><tr><th>Term</th><th>'+T('Kailangang DP','DP needed')+'</th></tr></thead><tbody>'+TERMS.map(function(n){var dp=P-t*n/(1+CFG.est_addon_rates[n]);
      var cell=dp>=P*0.9?'<span class="la-fit no">'+T('Hindi kaya sa term na ito','Not possible on this term')+'</span>':dp<=mn?peso(mn)+' ('+CFG.calc_min_dp_pct+'% min) · ~'+peso(estMo(P-mn,n))+'/mo':peso(Math.ceil(dp/1000)*1000)+' ('+Math.round(dp/P*100)+'%)';return '<tr><td>'+n+' mo</td><td>'+cell+'</td></tr>'}).join('')+'</tbody>')};
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
function reqs(){var REQ={common:[T('2 valid government IDs (hindi expired)','2 valid government IDs (unexpired)'),T('Proof of billing (hindi lalampas ng 3 months)','Proof of billing (not older than 3 months)'),'Signed credit application','Data Privacy consent'],
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
function bindContact(el,res){el.addEventListener('click',function(e){var f=e.target.closest&&e.target.closest('[data-fina]');if(f){e.preventDefault();px('Contact',{method:'crisp_chat',content_name:A.unit.n});openFina()}});el.querySelectorAll('[data-c]').forEach(function(a){a.addEventListener('click',function(){px('Contact',{method:a.dataset.c,content_name:A.unit.n});ga('contact',{method:a.dataset.c,result:res})})})}
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
   '<div id="la-calc"></div><dl class="la-sum"><div><dt>Documents</dt><dd id="la-docsum">'+T('I-check sa Step 5','Check in Step 5')+'</dd></div><div><dt>Unit</dt><dd>'+esc(u.n)+' · '+esc(A._color==='undecided'?T('Bahala na','Undecided'):A._color)+'</dd></div><div><dt>SRP / promo price</dt><dd>'+peso(u.price)+'</dd></div><div><dt>Down payment</dt><dd>'+(S._dp?peso(S._dp):'Zero DP')+'</dd></div><div><dt>Monthly (promo, '+S._term+' mo)</dt><dd>'+peso(S._amort)+'</dd></div><div><dt>Monthly vs income</dt><dd>'+(S.affordability_ratio*100).toFixed(1)+'%</dd></div></dl>'+
   (S.recommendations.length?'<h2 class="h3">'+T('Mga options para pumasa','Options to qualify')+'</h2><ol class="la-rec">'+S.recommendations.map(function(x){return '<li>'+esc(x)+'</li>'}).join('')+'</ol>':'')+
   '<h2 class="h3">'+T('Banks na pwedeng i-try','Banks you can try')+'</h2><p>'+S.eligible_banks.map(esc).join(' · ')+'</p><p class="muted">'+T('Subject to bank evaluation. Hindi kami nagbibigay ng interest rate; ang bank ang magko-compute.','Subject to bank evaluation. We do not quote interest rates; the bank computes them.')+'</p>'+
   '<div id="la-docbox"><h2 class="h3">Step 5: Requirements checklist</h2><p>'+T('Base sa checklist ni Fina para sa '+esc(EMPL[et]||et)+'. I-tick ang mga documents na <b>meron ka na</b>. Wala pang upload dito.','Based on Fina\'s checklist for '+esc(EMPL[et]||et)+'. Tick the documents you <b>already have</b>. No uploads here yet.')+'</p><ul class="la-docs">'+req.map(function(x,i){return '<li><span>'+esc(x)+'</span><label><input type="checkbox" data-doc="'+i+'"'+(x.indexOf('Data Privacy')===0?' checked':'')+'> '+T('Meron na ako','I have this')+'</label></li>'}).join('')+'</ul><p class="la-cnt" id="la-cnt"></p><button class="btn" type="button" id="la-docsave">'+T('I-save ang checklist','Save checklist')+'</button><p id="la-docerr" class="er" hidden>'+T('Hindi na-save. Pakisubukan ulit.','Not saved. Please try again.')+'</p><div id="la-docres" hidden></div></div>'+
   contactBtns(res)+
   '<div class="la-next"><h2 class="h3">'+T('Ituloy ang full application','Continue to the full application')+'</h2><p>'+T('Malapit na: online full application with secure document upload at reference number para ma-track mo ang status. Gusto mo bang mauna? I-tap lang at ime-message ka ni Richard pag ready na.','Coming soon: an online full application with secure document upload and a reference number to track your status. Want to be first? Tap below and Richard will message you when it is ready.')+'</p><button class="btn" type="button" id="la-intent">'+T('Oo, gusto kong ituloy','Yes, I want to continue')+'</button><p id="la-intent-err" class="er" hidden>'+T('Hindi na-send. Pakisubukan ulit, o mag-message na lang sa Messenger.','Not sent. Please try again, or message us on Messenger.')+'</p><p id="la-intent-ok" class="la-ok" hidden>'+T('Salamat! Naka-note na. Ime-message ka namin pag bukas na ang full application. Pwede ka ring mag-message na ngayon.','Thank you! Noted. We will message you once the full application opens. You can also message us now.')+'</p></div>'+
   '<p class="muted small">'+T('Initial pre-screening lang ito base sa sagot mo, hindi bank approval. Lahat ng figures ay subject sa bank evaluation at promo validity (','This is an initial pre-screening based on your answers, not a bank approval. All figures are subject to bank evaluation and promo validity (')+esc($('la-note').textContent)+').</p></div>');
  bindContact(R,res);window.scrollTo(0,0);initCalc(S,res);
  /* lead capture: existing pipeline (Apps Script webhook via /assets/lead.js, honeypot + Turnstile) */
  var L=Lead.base('loan_assessment');L.name=A.name;L.mobile=A.mobile;L.chosenUnit=u.n;L.unitParam=u.id;L.dpPreference=S._dp?peso(S._dp)+' DP':'Zero DP';
  L.employment=et;L.seg=isOFW()?'ofw_abroad':'local';L.income=A.gross_monthly_income;L.timeline='Assessment: '+LBL[res];
  L.usage=['Result: '+LBL[res],'Monthly '+peso(S._amort)+' ('+(S.affordability_ratio*100).toFixed(1)+'% AFF, '+(S.dti_ratio*100).toFixed(1)+'% DTI)','Color: '+A._color,'Purpose: '+A.purpose,A.email?'Email: '+A.email:'','Rules: '+S.rule_results.map(function(x){return x.rule_id+'='+x.outcome}).join(','),S.red_flags.length?'Flags: '+S.red_flags.join(','):'','Banks: '+S.eligible_banks.join('/'),'Pref bank: '+A.preferred_bank,'Source: '+A.source_of_sale,'Consent: '+A.privacy_consent.version+' '+A.privacy_consent.timestamp].filter(Boolean).join(' | ');
  L.language=A.lang;L.usage+=' | Language: '+A.lang;L.docsTotal=req.length;L.docsReady=0;L.docsLacking=req.length;L.assessment=JSON.stringify({result:res,affordability_ratio:S.affordability_ratio,dti_ratio:S.dti_ratio,rule_results:S.rule_results,red_flags:S.red_flags,eligible_banks:S.eligible_banks,recommendations:S.recommendations});
  A.leadId=L.leadId;crispSync();
  Lead.send(L).then(function(){if(!Lead.skipped()){px('Lead',{content_name:u.n});ga('generate_lead',{form:'loan_assessment',unit:u.n,result:res,value:0,currency:'PHP'})}});
  /* Step 5: documents client already has (no uploads) */
  var boxes=R.querySelectorAll('[data-doc]');function cnt(){var r=0;boxes.forEach(function(b){if(b.checked)r++});$('la-cnt').textContent=r+' ready / '+(req.length-r)+T(' kulang',' lacking');return r}
  boxes.forEach(function(b){b.addEventListener('change',cnt)});cnt();
  $('la-docsave').addEventListener('click',function(){var btn=this,r=cnt(),lack=[];boxes.forEach(function(b){if(!b.checked)lack.push(req[+b.dataset.doc])});prog(5);
    $('la-docsum').textContent=r+' ready / '+lack.length+T(' kulang',' lacking');
    $('la-docres').innerHTML=safe(lack.length?'<div class="la-lack"><p><b>'+T('Kulang pa','Still lacking')+' ('+lack.length+'):</b></p><ul>'+lack.map(function(x){return '<li>'+esc(x)+'</li>'}).join('')+'</ul><p>'+T('Okay lang yan! Tutulungan ka nina Fina at Richard kung paano at saan makukuha ang mga ito, at ano ang pwedeng ipalit kung wala ka pa. Mag-message lang sa Messenger.','That\'s okay! Fina and Richard will help you with how and where to get these, and what alternatives you can use. Just message us on Messenger.')+'</p></div>':'<p class="la-ok">'+T('Wow, kumpleto ka na sa '+r+' documents! Ihanda lang ang malinaw na kopya. Tutulungan ka nina Fina at Richard sa next step.','Great, you have all '+r+' documents! Just prepare clear copies. Fina and Richard will help you with the next step.')+'</p>');
    $('la-docres').hidden=false;A.docs={ready:r,lacking:lack.length,missing:lack};crispSync();$('la-docres').insertAdjacentHTML('beforeend','<div class="la-cta">'+finaBtn()+'</div>');
    var D=Lead.base('loan_docs_checklist');D.leadId=L.leadId;D.name=A.name;D.mobile=A.mobile;D.chosenUnit=u.n;D.employment=et;D.docsReady=r;D.docsLacking=lack.length;D.docsTotal=req.length;D.language=A.lang;
    D.timeline='Docs: '+r+' ready / '+lack.length+' kulang ('+LBL[res]+')';D.usage='Docs ready '+r+'/'+req.length+(lack.length?' | Kulang: '+lack.join('; '):'');
    btn.disabled=true;btn.textContent=T('Sine-send...','Sending...');Lead.send(D).then(function(ok){if(ok===false)throw 0;btn.disabled=false;btn.textContent=T('✓ Na-save · I-update ang checklist','✓ Saved · Update checklist');$('la-docerr').hidden=true}).catch(function(){btn.disabled=false;btn.textContent=T('I-save ang checklist','Save checklist');$('la-docerr').hidden=false});ga('docs_checklist',{ready:r,lacking:lack.length,result:res})});
  $('la-intent').addEventListener('click',function(){var b=this;b.disabled=true;b.textContent=T('Sine-send...','Sending...');
    var I=Lead.base('loan_app_intent');I.name=A.name;I.mobile=A.mobile;I.chosenUnit=u.n;I.timeline='Wants full application ('+LBL[res]+')';I.usage='Phase 2 intent: full application | Language: '+A.lang;I.language=A.lang;
    Lead.send(I).then(function(ok){if(ok===false)throw 0;b.textContent=T('✓ Naka-note na','✓ Noted');b.classList.add('la-done');$('la-intent-err').hidden=true;$('la-intent-ok').hidden=false;ga('full_application_intent',{unit:u.n,result:res})}).catch(function(){b.disabled=false;b.textContent=T('Oo, gusto kong ituloy','Yes, I want to continue');$('la-intent-err').hidden=false})});
}
document.addEventListener('DOMContentLoaded',function(){try{AS.init($('la-f1'))}catch(_){}});
})();
