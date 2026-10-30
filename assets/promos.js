/* /promos/ Option A unlock: one lead form reveals Option A (lowest DP + monthly) on every unit; persisted in localStorage. */
(function(){
var $=function(i){return document.getElementById(i)},K='promos_optA_unlocked',H=document.documentElement,A=[];
try{A=JSON.parse(atob($('ab-a').textContent.trim()))}catch(_){}
var lang='en';
function setLang(l){lang=l==='tl'?'tl':'en';H.setAttribute('data-lang',lang);try{localStorage.setItem('site_lang',lang)}catch(_){}}
(function(){var q=(new URLSearchParams(location.search).get('lang')||'').toLowerCase(),s='';try{s=localStorage.getItem('site_lang')||''}catch(_){}setLang(q==='tl'||q==='en'?q:(s||'en'))})();
document.querySelectorAll('[data-setlang]').forEach(function(b){b.addEventListener('click',function(){setLang(b.dataset.setlang)})});
function peso(n){return '₱'+Math.round(n).toLocaleString('en-PH')}
function reveal(){document.querySelectorAll('[data-a]').forEach(function(el){var a=A[+el.getAttribute('data-a')];if(!a)return;var x=el.querySelectorAll('.ab-x');if(x[0])x[0].textContent=a[0]===0?'Zero DP Promo':peso(a[0]);if(x[1])x[1].textContent=peso(a[1])});H.classList.add('ab-open')}
var open=false;try{open=localStorage.getItem(K)==='1'}catch(_){}
if(open)reveal();
function T(ev,p,c){try{if(window.rpTrack){window.rpTrack(ev,p,c);return}if(typeof window.fbq==='function')window.fbq(c?'trackCustom':'track',ev,p)}catch(_){}}
/* Lead pop-up (2026-10-30): same #unlock form is moved into the dialog while open, then put back. */
var P=$('ab-pop'),slot=P&&P.querySelector('.abp-slot'),home=null,opener=null,DK='promos_pop_dismissed';
function popOk(){if(!P||/^\/(apply|status|loan-assessment)\//.test(location.pathname))return false;return true}
function dismissed(){try{if(sessionStorage.getItem(DK))return true;var t=+localStorage.getItem(DK)||0;return Date.now()-t<7*864e5}catch(_){return false}}
function foc(){return [].slice.call(P.querySelectorAll('a[href],button:not([disabled]),input:not([disabled]),[tabindex]:not([tabindex="-1"])')).filter(function(e){return e.offsetParent!==null})}
function popOpen(src){if(!popOk())return false;var f=$('unlock');if(!f)return false;if(!P.hidden)return true;opener=document.activeElement;
 if(!P.contains(f)){home=document.createComment('ab-home');f.parentNode.insertBefore(home,f);slot.appendChild(f)}P.hidden=false;H.classList.add('ab-popon');
 setTimeout(function(){try{(H.classList.contains('ab-open')?P.querySelector('.abp-x'):$('ab-name')).focus()}catch(_){}},30);return true}
function popClose(){if(!P||P.hidden)return;var f=$('unlock');if(home&&f){home.parentNode.insertBefore(f,home);home.parentNode.removeChild(home);home=null}
 P.hidden=true;H.classList.remove('ab-popon');try{sessionStorage.setItem(DK,'1');if(!H.classList.contains('ab-open'))localStorage.setItem(DK,String(Date.now()))}catch(_){}
 try{if(opener&&opener.focus)opener.focus({preventScroll:true})}catch(_){}}
if(P){P.addEventListener('click',function(e){if(e.target===P||e.target.closest('[data-popclose]'))popClose()});
 document.addEventListener('keydown',function(e){if(P.hidden)return;if(e.key==='Escape'){e.preventDefault();popClose();return}
  if(e.key==='Tab'){var F=foc();if(!F.length)return;var a=F[0],z=F[F.length-1];if(e.shiftKey&&document.activeElement===a){e.preventDefault();z.focus()}else if(!e.shiftKey&&document.activeElement===z){e.preventDefault();a.focus()}else if(!P.contains(document.activeElement)){e.preventDefault();a.focus()}}});
 if(!open&&!dismissed()&&popOk()){var fired=false,fire=function(){if(fired)return;fired=true;window.removeEventListener('scroll',sc);clearTimeout(tm);if(!H.classList.contains('ab-open')&&!dismissed())popOpen('popup-auto')},
  sc=function(){var d=document.documentElement;if((window.scrollY+innerHeight)/d.scrollHeight>=0.4&&window.scrollY>0)fire()},tm=setTimeout(fire,8000);window.addEventListener('scroll',sc,{passive:true})}}
window.abPopOpen=popOpen;
function toForm(){$('unlock').scrollIntoView({behavior:'smooth',block:'start'});setTimeout(function(){try{$('ab-name').focus({preventScroll:true})}catch(_){}},400)}
document.querySelectorAll('[data-unlock]').forEach(function(b){b.addEventListener('click',function(e){e.stopPropagation();if(!popOpen('unlock-button'))toForm()})});
/* locked Option A areas open the pop-up too */
document.querySelectorAll('[data-a]').forEach(function(el){el.addEventListener('click',function(){if(!H.classList.contains('ab-open'))popOpen('locked-area')})});
function hu(){if(location.hash==='#unlock'&&!open&&!popOpen('hash'))toForm()}hu();window.addEventListener('hashchange',hu);
document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('[data-inquire]');if(a)T('InquirePromo',{source:a.getAttribute('data-inquire'),content_name:'inquire-promo',content_category:'promos'},true)},true);
var f=$('ab-form');if(!f)return;if(window.AS)AS.init(f);
function er(id,on){var e=$('e_'+id);if(e)e.hidden=!on;var i=$(id);if(i)i.setAttribute('aria-invalid',on?'true':'false');return on}
f.addEventListener('submit',function(ev){ev.preventDefault();
 var n=$('ab-name').value.trim(),mob=$('ab-mobile').value.trim(),em=$('ab-email').value.trim(),ok=$('ab-consent').checked,bad=false;
 bad=er('ab-name',n.length<2)||bad;bad=er('ab-mobile',!(window.Lead?Lead.okMobile(mob):/^09\d{9}$/.test(mob)))||bad;bad=er('ab-email',!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(em))||bad;bad=er('ab-consent',!ok)||bad;
 if(bad){var x=f.querySelector('[aria-invalid=true]');if(x)x.focus();return}
 var b=$('ab-btn');b.disabled=true;var S='promos-unlock-optionA';
 var done=function(){try{localStorage.setItem(K,'1');localStorage.setItem('promos_contact',JSON.stringify({n:n,m:mob,e:em}))}catch(_){}reveal();
  if(!(window.Lead&&Lead.skipped())){var p={content_name:'promos-optionA',content_category:'promos',source:S};T('Lead',p);T('UnlockLowestDP',p,true)}
  $('ab-ok').scrollIntoView({block:'nearest'})};
 if(!window.Lead){done();return}
 var L=Lead.base(S);L.leadSource=S;L.campaign=S;L.name=n;L.mobile=mob;L.email=em;L.chosenUnit='All units (Option A unlock)';
 var q=new URLSearchParams(location.search);L.utm_medium=q.get('utm_medium')||'';L.utm_term=q.get('utm_term')||'';L.fbclid=q.get('fbclid')||'';L.lang=lang;
 L.timeline='Promos: unlocked Option A (lowest DP) for all units';
 L.usage=['Email: '+em,'source='+S,'Pre-qualified, subject to bank approval'].join(' | ');
 Lead.send(L).then(done,done)});
})();
