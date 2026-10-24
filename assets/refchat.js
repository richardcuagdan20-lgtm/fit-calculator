/* Ref-linked application chat (inline panel). Thread key = MP- ref; every call carries ref + last-4 of mobile and the backend re-verifies them exactly like action 'status'.
   Loaded only when Lead.REFCHAT===true. Actions: refchat_poll {ref,last4} / refchat_send {ref,last4,msg}. */
(function(){if(window.RefChat)return;
var st=document.createElement('style');st.textContent=
'.rc{margin:18px 0;border:1px solid var(--ln,#e7e7ea);border-radius:var(--r,16px);overflow:hidden;background:#fff;box-shadow:0 10px 30px rgba(11,11,12,.07);text-align:left}'+
'.rc-h{display:flex;align-items:center;gap:12px;padding:14px 16px;background:var(--ink,#0b0b0c);color:#fff}'+
'.rc-av{width:38px;height:38px;border-radius:50%;background:linear-gradient(135deg,#E60012,#7a0009);display:grid;place-items:center;font-weight:800;flex:none;position:relative}'+
'.rc-av:after{content:"";position:absolute;right:0;bottom:0;width:10px;height:10px;border-radius:50%;background:#22c55e;border:2px solid var(--ink,#0b0b0c)}'+
'.rc-t{line-height:1.25}.rc-t b{display:block;font-size:16px}.rc-t small{color:#a1a1aa;font-size:12.5px}'+
'.rc-ref{margin-left:auto;font:700 12px ui-monospace,Menlo,monospace;letter-spacing:.06em;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.18);padding:4px 9px;border-radius:999px;white-space:nowrap}'+
'.rc-m{max-height:360px;min-height:180px;overflow:auto;padding:16px;display:flex;flex-direction:column;gap:10px;background:#f6f6f7}'+
'.rc-day{align-self:center;font-size:11.5px;color:var(--mu,#6b6b73);background:#ececef;padding:2px 10px;border-radius:999px}'+
'.rc-x{max-width:82%;padding:9px 13px;border-radius:16px 16px 16px 4px;background:#fff;border:1px solid #ececef;align-self:flex-start;white-space:pre-wrap;font-size:15px;line-height:1.45;color:var(--tx,#26262b)}'+
'.rc-x small{display:block;font-size:11px;color:var(--mu,#6b6b73);margin-top:3px}.rc-x .rc-who{font-weight:700;color:var(--red,#E60012);font-size:12px;margin:0 0 2px}'+
'.rc-x.you{align-self:flex-end;background:var(--red,#E60012);border-color:var(--red,#E60012);color:#fff;border-radius:16px 16px 4px 16px}.rc-x.you small{color:rgba(255,255,255,.8)}'+
'.rc-f{display:flex;gap:8px;padding:10px;border-top:1px solid var(--ln,#e7e7ea);background:#fff}'+
'.rc-f input{flex:1;min-width:0;padding:12px 14px;border:1px solid #d4d4d8;border-radius:999px;font:inherit;font-size:16px}.rc-f input:focus{outline:2px solid rgba(230,0,18,.25);border-color:var(--red,#E60012)}'+
'.rc-f button{flex:none;width:auto;margin:0;min-height:46px;background:var(--red,#E60012);color:#fff;border:0;border-radius:999px;padding:0 20px;font-weight:700;font-size:15px;cursor:pointer}'+
'@media(max-width:520px){.rc-h{flex-wrap:wrap}.rc-t{flex:1;min-width:0}.rc-t b{font-size:15px}.rc-ref{margin-left:50px;order:3}}'+
'.rc-n{margin:0;padding:8px 16px 12px;font-size:12.5px;color:var(--mu,#6b6b73);background:#fff}';
document.head.appendChild(st);
function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
function tm(t){try{return new Date(t).toLocaleString('en-PH',{timeZone:'Asia/Manila',month:'short',day:'numeric',hour:'numeric',minute:'2-digit'})}catch(e){return ''}}
function api(o){return fetch(Lead.url,{method:'POST',cache:'no-store',headers:{'Content-Type':'text/plain;charset=utf-8'},body:JSON.stringify(o)}).then(function(r){return r.json()})}
function mount(host,o){if(!host||!o||!o.ref||!/^\d{4}$/.test(o.last4||''))return;var ref=o.ref,l4=o.last4,timer;
 host.innerHTML='<section class="rc" aria-label="Application chat"><div class="rc-h"><div class="rc-av">F</div><div class="rc-t"><b>'+esc(o.title||'Questions about your application?')+'</b><small>Chat with Fina · Mitsubishi SJDM · usually replies in minutes</small></div><span class="rc-ref">'+esc(ref)+'</span></div>'+
  '<div class="rc-m" role="log" aria-live="polite"></div><form class="rc-f"><label class="vh" for="rc-in">Message</label><input id="rc-in" placeholder="Type your question…" maxlength="1000" autocomplete="off"><button>Send</button></form>'+
  '<p class="rc-n">🔒 This conversation is linked to '+esc(ref)+'. You can continue it anytime on <a href="/status/?ref='+encodeURIComponent(ref)+'">Track your application</a> with your reference number and last 4 digits of your mobile.</p></section>';
 var m=host.querySelector('.rc-m'),inp=host.querySelector('input');
 function draw(list){var h='<div class="rc-day">Conversation for '+esc(ref)+'</div>';if(!list||!list.length)h+='<div class="rc-x"><p class="rc-who">Fina · Mitsubishi SJDM</p>Hi'+(o.name?' '+esc(o.name):'')+'! I have your application '+esc(ref)+'. Ask me anything about your requirements, the bank review or your unit.</div>';
  (list||[]).forEach(function(x){h+='<div class="rc-x'+(x.from==='you'?' you':'')+'">'+(x.from==='you'?'':'<p class="rc-who">'+esc(x.agent||'Fina · Mitsubishi SJDM')+'</p>')+esc(x.text)+'<small>'+esc(tm(x.t))+'</small></div>'});m.innerHTML=h;m.scrollTop=1e9}
 function poll(){return api({action:'refchat_poll',ref:ref,last4:l4}).then(function(r){if(r&&r.ok)draw(r.msgs)}).catch(function(){})}
 host.querySelector('form').onsubmit=function(e){e.preventDefault();var t=inp.value.trim();if(!t)return;inp.value='';var d=document.createElement('div');d.className='rc-x you';d.textContent=t;m.appendChild(d);m.scrollTop=1e9;
  api({action:'refchat_send',ref:ref,last4:l4,msg:t,page:location.pathname}).then(poll).catch(function(){})};
 draw([]);poll();timer=setInterval(function(){if(!document.hidden&&document.body.contains(host))poll();else if(!document.body.contains(host))clearInterval(timer)},8000)}
window.RefChat={mount:mount};
})();
