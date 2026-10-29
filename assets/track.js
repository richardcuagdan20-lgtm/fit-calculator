/* rpTrack: Meta Pixel + GA4 funnel events and tracked Messenger links. Pixel ID lives in the page head (fbq init); this file never inits a pixel.
   window.rpTrack(event, params, custom)  -> fbq('track'|'trackCustom') + gtag('event'); safe no-op when trackers are blocked.
   window.rpMsgr(source)                  -> tracked Messenger URL (m.me/<page>?ref=web_<source>[__utm]) and fires Pixel "Contact". */
(function(){
var PAGE='https://m.me/504759566043148',K='rp_utm';
function utm(){var o={};try{o=JSON.parse(sessionStorage.getItem(K)||'{}')}catch(_){}
 try{var q=new URLSearchParams(location.search),n={};['utm_source','utm_medium','utm_campaign','utm_content'].forEach(function(k){var v=q.get(k);if(v)n[k]=v.slice(0,80)});
  if(Object.keys(n).length){o=n;sessionStorage.setItem(K,JSON.stringify(o))}}catch(_){}
 return o}
var U=utm();
function pg(){return (location.pathname.replace(/^\/|\/$/g,'').replace(/[\/]+/g,'_')||'home').slice(0,60)}
function clean(s){return String(s).replace(/[^A-Za-z0-9_.=:-]+/g,'-').slice(0,240)}
function ref(source){var r='web_'+source;var u=[U.utm_source,U.utm_medium,U.utm_campaign].filter(Boolean).join('_');if(u)r+='__'+u;return clean(r)}
function rpTrack(ev,p,custom){var d={};for(var k in U)d[k]=U[k];for(k in (p||{}))d[k]=p[k];d.page=d.page||pg();
 try{if(typeof window.fbq==='function')window.fbq(custom?'trackCustom':'track',ev,d)}catch(_){}
 try{if(typeof window.gtag==='function')window.gtag('event',ev,d)}catch(_){}}
function base(h){var m=/^https:\/\/m\.me\/[^?#]+/.exec(h||'');return m?m[0]:PAGE}
function src(a){var s=a.getAttribute('data-msgr');if(s==='header')return pg()+'-header';if(s)return s;var p=pg();if(a.closest&&a.closest('footer'))return p+'-footer';if(a.closest&&a.closest('header'))return p+'-header';return p}
function msgUrl(source,h){return base(h)+'?ref='+encodeURIComponent(ref(source))}
window.rpTrack=rpTrack;
window.rpMsgr=function(source,h){source=clean(source||pg());rpTrack('Contact',{source:source,method:'messenger',content_name:'messenger'});return msgUrl(source,h)};
function wire(){document.querySelectorAll('a[href^="https://m.me/"]').forEach(function(a){if(a.__rp)return;a.__rp=1;var s=clean(src(a));a.setAttribute('data-msgr',s);a.href=msgUrl(s,a.getAttribute('href'))})}
document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[href^="https://m.me/"]');if(!a)return;wire();
 rpTrack('Contact',{source:a.getAttribute('data-msgr')||pg(),method:'messenger',content_name:'messenger'})},true);
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',wire);else wire();
try{new MutationObserver(function(){wire()}).observe(document.documentElement,{childList:true,subtree:true})}catch(_){}
})();
