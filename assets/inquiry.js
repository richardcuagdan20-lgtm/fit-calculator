/* "Inquire this promo" (2026-10-30): inline inquiry form per variant on /promos/ and car pages.
   Lead source promos-inquiry via lead.js (same webhook + fields as the unlock; message/figures go in usage/dpPreference).
   Contact prefilled from the Option A unlock (localStorage promos_contact); otherwise name/mobile/email + consent are asked.
   Inquiry does NOT unlock Option A. */
(function(){
var H=document.documentElement,CK='promos_contact',S='promos-inquiry',A=[];
try{A=JSON.parse(atob(document.getElementById('ab-a').textContent.trim()))}catch(_){}
function tl(){return H.getAttribute('data-lang')==='tl'}
function L2(en,t){return '<span class="en">'+en+'</span><span class="tl">'+t+'</span>'}
function peso(n){return '₱'+Math.round(n).toLocaleString('en-PH')}
function who(){try{var c=JSON.parse(localStorage.getItem(CK)||'null');if(c&&c.n&&c.m&&c.e)return c}catch(_){}return null}
function esc(x){return String(x).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function T(ev,p,c){try{if(window.rpTrack){window.rpTrack(ev,p,c);return}if(typeof window.fbq==='function')window.fbq(c?'trackCustom':'track',ev,p)}catch(_){}}
var N=0;
function build(box,panel){var id='iq'+(++N),u=box.getAttribute('data-unit'),c=who();
 var msgEn='I would like to inquire about the '+u+' promo options (Option A and Option B).',msgTl='Gusto ko pong mag-inquire tungkol sa promo options ng '+u+' (Option A at Option B).';
 panel.innerHTML='<form class="iq-f" novalidate>'+
 '<label for="'+id+'-m">'+L2('Your message','Ang mensahe mo')+'</label><textarea id="'+id+'-m" rows="4" maxlength="1000">'+esc(tl()?msgTl:msgEn)+'</textarea>'+
 (c?'<p class="iq-as">'+L2('Sending as','Ipapadala bilang')+' <b>'+esc(c.n)+'</b> · '+esc(c.m)+' · '+esc(c.e)+' <button type="button" class="iq-edit">'+L2('Edit','Palitan')+'</button></p>':'')+
 '<div class="iq-who"'+(c?' hidden':'')+'>'+
  '<div><label for="'+id+'-n">'+L2('Full name','Buong pangalan')+'</label><input type="text" id="'+id+'-n" autocomplete="name" value="'+(c?esc(c.n):'')+'"><p class="ferr" hidden>'+L2('Please enter your name.','Pakilagay ang pangalan mo.')+'</p></div>'+
  '<div><label for="'+id+'-p">Mobile number</label><input type="tel" id="'+id+'-p" inputmode="tel" autocomplete="tel" placeholder="09XX XXX XXXX" value="'+(c?esc(c.m):'')+'"><p class="ferr" hidden>'+L2('Enter a valid mobile number (09XXXXXXXXX).','Maglagay ng tamang mobile number (09XXXXXXXXX).')+'</p></div>'+
  '<div><label for="'+id+'-e">Email</label><input type="email" id="'+id+'-e" autocomplete="email" value="'+(c?esc(c.e):'')+'"><p class="ferr" hidden>'+L2('Enter a valid email.','Maglagay ng tamang email.')+'</p></div></div>'+
 '<label class="chk"'+(c?' hidden':'')+'><input type="checkbox" id="'+id+'-c"'+(c?' checked':'')+'><span>'+L2('I agree to be contacted by Richard Cuagdan of Mitsubishi San Juan Motors about this inquiry, and to the <a href="/privacy/">privacy policy</a>.','Pumapayag akong i-contact ni Richard Cuagdan ng Mitsubishi San Juan Motors tungkol sa inquiry na ito, at sa <a href="/privacy/">privacy policy</a>.')+'</span></label>'+
 '<p class="ferr iq-ce" hidden>'+L2('Please tick the consent box.','Paki-check ang consent box.')+'</p>'+
 '<button type="submit" class="btn iq-send">'+L2('Send inquiry','I-send ang inquiry')+'</button>'+
 '<p class="iq-fine">'+L2('Pre-qualified, subject to bank approval. Richard replies by text, call or email.','Pre-qualified, subject to bank approval. Sasagot si Richard sa text, tawag o email.')+'</p></form>'+
 '<p class="iq-ok" role="status" hidden>'+L2('Thanks! Richard will reply to you soon.','Salamat! Sasagot si Richard sa iyo sa lalong madaling panahon.')+'</p>';
 var f=panel.querySelector('form');if(window.AS)AS.init(f);
 var ed=f.querySelector('.iq-edit');if(ed)ed.addEventListener('click',function(){f.querySelector('.iq-who').hidden=false;f.querySelector('.chk').hidden=false;f.querySelector('.iq-as').hidden=true;document.getElementById(id+'-n').focus()});
 function bad(el,on){var p=el.parentNode.querySelector('.ferr');if(p)p.hidden=!on;el.setAttribute('aria-invalid',on?'true':'false');return on}
 f.addEventListener('submit',function(ev){ev.preventDefault();
  var n=document.getElementById(id+'-n'),m=document.getElementById(id+'-p'),e=document.getElementById(id+'-e'),k=document.getElementById(id+'-c'),t=document.getElementById(id+'-m'),x=false;
  x=bad(n,n.value.trim().length<2)||x;x=bad(m,!(window.Lead?Lead.okMobile(m.value.trim()):/^09\d{9}$/.test(m.value.trim())))||x;x=bad(e,!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(e.value.trim()))||x;
  var ce=f.querySelector('.iq-ce');ce.hidden=k.checked;x=!k.checked||x;
  if(x){f.querySelector('.iq-who').hidden=false;f.querySelector('.chk').hidden=false;var a=f.querySelector('[aria-invalid=true]')||k;a.focus();return}
  var b=f.querySelector('.iq-send');b.disabled=true;
  var ai=+box.getAttribute('data-ai'),a=A[ai],open=H.classList.contains('ab-open');
  var fa=a?(open?'Option A: '+(a[0]===0?'Zero DP Promo':peso(a[0])+' DP')+', '+peso(a[1])+'/mo':'Option A: locked (not unlocked)'):'Option A: n/a';
  var fig=fa+' | Option B: '+box.getAttribute('data-b');
  var ok=function(){try{localStorage.setItem(CK,JSON.stringify({n:n.value.trim(),m:m.value.trim(),e:e.value.trim()}))}catch(_){}
   f.hidden=true;var o=panel.querySelector('.iq-ok');o.hidden=false;o.setAttribute('tabindex','-1');o.focus();
   if(!(window.Lead&&Lead.skipped())){var p={content_name:'promos-inquiry',content_category:'promos',source:S,unit:u};T('Lead',p);T('InquirePromo',p,true)}};
  if(!window.Lead){ok();return}
  var L=Lead.base(S);L.leadSource=S;L.campaign=S;L.name=n.value.trim();L.mobile=m.value.trim();L.email=e.value.trim();L.chosenUnit=u;L.unitParam=box.getAttribute('data-ref');
  L.dpPreference=fig;L.timeline='Promos: inquiry about '+u;L.lang=tl()?'tl':'en';
  var q=new URLSearchParams(location.search);L.fbclid=q.get('fbclid')||'';
  L.usage=['Email: '+L.email,'source='+S,'Message: '+t.value.trim().slice(0,1000),fig,'Pre-qualified, subject to bank approval'].join(' | ');
  Lead.send(L).then(ok,ok)})}
document.querySelectorAll('.iq').forEach(function(box){var b=box.querySelector('.ab-iq'),p=b&&document.getElementById(b.getAttribute('aria-controls'));if(!b||!p)return;
 b.addEventListener('click',function(){var o=b.getAttribute('aria-expanded')!=='true';if(o&&!p.firstChild)build(box,p);b.setAttribute('aria-expanded',o?'true':'false');p.hidden=!o;if(o){var t=p.querySelector('textarea');if(t)t.focus({preventScroll:true})}})});
})();
