/* Shared lead helpers: same webhook + payload format as /budgetcalculator/ (fields match apps_script.gs). */
/* Anti-spam guard: honeypot + min fill time + per-form rate limit + optional Cloudflare Turnstile (invisible). Bots get a silent fake success. */
var AS=(function(){
var TURNSTILE_SITEKEY='0x4AAAAAAFfHOepv9hv-XBSh'; // Cloudflare Turnstile sitekey. Empty = Turnstile skipped entirely.
var MIN_MS=3000,GAP_MS=30000,tok='',wid=null,pend=[],loading=false;
function since(){try{return performance.now()}catch(e){return 1e9}}
function hpVal(){var a=document.querySelectorAll('input.as-hp'),v='';for(var i=0;i<a.length;i++)v+=a[i].value||'';return v}
function render(el){try{wid=window.turnstile.render(el,{sitekey:TURNSTILE_SITEKEY,appearance:'interaction-only',execution:'execute',callback:function(t){tok=t;flush(t)},'expired-callback':function(){tok=''},'error-callback':function(){tok='';flush('');return true}})}catch(e){}}
var waiters=[];function flush(t){var w=waiters;waiters=[];w.forEach(function(f){f(t)})}
function getToken(ms){return new Promise(function(res){if(!TURNSTILE_SITEKEY||wid===null||!window.turnstile){res('');return}
 var done=false,fin=function(t){if(!done){done=true;res(t||'')}};waiters.push(fin);setTimeout(function(){fin('')},ms||5000);
 try{window.turnstile.reset(wid);window.turnstile.execute(wid)}catch(e){fin('')}})}
function loadTs(el){if(!TURNSTILE_SITEKEY)return;pend.push(el);if(window.turnstile){render(el);return}if(loading)return;loading=true;
 window.__asTsReady=function(){while(pend.length)render(pend.shift())};
 var s=document.createElement('script');s.src='https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit&onload=__asTsReady';s.async=true;s.defer=true;s.onerror=function(){pend=[]};document.head.appendChild(s)}
function init(el,before){if(!el||el.querySelector&&el.querySelector('.as-hp'))return;
 var d=document.createElement('div');d.setAttribute('aria-hidden','true');d.style.cssText='position:absolute!important;left:-10000px!important;top:auto;width:1px;height:1px;overflow:hidden';
 d.innerHTML='<label>Leave this field empty<input type="text" name="website" class="as-hp" tabindex="-1" autocomplete="off" value=""></label>';
 if(before)el.parentNode.insertBefore(d,el);else el.appendChild(d);
 if(TURNSTILE_SITEKEY){var t=document.createElement('div');t.className='as-ts';if(before)el.parentNode.insertBefore(t,el);else el.appendChild(t);loadTs(t)}}
function check(key){if(hpVal())return 'bot';if(since()<MIN_MS)return 'bot';
 var k='as_last_'+key,n=Date.now(),l=0;try{l=+localStorage.getItem(k)||0}catch(e){}
 if(l&&n-l<GAP_MS&&n>=l)return 'dup';try{localStorage.setItem(k,String(n))}catch(e){}return 'ok'}
function stamp(L,t){L.website=hpVal();L.cf_turnstile_token=t||'';return L}
return {getToken:getToken,init:init,check:check,stamp:stamp,SITEKEY:TURNSTILE_SITEKEY};
})();
(function(){
var URL_='https://script.google.com/macros/s/AKfycbzP4moZ9QL3YB_liQsoqM80o9IfTBa-GMapQg1uLJF1xAOPLyvJ6PVhHb-nQ7A__hWsTA/exec';
var MSG='https://m.me/504759566043148';
function $(id){return document.getElementById(id)}
function stamp(){var p=new Intl.DateTimeFormat('en-CA',{timeZone:'Asia/Manila',year:'numeric',month:'2-digit',day:'2-digit',hour:'2-digit',minute:'2-digit',second:'2-digit',hour12:false}).formatToParts(new Date()).reduce(function(a,x){a[x.type]=x.value;return a},{});return p.year+'-'+p.month+'-'+p.day+' '+(p.hour==='24'?'00':p.hour)+':'+p.minute+':'+p.second+' +08:00'}
function lid(){var c='ABCDEFGHJKLMNPQRSTUVWXYZ23456789',s='';for(var i=0;i<6;i++)s+=c[Math.floor(Math.random()*c.length)];return s}
function okMobile(m){m=m.replace(/[\s()-]/g,'');return /^(09\d{9}|\+639\d{9}|\+\d{8,15})$/.test(m)}
function beacon(b){try{return !!(navigator.sendBeacon&&navigator.sendBeacon(URL_,new Blob([b],{type:'text/plain;charset=utf-8'})))}catch(e){return false}}
var skip=false;
function send(lead){var c=AS.check(lead&&lead.via||'form');skip=c!=='ok';if(skip)return new Promise(function(r){setTimeout(function(){r(true)},600)});return AS.getToken(5000).then(function(t){AS.stamp(lead,t);return Promise.race([send0(lead),new Promise(function(r){setTimeout(function(){r(true)},2500)})])})}
function send0(lead){var b;try{b=JSON.stringify(lead)}catch(e){return Promise.resolve(false)}
  try{return fetch(URL_,{method:'POST',mode:'no-cors',keepalive:true,cache:'no-store',headers:{'Content-Type':'text/plain;charset=utf-8'},body:b}).then(function(){return true}).catch(function(){return beacon(b)})}catch(e){return Promise.resolve(beacon(b))}}
function track(unit){if(skip)return;
  try{if(typeof window.fbq==='function')window.fbq('track','Lead',{content_name:unit})}catch(_){}
  try{if(typeof window.gtag==='function')window.gtag('event','generate_lead',{unit:unit,value:0,currency:'PHP'})}catch(_){}
}
function base(via){var q=new URLSearchParams(location.search);
  return {timestamp:stamp(),leadId:lid(),tier:via,via:via,consent:true,source:location.origin+location.pathname,
   utm_source:q.get('utm_source')||'',utm_campaign:q.get('utm_campaign')||'',utm_content:q.get('utm_content')||'',adset:q.get('adset')||q.get('utm_term')||q.get('utm_medium')||''}}
function err(f,on){var el=$('e_'+f);if(el)el.hidden=!on;var i=$(f);if(i)i.setAttribute('aria-invalid',on?'true':'false');return on}
document.addEventListener('DOMContentLoaded',function(){['gf','af','tf'].forEach(function(i){var f=$(i);if(f)AS.init(f)})});
window.Lead={V4:true,CHAT:false,REFCHAT:false,url:URL_,skipped:function(){return skip},send:send,track:track,base:base,okMobile:okMobile,err:err,MSG:MSG};
})();
/* Own live chat widget: feature flag OFF (set CHAT:true above to load /assets/chat.js). */
(function(){try{if(window.Lead&&window.Lead.CHAT===true){var s=document.createElement('script');s.src='/assets/chat.js';s.defer=true;document.head.appendChild(s)}}catch(e){}})();
/* Ref-linked application chat on /apply/ thank-you + /status/: flag OFF (REFCHAT:true loads /assets/refchat.js). */
(function(){try{if(window.Lead&&window.Lead.REFCHAT===true){var s=document.createElement('script');s.src='/assets/refchat.js';s.defer=true;document.head.appendChild(s)}}catch(e){}})();
