/* Official Application Form (/apply/). Static: submits via /assets/lead.js (Apps Script -> Google Sheet, honeypot + Turnstile).
   Spec: Fina audit rulebook v1.0 §1 fields, §5 reference format. Per-requirement status (Ready / To follow) is sent as text. File uploads are behind UPLOADS_ON (off until the Apps Script handler is deployed).
   Meta Pixel: SubmitApplication custom event only, with NO PII / income / credit / assessment data. */
(function(){
'use strict';
var $=function(i){return document.getElementById(i)};
var CRISP_WEBSITE_ID='ca443e7b-7d1e-4819-87d3-59b97b4fa8c8';
var REF_ALPHA='ABCDEFGHJKMNPQRSTUVWXYZ23456789';   // rulebook §5: excludes 0,O,1,I,L
var REF_RE=/^MP-[A-HJKMNP-Z2-9]{5}$/i;
var BANNED=/\b(approved|aprobado|sure na|guaranteed|suzuki)\b/ig;
function safe(s){return String(s).replace(BANNED,'pre-qualified')}
var U=JSON.parse($('af-units').textContent),lang='en',P=null;
function T(t,e){return lang==='en'?e:t}
function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
function peso(n){return '₱'+Math.round(n).toLocaleString('en-PH')}
function px(ev,p){try{if(typeof window.fbq==='function')window.fbq('trackCustom',ev,p||{})}catch(_){}}
function ga(ev,p){try{if(typeof window.gtag==='function')window.gtag('event',ev,p||{})}catch(_){}}
function cp(){try{window.$crisp=window.$crisp||[];window.$crisp.push([].slice.call(arguments))}catch(_){}}
function crispLoad(){if(window.__crispLoaded)return;window.__crispLoaded=true;window.$crisp=window.$crisp||[];window.CRISP_WEBSITE_ID=CRISP_WEBSITE_ID;
  var d=document.createElement('script');d.src='https://client.crisp.chat/l.js';d.async=1;document.head.appendChild(d)}
/* MP-XXXXX with crypto randomness + rejection sampling (31 chars; 248 = 31*8). Uniqueness is enforced server-side in Phase 2. */
function newRef(){var s='',b=new Uint8Array(1),c=window.crypto||window.msCrypto;while(s.length<5){c.getRandomValues(b);if(b[0]<248)s+=REF_ALPHA[b[0]%31]}return 'MP-'+s}
window.ApplyForm={newRef:newRef,REF_RE:REF_RE};

/* ---------- language ---------- */
function setLang(l){lang=l;document.documentElement.setAttribute('data-lang',l);try{localStorage.setItem('site_lang',l)}catch(_){}
  document.querySelectorAll('option[data-tl]').forEach(function(o){o.textContent=l==='en'?o.dataset.en:o.dataset.tl});renderDocs();unitHints();if(window.__afw){stepT();if(STEP===NST)review()}}
document.querySelectorAll('[data-setlang]').forEach(function(b){b.addEventListener('click',function(){setLang(b.dataset.setlang)})});

/* ---------- conditional sections ---------- */
function val(i){var e=$(i);return e?String(e.value).trim():''}
function vis(){document.querySelectorAll('[data-show]').forEach(function(el){var p=el.dataset.show.split(':');el.hidden=p[1].split(',').indexOf(val(p[0]))<0});
  $('af-rentw').hidden=val('res')!=='rented';
  var n=0;document.querySelectorAll('#af .la-card').forEach(function(c){var s=c.querySelector('[data-num]');if(s&&!c.hidden){n++;s.textContent=n+'. '}});
  var cmo=document.querySelector('#cm option[value=spouse]');if(cmo){cmo.disabled=val('civil')!=='married';if(cmo.disabled&&val('cm')==='spouse')$('cm').value='no'}}

/* ---------- units (same data as the assessment: per-variant colors, Versa Van) ---------- */
function opt(v,t){var o=document.createElement('option');o.value=v;o.textContent=t;return o}
function fillModels(){var s=$('model'),seen={};U.forEach(function(u){if(!seen[u.model]){seen[u.model]=1;s.appendChild(opt(u.model,u.model))}})}
function fillVariants(){var s=$('variant');s.length=1;U.filter(function(u){return u.model===val('model')}).forEach(function(u){s.appendChild(opt(u.id,u.n+(u.price?' · SRP '+peso(u.price):'')))});if(s.length===2)s.selectedIndex=1;fillColors()}
function unit(){return U.filter(function(u){return u.id===val('variant')})[0]||null}
function fillColors(){var s=$('color'),u=unit(),keep=s.value;s.length=1;
  (u&&u.colors.length?u.colors:[]).forEach(function(c){s.appendChild(opt(c[0],c[1]?c[0]+' (+'+peso(c[1])+')':c[0]))});
  var o=opt('undecided',T('Bahala na / undecided','Undecided'));o.dataset.tl='Bahala na / undecided';o.dataset.en='Undecided';s.appendChild(o);
  if(keep)s.value=keep;unitHints()}
function term(){return document.querySelector('[name=tu]:checked').value==='m'?+$('term_m').value:+$('term_y').value}
function unitHints(){var u=unit(),h=$('af-price'),d=$('af-dphint');if(!h)return;if(!u){h.textContent='';d.textContent='';return}
  h.textContent=u.price?'SRP / promo price: '+peso(u.price):T('Presyo: itatanong namin sa dealer.','Price: we will confirm with the dealer.');
  var dp=parseFloat(val('dp'));d.textContent=(u.price&&!isNaN(dp)?Math.round(dp/u.price*1000)/10+'% DP. ':'')+
    (u.opts.length?T('Promo ngayong buwan: ','This month\'s promo: ')+u.opts.map(function(o){return (o.dp?peso(o.dp)+' DP':'Zero DP')+' → '+peso(o.mo)+'/mo (60 '+T('buwan','mo')+', all-in)'}).join(' · '):'')}

/* ---------- requirements (mirrors the assessment checklist, rulebook §4) ---------- */
var REQ={common:[['2 valid government IDs (hindi expired)','2 valid government IDs (unexpired)'],['Proof of billing (hindi lalampas ng 3 months)','Proof of billing (not older than 3 months)']],
 employed:[['COE with compensation'],['Latest 3 months payslips'],['ITR / BIR 2316']],
 business_owner:[['DTI / SEC registration'],['Mayor\'s permit'],['3–6 months bank statements'],['Audited FS / ITR']],
 ofw:[['Employment contract'],['3–6 months remittance proof'],['IDs ng AIF + SPA','AIF\'s IDs + SPA']],
 freelancer:[['PayPal / Wise statements'],['Client contracts'],['6 months bank statements']],
 pensioner:[['Pension statement / proof of pension']],other:[['Proof of income (ipapaalam namin kung ano)','Proof of income (we will tell you which)']],
 comaker:[['Co-maker: 2 IDs + sariling income documents','Co-maker: 2 IDs + own income documents']]};
REQ.seafarer=REQ.ofw;
var have={},later={},files={};  // key = Tagalog label -> true / File info
/* FEATURE FLAG: real uploads need the Apps Script upload handler (see /workspace/loanapp/uploads/apps_script_uploads.gs). Keep false until verified end-to-end. */
var UPLOADS_ON=true,MAXF=(window.Lead&&Lead.V4)?10:5,MAXB=5*1024*1024;
function stat(k){return files[k]?'Uploaded':have[k]?'Ready (send in chat)':'To follow'}
function reqList(){var e=val('emp'),l=REQ.common.concat(REQ[e]||[]);if(val('cm')==='yes'||val('cm')==='spouse')l=l.concat(REQ.comaker);return l}
function renderDocs(){var ul=$('af-docs');if(!ul)return;var l=reqList();
  document.querySelectorAll('.af-up').forEach(function(e){e.hidden=!UPLOADS_ON});
  ul.innerHTML=l.map(function(x,i){var k=x[0],f=files[k];return '<li class="af-rq"><span class="af-rn">'+esc(lang==='en'&&x[1]?x[1]:x[0])+'</span><div class="af-st">'+
   '<label><input type="radio" name="rq'+i+'" value="ready" data-k="'+esc(k)+'"'+(have[k]?' checked':'')+'> '+(UPLOADS_ON?'📎 '+T('Meron na / I-upload','I have it / Upload'):'✅ '+T('Meron na ako','I have this'))+'</label>'+
   '<label><input type="radio" name="rq'+i+'" value="later" data-k="'+esc(k)+'"'+(later[k]?' checked':'')+'> ⏳ '+T('Susunod na lang','I\'ll submit later')+'</label></div>'+
   (UPLOADS_ON&&have[k]?'<div class="af-fl"><div class="af-cam st-pick"><label>📷 '+T('Kumuha ng Photo','Take Photo')+'<input type="file" accept="image/*" capture="environment" data-k="'+esc(k)+'"></label><label>📁 '+T('Pumili ng file','Choose file')+'<input type="file" accept="image/*,application/pdf" data-k="'+esc(k)+'"></label></div><p class="af-fn">'+(f?'📎 '+esc(f.name):T('Optional: i-upload ngayon','Optional: upload now'))+'</p></div>':'')+'</li>'}).join('');
  ul.querySelectorAll('input[type=radio]').forEach(function(b){b.onchange=function(){var k=b.dataset.k;have[k]=b.value==='ready';later[k]=b.value==='later';if(!have[k])delete files[k];renderDocs()}});
  ul.querySelectorAll('input[type=file]').forEach(function(b){b.onchange=function(){pick(b)}});cnt()}
function pick(b){var k=b.dataset.k,f=b.files&&b.files[0],n=b.closest('.af-fl').querySelector('.af-fn');if(!f)return;
  if(!/^image\/|^application\/pdf$/.test(f.type)){n.textContent=T('Photo o PDF lang.','Photo or PDF only.');b.value='';return}
  if(!files[k]&&Object.keys(files).length>=MAXF){n.textContent=T('Hanggang '+MAXF+' files lang. Ipadala ang iba kay Fina.','Max '+MAXF+' files. Send the rest to Fina.');b.value='';return}
  n.textContent=T('Pinoproseso...','Processing...');
  (/^image\//.test(f.type)?shrink(f):readB64(f)).then(function(o){if(o.data.length*0.75>MAXB){n.textContent=T('Masyadong malaki (max 5MB).','Too large (max 5MB).');b.value='';return}
    o.name=f.name;o.req=lbl(k);files[k]=o;n.textContent='📎 '+f.name;cnt()}).catch(function(){n.textContent=T('Hindi mabasa ang file.','Could not read the file.')})}
function readB64(f){return new Promise(function(r,j){var fr=new FileReader();fr.onload=function(){r({type:f.type,data:String(fr.result).split(',')[1]})};fr.onerror=j;fr.readAsDataURL(f)})}
function shrink(f){return new Promise(function(r,j){var im=new Image(),u=URL.createObjectURL(f);im.onload=function(){var m=1600,sc=Math.min(1,m/Math.max(im.width,im.height)),c=document.createElement('canvas');c.width=Math.round(im.width*sc);c.height=Math.round(im.height*sc);
  c.getContext('2d').drawImage(im,0,0,c.width,c.height);URL.revokeObjectURL(u);r({type:'image/jpeg',data:c.toDataURL('image/jpeg',0.8).split(',')[1]})};im.onerror=function(){readB64(f).then(r,j)};im.src=u})}
function lbl(k){var x=reqList().filter(function(y){return y[0]===k})[0];return x?(x[1]||x[0]):k}
function docStatus(){return reqList().map(function(x){return (x[1]||x[0])+': '+stat(x[0])})}
function missing(){return reqList().filter(function(x){return !have[x[0]]})}
function cnt(){var l=reqList(),m=missing(),u=l.filter(function(x){return files[x[0]]}).length;$('af-cnt').textContent=(l.length-m.length)+' ready / '+m.length+T(' to follow',' to follow')+(u?' · '+u+' uploaded':'')}

/* ---------- prefill from the assessment (sessionStorage 'mp_app_prefill', written by loan-assessment.js) ---------- */
function setV(i,v){var e=$(i);if(e&&v!=null&&v!==''){e.value=String(v);if(e.tagName==='SELECT'&&e.value!==String(v))e.value=''}}
function ym(i,m){if(m==null||isNaN(m))return;m=Math.round(m);setV(i+'_y',Math.min(40,Math.floor(m/12)));setV(i+'_m',m%12)}
function prefill(){try{P=JSON.parse(sessionStorage.getItem('mp_app_prefill')||'null')}catch(_){P=null}
  if(!P){var q=new URLSearchParams(location.search).get('unit');if(q){q=q.replace(/[^a-z0-9-]/gi,'');var u=U.filter(function(x){return x.id===q})[0]||U.filter(function(x){return x.slug===q})[0];if(u){setV('model',u.model);fillVariants();if(u.id===q)setV('variant',u.id);fillColors()}}return}
  var nm=String(P.name||'').trim().split(/\s+/);if(nm.length>1){setV('last',nm.pop());setV('first',nm.join(' '))}else setV('first',nm[0]);
  setV('mobile',P.mobile);setV('email',P.email);setV('dob',P.dob);setV('civil',P.civil_status);setV('res',P.residential_status);ym('stay',P.stay_months);
  setV('emp',P.employment_type);setV('estat',P.employment_status);ym('ten',P.tenure_months);setV('gross',P.gross_monthly_income);setV('otherinc',P.other_household_income);setV('oblig',P.existing_monthly_obligations);
  if(P.ofw_remit)setV('ofw_remit',P.ofw_remit);setV('purpose',P.purpose);setV('bank',P.preferred_bank);setV('source',P.source_of_sale);
  if(P.co_borrower==='yes'){setV('cm',P.civil_status==='married'?'spouse':'yes');if(P.civil_status!=='married')setV('cm_inc',P.co_income);else setV('sp_inc',P.co_income)}else if(P.co_borrower==='no')setV('cm','no');
  var u=U.filter(function(x){return x.id===P.unit_id})[0];if(u){setV('model',u.model);fillVariants();setV('variant',u.id);fillColors();setV('color',P.color)}
  if(P.plan){setV('dp',P.plan.dp);var n=+P.plan.term_months;if(n%12===0){setV('term_y',n)}else{document.querySelector('[name=tu][value=m]').checked=true;setV('term_m',n);tu()}
    var pl=$('af-plan');pl.hidden=false;pl.textContent=T('Plan mula sa assessment: ','Plan from your assessment: ')+'DP '+peso(P.plan.dp)+' · '+n+T(' buwan',' months')+' · ~'+peso(P.plan.monthly)+'/mo'+(P.plan.type==='promo'?' (promo, all-in)':T(' (estimate)',' (estimate)'))}
  if(P.docs&&P.docs.missing){var miss=P.docs.missing;Object.keys(REQ).forEach(function(k){REQ[k].forEach(function(x){if(miss.indexOf(x[0])<0&&miss.indexOf(x[1]||x[0])<0)have[x[0]]=true})})}
  if(P.consent_ts)$('consent').checked=false;  // consent is re-confirmed on this form (covers the full application)
  $('af-pre').hidden=false;if((P.lang==='en'||P.lang==='tl')&&!/[?&]lang=/.test(location.search))setLang(P.lang)}
function tu(){var m=document.querySelector('[name=tu]:checked').value==='m';$('term_y').hidden=m;$('term_m').hidden=!m;
  if(m)$('term_m').value=$('term_y').value;else{var x=+$('term_m').value;$('term_y').value=String(Math.max(12,Math.min(60,Math.round(x/12)*12)))}}

/* ---------- validation ---------- */
function age(d){var b=new Date(d+'T00:00'),n=new Date(),a=n.getFullYear()-b.getFullYear(),m=n.getMonth()-b.getMonth();if(m<0||(m===0&&n.getDate()<b.getDate()))a--;return a}
function mob(v){return /^(09\d{9}|\+639\d{9}|\+\d{8,15})$/.test(v.replace(/[\s()-]/g,''))}
function flag(el,msg){var er=el.parentNode.querySelector('.er.af-e');if(msg){el.setAttribute('aria-invalid','true');if(!er){er=document.createElement('p');er.className='er af-e';el.parentNode.appendChild(er)}er.textContent=msg;er.hidden=false}else{el.removeAttribute('aria-invalid');if(er)er.hidden=true}return !!msg}
function inS(el,st){if(!st)return true;var c=el.closest('[data-step]');return !!c&&+c.dataset.step===st}
function validate(st){var bad=[],has=function(i){return inS($(i),st)};
  document.querySelectorAll('#af input,#af select').forEach(function(el){if(!inS(el,st))return;if(el.type==='checkbox'||el.type==='radio'||el.classList.contains('as-hp'))return;if(el.closest('[hidden]')){flag(el,'');return}
    var v=String(el.value).trim(),m='';
    if(el.required&&!v)m=T('Kailangan ito.','This is required.');
    else if(v&&el.dataset.v==='mobile'&&!mob(v))m=T('Pakilagay ang tamang mobile (09XXXXXXXXX o +639XXXXXXXXX).','Enter a valid mobile (09XXXXXXXXX or +639XXXXXXXXX).');
    else if(v&&el.dataset.v==='email'&&!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v))m=T('Pakicheck ang email.','Please check the email.');
    else if(v&&el.dataset.v==='num'&&(isNaN(+v)||+v<0))m=T('Pakilagay ang tamang numero.','Enter a valid number.');
    else if(v&&el.dataset.v==='dob'&&(isNaN(new Date(v))||age(v)<18||age(v)>75))m=T('Dapat 18 pataas ang edad.','Applicant must be 18 or older.');
    if(flag(el,m))bad.push(el)});
  if(has('ref1_mobile')){var me=val('mobile').replace(/\D/g,'').slice(-10);['ref1_mobile','ref2_mobile'].forEach(function(i){var x=$(i);if(x.getAttribute('aria-invalid')!=='true'&&me&&val(i).replace(/\D/g,'').slice(-10)===me&&flag(x,T('Dapat iba sa sarili mong number.','Must be different from your own number.')))bad.push(x)});
  if(val('ref1_mobile')&&val('ref1_mobile').replace(/\D/g,'').slice(-10)===val('ref2_mobile').replace(/\D/g,'').slice(-10)&&flag($('ref2_mobile'),T('Dapat magkaiba ang number ng 2 references.','The 2 references need different numbers.')))bad.push($('ref2_mobile'))}
  var u=unit(),dp=parseFloat(val('dp'));if(has('dp')&&u&&u.price&&dp>=u.price&&flag($('dp'),T('Mas mataas sa presyo ang DP.','DP is higher than the price.')))bad.push($('dp'));
  if(has('consent')){var c=!$('consent').checked;$('e_consent').hidden=!c;if(c)bad.push($('consent'))}
  if(st){$('af-serr').hidden=!bad.length}else $('af-errsum').hidden=!bad.length;if(bad.length){bad[0].scrollIntoView({block:'center'});try{bad[0].focus({preventScroll:true})}catch(_){}}return !bad.length}

/* ---------- submit ---------- */
function ymv(i){return (+val(i+'_y')||0)*12+(+val(i+'_m')||0)}
function collect(ref){var u=unit(),n=term();
  var a={ref_no:ref,status:'SUBMITTED',schema:'rulebook-1.0/official-form-static',language:lang,
   privacy_consent:{accepted:true,timestamp:new Date().toISOString(),version:'dpa-consent-draft-2026-10-22',controller:'SJ Legacy Motors',dpo:'richard.cuagdan20@gmail.com'},
   applicant:{full_name:{first:val('first'),middle:val('middle'),last:val('last'),suffix:val('suffix')},dob:val('dob'),gender:val('gender'),civil_status:val('civil'),nationality:val('nationality'),dependents:+val('dependents')||0,tin:val('tin'),
     mobile:val('mobile').replace(/[\s()-]/g,''),email:val('email'),address:{line1:val('addr1'),barangay:val('brgy'),city:val('city'),province:val('prov'),zip:val('zip')},length_of_stay_months:ymv('stay'),residential_status:val('res'),monthly_rent:val('res')==='rented'?+val('rent')||null:null,car_ownership:val('car'),main_bank:val('mainbank')},
   income:{employment_type:val('emp'),employment_status:val('emp')==='employed'?val('estat'):'',employer_name:val('employer'),position:val('position'),nature_of_business:val('nature'),tenure_months:val('emp')==='pensioner'?null:ymv('ten'),business_address:val('oaddr'),business_tel:val('otel'),business_email:val('oemail'),
     gross_monthly_income:+val('gross')||0,other_household_income:+val('otherinc')||0,existing_monthly_obligations:+val('oblig')||0},
   vehicle:{model:val('model'),variant_id:u?u.id:'',variant:u?u.n:'',color:val('color'),price:u?u.price:null,dp_amount:+val('dp')||0,dp_percent:u&&u.price?Math.round((+val('dp')||0)/u.price*1000)/10:null,term_months:n,purpose:val('purpose')},
   preferred_bank:val('bank'),source_of_sale:val('source'),
   references:[1,2].map(function(k){return {name:val('ref'+k+'_name'),relation:val('ref'+k+'_rel'),mobile:val('ref'+k+'_mobile').replace(/[\s()-]/g,''),address:val('ref'+k+'_addr')}}),
   documents:{total:reqList().length,missing:missing().map(function(x){return x[1]||x[0]}),status:reqList().map(function(x){return {item:x[1]||x[0],status:stat(x[0])}}),uploads_enabled:UPLOADS_ON}};
  if(val('emp')==='ofw'||val('emp')==='seafarer'){a.ofw={country:val('ofw_country'),agency:val('ofw_agency'),contract_start:val('ofw_start'),contract_end:val('ofw_end'),remittance_proof:val('ofw_remit')};a.aif={name:val('aif_name'),relation:val('aif_rel'),contact:val('aif_mobile').replace(/[\s()-]/g,'')}}
  if(val('civil')==='married')a.spouse={name:val('sp_name'),dob:val('sp_dob'),mobile:val('sp_mobile'),employment_type:val('sp_emp'),employer:val('sp_employer'),gross_monthly_income:+val('sp_inc')||0};
  a.co_borrower=val('cm')==='yes'?{name:val('cm_name'),relation:val('cm_rel'),mobile:val('cm_mobile').replace(/[\s()-]/g,''),dob:val('cm_dob'),employment_type:val('cm_emp'),gross_monthly_income:+val('cm_inc')||0,address:val('cm_addr')}:val('cm')==='spouse'?'spouse':null;
  if(P){a.assessment={lead_id:P.leadId||'',result:P.result||'',plan:P.plan||null}}
  return a}
var DONE=null;
/* Uploads: separate non-keepalive POST (keepalive caps bodies at 64KB). Only when UPLOADS_ON and files picked. Failure never blocks the application. */
function sendFiles(ref,L){var ks=Object.keys(files);if(!UPLOADS_ON||!ks.length||Lead.skipped())return Promise.resolve();
  $('af-btn').textContent=T('Ina-upload ang documents...','Uploading documents...');
  var body=JSON.stringify({action:'upload',leadId:ref,refNo:ref,last4:(window.Lead&&Lead.V4)?String(L.mobile||'').replace(/\D/g,'').slice(-4):undefined,name:L.name,docsStatus:L.docsStatus,files:ks.map(function(k){var f=files[k];return {req:f.req,name:f.name,type:f.type,data:f.data}})});
  return Promise.race([fetch(Lead.url,{method:'POST',mode:'no-cors',cache:'no-store',headers:{'Content-Type':'text/plain;charset=utf-8'},body:body}).catch(function(){}),new Promise(function(r){setTimeout(r,60000)})])}
function crispSet(a){crispLoad();var v=a.vehicle,nm=[a.applicant.full_name.first,a.applicant.full_name.last].join(' ');
  cp('set','user:nickname',[nm]);if(a.applicant.mobile)cp('set','user:phone',[a.applicant.mobile]);if(a.applicant.email)cp('set','user:email',[a.applicant.email]);
  var d=[['ref_no',a.ref_no],['source','official_application'],['language',a.language],['unit',v.variant],['color',v.color],['plan','DP '+v.dp_amount+' ('+v.dp_percent+'%) | '+v.term_months+' mo'],['employment_type',a.income.employment_type],['docs_missing',a.documents.missing.join('; ').slice(0,500)],['docs_lacking',a.documents.missing.length],['app_status','SUBMITTED / under review']];
  if(a.assessment){if(a.assessment.result)d.push(['result',a.assessment.result]);if(a.assessment.lead_id)d.push(['lead_id',a.assessment.lead_id]);if(a.assessment.plan)d.push(['monthly_est',String(a.assessment.plan.monthly)])}
  cp('set','session:data',[d]);cp('set','session:segments',[['official_application','loan_assessment']])}
function finaText(a){var m=a.documents.missing;return T('Hi Fina! Na-submit ko na ang Official Application Form. Ref: '+a.ref_no+'. Unit: '+a.vehicle.variant+'.'+(m.length?' Kulang pa: '+m.join(', ')+'.':' Kumpleto na ang documents ko.')+' Paano ko ipapadala ang documents?','Hi Fina! I submitted the Official Application Form. Ref: '+a.ref_no+'. Unit: '+a.vehicle.variant+'.'+(m.length?' Still missing: '+m.join(', ')+'.':' My documents are complete.')+' How do I send my documents?')}
function done(a){DONE=a;try{sessionStorage.removeItem(DKEY)}catch(_){}var m=a.documents.missing,pq=a.assessment&&a.assessment.result==='PRE_QUALIFIED';
  $('af-wrap').hidden=true;var D=$('af-done');D.hidden=false;
  D.innerHTML=safe('<p class="kick">'+T('Natanggap na ang application mo','Your application was received')+'</p><h2 class="h3">'+T('Salamat, ','Thank you, ')+esc(a.applicant.full_name.first)+'!</h2>'+
   '<p>'+T('Reference number mo:','Your reference number:')+'</p><p class="af-ref" id="af-refno">'+esc(a.ref_no)+'</p>'+
   '<p class="la-badge" style="background:#fef3c7;color:#92400e;font-size:17px">'+(pq?'Pre-qualified · ':'')+T('Under review','Under review')+'</p>'+
   '<p>'+T('Status: <b>'+(pq?'Pre-qualified (initial assessment), ':'')+'under review</b>. Hindi pa ito bank decision; ire-review namin ang application mo bago i-endorse sa bank. I-save ang reference number; kakailanganin din ang huling 4 digits ng mobile mo para sa status check.','Status: <b>'+(pq?'Pre-qualified (initial assessment), ':'')+'under review</b>. This is not yet a bank decision; we will review your application before endorsing it to the bank. Save your reference number; you will also need the last 4 digits of your mobile for status checks.')+'</p>'+
   '<dl class="la-sum"><div><dt>Unit</dt><dd>'+esc(a.vehicle.variant||a.vehicle.model)+'</dd></div><div><dt>Color</dt><dd>'+esc(a.vehicle.color==='undecided'?T('Bahala na','Undecided'):a.vehicle.color)+'</dd></div><div><dt>Down payment</dt><dd>'+peso(a.vehicle.dp_amount)+'</dd></div><div><dt>Term</dt><dd>'+a.vehicle.term_months+T(' buwan',' months')+'</dd></div></dl>'+
   (m.length?'<div class="la-lack"><p><b>'+T('Requirements na kulang pa','Requirements still missing')+' ('+m.length+'):</b></p><ul>'+m.map(function(x){return '<li>'+esc(x)+'</li>'}).join('')+'</ul></div>':'<p class="la-ok">'+T('Kumpleto ka na sa documents. Ihanda ang malinaw na kopya.','Your documents are complete. Prepare clear copies.')+'</p>')+
   '<p>'+T('Si Fina ang kukuha ng kulang na documents mo sa live chat. I-tap ang button para makausap siya; dala na nito ang reference number mo.','Fina will collect any remaining documents in live chat. Tap the button to chat with her; it already carries your reference number.')+'</p>'+
   (window.Lead&&Lead.V4?'<div class="la-card" style="margin:12px 0"><p><b>'+T('I-track ang application mo','Track your application')+'</b></p><p>'+T('Gamitin ang reference number <b>'+esc(a.ref_no)+'</b> at huling 4 digits ng mobile mo para makita ang status at mag-upload ng kulang na requirements.','Use reference number <b>'+esc(a.ref_no)+'</b> and the last 4 digits of your mobile to check your status and upload missing requirements.')+'</p><p><a class="btn ghost" href="/status/?ref='+encodeURIComponent(a.ref_no)+'">'+T('Track your application','Track your application')+' →</a></p></div>':'')+'<div id="af-rc"></div>'+'<button type="button" class="btn la-fina af-big" id="af-fina">💬 '+T('Makipag-chat kay Fina','Chat with Fina')+'</button>');
  $('af-fina').onclick=function(){crispSet(a);cp('do','chat:open');cp('set','message:text',[finaText(a)]);ga('chat_open',{provider:'crisp',form:'official_application'})};
  if(window.Lead&&Lead.REFCHAT&&window.RefChat){var l4=String(a.applicant&&a.applicant.mobile||a.contact&&a.contact.mobile||val('mobile')||'').replace(/\D/g,'').slice(-4);RefChat.mount($('af-rc'),{ref:a.ref_no,last4:l4,name:a.applicant.full_name.first})}
  window.scrollTo(0,0)}
$('af').addEventListener('submit',function(ev){ev.preventDefault();for(var q=1;q<=NST;q++){if(!validate(q)){go(q);validate(q);return}}if(!validate())return;
  var btn=$('af-btn'),ref=newRef(),a=collect(ref);btn.disabled=true;btn.textContent=T('Sine-send...','Sending...');
  var L=Lead.base('official_application');L.tag='official_application';L.refNo=ref;L.leadId=ref;L.status='SUBMITTED';
  L.name=[a.applicant.full_name.first,a.applicant.full_name.middle,a.applicant.full_name.last,a.applicant.full_name.suffix].filter(Boolean).join(' ');L.mobile=a.applicant.mobile;L.email=a.applicant.email;
  L.location=[a.applicant.address.city,a.applicant.address.province].filter(Boolean).join(', ');L.chosenUnit=a.vehicle.variant;L.unitParam=a.vehicle.variant_id;L.language=lang;
  L.employment=a.income.employment_type;L.seg=(a.income.employment_type==='ofw'||a.income.employment_type==='seafarer')?'ofw_abroad':'local';L.income=a.income.gross_monthly_income;
  L.dpPreference=peso(a.vehicle.dp_amount)+' DP ('+a.vehicle.dp_percent+'%)';L.planDp=a.vehicle.dp_amount;L.planTerm=a.vehicle.term_months;L.timeline='Official application '+ref+' (SUBMITTED)';
  L.docsTotal=a.documents.total;L.docsLacking=a.documents.missing.length;L.docsReady=a.documents.total-a.documents.missing.length;if(P&&P.leadId)L.assessmentLeadId=P.leadId;
  L.usage=['OFFICIAL APPLICATION '+ref,'Unit: '+a.vehicle.variant+' / '+a.vehicle.color,'DP '+peso(a.vehicle.dp_amount)+', '+a.vehicle.term_months+' mo','Emp: '+a.income.employment_type+' @ '+a.income.employer_name,'Gross '+peso(a.income.gross_monthly_income),'Missing docs: '+(a.documents.missing.join('; ')||'none'),'Docs status: '+docStatus().join('; '),'Lang: '+lang].join(' | ');
  L.docsStatus=docStatus().join(' | ');L.docsToFollow=a.documents.missing.join('; ');L.application=JSON.stringify(a);
  Lead.send(L).then(function(ok){if(ok===false)throw 0;return sendFiles(ref,L)}).then(function(){
    try{sessionStorage.removeItem('mp_app_prefill');sessionStorage.removeItem(DKEY)}catch(_){}
    if(!Lead.skipped()){px('SubmitApplication',{});ga('submit_application',{form:'official_application'})}
    done(a)}).catch(function(){btn.disabled=false;btn.textContent=T('I-submit ang application','Submit application');$('af-errsum').hidden=false;$('af-errsum').textContent=T('Hindi na-send. Pakisubukan ulit.','Not sent. Please try again.')})});

/* ---------- wizard: steps = .la-card[data-step] (1 Unit, 2 Personal, 3 Address, 4 Work, 5 Co-maker/refs, 6 Requirements, 7 Review) ---------- */
var NST=7,STEP=1,DKEY='mp_app_draft';
var SN=[['Unit at loan','Unit & loan'],['Personal info','Personal info'],['Address at contact','Address & contact'],['Trabaho / income','Work / income'],['Co-maker at references','Co-maker & references'],['Requirements','Requirements'],['Review at submit','Review & submit']];
function stepT(){$('af-pn').textContent=T('Step '+STEP+' of '+NST,'Step '+STEP+' of '+NST);$('af-pt').textContent='· '+T(SN[STEP-1][0],SN[STEP-1][1]);$('af-pb').style.width=Math.round(STEP/NST*100)+'%'}
function go(n,quiet){STEP=Math.max(1,Math.min(NST,n));document.querySelectorAll('#af [data-step]').forEach(function(c){c.classList.toggle('af-off',+c.dataset.step!==STEP)});
  document.querySelectorAll('#af [data-num]').forEach(function(x){x.textContent=''});
  $('af-back').hidden=STEP===1;$('af-next').hidden=STEP===NST;$('af-serr').hidden=true;$('af-errsum').hidden=true;stepT();if(STEP===NST)review();save();
  if(!quiet){var f=$('af-prog');try{f.scrollIntoView({block:'start'})}catch(_){window.scrollTo(0,0)}}
  ga('apply_step',{step:STEP})}
$('af-next').addEventListener('click',function(){if(validate(STEP))go(STEP+1)});
$('af-back').addEventListener('click',function(){go(STEP-1)});
/* autosave (sessionStorage; files are not saved, only per-requirement choices) */
function save(){if(DONE){try{sessionStorage.removeItem(DKEY)}catch(_){}return}try{var d={step:STEP,v:{},have:have,later:later};document.querySelectorAll('#af input,#af select').forEach(function(el){if(!el.id||el.type==='file'||el.classList.contains('as-hp'))return;d.v[el.id]=el.type==='checkbox'?el.checked:el.value});
  var t=document.querySelector('[name=tu]:checked');d.tu=t?t.value:'y';sessionStorage.setItem(DKEY,JSON.stringify(d));$('af-saved').hidden=false}catch(_){}}
function restore(){var d;try{d=JSON.parse(sessionStorage.getItem(DKEY)||'null')}catch(_){d=null}if(!d||!d.v)return;
  var V=d.v;if(V.model){setV('model',V.model);fillVariants();setV('variant',V.variant);fillColors();setV('color',V.color)}
  Object.keys(V).forEach(function(i){if(/^(model|variant|color|consent)$/.test(i))return;var el=$(i);if(!el)return;if(el.type==='checkbox')el.checked=!!V[i];else if(V[i]!=='')el.value=V[i]});
  if(d.tu==='m'){document.querySelector('[name=tu][value=m]').checked=true;$('term_y').hidden=true;$('term_m').hidden=false}
  have=d.have||have;later=d.later||later;STEP=+d.step||1}
window.addEventListener('pagehide',function(){if(!DONE)save()});document.addEventListener('visibilitychange',function(){if(document.visibilityState==='hidden'&&!DONE)save()});
var stimer=null;$('af').addEventListener('input',function(){clearTimeout(stimer);stimer=setTimeout(save,400)});$('af').addEventListener('change',function(){clearTimeout(stimer);stimer=setTimeout(save,200)});
/* review */
function shown(el){return !el.closest('[hidden]')}
function review(){var h='';for(var n=1;n<NST-1;n++){var rows='';
  document.querySelectorAll('#af [data-step="'+n+'"]').forEach(function(card){if(card.hasAttribute('hidden'))return;
    card.querySelectorAll('input,select').forEach(function(el){if(!el.id||el.type==='file'||el.type==='radio'||el.type==='checkbox'||el.classList.contains('as-hp')||!shown(el))return;
      var v=el.tagName==='SELECT'?(el.value?el.options[el.selectedIndex].textContent:''):String(el.value).trim();if(!v)return;
      var lb=card.querySelector('label[for="'+el.id+'"]'),l=lb?(lb.querySelector(lang==='en'?'.en':'.tl')||lb).textContent.replace(/\s*\*$/,''):(el.getAttribute('aria-label')||el.id);
      if(/_m$/.test(el.id)&&$(el.id.replace(/_m$/,'_y')))return;if(/_y$/.test(el.id)&&$(el.id.replace(/_y$/,'_m'))&&el.id!=='term_y'){v=v+' '+T('taon','yr')+' '+val(el.id.replace(/_y$/,'_m'))+' '+T('buwan','mo')}
      if(el.id==='term_y'||el.id==='term_m'){if(el.hidden)return;l='Term'}
      rows+='<dt>'+esc(l)+'</dt><dd>'+esc(v)+'</dd>'})});
  if(n===1&&rows)rows+='';
  h+='<div class="af-rv"><h3>'+esc(n+'. '+T(SN[n-1][0],SN[n-1][1]))+'<button type="button" data-go="'+n+'">Edit</button></h3><dl>'+(rows||'<dt>-</dt><dd>'+T('Wala / skipped','None / skipped')+'</dd>')+'</dl></div>'}
  h+='<div class="af-rv"><h3>6. Requirements<button type="button" data-go="6">Edit</button></h3><dl>'+reqList().map(function(x){var s=stat(x[0]);return '<dt>'+esc(lang==='en'&&x[1]?x[1]:x[0])+'</dt><dd>'+esc(s==='Uploaded'?'📎 Uploaded':s==='To follow'?'⏳ '+T('Susunod / to follow','To follow'):'✅ '+T('Meron na','Ready'))+'</dd>'}).join('')+'</dl></div>';
  var R=$('af-review');R.innerHTML=h;R.querySelectorAll('[data-go]').forEach(function(b){b.onclick=function(){go(+b.dataset.go)}})}

/* ---------- init ---------- */
function initLang(){var l='en';try{var s=localStorage.getItem('site_lang');if(s==='en'||s==='tl')l=s}catch(_){}try{var q=new URLSearchParams(location.search).get('lang');if(q==='en'||q==='tl'){l=q;localStorage.setItem('site_lang',q)}}catch(_){}return l}
lang=initLang();
document.documentElement.setAttribute('data-lang',lang);
fillModels();
$('model').addEventListener('change',fillVariants);$('variant').addEventListener('change',fillColors);$('dp').addEventListener('input',unitHints);
document.querySelectorAll('[name=tu]').forEach(function(r){r.addEventListener('change',tu)});
['emp','civil','cm','res'].forEach(function(i){$(i).addEventListener('change',function(){vis();renderDocs()})});
window.__afw=1;prefill();restore();setLang(lang);vis();renderDocs();go(STEP,true);
if(P)crispLoad();   // consent already given in the assessment; floating chat stays available (no auto-open)
document.addEventListener('DOMContentLoaded',function(){try{AS.init($('af'))}catch(_){}});
})();
