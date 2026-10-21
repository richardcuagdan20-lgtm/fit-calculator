/* Shared lead helpers: same webhook + payload format as /budgetcalculator/ (fields match apps_script.gs). */
(function(){
var URL_='https://script.google.com/macros/s/AKfycbzP4moZ9QL3YB_liQsoqM80o9IfTBa-GMapQg1uLJF1xAOPLyvJ6PVhHb-nQ7A__hWsTA/exec';
var MSG='https://m.me/504759566043148';
function $(id){return document.getElementById(id)}
function stamp(){var p=new Intl.DateTimeFormat('en-CA',{timeZone:'Asia/Manila',year:'numeric',month:'2-digit',day:'2-digit',hour:'2-digit',minute:'2-digit',second:'2-digit',hour12:false}).formatToParts(new Date()).reduce(function(a,x){a[x.type]=x.value;return a},{});return p.year+'-'+p.month+'-'+p.day+' '+(p.hour==='24'?'00':p.hour)+':'+p.minute+':'+p.second+' +08:00'}
function lid(){var c='ABCDEFGHJKLMNPQRSTUVWXYZ23456789',s='';for(var i=0;i<6;i++)s+=c[Math.floor(Math.random()*c.length)];return s}
function okMobile(m){m=m.replace(/[\s()-]/g,'');return /^(09\d{9}|\+639\d{9}|\+\d{8,15})$/.test(m)}
function beacon(b){try{return !!(navigator.sendBeacon&&navigator.sendBeacon(URL_,new Blob([b],{type:'text/plain;charset=utf-8'})))}catch(e){return false}}
function send(lead){var b;try{b=JSON.stringify(lead)}catch(e){return Promise.resolve(false)}
  try{return fetch(URL_,{method:'POST',mode:'no-cors',keepalive:true,cache:'no-store',headers:{'Content-Type':'text/plain;charset=utf-8'},body:b}).then(function(){return true}).catch(function(){return beacon(b)})}catch(e){return Promise.resolve(beacon(b))}}
function track(unit){
  try{if(typeof window.fbq==='function')window.fbq('track','Lead',{content_name:unit})}catch(_){}
  try{if(typeof window.gtag==='function')window.gtag('event','generate_lead',{unit:unit,value:0,currency:'PHP'})}catch(_){}
}
function base(via){var q=new URLSearchParams(location.search);
  return {timestamp:stamp(),leadId:lid(),tier:via,via:via,consent:true,source:location.origin+location.pathname,
   utm_source:q.get('utm_source')||'',utm_campaign:q.get('utm_campaign')||'',utm_content:q.get('utm_content')||'',adset:q.get('adset')||q.get('utm_term')||q.get('utm_medium')||''}}
function err(f,on){var el=$('e_'+f);if(el)el.hidden=!on;var i=$(f);if(i)i.setAttribute('aria-invalid',on?'true':'false');return on}
window.Lead={send:send,track:track,base:base,okMobile:okMobile,err:err,MSG:MSG};
})();
