# ---------- /loan-assessment/ (Phase 1, static). exec'd from build.py
def _dp(lbl):
    import re
    m=re.search(r"([\d.]+)K",lbl); return int(float(m.group(1))*1000) if m else 0
QWP=("Quartz White Pearl",15000);WD=("White Diamond",15000)
_C={"mg4glxat":["Titanium Gray Metallic","Red Metallic","Cool Silver Metallic","White Solid (order basis)"],
"xglxmt":["Blade Silver Metallic","Graphite Grey Metallic","Jet Black Mica"],
"xglsat":["Green Bronze Metallic","Red Metallic","Graphite Grey Metallic",QWP],
"xcross":["Sunrise Orange Metallic / Jet Black Mica roof","Green Bronze Metallic / Jet Black Mica roof",("Quartz White Pearl / Jet Black Mica roof",15000)],
"dglx":["Blade Silver Metallic","Graphite Gray Metallic","Red Metallic",QWP],
"dgls":["Lunar Blue Mica","Graphite Gray Metallic","Jet Black Mica",QWP],
"dgtm":["Graphite Gray Metallic","Jet Black Mica"],
"dgtt":["Lunar Blue Mica / Jet Black Mica roof","Graphite Gray Metallic / Jet Black Mica roof",("Quartz White Pearl / Jet Black Mica roof",15000)],
"mglxmt":["Jet Black Mica","Blade Silver Metallic",WD],
"mbs2wd":["Jet Black Mica","Graphite Gray Metallic with Black Roof",("White Diamond with Black Roof",15000)],
"tritongxat":["Red Solid","Blade Silver Metallic","Graphite Gray Metallic","Jet Black Mica",WD],
"l300":["White"],
"vvglx":["Silver Metallic","White Solid"]}
_C["mg4gls"]=_C["mg4glxat"];_C["xglxat"]=_C["xglxmt"];_C["mgls"]=_C["mglxmt"];_C["mbs4wd"]=_C["mbs2wd"]
def _cl(i): return [[c,0] if isinstance(c,str) else list(c) for c in _C.get(i,[])]
LAU=[]
for m in MODELS:
    for v in m["variants"]:
        if not v["promo"]: continue
        price=v["srp"] or v["promo"].get("srp")
        if not price: continue
        LAU.append({"id":v["id"],"model":m["name"],"n":v["n"],"price":price,"colors":_cl(v["id"]),"opts":[{"dp":_dp(l),"mo":mo} for l,mo in v["promo"]["opts"]]})
def B(tl,en): return f'<span class="tl">{tl}</span><span class="en">{en}</span>'
LA_CONSENT=B('Sa pag-check ng box na ito, pinapayagan ko ang <b>San Juan Motors</b> / mitsubishipromos.online na kolektahin, i-process, at i-store ang aking personal at sensitive personal information '
 '(kasama ang IDs, income, at financial documents) para lamang sa pag-assess ng aking car loan application, at i-share ito sa piling partner banks at financing companies '
 '(hal. Mitsubishi Motors Finance PH, BPI, BDO, Metrobank, Security Bank, PSBank, RCBC, EastWest) para sa credit evaluation, alinsunod sa Republic Act No. 10173 (Data Privacy Act of 2012). '
 'Alam ko ang aking karapatan na ma-access, maitama, ma-withdraw ang consent, at ipabura ang aking data, at maaari akong makipag-ugnayan sa aming Data Protection Officer (contact para sa privacy concerns) sa <b>richard.cuagdan20@gmail.com</b>. '
 'Kung mag-message ka kay Richard sa Facebook Messenger, gagamitin lang ang messages para sagutin ang inquiry mo. Nabasa ko ang <a href="/privacy/">Privacy Notice</a>.',
 'By checking this box, I allow <b>San Juan Motors</b> / mitsubishipromos.online to collect, process, and store my personal and sensitive personal information '
 '(including IDs, income, and financial documents) solely to assess my car loan application, and to share it with selected partner banks and financing companies '
 '(e.g. Mitsubishi Motors Finance PH, BPI, BDO, Metrobank, Security Bank, PSBank, RCBC, EastWest) for credit evaluation, in accordance with Republic Act No. 10173 (Data Privacy Act of 2012). '
 'I know my rights to access, correct, withdraw consent, and have my data erased, and I may contact the Data Protection Officer (contact for privacy concerns) at <b>richard.cuagdan20@gmail.com</b>. '
 'If you message Richard on Facebook Messenger, those messages are used only to reply to your inquiry. I have read the <a href="/privacy/">Privacy Notice</a>.')
LA_CSS='''<style>
.fab{display:none!important}.la-recbox{margin:14px 0}.la-recbox .la-opt{display:flex;flex-direction:column;gap:4px;text-align:left;width:100%;cursor:default}.la-recbox .la-opt .btn{align-self:flex-start;margin-top:6px}.la-why{background:#fff8e1;border-radius:10px;padding:10px 12px;margin:8px 0;font-size:.95em}.la-adj{margin:14px 0;border:1px solid #e5e5e5;border-radius:12px;padding:10px 12px}.la-adj>summary{cursor:pointer;font-weight:600;font-size:.95em}.la-final{text-align:center;margin-top:18px}.la-final .btn{width:100%}.la-fina{background:#16a34a!important}.la [hidden]{display:none!important}html[data-lang=tl] :is(.la,.la-hero,.la-stepbar) .en,html:not([data-lang=tl]) :is(.la,.la-hero,.la-stepbar) .tl{display:none!important}.la-lang{display:flex;gap:8px;margin:0 0 14px}.la-lang button{background:none;border:1px solid #52525b;color:#fff;border-radius:999px;padding:6px 14px;font:inherit;font-size:14px;cursor:pointer}html[data-lang=tl] .la-lang [data-setlang=tl],html:not([data-lang=tl]) .la-lang [data-setlang=en]{background:#fff;color:#0b0b0c}.la-start{display:flex;flex-wrap:wrap;gap:10px}.la-done{background:#166534!important;opacity:1!important}
.la{padding-bottom:110px!important;background:#f4f4f6;padding:28px 0 48px}
.la .w,.la-hero .w,.la-stepbar .w{max-width:720px}
.la-hero{background:#0b0b0c;padding:26px 0 30px}.la-hero h1{color:#fff;font-size:clamp(28px,6vw,42px)}.la-hero .lead{color:#e4e4e7;margin:0}.la-stepbar{position:sticky;top:64px;z-index:15;background:#fff;border-bottom:1px solid var(--ln);box-shadow:0 4px 14px rgba(0,0,0,.06)}.la-in .chip.sel{background:#c00;color:#fff;border-color:#c00}.la-in .chip:disabled{opacity:.45}.la-back{display:block;margin-top:10px;background:none;border:0;color:#52525b;font:inherit;font-size:14px;cursor:pointer;padding:4px 0;text-decoration:underline}.la-edit{cursor:pointer}.la-pen{font-size:12px;opacity:.75;margin-left:6px;white-space:nowrap}.la-edit:hover .la-bu{outline:2px solid #c00}
.la-steps{display:flex;justify-content:space-between;list-style:none;padding:10px 0 8px;margin:0;gap:4px}.la-steps li{flex:1;display:flex;flex-direction:column;align-items:center;gap:4px;font-size:13px;font-weight:600;color:#52525b;white-space:nowrap;position:relative;min-width:0}.la-steps li:not(:last-child)::after{content:"";position:absolute;top:14px;left:calc(50% + 18px);right:calc(-50% + 18px);height:2px;background:#d4d4d8}.la-steps li.done:not(:last-child)::after{background:#c00}.la-steps .n{width:28px;height:28px;border-radius:50%;border:2px solid #a1a1aa;color:#52525b;background:#fff;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;line-height:1}.la-steps li.on .n{background:#c00;border-color:#c00;color:#fff}.la-steps li.on{color:#0b0b0c}.la-steps li.done .n{background:#fff;border-color:#c00;color:#c00}.la-steps li.done{color:#3f3f46}@media(max-width:600px){.la-hero .lead{font-size:16px;line-height:1.5}.la-steps li{font-size:12px}}
.la-card{background:#fff;border-radius:20px;box-shadow:0 10px 40px rgba(0,0,0,.12);padding:22px}
.la-card .fld{margin-bottom:14px}.la-card label{font-weight:600;display:block;margin-bottom:4px}.la-card input[type=text],.la-card input[type=tel],.la-card input[type=email]{width:100%;padding:12px;border:1px solid var(--ln);border-radius:12px;font:inherit}
.la-cons{font-size:14px;background:#f8f8fa;border:1px solid var(--ln);border-radius:12px;padding:12px;max-height:180px;overflow:auto;margin:0 0 10px}
.la-log{display:flex;flex-direction:column;gap:12px;min-height:200px}
.la-b{scroll-margin-bottom:110px;display:flex;gap:8px;align-items:flex-end}.la-b.me{justify-content:flex-end}
.la-av{flex:0 0 32px;height:32px;border-radius:50%;background:var(--red);color:#fff;font-weight:700;display:flex;align-items:center;justify-content:center;font-size:14px}
.la-bu{max-width:86%;padding:12px 14px;border-radius:18px;background:#fff;box-shadow:0 2px 10px rgba(0,0,0,.06);font-size:16px}
.bot .la-bu{border-bottom-left-radius:6px}.me .la-bu{background:var(--ink);color:#fff;border-bottom-right-radius:6px}
.la-in{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}.la-in .chip{border:1px solid #d4d4d8;background:#fff;border-radius:999px;padding:9px 14px;font:inherit;font-size:15px;cursor:pointer;text-align:left}.la-in .chip:hover,.la-in .chip:focus{border-color:var(--red);color:var(--redd)}
.la-in input{flex:1 1 160px;padding:10px 12px;border:1px solid var(--ln);border-radius:12px;font:inherit}.la-in .er{flex-basis:100%;margin:0}
.la-badge{display:inline-block;font-weight:800;font-size:22px;padding:6px 16px;border-radius:999px;margin-bottom:10px}
.res-pre_qualified .la-badge{background:#dcfce7;color:#166534}.res-needs_review .la-badge{background:#fef3c7;color:#92400e}.res-not_yet_qualified .la-badge{background:#fee2e2;color:#991b1b}
.la-sum{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:16px 0}.la-sum div{background:#f8f8fa;border-radius:12px;padding:10px}.la-sum dt{font-size:12px;color:var(--mu)}.la-sum dd{margin:0;font-weight:700}
.la-cta{display:flex;flex-direction:column;gap:10px;margin:20px 0}.la-cta .btn{text-align:center;justify-content:center}.la-msg{background:#0866ff!important;font-size:18px;padding:16px!important}
.la-next{border:2px dashed #d4d4d8;border-radius:16px;padding:16px;margin:16px 0}.la-ok{color:#166534;font-weight:600}.small{font-size:13px}
.la-calcbox{border:1px solid var(--ln);border-radius:16px;padding:16px;margin:16px 0;background:#fcfcfd}.la-tabs{display:flex;gap:8px;margin-bottom:10px;flex-wrap:wrap}.la .chip{border:1px solid #d4d4d8;background:#fff;border-radius:999px;padding:8px 14px;font:inherit;font-size:15px;cursor:pointer}.la .chip.on{background:var(--ink);color:#fff;border-color:var(--ink)}#la-dpr{width:100%;margin:10px 0;accent-color:#E60012}
.la-tbl{width:100%;border-collapse:collapse;font-size:14px;margin:8px 0}.la-tbl th,.la-tbl td{border-bottom:1px solid var(--ln);padding:7px 6px;text-align:left}
.la-fit{display:inline-block;font-size:12px;font-weight:700;padding:2px 8px;border-radius:999px}.la-fit.ok{background:#dcfce7;color:#166534}.la-fit.mid{background:#fef3c7;color:#92400e}.la-fit.no{background:#fee2e2;color:#991b1b}
.la-opt{display:flex;flex-direction:column;gap:2px;width:100%;text-align:left;border:1px solid var(--ln);background:#fff;border-radius:14px;padding:12px;margin:8px 0;font:inherit;cursor:pointer}.la-opt span{font-size:14px;color:var(--mu)}.la-opt em{font-style:normal;color:var(--redd);font-weight:700;font-size:14px}.la-opt.hl{border:2px solid #16a34a;background:#f0fdf4}.la-promo{margin-top:12px}.la-link{background:none;border:0;color:var(--redd);text-decoration:underline;font:inherit;cursor:pointer;padding:0}
.la-docs{list-style:none;padding:0;margin:10px 0}.la-docs li{border:1px solid var(--ln);border-radius:12px;padding:10px 12px;margin-bottom:8px;display:flex;justify-content:space-between;gap:10px;align-items:center}.la-docs label{display:flex;gap:6px;align-items:center;font-weight:600;white-space:nowrap;font-size:14px;margin:0}.la-docs input{width:20px;height:20px}.la-cnt{font-weight:700}.la-lack{background:#fff7ed;border-radius:12px;padding:12px;margin:10px 0}
.la-x{display:grid;gap:10px;grid-template-columns:repeat(3,1fr);margin:16px 0 0}.la-x div{background:#f8f8fa;border-radius:12px;padding:10px;font-size:14px}
@media(min-width:760px){.la-cta{flex-direction:row}.la-cta .btn{flex:1}}
@media(max-width:520px){.la-sum,.la-x{grid-template-columns:1fr}}
.lacta{background:linear-gradient(135deg,#0b0b0c,#2a0a0d);color:#fff;border-radius:18px;padding:20px 22px;margin:24px 0}.lacta h2{color:#fff;margin:0 0 6px;font-size:22px}.lacta p{color:#d4d4d8;margin:0 0 12px}
.la-score{border-radius:16px;padding:14px 16px;margin:12px 0;background:#f4f4f5}.la-score.ok{background:#ecfdf5}.la-score.mid{background:#fffbeb}.la-score.no{background:#fef2f2}.la-sl{margin:0;font-size:12px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:#52525b}.la-sv{margin:2px 0 6px}.la-sv b{font-size:34px;line-height:1.1}.la-sv span{font-weight:700;color:#3f3f46}.la-sb{height:10px;background:#e4e4e7;border-radius:99px;overflow:hidden}.la-sb i{display:block;height:100%;background:#16a34a}.la-score.mid .la-sb i{background:#d97706}.la-score.no .la-sb i{background:#dc2626}.la-sc{font-size:13px;color:#52525b;margin:8px 0 0}.la-sd summary{cursor:pointer;font-size:14px;margin-top:6px}.la-sd ul{margin:6px 0 0;padding-left:18px}
.la-bu{font-size:15px;padding:10px 12px}.la-in .chip{padding:7px 12px;font-size:14px}.la-log{gap:9px}.la-card{padding:18px}
</style>'''
page("/loan-assessment/","AI Car Loan Application Assessment | Mitsubishi Motors - San Juan Motors",
 "AI Car Loan Application Assessment for Mitsubishi: answer a few questions, pick your unit and promo, and find out if you are Pre-qualified. Takes 3 minutes.",
LA_CSS+f'''<section class="la-hero"><div class="w">
<div class="la-lang" role="group" aria-label="Language / Wika"><button type="button" data-setlang="en">English</button><button type="button" data-setlang="tl">Tagalog / Taglish</button></div>
<p class="kick" style="color:#fca5a5">{B("Libreng pre-assessment · 3 minuto","Free pre-assessment · 3 minutes")}</p>
<h1>AI Car Loan Application Assessment</h1>
<p class="lead">{B("Alamin agad kung pasok ka sa car loan bago ka pumunta sa showroom. Sagutin lang ang ilang tanong, piliin ang Mitsubishi mo, at makikita mo ang resulta at mga options.","Find out if you qualify for a car loan before you visit the showroom. Answer a few questions, pick your Mitsubishi, and see your result and options.")}</p>
</div></section>
<div class="la-stepbar"><div class="w"><ol class="la-steps" aria-label="Progress"><li class=\"on\" aria-current=\"step\"><span class="n">1</span><span class="t">{B("Unit at tanong","Unit &amp; questions")}</span></li><li><span class="n">2</span><span class="t">{B("I-save","Save")}</span></li><li><span class="n">3</span><span class="t">{B("Resulta","Result")}</span></li><li><span class="n">4</span><span class="t">Docs</span></li></ol></div></div>
<section class="la"><div class="w" style="padding-top:18px">
<div id="la-s1" class="la-card" hidden><p class="kick" style="color:#b8000e">{B("Handa na ang resulta mo","Your results are ready")}</p><h2 class="h3">{B("I-save ang resulta mo","Save My Results")}</h2>
<p class="small">{B("Ilagay ang pangalan mo at mobile number o Messenger link para makita ang Likelihood Score at buong resulta, at para mai-save namin ito para sa follow-up ni Richard.","Enter your name and a mobile number or Messenger link to see your Likelihood Score and full results, and so we can keep them for Richard's follow-up.")}</p>
<form id="la-f1" novalidate>
<div class="fld"><label for="la-name">{B("Buong pangalan","Full name")} *</label><input type="text" id="la-name" autocomplete="name" required><p class="er" id="e_la-name" hidden>{B("Pakilagay ang pangalan mo.","Please enter your name.")}</p></div>
<div class="fld"><label for="la-mobile">Mobile number</label><input type="tel" id="la-mobile" inputmode="tel" autocomplete="tel" placeholder="09XX XXX XXXX"><p class="er" id="e_la-mobile" hidden>{B("Pakilagay ang tamang PH mobile (09XXXXXXXXX o +639XXXXXXXXX).","Please enter a valid PH mobile (09XXXXXXXXX or +639XXXXXXXXX).")}</p></div>
<div class="fld"><label for="la-fb">{B("o Messenger / Facebook link","or Messenger / Facebook link")}</label><input type="url" id="la-fb" inputmode="url" autocomplete="off" placeholder="m.me/yourname or facebook.com/yourname"><p class="er" id="e_la-fb" hidden>{B("Ilagay ang mobile number o tamang Messenger/Facebook link.","Enter a mobile number or a valid Messenger/Facebook link.")}</p></div>
<div class="fld"><label for="la-email">Email (optional)</label><input type="email" id="la-email" autocomplete="email"><p class="er" id="e_la-email" hidden>{B("Pakicheck ang email.","Please check your email.")}</p></div>
<p class="fl"><b>Data Privacy Consent</b></p><div class="la-cons" tabindex="0">{LA_CONSENT}</div>
<label class="chk"><input type="checkbox" id="la-consent"> <span>{B("Sumasang-ayon ako / I agree","I agree / Sumasang-ayon ako")}</span></label><p class="er" id="e_la-consent" hidden>{B("Kailangan ang consent bago namin i-save ang resulta.","Consent is required before we save your results.")}</p>
<button class="btn" type="submit">{B("I-save at tingnan ang resulta","Save and see my results")}</button></form></div>
<div id="la-chat"><div id="la-log" class="la-log" aria-live="polite"></div></div>
<div id="la-res" hidden></div>
<p id="la-note" hidden>{e(NOTE)}</p>
</div></section>
<script type="application/json" id="la-units">{json.dumps(LAU,ensure_ascii=False)}</script>
<script src="/assets/lead.js" defer></script>
<script src="/assets/loan-assessment.js" defer></script>''', crumbs=[("/","Home"),("/loan-assessment/","AI Car Loan Application Assessment")])
# Cache-busting: content hashes on the loan page's JS/CSS (Cloudflare caches /assets for 4h).
import hashlib as _hl
def _vh(f): return _hl.md5(open(R+f,'rb').read()).hexdigest()[:8]
_lp=R+"/loan-assessment/index.html"; _s=open(_lp).read()
_s=_s.replace('src="/assets/loan-assessment.js"',f'src="/assets/loan-assessment.js?v={_vh("/assets/loan-assessment.js")}"').replace('src="/assets/lead.js"',f'src="/assets/lead.js?v={_vh("/assets/lead.js")}"').replace('href="/assets/site.css"',f'href="/assets/site.css?v={_vh("/assets/site.css")}"')
open(_lp,'w').write(_s)
