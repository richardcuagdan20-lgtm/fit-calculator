/* Own site-wide live chat (bubble on every page). Backend: webhook v8 actions chat_send / chat_poll / chat_human.
   Loaded only when Lead.CHAT===true AND doGet features include 'chat'. Replaces the Messenger floating button (hidden via html.oc-on).
   - Visitor thread token in localStorage (own_chat_thread); ?chat=<token> (from the reply email) reopens it.
   - Pre-chat: name + mobile (required), email (optional) + consent line; kept in localStorage (oc_profile).
   - If this tab has an MP- application session (rc_sess, set by refchat.js on /apply/ thank-you or /status/), the bubble opens THAT thread instead. */
(function(){if(!window.Lead||window.__ownChat)return;window.__ownChat=1;
var U=Lead.url,K='own_chat_thread',PK='oc_profile',AGENT='Richard Cuagdan',ROLE='Mitsubishi Car Sales Executive',id,prof={},open=false,timer=null,last=[],sys=[],booted=false,pend=null;
function lang(){var l=document.documentElement.getAttribute('data-lang');if(l!=='tl'&&l!=='en'){try{l=localStorage.getItem('site_lang')}catch(e){}}return l==='tl'?'tl':'en'}
function T(tl,en){return lang()==='tl'?tl:en}
function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
function tm(t){try{return new Date(t).toLocaleString('en-PH',{timeZone:'Asia/Manila',month:'short',day:'numeric',hour:'numeric',minute:'2-digit'})}catch(e){return ''}}
function newId(){var c='ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789',a=new Uint32Array(24),s='';(window.crypto||{getRandomValues:function(x){for(var i=0;i<x.length;i++)x[i]=Math.random()*4e9;return x}}).getRandomValues(a);for(var i=0;i<24;i++)s+=c[a[i]%c.length];return s}
try{var q=new URLSearchParams(location.search).get('chat');if(q&&/^[A-Za-z0-9]{16,40}$/.test(q)){localStorage.setItem(K,q);pend={resume:1};history.replaceState(null,'',location.pathname+location.hash)}else if(q==='open')pend={}}catch(e){}
try{id=localStorage.getItem(K)}catch(e){}if(!id||!/^[A-Za-z0-9]{16,40}$/.test(id)){id=newId();try{localStorage.setItem(K,id)}catch(e){}}
try{prof=JSON.parse(localStorage.getItem(PK)||'{}')||{}}catch(e){prof={}}
function post(o){o.thread=id;return fetch(U,{method:'POST',cache:'no-store',headers:{'Content-Type':'text/plain;charset=utf-8'},body:JSON.stringify(o)}).then(function(r){return r.json()})}
function el(t,c,h){var e=document.createElement(t);if(c)e.className=c;if(h!=null)e.innerHTML=h;return e}
function refSess(){try{var s=JSON.parse(sessionStorage.getItem('rc_sess')||'null');if(s&&/^MP-[A-Z0-9]{5}$/.test(s.ref)&&/^\d{4}$/.test(s.last4))return s}catch(e){}return null}
var api={open:function(o){o=o||{};if(!booted){pend=o;return}show(o)},ready:false};window.SiteChat=api;
document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('[data-chat]');if(a&&booted){e.preventDefault();api.open({})}},true);
fetch(U,{cache:'no-store'}).then(function(r){return r.json()}).then(function(g){if(g&&g.features&&g.features.indexOf('chat')>=0)boot()}).catch(function(){});
var b,p,m,body;
function boot(){booted=true;api.ready=true;document.documentElement.classList.add('oc-on');
 var st=el('style');st.textContent=
 'html.oc-on .fab{display:none!important}'+
 '.oc-b{position:fixed;right:18px;bottom:18px;z-index:9998;display:flex;align-items:center;gap:10px;background:#0b0b0c;color:#fff;border:0;border-radius:999px;padding:6px 18px 6px 6px;font:700 15px system-ui,-apple-system,sans-serif;box-shadow:0 10px 28px rgba(0,0,0,.28);cursor:pointer}'+
 '.oc-b img{width:40px;height:40px;border-radius:50%;object-fit:cover;border:2px solid #E60012}.oc-b .oc-dot{position:absolute;left:38px;top:6px;width:11px;height:11px;border-radius:50%;background:#22c55e;border:2px solid #0b0b0c}'+
 '.oc-b small{display:block;font-weight:500;font-size:11.5px;color:#a1a1aa;line-height:1.2;margin-top:1px}.oc-b span{line-height:1.2;text-align:left;max-width:360px}.oc-b b{display:block;font-weight:700}.oc-b .oc-short{display:none}'+
 '.oc-p{position:fixed;right:16px;bottom:84px;z-index:9999;width:min(380px,calc(100vw - 24px));height:min(600px,calc(100vh - 110px));background:#fff;border-radius:18px;box-shadow:0 18px 50px rgba(0,0,0,.32);display:none;flex-direction:column;overflow:hidden;font:15px/1.45 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:#26262b}.oc-p.on{display:flex}'+
 '.oc-h{display:flex;align-items:center;gap:11px;padding:13px 14px;background:#0b0b0c;color:#fff}.oc-h img{width:42px;height:42px;border-radius:50%;object-fit:cover;flex:none}.oc-h b{display:block;font-size:15.5px}.oc-h small{color:#a1a1aa;font-size:12px}'+
 '.oc-x0{margin-left:auto;background:none;border:0;color:#fff;font-size:24px;line-height:1;cursor:pointer;padding:4px 6px;width:auto}'+
 '.oc-bd{flex:1;display:flex;flex-direction:column;min-height:0}'+
 '.oc-m{flex:1;overflow:auto;padding:14px;display:flex;flex-direction:column;gap:9px;background:#f6f6f7}'+
 '.oc-x{max-width:84%;padding:8px 12px;border-radius:15px 15px 15px 4px;background:#fff;border:1px solid #ececef;align-self:flex-start;white-space:pre-wrap;font-size:14.5px}.oc-x small{display:block;font-size:10.5px;color:#6b6b73;margin-top:2px}.oc-x .oc-who{font-weight:700;color:#E60012;font-size:11.5px;margin:0 0 2px}'+
 '.oc-x.you{align-self:flex-end;background:#E60012;border-color:#E60012;color:#fff;border-radius:15px 15px 4px 15px}.oc-x.you small{color:rgba(255,255,255,.8)}'+
 '.oc-sys{align-self:center;text-align:center;font-size:12.5px;color:#166534;background:#dcfce7;border-radius:10px;padding:6px 12px;max-width:92%}'+
 '.oc-f{display:flex;gap:8px;padding:10px;border-top:1px solid #e7e7ea;background:#fff}.oc-f input{flex:1;min-width:0;width:auto;padding:11px 14px;border:1px solid #d4d4d8;border-radius:999px;font:inherit;font-size:16px;margin:0}'+
 '.oc-f button,.oc-pre button.oc-go{flex:none;width:auto;margin:0;background:#E60012;color:#fff;border:0;border-radius:999px;padding:0 18px;font-weight:700;font-size:15px;cursor:pointer;min-height:44px}'+
 '.oc-ft{display:flex;justify-content:space-between;align-items:center;gap:8px;padding:6px 12px 10px;background:#fff;font-size:12px;color:#6b6b73}'+
 '.oc-hu{flex:none;width:auto;margin:0;background:#fff;color:#0b0b0c;border:1.5px solid #0b0b0c;border-radius:999px;padding:6px 12px;font:600 13px system-ui,sans-serif;cursor:pointer}.oc-hu[disabled]{opacity:.5}'+
 '.oc-pre{padding:16px;overflow:auto;background:#fff}.oc-pre p{margin:0 0 10px;font-size:14.5px}.oc-pre label{display:block;font-weight:600;font-size:13.5px;margin:10px 0 4px}.oc-pre label small{font-weight:400;color:#6b6b73}'+
 '.oc-pre input{display:block;width:100%;box-sizing:border-box;padding:11px 12px;border:1px solid #d4d4d8;border-radius:10px;font:inherit;font-size:16px;margin:0}.oc-pre input:focus,.oc-f input:focus{outline:2px solid rgba(230,0,18,.25);border-color:#E60012}'+
 '.oc-pre .oc-err{color:#b91c1c;font-size:12.5px;margin:3px 0 0}.oc-pre .oc-cons{font-size:12px;color:#6b6b73;margin:12px 0}.oc-pre .oc-cons a{color:#b8000e}.oc-pre button.oc-go{width:100%;margin-top:4px}'+
 '@media(max-width:600px){.oc-b.oc-seen .oc-full{display:none}.oc-b.oc-seen .oc-short{display:block}.oc-b.oc-app .oc-full{display:block!important;font-size:12.5px;white-space:normal;max-width:210px;line-height:1.2}.oc-b.oc-app .oc-short{display:none!important}.oc-b.oc-app small{display:none}}'+
 '@media(max-width:340px){.oc-b .oc-full{display:none}.oc-b .oc-short{display:block}}'+
 '@media(max-width:600px){.oc-b{right:12px;bottom:12px;padding:5px 14px 5px 5px;font-size:13.5px;max-width:calc(100vw - 24px)}.oc-b span{max-width:215px}.oc-b small{display:none}.oc-b img{width:36px;height:36px}.oc-b .oc-dot{left:34px}.oc-p{right:8px;left:8px;width:auto;bottom:70px;height:calc(100vh - 86px);height:calc(100dvh - 86px)}}';
 document.head.appendChild(st);
 b=el('button','oc-b');b.type='button';b.setAttribute('aria-label','Chat with Richard Cuagdan');b.style.position='fixed';
 b.innerHTML='<img src="/assets/img/richard-300.webp" alt="" width="40" height="40"><i class="oc-dot"></i><span class="oc-bl"></span>';
 p=el('div','oc-p');p.setAttribute('role','dialog');p.setAttribute('aria-label','Chat with Richard Cuagdan');
 p.innerHTML='<div class="oc-h"><img src="/assets/img/richard-300.webp" alt="" width="42" height="42"><div><b>'+AGENT+'</b><small>'+ROLE+'</small></div><button type="button" class="oc-x0" aria-label="Close">×</button></div><div class="oc-bd"></div>';
 document.body.appendChild(b);document.body.appendChild(p);body=p.querySelector('.oc-bd');label();
 try{if(localStorage.getItem('oc_seen'))b.classList.add('oc-seen')}catch(e){}
 b.onclick=function(){try{localStorage.setItem('oc_seen','1')}catch(e){}if(p.classList.contains('on'))hide();else show({})};p.querySelector('.oc-x0').onclick=hide;
 document.addEventListener('keydown',function(e){if(e.key==='Escape'&&p.classList.contains('on'))hide()});
 new MutationObserver(label).observe(document.documentElement,{attributes:true,attributeFilter:['data-lang']});document.addEventListener('rc:mounted',label);document.addEventListener('st:tracked',label);
 if(pend){var o=pend;pend=null;show(o)}}
function appMode(){return /^\/status\/?$/.test(location.pathname)&&!!window.__stTracked&&!!refSess()}
function label(){var l=b&&b.querySelector('.oc-bl');if(!l)return;var ap=appMode();b.classList.toggle('oc-app',ap);
 l.innerHTML='<b class="oc-full">'+(ap?T('May tanong sa application mo? Chat with us','Questions about your application? Chat with us'):T('Mag-inquire kay Richard','Inquire with Richard'))+'</b><b class="oc-short">'+(ap?'Chat with us':T('Mag-inquire kay Richard','Inquire with Richard'))+'</b><small>'+T('Karaniwang sumasagot within the day','Usually replies within the day')+'</small>'}
function hide(){p.classList.remove('on');clearInterval(timer);timer=null}
function show(o){var rs=refSess();
 if(rs){var inl=document.querySelector('#af-rc .rc,#st-rc .rc');if(inl){inl.scrollIntoView({behavior:'smooth',block:'center'});var i=inl.querySelector('.rc-f input');if(i)setTimeout(function(){i.focus()},400);return}
  p.classList.add('on');body.innerHTML='<div class="oc-ref" style="overflow:auto;padding:0 8px"></div>';var host=body.firstChild;
  (function w(n){if(window.RefChat){RefChat.mount(host,{ref:rs.ref,last4:rs.last4,name:rs.name,title:T('Ang application mo','Your application')})}else{if(n===0){var s=document.createElement('script');s.src='/assets/refchat.js';document.head.appendChild(s)}if(n<40)setTimeout(function(){w(n+1)},250)}})(0);return}
 if(o.name)prof.name=o.name;if(o.mobile)prof.mobile=o.mobile;if(o.email)prof.email=o.email;
 p.classList.add('on');if(o.name&&o.mobile)save();
 if(!prof.name||!prof.mobile)pre(o);else chat(o)}
function save(){try{localStorage.setItem(PK,JSON.stringify({name:prof.name,mobile:prof.mobile,email:prof.email||''}))}catch(e){}}
function pre(o){clearInterval(timer);
 body.innerHTML='<form class="oc-pre" novalidate><p><b>'+T('Hi! Ako si Richard.','Hi! I\'m Richard.')+'</b> '+T('Ilagay lang ang pangalan at mobile para makasagot ako agad, kahit offline ka na.','Leave your name and mobile so I can get back to you, even if you go offline.')+'</p>'+
  '<label for="oc-n">'+T('Pangalan','Name')+'</label><input id="oc-n" autocomplete="name" maxlength="60" required><p class="oc-err" hidden id="oc-en">'+T('Ilagay ang pangalan mo.','Please enter your name.')+'</p>'+
  '<label for="oc-mo">Mobile</label><input id="oc-mo" type="tel" inputmode="tel" autocomplete="tel" placeholder="09XX XXX XXXX" maxlength="16" required><p class="oc-err" hidden id="oc-emo">'+T('Pakicheck ang mobile number (hal. 09171234567).','Please check the mobile number (e.g. 09171234567).')+'</p>'+
  '<label for="oc-em">Email <small>('+T('optional, para ma-email ka kapag sumagot ako','optional, so I can email you when I reply')+')</small></label><input id="oc-em" type="email" inputmode="email" autocomplete="email" maxlength="120" placeholder="you@email.com"><p class="oc-err" hidden id="oc-eem">'+T('Pakicheck ang email.','Please check the email.')+'</p>'+
  '<p class="oc-cons">🔒 '+T('Sa pag-start ng chat, pumapayag ka na gamitin ang info mo para sagutin ang inquiry mo, ayon sa aming <a href="/privacy/" target="_blank">Privacy Notice</a>.','By starting the chat, you agree that we use your details only to reply to your inquiry, per our <a href="/privacy/" target="_blank">Privacy Notice</a>.')+'</p>'+
  '<button class="oc-go">'+T('Simulan ang chat','Start chat')+'</button></form>';
 var f=body.querySelector('form'),n=f.querySelector('#oc-n'),mo=f.querySelector('#oc-mo'),em=f.querySelector('#oc-em');n.value=prof.name||'';mo.value=prof.mobile||'';em.value=prof.email||'';
 setTimeout(function(){(prof.name?mo:n).focus()},50);
 f.onsubmit=function(e){e.preventDefault();var nv=n.value.trim(),mv=mo.value.replace(/[\s()-]/g,''),ev=em.value.trim(),bad=false;
  function err(i,on){f.querySelector('#'+i).hidden=!on;if(on)bad=true}
  err('oc-en',nv.length<2);err('oc-emo',!Lead.okMobile(mv));err('oc-eem',!!ev&&!/^[^@\s<>"',;]+@[^@\s<>"',;]+\.[A-Za-z]{2,}$/.test(ev));if(bad)return;
  prof={name:nv,mobile:mv,email:ev};save();chat(o||{})}}
function draw(list){if(list)last=list;var h='';
 if(!last.length)h+='<div class="oc-x"><p class="oc-who">'+AGENT+' · '+ROLE+'</p>'+esc(T('Hi '+(prof.name||'').split(' ')[0]+'! Ano ang gusto mong malaman: unit, promo, down payment o financing?','Hi '+(prof.name||'').split(' ')[0]+'! What can I help you with: a unit, promos, down payment or financing?'))+'</div>';
 last.forEach(function(x){h+='<div class="oc-x'+(x.from==='you'?' you':'')+'">'+(x.from==='you'?'':'<p class="oc-who">'+AGENT+' · '+ROLE+'</p>')+esc(x.text)+'<small>'+esc(tm(x.t))+'</small></div>'});
 sys.forEach(function(t){h+='<div class="oc-sys">'+esc(t)+'</div>'});if(m){m.innerHTML=h;m.scrollTop=1e9}}
function poll(){return post({action:'chat_poll'}).then(function(r){if(r&&r.ok)draw(r.msgs)}).catch(function(){})}
function chat(o){body.innerHTML='<div class="oc-m" role="log" aria-live="polite"></div><form class="oc-f"><label class="vh" for="oc-in" style="position:absolute;left:-9999px">Message</label><input id="oc-in" placeholder="'+esc(T('I-type ang mensahe…','Type your message…'))+'" maxlength="1000" autocomplete="off"><button>'+T('Send','Send')+'</button></form>'+
  '<div class="oc-ft"><span>'+T('Mon–Sat, 8AM–5PM · sasagot ako dito','Mon–Sat, 8AM–5PM · I reply here')+(prof.email?'':' · <a href="#" class="oc-ed" style="color:#b8000e">'+T('+ email','+ email')+'</a>')+'</span><button type="button" class="oc-hu">🙋 '+T('Kausapin si Richard','Talk to a human')+'</button></div>';
 m=body.querySelector('.oc-m');var inp=body.querySelector('#oc-in'),hu=body.querySelector('.oc-hu'),ed=body.querySelector('.oc-ed');
 if(ed)ed.onclick=function(e){e.preventDefault();pre(o)};
 if(o&&o.text)inp.value=o.text;
 body.querySelector('.oc-f').onsubmit=function(e){e.preventDefault();var t=inp.value.trim();if(!t)return;inp.value='';last=last.concat([{from:'you',text:t,t:Date.now()}]);draw();
  post({action:'chat_send',msg:t,name:prof.name,mobile:prof.mobile,email:prof.email||'',page:location.pathname}).then(function(r){if(r&&r.ok)return poll();if(r&&r.error==='need_contact'){pre(o);return}sys.push(r&&r.error==='rate'?T('Masyadong maraming message. Subukan ulit mamaya.','Too many messages. Please try again later.'):T('Hindi na-send. Pakisubukan ulit.','Not sent. Please try again.'));draw()}).catch(function(){sys.push(T('May problema sa connection.','Connection problem.'));draw()});
  try{if(typeof gtag==='function')gtag('event','chat_message',{provider:'own'})}catch(_){}};
 hu.onclick=function(){hu.disabled=true;var go=function(){post({action:'chat_human',page:location.pathname}).then(function(r){sys.push(r&&r.ok?T('Na-notify na si Richard Cuagdan at sasagot siya dito sa lalong madaling panahon.','Richard Cuagdan has been notified and will reply here shortly.'):T('Hindi ma-notify ngayon. Pakisubukan ulit.','Could not notify right now. Please try again.'));if(!(r&&r.ok))hu.disabled=false;draw()}).catch(function(){hu.disabled=false})};
  if(last.some(function(x){return x.from==='you'}))go();else post({action:'chat_send',msg:T('Gusto kong makausap si Richard.','I would like to talk to Richard.'),name:prof.name,mobile:prof.mobile,email:prof.email||'',page:location.pathname}).then(go)};
 draw();poll();setTimeout(function(){inp.focus()},50);clearInterval(timer);timer=setInterval(function(){if(!document.hidden&&p.classList.contains('on'))poll()},8000)}
})();
