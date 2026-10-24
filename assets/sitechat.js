/* Site-wide loader for the own live chat bubble. The on/off flag is window.SITECHAT_ON, written into every page by _src/build.py (data.py SITECHAT).
   Works on pages without /assets/lead.js by defining the minimal Lead API chat.js needs (does not touch other globals). */
(function(){if(window.SITECHAT_ON!==true)return;
function go(){if(window.__ownChatLoaded)return;window.__ownChatLoaded=1;
 if(!window.Lead)window.Lead={url:'https://script.google.com/macros/s/AKfycbzP4moZ9QL3YB_liQsoqM80o9IfTBa-GMapQg1uLJF1xAOPLyvJ6PVhHb-nQ7A__hWsTA/exec',CHAT:true,
  okMobile:function(m){m=String(m||'').replace(/[\s()-]/g,'');return /^(09\d{9}|\+639\d{9}|\+\d{8,15})$/.test(m)}};
 var s=document.createElement('script');s.src='/assets/chat.js?v='+(window.SITECHAT_V||'1');s.defer=true;document.head.appendChild(s)}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',go);else go()})();
