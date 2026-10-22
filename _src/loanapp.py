# ---------- /loan-assessment/ (Phase 1, static). exec'd from build.py
def _dp(lbl):
    import re
    m=re.search(r"([\d.]+)K",lbl); return int(float(m.group(1))*1000) if m else 0
LAU=[]
for m in MODELS:
    for v in m["variants"]:
        if not v["promo"]: continue
        price=v["srp"] or v["promo"].get("srp")
        if not price: continue
        LAU.append({"id":v["id"],"model":m["name"],"n":v["n"],"price":price,"opts":[{"dp":_dp(l),"mo":mo} for l,mo in v["promo"]["opts"]]})
LA_CONSENT=('Sa pag-check ng box na ito, pinapayagan ko ang <b>[Dealer Legal Name]</b> / mitsubishipromos.online na kolektahin, i-process, at i-store ang aking personal at sensitive personal information '
 '(kasama ang IDs, income, at financial documents) para lamang sa pag-assess ng aking car loan application, at i-share ito sa piling partner banks at financing companies '
 '(hal. Mitsubishi Motors Finance PH, BPI, BDO, Metrobank, Security Bank, PSBank, RCBC, EastWest) para sa credit evaluation, alinsunod sa Republic Act No. 10173 (Data Privacy Act of 2012). '
 'Alam ko ang aking karapatan na ma-access, maitama, ma-withdraw ang consent, at ipabura ang aking data, at maaari akong makipag-ugnayan sa aming Data Protection Officer sa <b>[DPO email]</b>. '
 'Nabasa ko ang <a href="/privacy/">Privacy Notice</a>.')
LA_CSS='''<style>
.la{background:linear-gradient(180deg,#0b0b0c 0,#17171a 260px,#f4f4f6 260px);padding:28px 0 48px}
.la .w{max-width:720px}.la h1{color:#fff;font-size:clamp(28px,6vw,42px)}.la .lead{color:#d4d4d8}
.la-steps{display:flex;gap:6px;list-style:none;padding:0;margin:0 0 18px;counter-reset:s}.la-steps li{flex:1;font-size:12px;color:#a1a1aa;border-top:3px solid #3f3f46;padding-top:6px}.la-steps li.on{color:#fff;border-color:var(--red)}
.la-card{background:#fff;border-radius:20px;box-shadow:0 10px 40px rgba(0,0,0,.12);padding:22px}
.la-card .fld{margin-bottom:14px}.la-card label{font-weight:600;display:block;margin-bottom:4px}.la-card input[type=text],.la-card input[type=tel],.la-card input[type=email]{width:100%;padding:12px;border:1px solid var(--ln);border-radius:12px;font:inherit}
.la-cons{font-size:14px;background:#f8f8fa;border:1px solid var(--ln);border-radius:12px;padding:12px;max-height:180px;overflow:auto;margin:0 0 10px}
.la-log{display:flex;flex-direction:column;gap:12px;min-height:200px}
.la-b{display:flex;gap:8px;align-items:flex-end}.la-b.me{justify-content:flex-end}
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
.la-x{display:grid;gap:10px;grid-template-columns:repeat(3,1fr);margin:16px 0 0}.la-x div{background:#f8f8fa;border-radius:12px;padding:10px;font-size:14px}
@media(min-width:760px){.la-cta{flex-direction:row}.la-cta .btn{flex:1}}
@media(max-width:520px){.la-sum,.la-x{grid-template-columns:1fr}}
.lacta{background:linear-gradient(135deg,#0b0b0c,#2a0a0d);color:#fff;border-radius:18px;padding:20px 22px;margin:24px 0}.lacta h2{color:#fff;margin:0 0 6px;font-size:22px}.lacta p{color:#d4d4d8;margin:0 0 12px}
</style>'''
page("/loan-assessment/","AI Car Loan Assessment | Mitsubishi Motors - SJ Legacy Motors",
 "Libreng car loan pre-assessment para sa Mitsubishi: sagutin ang ilang tanong, piliin ang unit at promo, at alamin kung Pre-qualified ka. 3 minuto lang.",
LA_CSS+f'''<section class="la"><div class="w">
<p class="kick" style="color:#fca5a5">Libreng pre-assessment · 3 minuto</p>
<h1>Car Loan Assessment</h1>
<p class="lead">Alamin agad kung pasok ka sa car loan bago ka pumunta sa showroom. Sagutin lang ang ilang tanong, piliin ang Mitsubishi mo, at makikita mo ang resulta at mga options.</p>
<ol class="la-steps" aria-label="Progress"><li class="on">1. Contact</li><li>2. Tanong</li><li>3. Unit</li><li>4. Resulta</li></ol>
<div id="la-intro" class="la-card"><h2 class="h3">Paano ito gumagana?</h2>
<div class="la-x"><div><b>Sagutin</b><br>Income, trabaho at existing loans.</div><div><b>Pumili</b><br>Unit, DP at monthly mula sa promo ngayong buwan.</div><div><b>Alamin</b><br>Pre-qualified, Needs Review, o mga options para pumasa.</div></div>
<p class="muted small" style="margin-top:14px">Pre-screening lang ito, hindi bank approval. Walang IDs o documents na hihingin dito.</p>
<button class="btn" type="button" id="la-start">Simulan ang assessment</button></div>
<div id="la-s1" class="la-card" hidden><h2 class="h3">Hi! Ako si Richard. Unahin natin ang contact details mo.</h2>
<form id="la-f1" novalidate>
<div class="fld"><label for="la-name">Buong pangalan *</label><input type="text" id="la-name" autocomplete="name" required><p class="er" id="e_la-name" hidden>Pakilagay ang pangalan mo.</p></div>
<div class="fld"><label for="la-mobile">Mobile number *</label><input type="tel" id="la-mobile" inputmode="tel" autocomplete="tel" placeholder="09XX XXX XXXX" required><p class="er" id="e_la-mobile" hidden>Pakilagay ang tamang PH mobile (09XXXXXXXXX o +639XXXXXXXXX).</p></div>
<div class="fld"><label for="la-email">Email (optional)</label><input type="email" id="la-email" autocomplete="email"><p class="er" id="e_la-email" hidden>Pakicheck ang email.</p></div>
<p class="fl"><b>Data Privacy Consent</b></p><div class="la-cons" tabindex="0">{LA_CONSENT}</div>
<label class="chk"><input type="checkbox" id="la-consent"> <span>I agree / Sumasang-ayon ako</span></label><p class="er" id="e_la-consent" hidden>Kailangan ang consent bago tayo magpatuloy.</p>
<button class="btn" type="submit">Tuloy</button></form></div>
<div id="la-chat" hidden><div id="la-log" class="la-log" aria-live="polite"></div></div>
<div id="la-res" hidden></div>
<p id="la-note" hidden>{e(NOTE)}</p>
</div></section>
<script type="application/json" id="la-units">{json.dumps(LAU,ensure_ascii=False)}</script>
<script src="/assets/lead.js" defer></script>
<script src="/assets/loan-assessment.js" defer></script>''', crumbs=[("/","Home"),("/loan-assessment/","Loan Assessment")])
