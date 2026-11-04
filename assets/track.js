/* rpTrack: Meta Pixel + GA4 funnel events and tracked Messenger links. Pixel ID lives in the page head (fbq init); this file never inits a pixel.
   window.rpTrack(event, params, custom)  -> fbq('track'|'trackCustom') + gtag('event'); safe no-op when trackers are blocked.
   window.rpMsgr(source)                  -> tracked Messenger URL (m.me/<page>?ref=web_<source>[__utm]) and fires Pixel "Contact". */
(function(){
var PAGE='https://m.me/504759566043148',K='rp_utm';
/* MPTrack attribution: first touch (never overwritten for 30 days) + last touch (updated on each new UTM/click-id arrival).
   Stored in sessionStorage AND a first-party cookie (30 days, SameSite=Lax, path=/). No personal data. */
var AK=['utm_source','utm_medium','utm_campaign','utm_content','utm_term','utm_id','fbclid','gclid'],FT='mp_ft',LT='mp_lt',DAYS=30;
function rdC(n){try{var m=document.cookie.match(new RegExp('(?:^|; )'+n+'=([^;]*)'));return m?JSON.parse(decodeURIComponent(m[1])):null}catch(_){return null}}
function wrC(n,o){try{document.cookie=n+'='+encodeURIComponent(JSON.stringify(o))+';max-age='+(DAYS*86400)+';path=/;SameSite=Lax'+(location.protocol==='https:'?';Secure':'')}catch(_){}}
function rdS(n){try{return JSON.parse(sessionStorage.getItem(n)||'null')}catch(_){return null}}
function wrS(n,o){try{sessionStorage.setItem(n,JSON.stringify(o))}catch(_){}}
function get(n){return rdS(n)||rdC(n)}
function put(n,o){wrS(n,o);wrC(n,o)}
function nowIso(){try{return new Date().toISOString()}catch(_){return ''}}
function attrInit(){var q,n={},has=false;try{q=new URLSearchParams(location.search)}catch(_){q=null}
 if(q)AK.forEach(function(k){var v=q.get(k);if(v){n[k]=String(v).slice(0,k==='fbclid'||k==='gclid'?300:120);has=true}});
 var land=(location.origin+location.pathname).slice(0,200),ft=get(FT);
 if(!ft){ft={landing:land,ts:nowIso(),ref:(document.referrer||'').slice(0,200)};AK.forEach(function(k){if(n[k])ft[k]=n[k]});put(FT,ft)}
 else{wrS(FT,ft)}   /* refresh session copy; cookie keeps its original 30-day expiry window */
 if(has){var lt={landing:land,ts:nowIso()};AK.forEach(function(k){if(n[k])lt[k]=n[k]});put(LT,lt)}
}
try{attrInit()}catch(_){}
function getAttribution(){var ft=get(FT)||{},lt=get(LT)||{},o={},src=AK.some(function(k){return ft[k]})?ft:lt;
 AK.forEach(function(k){o[k]=src[k]||''});
 o.ad_id=o.utm_content;o.ft_landing=ft.landing||'';o.ft_time=ft.ts||'';
 o.lt_utm=lt.ts?[lt.utm_source,lt.utm_medium,lt.utm_campaign,lt.utm_content,lt.utm_term].map(function(x){return x||''}).join('|')+' @ '+lt.ts:'';
 return o}
window.MPTrack={getAttribution:getAttribution,KEYS:AK.slice()};
function utm(){var a=getAttribution(),o={};['utm_source','utm_medium','utm_campaign','utm_content'].forEach(function(k){if(a[k])o[k]=String(a[k]).slice(0,80)});
 try{if(Object.keys(o).length)sessionStorage.setItem(K,JSON.stringify(o))}catch(_){}
 return o}
var U=utm();
function pg(){return (location.pathname.replace(/^\/|\/$/g,'').replace(/[\/]+/g,'_')||'home').slice(0,60)}
function clean(s){return String(s).replace(/[^A-Za-z0-9_.=:-]+/g,'-').slice(0,240)}
function ref(source){var r='web_'+source;var u=[U.utm_source,U.utm_medium,U.utm_campaign,U.utm_content].filter(Boolean).join('_');if(u)r+='__'+u;return clean(r)}
function rpTrack(ev,p,custom){var d={};for(var k in U)d[k]=U[k];for(k in (p||{}))d[k]=p[k];d.page=d.page||pg();
 try{if(typeof window.fbq==='function')window.fbq(custom?'trackCustom':'track',ev,d)}catch(_){}
 try{if(typeof window.gtag==='function')window.gtag('event',ev,d)}catch(_){}}
function base(h){var m=/^https:\/\/m\.me\/[^?#]+/.exec(h||'');return m?m[0]:PAGE}
function src(a){var s=a.getAttribute('data-msgr');if(s==='header')return pg()+'-header';if(s==='floating')return 'floating_'+pg();if(s)return s;var p=pg();if(a.closest&&a.closest('footer'))return p+'-footer';if(a.closest&&a.closest('header'))return p+'-header';return p}
function msgUrl(source,h){return base(h)+'?ref='+encodeURIComponent(ref(source))}
window.rpTrack=rpTrack;
window.rpMsgr=function(source,h){source=clean(source||pg());rpTrack('Contact',{source:source,method:'messenger',content_name:'messenger'});return msgUrl(source,h)};
function wire(){document.querySelectorAll('a[href^="https://m.me/"]').forEach(function(a){if(a.__rp)return;a.__rp=1;var s=clean(src(a));a.setAttribute('data-msgr',s);a.href=msgUrl(s,a.getAttribute('href'))})}
document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[href^="https://m.me/"]');if(!a)return;wire();
 rpTrack('Contact',{source:a.getAttribute('data-msgr')||pg(),method:'messenger',content_name:'messenger'})},true);
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',wire);else wire();
try{new MutationObserver(function(){wire()}).observe(document.documentElement,{childList:true,subtree:true})}catch(_){}
})();
/* HeroCTA: single hero button click -> Pixel ViewContent + custom HeroCTA */
document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[data-herocta]');if(!a||!window.rpTrack)return;var p={source:a.getAttribute('data-herocta'),content_name:'hero_view_promos',content_category:'promos'};window.rpTrack('ViewContent',p);window.rpTrack('HeroCTA',p,true)});

document.addEventListener('click',function(ev){var a=ev.target.closest&&ev.target.closest('a[data-brochure]');if(!a)return;try{if(typeof window.gtag==='function')window.gtag('event','brochure_download',{model:a.getAttribute('data-brochure'),link_url:a.href})}catch(_){}},true);

/* Wave 1 (draft): funnel events. ViewContent/view_item on [data-vc]; Contact/contact_messenger on [data-track=msg];
   PreQualStart/prequal_start on every link to /loan-assessment/; faq_open on accordion FAQs. */
(function(){
function px(ev,p,c){try{if(typeof window.fbq==='function')window.fbq(c?'trackCustom':'track',ev,p)}catch(_){}}
function ga(ev,p){try{if(typeof window.gtag==='function')window.gtag('event',ev,p)}catch(_){}}
function init(){var v=document.querySelector('[data-vc]');if(v){var m=v.getAttribute('data-model'),t=v.getAttribute('data-ptype');px('ViewContent',{content_name:m,content_category:t});ga('view_item',{model:m,page_type:t})}
 document.querySelectorAll('details.faq').forEach(function(d){d.addEventListener('toggle',function(){if(d.open){var s=d.querySelector('summary');ga('faq_open',{question:s?s.textContent.slice(0,100):''})}})})}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a');if(!a)return;var h=a.getAttribute('href')||'',v=document.querySelector('[data-vc]'),mdl=a.getAttribute('data-model')||(v&&v.getAttribute('data-model'))||'';
 if(a.getAttribute('data-track')==='msg'){ga('contact_messenger',{placement:a.getAttribute('data-place')||'',variant:a.getAttribute('data-variant')||'',model:mdl})}
 if(h.indexOf('/loan-assessment/')===0){var s='';try{s=new URL(a.href).searchParams.get('src')||''}catch(_){}px('PreQualStart',{src:s,model:mdl},true);ga('prequal_start',{src:s,model:mdl})}},true);
})();
