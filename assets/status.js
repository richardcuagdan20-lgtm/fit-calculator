/* Application Status (/status/). Verification: MP- ref + last 4 digits of the application mobile (checked server-side, Apps Script action 'status').
   Shown only when Lead.V4 is true (assets/lead.js). No PII, Drive links or other applicants' data ever come back from the server. */
(function(){'use strict';
var $=function(i){return document.getElementById(i)},lang='tl',S=null,files={},MAXF=10,MAXB=5*1024*1024,REF=/^MP-[A-HJKMNP-Z2-9]{5}$/;
function T(t,e){return lang==='en'?e:t}
function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
function setLang(l){lang=l;document.documentElement.setAttribute('data-lang',l);try{localStorage.setItem('la_lang',l)}catch(_){}if(S)render()}
document.querySelectorAll('[data-setlang]').forEach(function(b){b.addEventListener('click',function(){setLang(b.dataset.setlang)})});
function api(o){return fetch(Lead.url,{method:'POST',cache:'no-store',headers:{'Content-Type':'text/plain;charset=utf-8'},body:JSON.stringify(o)}).then(function(r){return r.json()})}
var SL={'Submitted':['Submitted','s-sub'],'Under review':['Under review','s-rev'],'Approved':['Approved','s-ok'],'Declined':['Declined','s-no'],'Needs more documents':[T('Kailangan ng dagdag na documents','Needs more documents'),'s-doc']};
var OV={'Received – under review':['Natanggap na – under review','Received – under review'],'Submitted to bank':['Na-submit na sa bank','Submitted to bank'],'Under review':['Under review ng bank','Under review by the bank'],'Needs more documents':['Kailangan ng dagdag na documents','Needs more documents'],'Approved by a bank':['Approved ng isang bank','Approved by a bank'],'Declined':['Declined','Declined']};
function pill(s){var c={'Submitted':'s-sub','Under review':'s-rev','Approved':'s-ok','Declined':'s-no','Needs more documents':'s-doc','Uploaded':'s-ok','Ready':'s-sub','To follow':'s-doc'}[s]||'s-rev';
  var lbl={'Needs more documents':T('Kailangan ng dagdag na docs','Needs more documents'),'To follow':T('Susunod / to follow','To follow'),'Ready':T('Ready (ipadala kay Fina)','Ready (send to Fina)')}[s]||s;return '<span class="st-pill '+c+'">'+esc(lbl)+'</span>'}
function render(){var d=S,ov=OV[d.overall]||[d.overall,d.overall],R=$('st-r');
  var h='<div class="la-card"><p class="kick">'+esc(d.ref)+'</p><h2 class="h3">'+T('Hi ','Hi ')+esc(d.first_name)+'!</h2>'+
   '<dl class="la-sum"><div><dt>Unit</dt><dd>'+esc(d.unit||'-')+'</dd></div><div><dt>'+T('Petsa ng submit','Date submitted')+'</dt><dd>'+esc(d.submitted)+'</dd></div></dl>'+
   '<p>'+T('Overall status: ','Overall status: ')+'<b>'+esc(T(ov[0],ov[1]))+'</b></p>'+
   '<p class="muted small">'+T('Ina-update ito ng aming team. Ang final approval ay desisyon ng bank (subject to bank approval).','Updated by our team. Final approval is the bank\'s decision (subject to bank approval).')+'</p></div>';
  h+='<div class="la-card"><h2 class="h3">'+T('Status sa bawat bank','Status per bank')+'</h2>'+(d.banks.length?'<ul class="st-bank">'+d.banks.map(function(b){return '<li><b>'+esc(b.bank)+'</b>'+pill(b.status)+(b.note?'<p class="st-n">'+esc(b.note)+'</p>':'')+(b.updated?'<p class="st-n">'+T('Updated: ','Updated: ')+esc(b.updated)+'</p>':'')+'</li>'}).join('')+'</ul>':'<p>'+T('Wala pang bank update. Ire-review muna namin ang application mo bago i-endorse sa bank.','No bank updates yet. We will review your application before endorsing it to the bank.')+'</p>')+'</div>';
  var todo=d.docs.filter(function(x){return x.status!=='Uploaded'});
  h+='<div class="la-card"><h2 class="h3">Requirements</h2><p>'+T('I-upload ang kulang o bagong requirements. Photo o PDF, hanggang '+MAXF+' files bawat send, 5MB bawat isa.','Upload missing or new requirements. Photo or PDF, up to '+MAXF+' files per send, 5MB each.')+'</p><ul class="la-docs st-docs">'+
   d.docs.concat([{item:T('Iba pang document','Other document'),status:'',other:1}]).map(function(x,i){var f=files[i];return '<li><div class="st-dh"><span>'+esc(x.item)+'</span>'+(x.status?pill(x.status):'')+'</div>'+
    '<div class="st-pick"><label>📷 '+T('Kumuha ng Photo','Take Photo')+'<input type="file" accept="image/*" capture="environment" data-i="'+i+'"></label><label>📁 '+T('Pumili ng file','Choose file')+'<input type="file" accept="image/*,application/pdf" data-i="'+i+'"></label></div>'+
    '<p class="st-fn" id="fn'+i+'">'+(f?'📎 '+esc(f.name):'')+'</p></li>'}).join('')+'</ul>'+
   '<p class="st-err" id="up-e" hidden></p><p class="st-ok" id="up-ok" hidden></p><button type="button" class="btn af-big" id="up-btn">'+T('I-send ang documents','Send documents')+' (<span id="up-n">'+Object.keys(files).length+'</span>)</button>'+
   '<p class="muted small">🔒 '+T('Gagamitin lang ang files mo para sa loan processing. Pwede ring ipadala kay Fina sa chat.','Your files are used only for loan processing. You can also send them to Fina in chat.')+'</p></div>'+
   '<p><button type="button" class="btn ghost" id="st-again">'+T('Ibang reference number','Different reference number')+'</button></p>';
  R.innerHTML=h;R.hidden=false;$('st-f').hidden=true;
  R.querySelectorAll('input[type=file]').forEach(function(b){b.onchange=function(){pick(b)}});
  $('up-btn').onclick=send;$('st-again').onclick=function(){S=null;files={};R.hidden=true;$('st-f').hidden=false}}
function label(i){return i<S.docs.length?S.docs[i].item:'Other document'}
function pick(b){var i=+b.dataset.i,f=b.files&&b.files[0],n=$('fn'+i);if(!f)return;
  if(!/^image\/|^application\/pdf$/.test(f.type)){n.textContent=T('Photo o PDF lang.','Photo or PDF only.');b.value='';return}
  if(!files[i]&&Object.keys(files).length>=MAXF){n.textContent=T('Hanggang '+MAXF+' files bawat send.','Max '+MAXF+' files per send.');b.value='';return}
  n.textContent=T('Pinoproseso...','Processing...');
  (/^image\//.test(f.type)?shrink(f):readB64(f)).then(function(o){if(o.data.length*0.75>MAXB){n.textContent=T('Masyadong malaki (max 5MB).','Too large (max 5MB).');return}
   o.name=f.name||'photo.jpg';o.req=label(i);files[i]=o;n.textContent='📎 '+o.name;$('up-n').textContent=Object.keys(files).length}).catch(function(){n.textContent=T('Hindi mabasa ang file.','Could not read the file.')})}
function readB64(f){return new Promise(function(r,j){var fr=new FileReader();fr.onload=function(){r({type:f.type,data:String(fr.result).split(',')[1]})};fr.onerror=j;fr.readAsDataURL(f)})}
function shrink(f){return new Promise(function(r,j){var im=new Image(),u=URL.createObjectURL(f);im.onload=function(){var sc=Math.min(1,1600/Math.max(im.width,im.height)),c=document.createElement('canvas');c.width=Math.round(im.width*sc);c.height=Math.round(im.height*sc);
  c.getContext('2d').drawImage(im,0,0,c.width,c.height);URL.revokeObjectURL(u);r({type:'image/jpeg',data:c.toDataURL('image/jpeg',0.8).split(',')[1]})};im.onerror=function(){readB64(f).then(r,j)};im.src=u})}
function send(){var ks=Object.keys(files),e=$('up-e'),ok=$('up-ok'),b=$('up-btn');e.hidden=true;ok.hidden=true;if(!ks.length){e.textContent=T('Pumili muna ng file o kumuha ng photo.','Choose a file or take a photo first.');e.hidden=false;return}
  b.disabled=true;b.textContent=T('Ina-upload...','Uploading...');
  api({action:'upload',leadId:S.ref,last4:S.l4,files:ks.map(function(k){var f=files[k];return {req:f.req,name:f.name,type:f.type,data:f.data}})}).then(function(r){
    if(!r||!r.ok)throw r;files={};return api({action:'status',ref:S.ref,last4:S.l4}).then(function(d){if(d&&d.ok){d.l4=S.l4;S=d}render();var o=$('up-ok');o.textContent=T('Salamat! Natanggap namin ang '+r.saved+' document(s).','Thank you! We received '+r.saved+' document(s).');o.hidden=false;o.scrollIntoView({block:'center'})})})
  .catch(function(r){b.disabled=false;b.textContent=T('I-send ang documents','Send documents');e.textContent=r&&r.error==='rate'?T('Masyadong maraming upload ngayon. Subukan ulit mamaya o ipadala kay Fina.','Too many uploads right now. Try again later or send them to Fina.'):T('Hindi na-upload. Pakisubukan ulit o ipadala kay Fina sa chat.','Upload failed. Please try again or send them to Fina in chat.');e.hidden=false})}
$('st-f').addEventListener('submit',function(ev){ev.preventDefault();var ref=$('st-ref').value.trim().toUpperCase().replace(/^MP(?=[A-Z0-9]{5}$)/,'MP-'),l4=$('st-l4').value.replace(/\D/g,''),e=$('st-e'),b=$('st-btn');
  if(!REF.test(ref)||l4.length!==4){e.textContent=T('Pakicheck ang reference number (MP-XXXXX) at 4 digits.','Please check the reference number (MP-XXXXX) and the 4 digits.');e.hidden=false;return}
  e.hidden=true;b.disabled=true;b.textContent=T('Hinahanap...','Searching...');
  api({action:'status',ref:ref,last4:l4}).then(function(d){b.disabled=false;b.textContent=T('Tingnan ang status','Check status');
    if(!d||!d.ok){e.textContent=d&&d.error==='rate'?T('Masyadong maraming subok. Subukan ulit pagkalipas ng 1 oras.','Too many attempts. Please try again in an hour.'):T('Hindi namin mahanap ang application na may ganitong reference number at mobile digits. Pakicheck at subukan ulit.','We could not find an application with that reference number and mobile digits. Please check and try again.');e.hidden=false;return}
    d.l4=l4;S=d;files={};render();window.scrollTo(0,0)}).catch(function(){b.disabled=false;b.textContent=T('Tingnan ang status','Check status');e.textContent=T('May problema sa connection. Pakisubukan ulit.','Connection problem. Please try again.');e.hidden=false})});
try{var sl=localStorage.getItem('la_lang');if(sl==='en'||sl==='tl')lang=sl}catch(_){}
document.documentElement.setAttribute('data-lang',lang);
var on=window.Lead&&Lead.V4;$('st-off').hidden=!!on;$('st-f').hidden=!on;
if(on){var q=new URLSearchParams(location.search).get('ref');if(q&&REF.test(q.toUpperCase()))$('st-ref').value=q.toUpperCase()}
})();
