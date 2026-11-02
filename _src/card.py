# Digital business card for NFC / QR: /card/ (standalone mobile page) + downloadable contact file.
# Built from build.py (exec). Not in the sitemap (noindex).
CARD_NAME="Richard Dennis Cuagdan"
CARD_CORP="Authorized Mitsubishi Sales Executive · SJDM Bulacan"
_U="?utm_source=nfc&utm_medium=card&utm_campaign=business-card"
_NAVC=[("/promos/","Promos","Option A and Option B for every unit","M4 7h16v3H4zm2 5h12v7H6z"),
 ("/cars/","Cars and prices","All models, variants and inclusions","M5 16l1.5-5h11L19 16M5 16v3h2v-1h10v1h2v-3M7.5 14h.01M16.5 14h.01"),
 ("/loan-assessment/","Pre-qualify in 2 minutes","Free AI Car Loan Assessment","M12 3l7 3v5c0 4-3 7-7 9-4-2-7-5-7-9V6z"),
 ("/apply/","Apply now","Send your details and documents online","M7 3h8l4 4v14H7zM15 3v4h4"),
 ("/status/","Track my application","Use your MP- reference number","M12 7v5l3 2M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18"),
 ("/test-drive/","Book a test drive","Pick a unit and a schedule","M3 13l2-5h14l2 5M5 13v5h3v-2h8v2h3v-5M7 13h.01M17 13h.01"),
 ("/budgetcalculator/","Compute my monthly","Estimate by DP and term","M6 3h12v18H6zM9 7h6M9 11h2M13 11h2M9 15h2M13 15h2"),
 ("/tips/","Guides and tips","Requirements, OFW, FAQ and more","M5 4h11a3 3 0 0 1 3 3v13H8a3 3 0 0 1-3-3zM8 8h7M8 12h7"),
 ("/about/","About Richard","Who you will be dealing with","M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM4 21c1-4 4-6 8-6s7 2 8 6"),
 ("/contact/","Contact and showroom","Call, text or message","M5 5h14v10H9l-4 4z")]
def _ic(d): return f'<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="{d}"/></svg>'
_IC={"call":"M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2",
 "sms":"M4 5h16v11H8l-4 4z","msgr":"M12 3C7 3 3 6.8 3 11.5c0 2.6 1.3 4.9 3.3 6.4V21l3-1.7c.9.2 1.8.4 2.7.4 5 0 9-3.800 9-8.200S17 3 12 3zM7 13.500l3.500-3.700 2 2 3.500-2.800L12.500 14l-2-2z",
 "web":"M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18","save":"M12 4v11m0 0l-4-4m4 4l4-4M5 20h14","fb":"M14 8h3V4h-3a4 4 0 0 0-4 4v2H7v4h3v7h4v-7h3l1-4h-4V8z"}
def _card_html():
    tiles="".join(f'<a class="nt" href="{p}{_U}"><span class="ni">{_ic(i)}</span><span class="nx"><b>{e(t)}</b><small>{e(s)}</small></span><span class="ch" aria-hidden="true">›</span></a>' for p,t,s,i in _NAVC)
    acts=[("call",f"tel:{TEL}","Call",TELD,"pri"),("sms",f"sms:{TEL}","Text","SMS",""),("msgr",MSG,"Messenger","Message me",""),("web",D+"/"+_U,"Website","mitsubishipromos.online",""),("fb",FB,"Facebook","My page",""),("save","/card/richard-cuagdan.vcf","Save contact","Add to phone","")]
    ab="".join(f'<a class="ab {c}" href="{h}"{" rel=\"noopener\" target=\"_blank\"" if h.startswith("http") and "m.me" in h or h==FB else ""} data-ev="{k}"><span class="ai">{_ic(_IC[k])}</span><span class="al"><b>{l}</b><small>{s}</small></span></a>' for k,h,l,s,c in acts)
    ld={"@context":"https://schema.org","@type":"ProfilePage","mainEntity":{"@id":D+"/#richard"}}
    return f'''<!doctype html>
<html lang="en-PH"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{GA}
{CL}<title>Richard Cuagdan | Mitsubishi Car Sales Executive, SJDM Bulacan</title>
<meta name="description" content="Digital business card of Richard Dennis Cuagdan, authorized Mitsubishi Sales Executive in San Jose del Monte, Bulacan. Call, text, Messenger, promos, loan pre-qualification and test drive.">
<meta name="robots" content="noindex,follow">
<link rel="canonical" href="{D}/card/">
<meta property="og:type" content="profile"><meta property="og:title" content="Richard Cuagdan | Mitsubishi Car Sales Executive">
<meta property="og:description" content="Call, text or message me. See promos, get pre-qualified, book a test drive.">
<meta property="og:url" content="{D}/card/"><meta property="og:image" content="{D}/assets/card/card-og.jpg"><meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0b0b0c">
<link rel="icon" href="/favicon.ico?v=2" sizes="48x48"><link rel="apple-touch-icon" href="/apple-touch-icon.png?v=2">
<style>
*{{box-sizing:border-box}}body{{margin:0;font-family:system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;background:#f4f4f5;color:#26262b;line-height:1.5;-webkit-font-smoothing:antialiased}}
a{{text-decoration:none;color:inherit}}.wrap{{max-width:520px;margin:0 auto;padding:0 0 calc(24px + env(safe-area-inset-bottom))}}
.hero{{background:#0b0b0c;color:#fff;padding:calc(28px + env(safe-area-inset-top)) 20px 30px;text-align:center;border-radius:0 0 28px 28px;position:relative;overflow:hidden}}
.hero:before{{content:"";position:absolute;left:50%;top:-120px;width:340px;height:340px;margin-left:-170px;border-radius:50%;background:radial-gradient(#e6001833,transparent 70%)}}
.logo{{position:relative;display:flex;align-items:center;justify-content:center;gap:8px;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:#bdbdc4;margin-bottom:18px}}
.ph{{position:relative;width:132px;height:132px;margin:0 auto 14px;border-radius:50%;background:#fff;border:3px solid #e60012;overflow:hidden}}.ph img{{width:100%;height:100%;object-fit:cover;object-position:50% 30%}}
h1{{position:relative;margin:0;font-size:26px;letter-spacing:-.01em}}.role{{position:relative;margin:4px 0 0;color:#fff;font-weight:600}}.corp{{position:relative;margin:2px 0 0;color:#bdbdc4;font-size:14px}}.area{{position:relative;margin:10px 0 0;color:#bdbdc4;font-size:13.5px}}
.acts{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;padding:16px 16px 0;margin-top:-22px;position:relative}}
.ab{{min-width:0;display:flex;align-items:center;gap:10px;background:#fff;border-radius:16px;padding:12px;box-shadow:0 4px 14px #0000001a;min-height:60px}}
.ab.pri,.ab:last-child{{grid-column:1/-1;background:#e60012;color:#fff;font-size:17px}}.ai{{flex:none;width:38px;height:38px;border-radius:12px;background:#f4f4f5;color:#b8000e;display:grid;place-items:center}}.pri .ai{{background:#ffffff26;color:#fff}}
.al{{display:flex;flex-direction:column;min-width:0}}.al b{{font-size:15px;line-height:1.2}}.al small{{font-size:12.5px;opacity:.7;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}
h2{{font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:#6b6b73;margin:26px 20px 10px}}
.nav{{display:grid;gap:8px;padding:0 16px}}.nt{{display:flex;align-items:center;gap:12px;background:#fff;border:1px solid #e7e7ea;border-radius:14px;padding:12px 14px;min-height:60px}}
.ni{{flex:none;width:40px;height:40px;border-radius:12px;background:#fdecee;color:#b8000e;display:grid;place-items:center}}.nx{{display:flex;flex-direction:column;flex:1;min-width:0}}.nx b{{font-size:15.5px;color:#0b0b0c}}.nx small{{font-size:13px;color:#6b6b73}}.ch{{font-size:24px;color:#b8000e}}
.qrb{{display:flex;align-items:center;gap:10px;width:calc(100% - 32px);margin:10px 16px 0;background:#0b0b0c;color:#fff;border:0;border-radius:16px;padding:12px;min-height:60px;font:inherit;text-align:left;cursor:pointer}}.qrb .ai{{background:#ffffff1f;color:#fff}}
.qrm{{position:fixed;inset:0;background:#000000cc;display:grid;place-items:center;padding:20px;z-index:50}}.qrm[hidden]{{display:none}}.qrc{{background:#fff;border-radius:24px;padding:22px;text-align:center;max-width:360px;width:100%}}.qrc img{{width:100%;max-width:300px;height:auto;margin:8px auto}}.qrc p{{margin:0;color:#0b0b0c}}.qs{{font-size:13px;color:#6b6b73!important}}.qx{{margin-top:14px;background:#e60012;color:#fff;border:0;border-radius:999px;padding:12px 28px;font:inherit;font-weight:700;cursor:pointer}}
.note{{margin:22px 20px 0;font-size:12px;color:#6b6b73;line-height:1.55}}.note a{{color:#b8000e}}
a:focus-visible{{outline:3px solid #e60012;outline-offset:2px}}
@media(min-width:560px){{body{{padding:24px 0}}.wrap{{border-radius:28px;overflow:hidden;background:#f4f4f5;box-shadow:0 10px 40px #0000001f}}}}
</style>
<script type="application/ld+json">{json.dumps(ld)}</script>
</head><body><div class="wrap">
<header class="hero"><div class="logo"><svg viewBox="0 -15.465 224.9 224.9" width="22" height="22" aria-hidden="true"><path fill="#e60012" d="m112.45 0 38.42 65.13-38.42 65.12L74.03 65.6Zm0 130.25h74.96l37.49 63.72h-74.97zm0 0H37.48L0 193.97h74.97z"/></svg>Mitsubishi Motors</div>
<div class="ph"><img src="/assets/img/richard-300.webp" width="300" height="300" alt="{CARD_NAME}, Mitsubishi Car Sales Executive"></div>
<h1>{CARD_NAME}</h1><p class="role">Car Sales Executive</p><p class="corp">{CARD_CORP}</p><p class="area">Serving San Jose del Monte (SJDM), Bulacan and Quezon City</p></header>
<section class="acts" aria-label="Contact">{ab}</section>
<button class="qrb" id="qrb" type="button" aria-haspopup="dialog"><span class="ai">{_ic("M4 4h6v6H4zM14 4h6v6h-6zM4 14h6v6H4zM14 14h2v2h-2zM18 14h2v2h-2zM14 18h2v2h-2zM18 18h2v2h-2z")}</span><span class="al"><b>Show my QR code</b><small>Let a client scan this card from my phone</small></span></button>
<div class="qrm" id="qrm" role="dialog" aria-modal="true" aria-label="QR code" hidden><div class="qrc"><p><b>Scan to open my card</b></p><img src="/assets/card/card-qr.png" width="320" height="320" alt="QR code for Richard Cuagdan's digital business card"><p class="qs">{CARD_NAME}<br>mitsubishipromos.online/card</p><button type="button" id="qrx" class="qx">Close</button></div></div>
<h2>Explore my website</h2><nav class="nav" aria-label="Website sections">{tiles}</nav>
<p class="note">{CARD_NAME} is an authorized Mitsubishi sales executive in San Jose del Monte, Bulacan. This is his independent personal sales page and not the official website of Mitsubishi Motors Philippines Corporation. All monthly amounts are estimates, pre-qualified and subject to bank approval. <a href="/privacy/">Privacy</a></p>
</div>
<script>(function(){{var m=document.getElementById('qrm'),b=document.getElementById('qrb'),x=document.getElementById('qrx');function o(){{m.hidden=false;x.focus();if(window.gtag)gtag('event','card_qr_open')}}function c(){{m.hidden=true;b.focus()}}b.addEventListener('click',o);x.addEventListener('click',c);m.addEventListener('click',function(e){{if(e.target===m)c()}});document.addEventListener('keydown',function(e){{if(e.key==='Escape'&&!m.hidden)c()}})}})();</script>
<script>document.addEventListener('click',function(ev){{var a=ev.target.closest('a[data-ev]');if(a&&window.gtag)gtag('event','card_'+a.dataset.ev,{{transport_type:'beacon'}})}});</script>
</body></html>'''
os.makedirs(R+"/card",exist_ok=True); os.makedirs(R+"/assets/card",exist_ok=True)
open(R+"/card/index.html","w").write(_card_html())
open(R+"/card/richard-cuagdan.vcf","w",newline="").write("\r\n".join(["BEGIN:VCARD","VERSION:3.0",f"N:Cuagdan;Richard Dennis;;;",f"FN:{CARD_NAME}",f"ORG:{CARD_CORP}","TITLE:Car Sales Executive",f"TEL;TYPE=CELL,VOICE:{TEL}",f"URL:{D}/",f"URL;TYPE=Messenger:{MSG}",f"URL;TYPE=Facebook:{FB}","ADR;TYPE=WORK:;;;San Jose del Monte;Bulacan;;Philippines","NOTE:Mitsubishi car sales. Serving SJDM Bulacan and Quezon City.","END:VCARD",""]))
