/* /lowest-down-payment/ campaign: language switch, standard amortization estimator, unlock lead form.
   Formula = existing calculator (assets/calc.js): monthly = (SRP - DP) x AOR / months; AOR 5y 1.55, 4y 1.48, 3y 1.32, 2y 1.24, 1y 1.22. */
(function(){
var $=function(i){return document.getElementById(i)},U=JSON.parse($('ld-data').textContent),RATE={5:1.55,4:1.48,3:1.32,2:1.24,1:1.22};
var lang='en';
function setLang(l){lang=l==='tl'?'tl':'en';document.documentElement.setAttribute('data-lang',lang);try{localStorage.setItem('site_lang',lang)}catch(_){}}
(function(){var q=(new URLSearchParams(location.search).get('lang')||'').toLowerCase(),s='';try{s=localStorage.getItem('site_lang')||''}catch(_){}setLang(q==='tl'||q==='en'?q:(s||'en'))})();
document.querySelectorAll('[data-setlang]').forEach(function(b){b.addEventListener('click',function(){setLang(b.dataset.setlang)})});
function peso(n){return '₱'+Math.round(n).toLocaleString('en-PH')}
function num(s){return +String(s||'').replace(/[^\d]/g,'')}
function T(ev,p,c){try{if(window.rpTrack){window.rpTrack(ev,p,c);return}if(typeof window.fbq==='function')window.fbq(c?'trackCustom':'track',ev,p)}catch(_){}}
function unit(){return U[+$('ld-unit').value]}
function fill(){var u=unit(),d=$('ld-dp'),c=d.value;d.innerHTML='';[u.lo,u.hi].filter(function(x,i,a){return a.indexOf(x)===i}).forEach(function(x){var o=document.createElement('option');o.value=x;o.textContent=peso(x);d.appendChild(o)});
 var o=document.createElement('option');o.value='other';o.textContent=lang==='tl'?'Iba pang DP':'Other DP';d.appendChild(o);calc()}
function dp(){var d=$('ld-dp').value;if(d==='other'){$('ld-dpo-w').hidden=false;return num($('ld-dpo').value)}$('ld-dpo-w').hidden=true;return +d}
function calc(){var u=unit(),y=+$('ld-term').value,x=dp(),r=$('ld-res');
 if(!(x>=0)||x>=u.srp){r.innerHTML='<span class="en">Enter a down payment below the SRP.</span><span class="tl">Maglagay ng DP na mas mababa sa SRP.</span>';return null}
 var m=(u.srp-x)*RATE[y]/(y*12);
 r.innerHTML='<span class="ld-mo">'+peso(m)+'<small>/mo</small></span><span class="ld-f">('+peso(u.srp)+' − '+peso(x)+') × '+RATE[y]+' ÷ '+(y*12)+'</span><span class="ld-f"><span class="en">Base variant: </span><span class="tl">Base variant: </span>'+u.base+'</span>';return m}
['ld-unit'].forEach(function(i){$(i).addEventListener('change',function(){fill();T('UnlockStep_Unit',{content_name:unit().n},true)})});
['ld-dp','ld-term'].forEach(function(i){$(i).addEventListener('change',calc)});$('ld-dpo').addEventListener('input',calc);
document.querySelectorAll('[data-pick]').forEach(function(b){b.addEventListener('click',function(){$('ld-unit').value=b.dataset.pick;fill();$('unlock').scrollIntoView({behavior:'smooth',block:'start'})})});
fill();
var f=$('ld-form');if(window.AS)AS.init(f);
function er(id,on){var e=$('e_'+id);if(e)e.hidden=!on;var i=$(id);if(i)i.setAttribute('aria-invalid',on?'true':'false');return on}
f.addEventListener('submit',function(ev){ev.preventDefault();
 var n=$('ld-name').value.trim(),mob=$('ld-mobile').value.trim(),em=$('ld-email').value.trim(),ok=$('ld-consent').checked,bad=false;
 bad=er('ld-name',n.length<2)||bad;bad=er('ld-mobile',!(window.Lead?Lead.okMobile(mob):/^09\d{9}$/.test(mob)))||bad;bad=er('ld-email',!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(em))||bad;bad=er('ld-consent',!ok)||bad;
 if(bad){var x=f.querySelector('[aria-invalid=true]');if(x)x.focus();return}
 var u=unit(),y=+$('ld-term').value,x=dp(),m=calc(),b=$('ld-btn');b.disabled=true;
 var done=function(){var fn=n.split(' ')[0];$('ld-ok').innerHTML='<p><b><span class="en">Unlocked, '+fn+'!</span><span class="tl">Na-unlock na, '+fn+'!</span></b></p><p><span class="en">Lowest DP for the '+u.n+': </span><span class="tl">Lowest DP ng '+u.n+': </span><b>'+peso(u.lo)+' – '+peso(u.hi)+'</b></p>'+(m?'<p><span class="en">Your standard estimate: </span><span class="tl">Standard estimate mo: </span><b>'+peso(m)+'/mo</b> ('+peso(x)+' DP, '+y+(y>1?' yrs':' yr')+')</p>':'')+'<p><span class="en">Richard will contact you with the exact all-in computation for the '+u.n+'.</span><span class="tl">Kokontakin ka ni Richard para sa eksaktong all-in computation ng '+u.n+'.</span></p><p class="muted">Pre-qualified only, subject to bank approval.</p>';
  $('ld-ok').hidden=false;f.hidden=true;
  if(!(window.Lead&&Lead.skipped())){var p={content_name:u.n,content_category:'lowest-dp-campaign',source:'lowest-dp-campaign'};
   try{if(typeof window.fbq==='function')window.fbq('track','Lead',p)}catch(_){}try{if(typeof window.fbq==='function')window.fbq('trackCustom','UnlockLowestDP',p)}catch(_){}
   try{if(typeof window.gtag==='function'){window.gtag('event','generate_lead',{unit:u.n,source:'lowest-dp-campaign'});window.gtag('event','UnlockLowestDP',{unit:u.n})}}catch(_){}}
  $('ld-ok').scrollIntoView({block:'nearest'})};
 if(!window.Lead){done();return}
 var L=Lead.base('lowest-dp-campaign');L.leadSource='lowest-dp-campaign';L.campaign='lowest-dp-campaign';L.name=n;L.mobile=mob;L.email=em;L.chosenUnit=u.n;L.unitParam=u.id;L.monthly=m?Math.round(m):'';
 var q=new URLSearchParams(location.search);L.utm_medium=q.get('utm_medium')||'';L.utm_term=q.get('utm_term')||'';L.fbclid=q.get('fbclid')||'';L.lang=lang;
 L.timeline='LowestDP: '+u.n+' range '+u.lo+'-'+u.hi+'; chosen DP '+x+', '+y+' yrs, ~'+(m?Math.round(m):'')+'/mo (base SRP '+u.srp+', AOR '+RATE[y]+')';
 L.usage=['Email: '+em,'source=lowest-dp-campaign','Pre-qualified only, subject to bank approval'].join(' | ');
 Lead.send(L).then(done,done)});
})();
