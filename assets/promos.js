/* /promos/ Option A unlock: one lead form reveals Option A (lowest DP + monthly) on every unit; persisted in localStorage. */
(function(){
var $=function(i){return document.getElementById(i)},K='promos_optA_unlocked',H=document.documentElement,A=[];
try{A=JSON.parse(atob($('ab-a').textContent.trim()))}catch(_){}
var lang='en';
function setLang(l){lang=l==='tl'?'tl':'en';H.setAttribute('data-lang',lang);try{localStorage.setItem('site_lang',lang)}catch(_){}}
(function(){var q=(new URLSearchParams(location.search).get('lang')||'').toLowerCase(),s='';try{s=localStorage.getItem('site_lang')||''}catch(_){}setLang(q==='tl'||q==='en'?q:(s||'en'))})();
document.querySelectorAll('[data-setlang]').forEach(function(b){b.addEventListener('click',function(){setLang(b.dataset.setlang)})});
function peso(n){return '₱'+Math.round(n).toLocaleString('en-PH')}
function reveal(){document.querySelectorAll('[data-a]').forEach(function(el){var a=A[+el.getAttribute('data-a')];if(!a)return;var x=el.querySelectorAll('.ab-x');if(x[0])x[0].textContent=peso(a[0]);if(x[1])x[1].textContent=peso(a[1])});H.classList.add('ab-open')}
var open=false;try{open=localStorage.getItem(K)==='1'}catch(_){}
if(open)reveal();
function T(ev,p,c){try{if(window.rpTrack){window.rpTrack(ev,p,c);return}if(typeof window.fbq==='function')window.fbq(c?'trackCustom':'track',ev,p)}catch(_){}}
document.querySelectorAll('[data-unlock]').forEach(function(b){b.addEventListener('click',function(){$('unlock').scrollIntoView({behavior:'smooth',block:'start'});setTimeout(function(){try{$('ab-name').focus({preventScroll:true})}catch(_){}},400)})});
var f=$('ab-form');if(!f)return;if(window.AS)AS.init(f);
function er(id,on){var e=$('e_'+id);if(e)e.hidden=!on;var i=$(id);if(i)i.setAttribute('aria-invalid',on?'true':'false');return on}
f.addEventListener('submit',function(ev){ev.preventDefault();
 var n=$('ab-name').value.trim(),mob=$('ab-mobile').value.trim(),em=$('ab-email').value.trim(),ok=$('ab-consent').checked,bad=false;
 bad=er('ab-name',n.length<2)||bad;bad=er('ab-mobile',!(window.Lead?Lead.okMobile(mob):/^09\d{9}$/.test(mob)))||bad;bad=er('ab-email',!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(em))||bad;bad=er('ab-consent',!ok)||bad;
 if(bad){var x=f.querySelector('[aria-invalid=true]');if(x)x.focus();return}
 var b=$('ab-btn');b.disabled=true;var S='promos-unlock-optionA';
 var done=function(){try{localStorage.setItem(K,'1')}catch(_){}reveal();
  if(!(window.Lead&&Lead.skipped())){var p={content_name:'promos-optionA',content_category:'promos',source:S};T('Lead',p);T('UnlockLowestDP',p,true)}
  $('ab-ok').scrollIntoView({block:'nearest'})};
 if(!window.Lead){done();return}
 var L=Lead.base(S);L.leadSource=S;L.campaign=S;L.name=n;L.mobile=mob;L.email=em;L.chosenUnit='All units (Option A unlock)';
 var q=new URLSearchParams(location.search);L.utm_medium=q.get('utm_medium')||'';L.utm_term=q.get('utm_term')||'';L.fbclid=q.get('fbclid')||'';L.lang=lang;
 L.timeline='Promos: unlocked Option A (lowest DP) for all units';
 L.usage=['Email: '+em,'source='+S,'Pre-qualified, subject to bank approval'].join(' | ');
 Lead.send(L).then(done,done)});
})();
