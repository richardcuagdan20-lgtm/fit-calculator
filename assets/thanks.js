/* /thank-you/ conversion point for "Inquire this promo" (one source of truth for the inquiry conversion).
   inquiry.js sets sessionStorage "iq_ty" ({id,unit,ts}) only after a real, non-spam send, then redirects here.
   This page reads the token, REMOVES it, and fires once: Meta Pixel Lead + GA4 generate_lead (via Lead.fire, same value + event_id),
   custom InquirePromo, and the Google Ads conversion when window.GADS_CONV = {id:"AW-...",label:"..."} is set by the build.
   Direct visit, refresh, back/forward or a stale token (>30 min) -> token missing -> nothing fires. */
(function(){
var K='iq_ty',t=null;
try{t=JSON.parse(sessionStorage.getItem(K)||'null');sessionStorage.removeItem(K)}catch(_){t=null}
if(!t||typeof t.id!=='string'||!/^[A-Za-z0-9_.-]{6,80}$/.test(t.id)||!(Date.now()-(+t.ts||0)<30*60*1000))return;
function go(){
 var unit=String(t.unit||'').slice(0,80),ex={content_category:'promos',source:'promos-inquiry',unit:unit},L={event_id:t.id},val=100;
 try{if(window.Lead&&Lead.LEAD_VALUES&&Lead.LEAD_VALUES['promos-inquiry']!==undefined)val=Lead.LEAD_VALUES['promos-inquiry']}catch(_){}
 try{
  if(window.Lead&&Lead.fire)Lead.fire('promos-inquiry',L,ex);
  else{
   if(typeof window.fbq==='function')window.fbq('track','Lead',{value:val,currency:'PHP',content_name:'promos-inquiry',content_category:'promos',source:'promos-inquiry',unit:unit},{eventID:t.id});
   if(typeof window.gtag==='function')window.gtag('event','generate_lead',{value:val,currency:'PHP',form:'promos-inquiry',event_id:t.id,unit:unit});
  }
 }catch(_){}
 try{if(window.rpTrack)window.rpTrack('InquirePromo',{content_name:'promos-inquiry',content_category:'promos',source:'promos-inquiry',unit:unit},true)}catch(_){}
 try{var G=window.GADS_CONV||{};
  if(G.id&&G.label&&typeof window.gtag==='function')window.gtag('event','conversion',{send_to:G.id+'/'+G.label,value:val,currency:'PHP',transaction_id:t.id})}catch(_){}
}
if(document.readyState!=='complete')document.addEventListener('DOMContentLoaded',go);else go();  /* deferred: runs after track.js (rpTrack) */
})();
