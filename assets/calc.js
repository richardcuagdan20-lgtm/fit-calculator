/* Monthly estimate calculator: Choose a Car > Down payment > Years > Estimate (+ lead capture at the end).
   Hidden formula: monthly = (SRP - DP) x add-on factor / term months. Factors are multipliers on the financed amount
   (check: L300 Dual AC, SRP 1,039,000, DP 123,000, 5 yrs -> 916,000 x 1.55 / 60 = 23,663). Data: #calc-data (built from _src/data.py). */
(function(){
var RATE={5:1.55,4:1.48,3:1.32,2:1.24,1:1.22},PCT=[10,15,20,30];
function $(s,r){return (r||document).querySelector(s)}
function peso(n){return '\u20b1'+Math.round(n).toLocaleString('en-PH')}
function esc(t){return String(t).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
function T(ev,p,c){try{if(window.rpTrack)window.rpTrack(ev,p,c)}catch(_){}}
function mo(srp,dp,y){return Math.max(0,srp-dp)*RATE[y]/(y*12)}
function k(n){return n%1000===0?'\u20b1'+(n/1000)+'K':peso(n)}
function init(root){
 var D=JSON.parse($('#calc-data').textContent),src=root.getAttribute('data-src')||'calc',S={m:null,v:null,dp:null,y:5},started=false;
 root.innerHTML='<div class="cc"><ol class="cc-steps" aria-label="Progress"><li data-s="1" class="on">Car</li><li data-s="2">DP</li><li data-s="3">Years</li><li data-s="4">Estimate</li></ol><div class="cc-body" aria-live="polite"></div></div>';
 var B=$('.cc-body',root);
 function bar(n){root.querySelectorAll('.cc-steps li').forEach(function(l){var i=+l.dataset.s;l.className=i<n?'done':i===n?'on':''})}
 function start(){if(!started){started=true;T('ViewContent',{content_name:'calculator',source:src})}}
 function top(){var r=root.getBoundingClientRect();if(r.top<0||r.top>innerHeight*.6)window.scrollTo({top:scrollY+r.top-80,behavior:'smooth'})}
 function back(n,l){return '<button type="button" class="cc-back" data-go="'+n+'">\u2190 '+l+'</button>'}
 function step1(){bar(1);
  B.innerHTML='<h3 class="cc-h">Choose a car</h3><div class="cc-chips">'+D.map(function(m,i){return '<button type="button" class="cc-chip'+(S.m===i?' on':'')+'" data-m="'+i+'">'+esc(m.name)+'</button>'}).join('')+'</div><div class="cc-var"></div>';
  if(S.m!==null)vars();}
 function vars(){var m=D[S.m],w=$('.cc-var',B);
  w.innerHTML='<p class="cc-l">Variant</p><div class="cc-list">'+m.v.map(function(v,i){return '<button type="button" class="cc-row'+(S.v===i?' on':'')+'" data-v="'+i+'"><span>'+esc(v.n)+'</span><b>'+peso(v.srp)+'</b></button>'}).join('')+'</div>';}
 function step2(){bar(2);var v=D[S.m].v[S.v],o=[],seen={};
  (v.p||[]).forEach(function(p){if(p.dp>0&&!seen[p.dp]){seen[p.dp]=1;o.push({dp:p.dp,l:k(p.dp),t:'Promo DP'})}});
  PCT.forEach(function(p){var d=Math.ceil(v.srp*p/100/1000)*1000;if(!seen[d]){seen[d]=1;o.push({dp:d,l:k(d),t:p+'% of SRP'})}});
  o.sort(function(a,b){return a.dp-b.dp});
  B.innerHTML='<h3 class="cc-h">Down payment</h3><p class="cc-sub">'+esc(v.n)+' \u00b7 SRP '+peso(v.srp)+'</p><div class="cc-chips">'+o.map(function(x){return '<button type="button" class="cc-chip cc-dp'+(S.dp===x.dp?' on':'')+'" data-dp="'+x.dp+'">'+x.l+'<small>'+x.t+'</small></button>'}).join('')+'</div>'+
  '<div class="cc-cust"><label for="cc-dpi">Or type your down payment</label><div class="cc-in"><span>\u20b1</span><input id="cc-dpi" inputmode="numeric" placeholder="e.g. 150000" value="'+(S.dp!==null&&!o.some(function(x){return x.dp===S.dp})?S.dp:'')+'"><button type="button" class="btn sm" data-cust>Use</button></div><p class="cc-er" hidden>Enter an amount below the SRP.</p></div>'+back(1,'Change car');}
 function step3(){bar(3);var v=D[S.m].v[S.v];
  B.innerHTML='<h3 class="cc-h">How many years?</h3><p class="cc-sub">'+esc(v.n)+' \u00b7 DP '+peso(S.dp)+'</p><div class="cc-chips">'+[5,4,3,2,1].map(function(y){return '<button type="button" class="cc-chip'+(S.y===y?' on':'')+'" data-y="'+y+'">'+y+' year'+(y>1?'s':'')+'<small>'+(y*12)+' months</small></button>'}).join('')+'</div>'+back(2,'Change down payment');}
 function step4(){bar(4);var m=D[S.m],v=m.v[S.v],y=S.y,M=mo(v.srp,S.dp,y),n=y*12,h='';
  var promos=(v.p||[]).filter(function(p){return p.dp>0}),same=promos.filter(function(p){return p.dp===S.dp})[0];
  h+='<h3 class="cc-h">Your estimate</h3><dl class="cc-res"><div><dt>Unit</dt><dd>'+esc(v.n)+'</dd></div><div><dt>SRP</dt><dd>'+peso(v.srp)+'</dd></div><div><dt>Down payment</dt><dd>'+peso(S.dp)+'</dd></div><div><dt>Term</dt><dd>'+y+' year'+(y>1?'s':'')+' ('+n+' months)</dd></div></dl>';
  h+='<div class="cc-big"><span>Estimated monthly</span><b>'+peso(M)+'</b><small>Total of monthly payments: '+peso(M*n)+'</small></div>';
  // savings vs lowest-DP option (same term), shown only when 5% or more
  var lo=Math.min.apply(null,[Math.ceil(v.srp*PCT[0]/100/1000)*1000].concat(promos.map(function(p){return p.dp})));
  if(S.dp>lo){var ml=mo(v.srp,lo,y),sv=(ml-M)/ml*100;if(sv>=5)h+='<p class="cc-save">About <b>'+Math.round(sv)+'% lower</b> monthly than the lowest down payment option ('+peso(lo)+' DP, ~'+peso(ml)+'/mo).</p>'}
  if(same&&y===5){var d=M-same.mo;
   h+='<div class="cc-promo"><p class="cc-pt">Official promo for this down payment</p><p><b>'+peso(same.mo)+'/mo</b> for 60 months with '+peso(same.dp)+' DP, all-in'+(v.fuel?' plus '+Number(v.fuel).toLocaleString('en-US')+' fuel points':'')+'.</p><p class="cc-rec">'+(d>0?'Recommendation: take the official promo. It is about '+peso(d)+' lower per month than this estimate and already includes the all-in package.':'Recommendation: the official promo is the simpler choice, since it is all-in with freebies. Ask Richard to compare both for you.')+'</p></div>';}
  else if(promos.length){var best=promos.slice().sort(function(a,b){return Math.abs(a.dp-S.dp)-Math.abs(b.dp-S.dp)})[0],better=best.mo<M;
   h+='<div class="cc-promo"><p class="cc-pt">Official promo for this unit</p><p><b>'+peso(best.mo)+'/mo</b> for 60 months with '+peso(best.dp)+' DP, all-in'+(v.fuel?' plus '+Number(v.fuel).toLocaleString('en-US')+' fuel points':'')+'.</p><p class="cc-rec">'+(better?'Recommendation: the official promo gives a lower monthly than this estimate. If the promo down payment works for you, choose the promo.':'Recommendation: your plan has a lower monthly because of the bigger down payment or different term. Compare it with the all-in promo before deciding.')+'</p><p><a href="/promos/#'+m.slug+'">See all '+esc(m.name)+' promos</a></p></div>';}
  h+='<p class="cc-cav">Estimate only, subject to bank evaluation. Actual rates, monthly and approval depend on the bank, your documents and current promos.</p>';
  h+='<div class="cc-act"><button type="button" class="cc-back" data-go="2">Change down payment</button><button type="button" class="cc-back" data-go="3">Change years</button><button type="button" class="cc-back" data-go="1">Change car</button></div>';
  h+='<form class="cc-lead" novalidate><h4>Get this estimate and the latest promo from Richard</h4><div class="cc-f"><label for="cc-n">Full name</label><input id="cc-n" autocomplete="name"></div><div class="cc-f"><label for="cc-mo">Mobile number</label><input id="cc-mo" type="tel" inputmode="tel" autocomplete="tel" placeholder="09XX XXX XXXX"></div><div class="cc-f"><label for="cc-em">or Email</label><input id="cc-em" type="email" autocomplete="email"></div>'+
   '<label class="chk"><input type="checkbox" id="cc-c"> <span>I agree to the processing of my personal information under the Data Privacy Act of 2012 (RA 10173), as described in the <a href="/privacy/">Privacy Policy</a>, so Richard Cuagdan can contact me about this inquiry.</span></label><p class="cc-er" hidden></p><button class="btn" type="submit">Send me this estimate</button></form>'+
   '<div class="cc-next"><p><b>Next step:</b> see how a bank is likely to view your application.</p><p class="row"><a class="btn" href="/loan-assessment/?unit='+encodeURIComponent(v.id)+'">Take the Loan Application Assessment</a></p></div>';
  B.innerHTML=h;T('CalcResult',{content_name:v.n,source:src,term_years:y},true);}
 function lead(f){var v=D[S.m].v[S.v],n=$('#cc-n',f).value.trim(),mob=$('#cc-mo',f).value.replace(/[\s()-]/g,''),em=$('#cc-em',f).value.trim(),c=$('#cc-c',f).checked,er=$('.cc-er',f),msg='';
  if(n.length<2)msg='Please enter your name.';else if(!mob&&!em)msg='Please enter your mobile number or email.';else if(mob&&!(window.Lead?Lead.okMobile(mob):/^(09\d{9}|\+\d{8,15})$/.test(mob)))msg='Please check your mobile number.';else if(em&&!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(em))msg='Please check your email.';else if(!c)msg='Please tick the consent box.';
  er.textContent=msg;er.hidden=!msg;if(msg)return;
  var b=$('button[type=submit]',f);b.disabled=true;b.textContent='Sending...';var M=Math.round(mo(v.srp,S.dp,S.y));
  var done=function(){f.innerHTML='<p class="cc-ok"><b>Thank you, '+esc(n.split(' ')[0])+'!</b> Richard will send you this estimate and the current promo for the '+esc(v.n)+'. For a clearer picture of your chances, take the Loan Application Assessment below.</p>';T('Lead',{content_name:v.n,source:'calculator-'+src})};
  if(!window.Lead){done();return}
  var L=Lead.base('calculator');L.name=n;L.mobile=mob;L.chosenUnit=v.n;L.unitParam=v.id;L.monthly=M;L.seg='';
  L.timeline='Calc: DP '+S.dp+', '+S.y+' yrs, ~'+M+'/mo (SRP '+v.srp+')';L.usage=[em?'Email: '+em:'','Calculator estimate, subject to bank evaluation'].filter(Boolean).join(' | ');
  Lead.send(L).then(done);}
 root.addEventListener('click',function(e){var t=e.target.closest('button');if(!t||!root.contains(t))return;start();
  if(t.dataset.m!==undefined){S.m=+t.dataset.m;S.v=null;S.dp=null;root.querySelectorAll('[data-m]').forEach(function(b){b.classList.toggle('on',b===t)});vars();var l=$('.cc-var',B);if(l)l.scrollIntoView({block:'nearest',behavior:'smooth'});return}
  if(t.dataset.v!==undefined){S.v=+t.dataset.v;S.dp=null;T('CalcStep_Car',{content_name:D[S.m].v[S.v].n,source:src},true);step2();top();return}
  if(t.dataset.dp!==undefined){S.dp=+t.dataset.dp;T('CalcStep_DP',{content_name:D[S.m].v[S.v].n,source:src},true);step3();top();return}
  if(t.hasAttribute('data-cust')){var x=+String($('#cc-dpi',B).value).replace(/[^\d]/g,''),v=D[S.m].v[S.v],er=$('.cc-cust .cc-er',B);if(!(x>=0)||x>=v.srp||$('#cc-dpi',B).value===''){er.hidden=false;return}S.dp=x;T('CalcStep_DP',{content_name:v.n,source:src,custom:1},true);step3();top();return}
  if(t.dataset.y!==undefined){S.y=+t.dataset.y;T('CalcStep_Years',{content_name:D[S.m].v[S.v].n,source:src,term_years:S.y},true);step4();top();return}
  if(t.dataset.go){var g=+t.dataset.go;(g===1?step1:g===2?step2:step3)();top();return}});
 root.addEventListener('submit',function(e){e.preventDefault();lead(e.target)});
 root.addEventListener('keydown',function(e){if(e.key==='Enter'&&e.target.id==='cc-dpi'){e.preventDefault();$('[data-cust]',B).click()}});
 var q=new URLSearchParams(location.search).get('unit');
 if(q){D.forEach(function(m,i){m.v.forEach(function(v,j){if(v.id===q||(m.slug===q&&S.m===null)){S.m=i;if(v.id===q)S.v=j}})})}
 if(S.m!==null&&S.v!==null)step2();else step1();
}
function go(){document.querySelectorAll('[data-rpcalc]').forEach(init)}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',go);else go();
})();
