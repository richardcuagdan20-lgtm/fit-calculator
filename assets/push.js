/* Web push soft-prompt (OneSignal v16). Inert unless window.PUSH_APP_ID is set. SDK loads only on opt-in or for existing subscribers. */
(function(){
var ID=window.PUSH_APP_ID;if(!ID||!("Notification" in window)||!("serviceWorker" in navigator))return;
var P=location.pathname,K="push_",D=14*864e5,ls=window.localStorage;
function g(k){try{return ls.getItem(K+k)}catch(e){return null}}function s(k,v){try{ls.setItem(K+k,v)}catch(e){}}
function ev(n,p){try{window.gtag&&gtag("event",n,Object.assign({page_path:P},p||{}))}catch(e){}}
var m=P.match(/^\/cars\/([^\/]+)/),interest=m?m[1]:(P.indexOf("/promos")==0?"promos":P.indexOf("/blog")==0||P.indexOf("/tips")==0?"blog":"general");
var sdk=0;function load(cb){window.OneSignalDeferred=window.OneSignalDeferred||[];OneSignalDeferred.push(cb);if(sdk)return;sdk=1;
 OneSignalDeferred.unshift(function(OS){return OS.init({appId:ID,serviceWorkerPath:"/OneSignalSDKWorker.js",serviceWorkerParam:{scope:"/"},notifyButton:{enable:false},promptOptions:{autoPrompt:false}})});
 var t=document.createElement("script");t.src="https://cdn.onesignal.com/sdks/web/v16/OneSignalSDK.page.js";t.defer=1;document.head.appendChild(t)}
function tag(OS){try{OS.User.addTags({interest:interest,source_page:P.slice(0,100)})}catch(e){}}
if(g("state")==="on"){if(Notification.permission==="granted")load(tag);return}
if(Notification.permission!=="default")return;
if(/^\/(card|apply|status)(\/|$)/.test(P))return;
var d=+g("dismiss")||0;if(d&&Date.now()-d<D)return;
var v=(+g("views")||0)+1;s("views",v);
var shown=0;function show(){if(shown)return;shown=1;
 var b=document.createElement("div");b.className="pushbar";b.setAttribute("role","dialog");b.setAttribute("aria-label","Promo notifications");
 b.innerHTML='<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#e60012" d="M12 22a2.5 2.5 0 0 0 2.45-2h-4.9A2.5 2.5 0 0 0 12 22zm7-6V11a7 7 0 0 0-5.5-6.84V3.5a1.5 1.5 0 0 0-3 0v.66A7 7 0 0 0 5 11v5l-2 2v1h18v-1l-2-2z"/></svg><p><b>Get new promo and price updates</b><span>From Richard Cuagdan, Mitsubishi Sales Executive. No spam, unsubscribe anytime.</span></p><div class="pb-a"><button type="button" class="pb-n">Not now</button><button type="button" class="pb-y">Notify me</button></div>';
 document.body.appendChild(b);requestAnimationFrame(function(){requestAnimationFrame(function(){b.classList.add("on")})});ev("push_prompt_shown",{interest:interest});
 function hide(){b.classList.remove("on");setTimeout(function(){b.remove()},400)}
 b.querySelector(".pb-n").onclick=function(){s("dismiss",Date.now());ev("push_dismiss",{interest:interest});hide()};
 b.querySelector(".pb-y").onclick=function(){hide();load(function(OS){return OS.Notifications.requestPermission().then(function(){if(OS.Notifications.permission){s("state","on");tag(OS);ev("push_optin",{interest:interest})}else{s("dismiss",Date.now());ev("push_dismiss",{interest:interest,reason:"native_block"})}})})}}
if(v>=2)setTimeout(show,3000);else setTimeout(show,20000);
})();
