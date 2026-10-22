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
  promo_term_months:60                      // promo table term [U for Destinator/L300]
};
/* Messenger: ONE config value. Page username per Mark.
   Fallback (page ID): 'https://m.me/504759566043148' */
var MESSENGER_URL='https://m.me/MitsubishiRDC';
var CALL_TEL='tel:09542911201';
var BANNED=/\b(approved|aprobado|sure na|guaranteed|suzuki)\b/ig;
function safe(s){return String(s).replace(BANNED,'pre-qualified')}   // §2.4 banned-word filter

var $=function(i){return document.getElementById(i)};
var U=JSON.parse($('la-units').textContent);
var A={},log=$('la-log'),started=false,stepN=1;
function peso(n){return '₱'+Math.round(n).toLocaleString('en-PH')}
function esc(s){return String(s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
function px(ev,p){try{if(typeof window.fbq==='function'){if(ev==='StartAssessment'||ev==='SubmitApplication')window.fbq('trackCustom',ev,p||{});else window.fbq('track',ev,p||{})}}catch(_){}}
function ga(ev,p){try{if(typeof window.gtag==='function')window.gtag('event',ev,p||{})}catch(_){}}
/* Phase 2 stub: call after the backend returns an MP-XXXXX ref. Not fired in Phase 1. */
window.LoanApp={submitApplication:function(ref){if(!/^MP-[A-HJKMNP-Z2-9]{5}$/i.test(ref))return false;px('SubmitApplication',{ref_no:ref.toUpperCase()});ga('submit_application',{ref_no:ref.toUpperCase()});return true},CFG:CFG};

function prog(n){stepN=n;document.querySelectorAll('.la-steps li').forEach(function(li,i){li.className=i<n?'on':''})}
function bot(html){var d=document.createElement('div');d.className='la-b bot';d.innerHTML='<span class="la-av" aria-hidden="true">R</span><div class="la-bu">'+html+'</div>';log.appendChild(d);return d}
function me(t){var d=document.createElement('div');d.className='la-b me';d.innerHTML='<div class="la-bu">'+esc(t)+'</div>';log.appendChild(d)}
function scroll(el){setTimeout(function(){el.scrollIntoView({behavior:'smooth',block:'end'})},40)}

/* ---------- Step 1: contact + consent ---------- */
$('la-start').addEventListener('click',function(){
  $('la-intro').hidden=true;$('la-s1').hidden=false;prog(1);
  if(!started){started=true;px('StartAssessment',{page:'loan-assessment'});ga('start_assessment',{})}
  $('la-name').focus();
});
$('la-f1').addEventListener('submit',function(ev){ev.preventDefault();
  var nm=$('la-name').value.trim(),mob=$('la-mobile').value.replace(/[\s()-]/g,''),em=$('la-email').value.trim();
  var bad=[Lead.err('la-name',nm.length<2),Lead.err('la-mobile',!/^(09\d{9}|\+639\d{9})$/.test(mob)),Lead.err('la-email',!!em&&!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(em)),Lead.err('la-consent',!$('la-consent').checked)];
  if(bad.some(Boolean))return;
  A.name=nm;A.mobile=mob;A.email=em;A.privacy_consent={accepted:true,timestamp:new Date().toISOString(),version:CFG.consent_version};
  $('la-s1').hidden=true;$('la-chat').hidden=false;prog(2);
  bot('Salamat, <b>'+esc(nm.split(' ')[0])+'</b>! Ilang tanong lang tungkol sa income at trabaho mo. Mga 2 minuto lang ito.');
  next(0);
});

/* ---------- Step 2/3: question engine (rulebook §1 order, scoring subset) ---------- */
var EMP=[['employed','Employed'],['business_owner','Business owner'],['ofw','OFW'],['seafarer','Seafarer'],['freelancer','Freelancer / VA'],['pensioner','Pensioner'],['other','Iba pa']];
function isOFW(){return A.employment_type==='ofw'||A.employment_type==='seafarer'}
var Q=[
 {id:'purpose',q:'Para saan gagamitin ang sasakyan?',t:'c',o:[['personal','Personal / family'],['business','Business'],['tnvs','Grab / TNVS'],['other','Iba pa']]},
 {id:'dob',q:'Kailan ang birthday mo?',t:'date'},
 {id:'civil_status',q:'Civil status?',t:'c',o:[['single','Single'],['married','Married'],['widowed','Widowed'],['separated','Separated']]},
 {id:'residential_status',q:'Owned, rented, o nakatira sa family ang bahay?',t:'c',o:[['owned','Owned'],['mortgaged','Mortgaged / hinuhulugan'],['rented','Rented'],['living_with_relatives','Kasama ang family'],['company_provided','Company-provided']]},
 {id:'length_of_stay_years',q:'Gaano ka na katagal diyan? (taon, hal. 0.5 kung 6 months)',t:'n',min:0,max:80,step:0.5},
 {id:'employment_type',q:'Ano ang source of income mo?',t:'c',o:EMP},
 {id:'years_in_employment',q:'Ilang taon ka na sa trabaho o negosyo na ito? (hal. 0.5 kung 6 months)',t:'n',min:0,max:60,step:0.5,show:function(){return A.employment_type!=='pensioner'}},
 {id:'employment_status',q:'Permanent, probationary, o contractual ka?',t:'c',o:[['permanent','Permanent / regular'],['probationary','Probationary'],['contractual','Contractual']],show:function(){return A.employment_type==='employed'}},
 {id:'biz_profitable',q:'Kumikita (profitable) ba ang negosyo sa huling 2 taon, may ITR o FS?',t:'c',o:[['yes','Oo'],['no','Hindi pa / walang ITR']],show:function(){return A.employment_type==='business_owner'}},
 {id:'ofw_contract',q:'May active contract ka ba ngayon?',t:'c',o:[['yes','Oo'],['no','Wala pa']],show:isOFW},
 {id:'ofw_remit',q:'May 3–6 months remittance proof ka ba?',t:'c',o:[['yes','Oo'],['no','Wala pa']],show:isOFW},
 {id:'ofw_aif',q:'May magiging attorney-in-fact (AIF) ka ba dito sa PH, na pwedeng pirmahan ng SPA?',t:'c',o:[['yes','Oo, meron'],['maybe','Hahanap pa'],['no','Wala talaga']],show:isOFW},
 {id:'gross_monthly_income',q:'Magkano ang gross monthly income mo? (₱)',t:'n',min:0,max:100000000,step:500},
 {id:'other_household_income',q:'May iba pang income sa household (hal. spouse)? Magkano kada buwan? Ilagay ang 0 kung wala.',t:'n',min:0,max:100000000,step:500},
 {id:'existing_monthly_obligations',q:'May binabayaran ka bang loans ngayon (housing, car, personal, credit card minimum)? Magkano lahat kada buwan? 0 kung wala.',t:'n',min:0,max:100000000,step:500},
 {id:'co_borrower',q:'May co-borrower o co-maker ka ba? (hal. spouse o kamag-anak na may income)',t:'c',o:[['yes','Oo, meron'],['no','Wala']]},
 {id:'co_income',q:'Magkano ang gross monthly income ng co-maker? (₱)',t:'n',min:0,max:100000000,step:500,show:function(){return A.co_borrower==='yes'}},
 {id:'registered_owner',q:'Kanino ipapangalan ang unit?',t:'c',o:[['self','Sa akin'],['other','Sa ibang tao']]},
 {id:'preferred_bank',q:'May preferred bank ka ba?',t:'c',o:[['no_preference','Wala, kayo na bahala'],['MMPF','Mitsubishi Motors Finance PH'],['BPI','BPI'],['BDO','BDO'],['Metrobank','Metrobank'],['Security Bank','Security Bank'],['PSBank','PSBank'],['RCBC','RCBC'],['EastWest','EastWest']]},
 {id:'source_of_sale',q:'Last na: paano mo kami nahanap?',t:'c',o:[['facebook','Facebook'],['google','Google'],['referral','Referral'],['walk_in','Walk-in'],['other','Iba pa']]}
];
function next(i){while(i<Q.length&&Q[i].show&&!Q[i].show())i++;if(i>=Q.length){unitStep();return}ask(Q[i],function(){next(i+1)})}
function ask(q,done){
  var b=bot(esc(q.q)),bu=b.querySelector('.la-bu'),w=document.createElement('div');w.className='la-in';
  if(q.t==='c'){q.o.forEach(function(o){var x=document.createElement('button');x.type='button';x.className='chip';x.textContent=o[1];
     x.onclick=function(){A[q.id]=o[0];w.remove();me(o[1]);done()};w.appendChild(x)})}
  else{var inp=document.createElement('input');inp.type=q.t==='date'?'date':'number';inp.inputMode=q.t==='n'?'decimal':'';
    if(q.t==='n'){inp.min=q.min;inp.max=q.max;inp.step=q.step}else{var t=new Date();inp.max=t.toISOString().slice(0,10)}
    inp.setAttribute('aria-label',q.q);var ok=document.createElement('button');ok.type='button';ok.className='btn sm';ok.textContent='OK';
    var er=document.createElement('p');er.className='er';er.hidden=true;er.textContent=q.t==='date'?'Pakilagay ang tamang petsa.':'Pakilagay ang tamang numero.';
    var go=function(){var v=inp.value;if(q.t==='n'){var n=parseFloat(v);if(isNaN(n)||n<q.min||n>q.max){er.hidden=false;return}A[q.id]=n;w.remove();me(q.id.indexOf('income')>=0||q.id.indexOf('oblig')>=0?peso(n):String(n))}
      else{if(!v||new Date(v)>new Date()){er.hidden=false;return}A[q.id]=v;w.remove();me(new Date(v+'T00:00').toLocaleDateString('en-PH',{year:'numeric',month:'long',day:'numeric'}))}done()};
    ok.onclick=go;inp.onkeydown=function(e){if(e.key==='Enter'){e.preventDefault();go()}};w.appendChild(inp);w.appendChild(ok);w.appendChild(er);setTimeout(function(){inp.focus({preventScroll:true})},60)}
  bu.appendChild(w);scroll(b);
}
var COLORS=['White Pearl','Silver','Graphite Gray','Black','Red','Bahala na / undecided'];
function unitStep(){prog(3);
  bot('Ayos! Ngayon, piliin natin ang <b>unit</b>. Ang DP at monthly ay galing sa promo ngayong buwan.');
  var models=[];U.forEach(function(u){if(models.indexOf(u.model)<0)models.push(u.model)});
  ask({id:'_model',q:'Anong Mitsubishi model ang gusto mo?',t:'c',o:models.map(function(m){return [m,m]})},function(){
    var vs=U.filter(function(u){return u.model===A._model});
    ask({id:'_variant',q:'Anong variant?',t:'c',o:vs.map(function(u){return [u.id,u.n+' · SRP '+peso(u.price)]})},function(){
      var u=U.filter(function(x){return x.id===A._variant})[0];A.unit=u;
      ask({id:'_opt',q:'Anong promo ang kaya mo? (All-in, '+CFG.promo_term_months+' months)',t:'c',o:u.opts.map(function(o,i){return [i,(o.dp?peso(o.dp)+' DP':'Zero DP')+' · '+peso(o.mo)+'/mo']})},function(){
        ask({id:'_color',q:'Anong color ang gusto mo? (subject sa availability)',t:'c',o:COLORS.map(function(c){return [c,c]})},function(){result()})})})});
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
  if(et==='employed'){var T=CFG.ten_employed;r('TEN-01',(y>=T.pass_regular_yrs&&A.employment_status==='permanent')||(A.employment_status==='permanent'&&y>=T.pass_permanent_yrs)?'pass':y<T.fail_below_yrs?'fail':'review',y+' yrs, '+A.employment_status)}
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
        if(need<u.price*0.9)rec.push('Mas mataas na DP: mga '+peso(Math.ceil(need/1000)*1000)+' DP para bumaba ang monthly sa ~'+peso(target)+' (30% ng income). Estimate lang ito, subject sa bank computation.')}
      else rec.push('Mas mataas na DP: ipapa-compute namin sa bank kung magkano ang DP para bumaba ang monthly sa ~'+peso(target)+'.')}
    if(term<CFG.max_term)rec.push('Mas mahabang term: '+CFG.max_term+' months.');
    if(amort>target){var ch=U.filter(function(x){return x.id!==u.id&&Math.min.apply(null,x.opts.map(function(p){return p.mo}))<=target}).sort(function(a,b){return Math.min.apply(null,b.opts.map(function(p){return p.mo}))-Math.min.apply(null,a.opts.map(function(p){return p.mo}))})[0];
      rec.push(ch?'Mas abot-kayang unit: '+ch.n+' (from '+peso(Math.min.apply(null,ch.opts.map(function(p){return p.mo})))+'/mo).':'Mas abot-kayang unit: L300 o Mirage G4, ipapa-quote namin ang pinakabagong promo.')}
    if(co===0&&(amort>target||isOFW()||dti>CFG.dti.pass))rec.push('Mag-add ng co-maker: spouse o kamag-anak na may income'+(isOFW()?' (kailangan ng PH co-maker sa Security Bank; spouse co-maker sa EastWest kung married).':'.'));
    if(hardFail)rec.push('Pwede tayong mag-try ulit after ma-build ang income o tenure. Pwede ka naming i-follow up in 3–6 months kung gusto mo.');
    if(flags.indexOf('RF-08')>=0)rec.push('Kung sa ibang tao ipapangalan ang unit, siya ang dapat mag-apply bilang borrower. Pag-usapan natin.');
  }
  return {result:res,affordability_ratio:+aff.toFixed(4),dti_ratio:+dti.toFixed(4),rule_results:R,red_flags:flags,eligible_banks:banks,recommendations:rec.slice(0,3),_amort:amort,_fin:fin,_dp:o.dp,_term:term,_dpPct:dpPct};
}
var REQ={common:['2 valid government IDs (hindi expired)','Proof of billing (hindi lalampas ng 3 months)','Signed credit application','Data Privacy consent'],
 employed:['COE with compensation','Latest 3 months payslips','ITR / BIR 2316'],
 business_owner:['DTI / SEC registration','Mayor\'s permit','3–6 months bank statements','Audited FS / ITR'],
 ofw:['Employment contract','3–6 months remittance proof','IDs ng AIF + SPA'],
 freelancer:['PayPal / Wise statements','Client contracts','6 months bank statements'],
 comaker:['Co-maker: 2 IDs + sariling income documents']};
REQ.seafarer=REQ.ofw;REQ.pensioner=['Pension statement / proof of pension'];REQ.other=['Proof of income (ipapaalam namin kung ano)'];
var EMPL={employed:'Employed',business_owner:'Business owner',ofw:'OFW',seafarer:'Seafarer',freelancer:'Freelancer / VA',pensioner:'Pensioner',other:'iba pang income type'};
var LBL={PRE_QUALIFIED:'Pre-qualified',NEEDS_REVIEW:'Needs Review',NOT_YET_QUALIFIED:'Not yet qualified'};
function msgr(res){var ref=('loan-assessment-'+res.toLowerCase().replace(/_/g,'-')+'-'+A.unit.id).replace(/[^a-z0-9-]/gi,'').slice(0,240);return MESSENGER_URL+'?ref='+encodeURIComponent(ref)}
function contactBtns(res){return '<div class="la-cta"><a class="btn la-msg" href="'+msgr(res)+'" rel="noopener" data-c="messenger">💬 Makipag-usap sa tao sa Messenger</a><a class="btn ghost dk" href="'+CALL_TEL+'" data-c="call">📞 Tumawag: 0954 291 1201</a></div>'}
function bindContact(el,res){el.querySelectorAll('[data-c]').forEach(function(a){a.addEventListener('click',function(){px('Contact',{method:a.dataset.c,result:res,content_name:A.unit.n});ga('contact',{method:a.dataset.c,result:res})})})}
function result(){
  var S=assess(),u=A.unit,first=A.name.split(' ')[0],res=S.result;A.assessment=S;prog(4);
  var head={PRE_QUALIFIED:'Good news, '+first+'! Base sa initial assessment, <b>Pre-qualified</b> ka para sa '+esc(u.n)+'. Hindi pa ito bank approval. Ang final decision ay sa bank pa rin. Next step: i-ready ang requirements.',
   NEEDS_REVIEW:'Hi '+first+', kailangan pa naming i-review ang ilang details ng assessment mo para sa '+esc(u.n)+'. Tatawagan o ime-message ka ni Richard, ang sales consultant mo.',
   NOT_YET_QUALIFIED:'Hi '+first+', salamat sa interest! Sa ngayon, hindi pa pasok ang profile sa requirements. Pero may options tayo, tingnan sa baba. Gusto mo bang i-try natin ang isa dito?'}[res];
  var et=A.employment_type,req=REQ.common.concat(REQ[et]||[]).concat(A.co_borrower==='yes'||S.recommendations.join().indexOf('co-maker')>=0?REQ.comaker:[]);
  $('la-chat').hidden=true;var R=$('la-res');R.hidden=false;
  R.innerHTML=safe('<div class="la-card res-'+res.toLowerCase()+'"><p class="kick">Resulta ng assessment</p><p class="la-badge">'+LBL[res]+'</p><p>'+head+'</p>'+
   '<dl class="la-sum"><div><dt>Documents</dt><dd id="la-docsum">I-check sa Step 5</dd></div><div><dt>Unit</dt><dd>'+esc(u.n)+' · '+esc(A._color)+'</dd></div><div><dt>SRP / promo price</dt><dd>'+peso(u.price)+'</dd></div><div><dt>Down payment</dt><dd>'+(S._dp?peso(S._dp):'Zero DP')+'</dd></div><div><dt>Monthly (promo, '+S._term+' mo)</dt><dd>'+peso(S._amort)+'</dd></div><div><dt>Monthly vs income</dt><dd>'+(S.affordability_ratio*100).toFixed(1)+'%</dd></div></dl>'+
   (S.recommendations.length?'<h2 class="h3">Mga options para pumasa</h2><ol class="la-rec">'+S.recommendations.map(function(x){return '<li>'+esc(x)+'</li>'}).join('')+'</ol>':'')+
   '<h2 class="h3">Banks na pwedeng i-try</h2><p>'+S.eligible_banks.map(esc).join(' · ')+'</p><p class="muted">Subject to bank evaluation. Hindi kami nagbibigay ng interest rate; ang bank ang magko-compute.</p>'+
   '<div id="la-docbox"><h2 class="h3">Step 5: Requirements checklist</h2><p>Base sa checklist ni Fina para sa '+esc(EMPL[et]||et)+'. I-tick ang mga documents na <b>meron ka na</b>. Wala pang upload dito.</p><ul class="la-docs">'+req.map(function(x,i){return '<li><span>'+esc(x)+'</span><label><input type="checkbox" data-doc="'+i+'"'+(x.indexOf('Data Privacy')===0?' checked':'')+'> Meron na ako</label></li>'}).join('')+'</ul><p class="la-cnt" id="la-cnt">0 ready / '+req.length+' kulang</p><button class="btn" type="button" id="la-docsave">I-save ang checklist</button><div id="la-docres" hidden></div></div>'+
   contactBtns(res)+
   '<div class="la-next"><h2 class="h3">Ituloy ang full application</h2><p>Malapit na: online full application with secure document upload at reference number para ma-track mo ang status. Gusto mo bang mauna? I-tap lang at ime-message ka ni Richard pag ready na.</p><button class="btn" type="button" id="la-intent">Oo, gusto kong ituloy</button><p id="la-intent-ok" class="la-ok" hidden>Salamat! Naka-note na. Ime-message ka namin pag bukas na ang full application. Pwede ka ring mag-message na ngayon.</p></div>'+
   '<p class="muted small">Initial pre-screening lang ito base sa sagot mo, hindi bank approval. Lahat ng figures ay subject sa bank evaluation at promo validity ('+esc($('la-note').textContent)+').</p></div>');
  bindContact(R,res);window.scrollTo(0,0);
  /* lead capture: existing pipeline (Apps Script webhook via /assets/lead.js, honeypot + Turnstile) */
  var L=Lead.base('loan_assessment');L.name=A.name;L.mobile=A.mobile;L.chosenUnit=u.n;L.unitParam=u.id;L.dpPreference=S._dp?peso(S._dp)+' DP':'Zero DP';
  L.employment=et;L.seg=isOFW()?'ofw_abroad':'local';L.income=A.gross_monthly_income;L.timeline='Assessment: '+LBL[res];
  L.usage=['Result: '+LBL[res],'Monthly '+peso(S._amort)+' ('+(S.affordability_ratio*100).toFixed(1)+'% AFF, '+(S.dti_ratio*100).toFixed(1)+'% DTI)','Color: '+A._color,'Purpose: '+A.purpose,A.email?'Email: '+A.email:'','Rules: '+S.rule_results.map(function(x){return x.rule_id+'='+x.outcome}).join(','),S.red_flags.length?'Flags: '+S.red_flags.join(','):'','Banks: '+S.eligible_banks.join('/'),'Pref bank: '+A.preferred_bank,'Source: '+A.source_of_sale,'Consent: '+A.privacy_consent.version+' '+A.privacy_consent.timestamp].filter(Boolean).join(' | ');
  L.docsTotal=req.length;L.docsReady=0;L.docsLacking=req.length;L.assessment=JSON.stringify({result:res,affordability_ratio:S.affordability_ratio,dti_ratio:S.dti_ratio,rule_results:S.rule_results,red_flags:S.red_flags,eligible_banks:S.eligible_banks,recommendations:S.recommendations});
  Lead.send(L).then(function(){if(!Lead.skipped()){px('Lead',{content_name:u.n,content_category:'loan_assessment',status:res});ga('generate_lead',{form:'loan_assessment',unit:u.n,result:res,value:0,currency:'PHP'})}});
  /* Step 5: documents client already has (no uploads) */
  var boxes=R.querySelectorAll('[data-doc]');function cnt(){var r=0;boxes.forEach(function(b){if(b.checked)r++});$('la-cnt').textContent=r+' ready / '+(req.length-r)+' kulang';return r}
  boxes.forEach(function(b){b.addEventListener('change',cnt)});cnt();
  $('la-docsave').addEventListener('click',function(){var btn=this,r=cnt(),lack=[];boxes.forEach(function(b){if(!b.checked)lack.push(req[+b.dataset.doc])});prog(5);
    $('la-docsum').textContent=r+' ready / '+lack.length+' kulang';
    $('la-docres').innerHTML=safe(lack.length?'<div class="la-lack"><p><b>Kulang pa ('+lack.length+'):</b></p><ul>'+lack.map(function(x){return '<li>'+esc(x)+'</li>'}).join('')+'</ul><p>Okay lang yan! Tutulungan ka nina Fina at Richard kung paano at saan makukuha ang mga ito, at ano ang pwedeng ipalit kung wala ka pa. Mag-message lang sa Messenger.</p></div>':'<p class="la-ok">Wow, kumpleto ka na sa '+r+' documents! Ihanda lang ang malinaw na kopya. Tutulungan ka nina Fina at Richard sa next step.</p>');
    $('la-docres').hidden=false;btn.textContent='I-update ang checklist';
    var D=Lead.base('loan_docs_checklist');D.leadId=L.leadId;D.name=A.name;D.mobile=A.mobile;D.chosenUnit=u.n;D.employment=et;D.docsReady=r;D.docsLacking=lack.length;D.docsTotal=req.length;
    D.timeline='Docs: '+r+' ready / '+lack.length+' kulang ('+LBL[res]+')';D.usage='Docs ready '+r+'/'+req.length+(lack.length?' | Kulang: '+lack.join('; '):'');
    Lead.send(D);ga('docs_checklist',{ready:r,lacking:lack.length,result:res})});
  $('la-intent').addEventListener('click',function(){var b=this;b.disabled=true;b.textContent='Sending...';
    var I=Lead.base('loan_app_intent');I.name=A.name;I.mobile=A.mobile;I.chosenUnit=u.n;I.timeline='Wants full application ('+LBL[res]+')';I.usage='Phase 2 intent: full application';
    Lead.send(I).then(function(){b.hidden=true;$('la-intent-ok').hidden=false;ga('full_application_intent',{unit:u.n,result:res})})});
}
document.addEventListener('DOMContentLoaded',function(){try{AS.init($('la-f1'))}catch(_){}});
})();
