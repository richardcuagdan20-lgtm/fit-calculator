/* Ref-linked application chat (inline panel on the /apply/ thank-you screen and /status/).
   Thread key = MP- ref; every call carries ref + last-4 of mobile and the backend re-verifies them exactly like action 'status'.
   Loaded only when Lead.REFCHAT===true (see lead.js). Actions: refchat_poll / refchat_send / refchat_email / refchat_human. */
(function(){if(window.RefChat)return;
var AGENT='Richard Cuagdan',ROLE='Mitsubishi Car Sales Executive';
var st=document.createElement('style');st.textContent=
'.rc{margin:18px 0;border:1px solid var(--ln,#e7e7ea);border-radius:var(--r,16px);overflow:hidden;background:#fff;box-shadow:0 10px 30px rgba(11,11,12,.07);text-align:left}'+
'.rc .rc-h{display:flex;align-items:center;gap:12px;padding:14px 16px;background:var(--ink,#0b0b0c);color:#fff}'+
'.rc .rc-av{width:42px;height:42px;border-radius:50%;flex:none;position:relative;background:#333}.rc .rc-av img{width:42px;height:42px;border-radius:50%;object-fit:cover}'+
'.rc .rc-av:after{content:"";position:absolute;right:0;bottom:0;width:11px;height:11px;border-radius:50%;background:#22c55e;border:2px solid var(--ink,#0b0b0c)}'+
'.rc .rc-t{line-height:1.25;flex:1;min-width:0}.rc .rc-t b{display:block;font-size:16px}.rc .rc-t small{color:#a1a1aa;font-size:12.5px;display:block}'+
'.rc .rc-ref{font:700 12px ui-monospace,Menlo,monospace;letter-spacing:.06em;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.18);padding:4px 9px;border-radius:999px;white-space:nowrap}'+
'.rc .rc-m{max-height:380px;min-height:170px;overflow:auto;padding:16px;display:flex;flex-direction:column;gap:10px;background:#f6f6f7}'+
'.rc .rc-day{align-self:center;font-size:11.5px;color:var(--mu,#6b6b73);background:#ececef;padding:2px 10px;border-radius:999px}'+
'.rc .rc-x{max-width:84%;padding:9px 13px;border-radius:16px 16px 16px 4px;background:#fff;border:1px solid #ececef;align-self:flex-start;white-space:pre-wrap;font-size:15px;line-height:1.45;color:var(--tx,#26262b)}'+
'.rc .rc-x small{display:block;font-size:11px;color:var(--mu,#6b6b73);margin-top:3px}.rc .rc-x .rc-who{font-weight:700;color:var(--red,#E60012);font-size:12px;margin:0 0 2px}'+
'.rc .rc-x.you{align-self:flex-end;background:var(--red,#E60012);border-color:var(--red,#E60012);color:#fff;border-radius:16px 16px 4px 16px}.rc .rc-x.you small{color:rgba(255,255,255,.8)}'+
'.rc .rc-sys{align-self:center;max-width:92%;text-align:center;font-size:13px;color:#166534;background:#dcfce7;border-radius:10px;padding:6px 12px}'+
'.rc .rc-em{padding:12px 14px;background:#fffbeb;border-top:1px solid #fde68a;font-size:14px}.rc .rc-em p{margin:0 0 8px}.rc .rc-em form{gap:8px}'+
'.rc .rc-em input{flex:1;min-width:0;padding:10px 12px;border:1px solid #d4d4d8;border-radius:10px;font:inherit;font-size:16px}'+
'.rc .rc-em button{flex:none;width:auto;margin:0;background:var(--ink,#0b0b0c);color:#fff;border:0;border-radius:10px;padding:0 14px;font-weight:700;cursor:pointer}.rc .rc-em .rc-skip{background:none;color:var(--mu,#6b6b73);padding:0 6px;font-weight:500}'+
'.rc .rc-em .rc-err{color:#b91c1c;margin:6px 0 0;font-size:13px}'+
'.rc .rc-f,.rc .rc-em form{display:flex!important;flex-wrap:nowrap;align-items:stretch;gap:8px;padding:10px;border-top:1px solid var(--ln,#e7e7ea);background:#fff}'+
'.rc .rc-f input{flex:1;min-width:0;padding:12px 14px;border:1px solid #d4d4d8;border-radius:999px;font:inherit;font-size:16px}.rc .rc-f input:focus,.rc .rc-em input:focus{outline:2px solid rgba(230,0,18,.25);border-color:var(--red,#E60012)}'+
'.rc .rc-f button{flex:none;width:auto;margin:0;min-height:46px;background:var(--red,#E60012);color:#fff;border:0;border-radius:999px;padding:0 20px;font-weight:700;font-size:15px;cursor:pointer}'+
'.rc .rc-b{display:flex;flex-wrap:wrap;gap:8px;align-items:center;justify-content:space-between;padding:8px 14px 12px;background:#fff;font-size:12.5px;color:var(--mu,#6b6b73)}'+
'.rc .rc-hu{flex:none;width:auto;margin:0;background:#fff;color:var(--ink,#0b0b0c);border:1.5px solid var(--ink,#0b0b0c);border-radius:999px;padding:7px 14px;font:600 13.5px system-ui,sans-serif;cursor:pointer}.rc .rc-hu[disabled]{opacity:.55;cursor:default}'+
'.rc .rc-n{margin:0;padding:0 14px 12px;font-size:12.5px;color:var(--mu,#6b6b73);background:#fff}'+
'@media(max-width:520px){.rc .rc-h{flex-wrap:wrap;padding:12px}.rc .rc-t{flex:1 1 150px}.rc .rc-ref{margin-left:54px}.rc .rc-t b{font-size:15px}}';
document.head.appendChild(st);
function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
function tm(t){try{return new Date(t).toLocaleString('en-PH',{timeZone:'Asia/Manila',month:'short',day:'numeric',hour:'numeric',minute:'2-digit'})}catch(e){return ''}}
function api(o){return fetch(Lead.url,{method:'POST',cache:'no-store',headers:{'Content-Type':'text/plain;charset=utf-8'},body:JSON.stringify(o)}).then(function(r){return r.json()})}
var EM=/^[^@\s<>"',;]+@[^@\s<>"',;]+\.[A-Za-z]{2,}$/;
function mount(host,o){if(!host||!o||!o.ref||!/^\d{4}$/.test(o.last4||''))return;var ref=o.ref,l4=o.last4,timer,sys=[],asked=false,skipK='rc_em_skip_'+ref;
 host.innerHTML='<section class="rc" aria-label="Application chat"><div class="rc-h"><div class="rc-av"><img src="/assets/img/richard-300.webp" alt="" width="42" height="42"></div><div class="rc-t"><b>'+esc(o.title||'Questions about your application? Chat with us')+'</b><small>'+AGENT+' · '+ROLE+'</small></div><span class="rc-ref">'+esc(ref)+'</span></div>'+
  '<div class="rc-m" role="log" aria-live="polite"></div><div class="rc-emw"></div><form class="rc-f"><label class="vh" for="rc-in-'+esc(ref)+'">Message</label><input id="rc-in-'+esc(ref)+'" placeholder="Type your question…" maxlength="1000" autocomplete="off"><button>Send</button></form>'+
  '<div class="rc-b"><span>Usually replies within the day (Mon–Sat, 8AM–5PM)</span><button type="button" class="rc-hu">🙋 Talk to a human</button></div>'+
  '<p class="rc-n">🔒 Linked to '+esc(ref)+'. Continue anytime on <a href="/status/?ref='+encodeURIComponent(ref)+'">Track your application</a> with your reference number and the last 4 digits of your mobile.</p></section>';
 var m=host.querySelector('.rc-m'),inp=host.querySelector('.rc-f input'),emw=host.querySelector('.rc-emw'),hu=host.querySelector('.rc-hu'),last=[];
 function draw(list){last=list||last;var h='<div class="rc-day">Conversation for '+esc(ref)+'</div>';
  if(!last.length)h+='<div class="rc-x"><p class="rc-who">'+AGENT+' · '+ROLE+'</p>Hi'+(o.name?' '+esc(o.name):'')+'! I have your application '+esc(ref)+'. Ask me anything about your requirements, the bank review or your unit.</div>';
  last.forEach(function(x){h+='<div class="rc-x'+(x.from==='you'?' you':'')+'">'+(x.from==='you'?'':'<p class="rc-who">'+AGENT+' · '+ROLE+'</p>')+esc(x.text)+'<small>'+esc(tm(x.t))+'</small></div>'});
  sys.forEach(function(t){h+='<div class="rc-sys">'+esc(t)+'</div>'});m.innerHTML=h;m.scrollTop=1e9}
 function askEmail(){var sk=false;try{sk=sessionStorage.getItem(skipK)==='1'}catch(e){}if(asked||sk)return;asked=true;
  emw.innerHTML='<div class="rc-em"><p><b>Get notified by email when '+AGENT+' replies?</b> (optional)</p><form><label class="vh" for="rc-em-'+esc(ref)+'">Email</label><input id="rc-em-'+esc(ref)+'" type="email" inputmode="email" autocomplete="email" placeholder="you@email.com" maxlength="120"><button>Save</button><button type="button" class="rc-skip">Skip</button></form><p class="rc-err" hidden></p></div>';
  var f=emw.querySelector('form'),ei=f.querySelector('input'),er=emw.querySelector('.rc-err');
  emw.querySelector('.rc-skip').onclick=function(){try{sessionStorage.setItem(skipK,'1')}catch(e){}emw.innerHTML=''};
  f.onsubmit=function(e){e.preventDefault();var v=ei.value.trim();if(!EM.test(v)){er.textContent='Please check the email address.';er.hidden=false;return}
   api({action:'refchat_email',ref:ref,last4:l4,email:v,page:location.pathname}).then(function(r){if(r&&r.ok){emw.innerHTML='';sys.push('We will email '+(r.email_masked||'you')+' when '+AGENT+' replies.');draw()}else{er.textContent='Could not save the email. Please try again.';er.hidden=false}}).catch(function(){er.textContent='Connection problem. Please try again.';er.hidden=false})}}
 function poll(){return api({action:'refchat_poll',ref:ref,last4:l4}).then(function(r){if(r&&r.ok){draw(r.msgs);if(!r.has_email)askEmail()}}).catch(function(){})}
 host.querySelector('.rc-f').onsubmit=function(e){e.preventDefault();var t=inp.value.trim();if(!t)return;inp.value='';last=last.concat([{from:'you',text:t,t:Date.now()}]);draw();
  api({action:'refchat_send',ref:ref,last4:l4,msg:t,page:location.pathname}).then(poll).catch(function(){})};
 hu.onclick=function(){hu.disabled=true;api({action:'refchat_human',ref:ref,last4:l4,page:location.pathname}).then(function(r){
   sys.push(r&&r.ok?AGENT+' has been notified and will reply here shortly.':'Could not reach '+AGENT+' right now. Please try again in a few minutes.');if(!(r&&r.ok))hu.disabled=false;draw()}).catch(function(){hu.disabled=false})};
 draw([]);poll();timer=setInterval(function(){if(!document.body.contains(host)){clearInterval(timer);return}if(!document.hidden)poll()},8000)}
window.RefChat={mount:mount,AGENT:AGENT};
})();
