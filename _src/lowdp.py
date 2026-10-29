# /lowest-down-payment/ campaign page (2026-10-29, Richard). Overrides the earlier no-Zero-DP rule for this page only.
import json, hashlib, os
LOWDP=[("mirage-g4","Mirage G4",0,18000),("xpander","Xpander",18000,33000),("xforce","Xforce",18000,48000),("destinator","Destinator",0,33000),
 ("triton","Triton",0,18000),("montero-sport","Montero Sport",0,33000),("l300","L300",18000,53000),("versa-van","Versa Van",18000,48000),("outlander-phev","Outlander PHEV",68000,183000)]
# base-variant SRPs from /workspace/loanapp/pricelist/option_AB_table.csv (first row per family)
BASE={"mirage-g4":("Mirage G4 GLX 1.2G M/T",793000),"xpander":("Xpander GLX 1.5G 2WD M/T",1099000),"xforce":("Xforce GLX 1.5G 2WD CVT",1119000),
 "destinator":("Destinator GLX 1.5G Turbo 2WD CVT",1389000),"triton":("Triton GL 2.4D 2WD M/T",1266000),"montero-sport":("Montero Sport GLX 2.4D 2WD M/T",1568000),
 "l300":("L300 Cab & Chassis 2.2D M/T",829000),"versa-van":("Versa Van GLX 2.5D 2WD M/T",1749000),"outlander-phev":("Outlander PHEV GT 2.4G AWD",2848000)}
DISC="Subject to bank approval. Pre-qualified only; rates, promos and DP may change without prior notice."
def build(page,e,f,img,hero,R):
    data=[dict(id=s,n=n,lo=lo,hi=hi,base=BASE[s][0],srp=BASE[s][1]) for s,n,lo,hi in LOWDP]
    rng=lambda lo,hi: f"{f(lo)} – {f(hi)}"
    rows="".join(f'<tr><th scope="row">{e(n)}</th><td><b>{rng(lo,hi)}</b></td><td class="ld-act"><button type="button" class="ld-pick" data-pick="{i}"><span class="en">Unlock</span><span class="tl">I-unlock</span></button></td></tr>' for i,(s,n,lo,hi) in enumerate(LOWDP))
    opts="".join(f'<option value="{i}">{e(n)}</option>' for i,(s,n,lo,hi) in enumerate(LOWDP))
    lv=hashlib.md5(open(R+"/assets/lead.js","rb").read()).hexdigest()[:8]
    jv=hashlib.md5(open(R+"/assets/lowdp.js","rb").read()).hexdigest()[:8]
    css='''<style>html[data-lang=tl] .ld .en,html:not([data-lang=tl]) .ld .tl{display:none!important}
.ld-lang{display:flex;gap:8px;margin:0 0 14px}.ld-lang button{background:none;border:1px solid #52525b;color:#fff;border-radius:999px;padding:8px 14px;min-height:40px;font:inherit;font-size:14px;cursor:pointer}html[data-lang=tl] .ld-lang [data-setlang=tl],html:not([data-lang=tl]) .ld-lang [data-setlang=en]{background:#fff;color:#0b0b0c}
.ld-tw{overflow-x:auto;border:1px solid var(--ln);border-radius:var(--r);background:#fff}.ld-t{width:100%;border-collapse:collapse;font-size:16px}.ld-t th,.ld-t td{padding:14px 16px;text-align:left;border-bottom:1px solid var(--ln)}.ld-t thead th{background:#0b0b0c;color:#fff;font-size:13px;letter-spacing:.06em;text-transform:uppercase}.ld-t tr:last-child th,.ld-t tr:last-child td{border-bottom:0}.ld-t td b{color:var(--redd);white-space:nowrap}.ld-act{text-align:right!important}
.ld-pick{background:var(--red);color:#fff;border:0;border-radius:999px;padding:8px 14px;min-height:40px;font:inherit;font-size:14px;font-weight:700;cursor:pointer}.ld-pick:hover{background:var(--redd)}
.ld-disc{background:#fff8e1;border-left:4px solid #f59e0b;border-radius:10px;padding:12px 14px;margin:16px 0 0;font-size:14px;color:#3f3f46}
.ld-grid{display:grid;gap:24px}@media(min-width:900px){.ld-grid{grid-template-columns:1fr 1fr;align-items:start}}.ld-grid>*{min-width:0}
.ld-res{display:flex;flex-direction:column;gap:4px;background:#0b0b0c;color:#e4e4e7;border-radius:14px;padding:16px;margin-top:6px}.ld-mo{font-size:32px;font-weight:800;color:#fff}.ld-mo small{font-size:15px;font-weight:600;color:#a1a1aa}.ld-f{font-size:13px;color:#a1a1aa;overflow-wrap:anywhere}
.ld .chk{font-size:14px;display:flex;gap:10px;align-items:flex-start;margin:6px 0 14px}.ld .chk input{width:20px;height:20px;flex:none;margin-top:2px}.ld .ferr{color:#b8000e;font-size:13px;margin:4px 0 0}.ld-ok{background:#f0fdf4;border:1px solid #bbf7d0;border-radius:14px;padding:16px}.ld-btn{width:100%;font-size:17px}
@media(max-width:520px){.ld-t th,.ld-t td{padding:12px 10px;font-size:15px}.ld-pick{padding:8px 10px;font-size:13px}}</style>'''
    body=css+f'''<div class="ld"><section class="hero"><div class="w hgrid"><div>
<div class="ld-lang" role="group" aria-label="Language / Wika"><button type="button" data-setlang="en">English</button><button type="button" data-setlang="tl">Taglish</button></div>
<p class="kick"><span class="en">October 2026 campaign · Mitsubishi San Juan Motors</span><span class="tl">October 2026 campaign · Mitsubishi San Juan Motors</span></p>
<h1><span class="en">Unlock Lowest Down up to Zero Downpayment Promos</span><span class="tl">I-unlock ang Lowest Down, hanggang Zero Downpayment Promos</span></h1>
<p class="lead"><span class="en">See the lowest down payment range for every Mitsubishi, estimate your standard monthly, then unlock the exact computation for your chosen unit.</span><span class="tl">Tingnan ang pinakamababang down payment ng bawat Mitsubishi, i-estimate ang standard monthly mo, tapos i-unlock ang eksaktong computation para sa unit na gusto mo.</span></p>
<p class="row hcta"><a class="btn" href="#unlock" data-herocta="lowest-dp"><span class="en">Unlock my computation</span><span class="tl">I-unlock ang computation ko</span></a></p>
</div>{img("xpglx_x37","Mitsubishi Xpander",eager=True,cls="himg")}</div></section>
<section class="sec" id="table"><div class="w"><h2><span class="en">Lowest down payment per unit</span><span class="tl">Lowest down payment kada unit</span></h2>
<p class="sub"><span class="en">Ranges depend on the variant, bank and promo. Tap Unlock to get the exact figure for your unit.</span><span class="tl">Depende sa variant, bangko at promo ang range. I-tap ang I-unlock para sa eksaktong figure ng unit mo.</span></p>
<div class="ld-tw"><table class="ld-t"><thead><tr><th scope="col">Unit</th><th scope="col">Lowest DP</th><th scope="col" class="ld-act"><span class="en">Details</span><span class="tl">Detalye</span></th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="ld-disc"><b>{e(DISC)}</b></p></div></section>
<section class="sec alt" id="unlock"><div class="w"><h2><span class="en">Unlock my computation</span><span class="tl">I-unlock ang computation ko</span></h2>
<p class="sub"><span class="en">Choose your unit and down payment, check the standard estimate, then leave your details so Richard can send the exact all-in computation.</span><span class="tl">Piliin ang unit at DP, tingnan ang standard estimate, tapos iwan ang details mo para ma-send ni Richard ang eksaktong all-in computation.</span></p>
<div class="ld-grid"><div class="card pad"><h3><span class="en">1. Standard amortization estimate</span><span class="tl">1. Standard amortization estimate</span></h3>
<div class="fld"><label for="ld-unit">Unit</label><select id="ld-unit">{opts}</select></div>
<div class="fld"><label for="ld-dp"><span class="en">Down payment</span><span class="tl">Down payment (DP)</span></label><select id="ld-dp"></select></div>
<div class="fld" id="ld-dpo-w" hidden><label for="ld-dpo"><span class="en">Your down payment (₱)</span><span class="tl">DP mo (₱)</span></label><input id="ld-dpo" inputmode="numeric" autocomplete="off" placeholder="e.g. 50000"></div>
<div class="fld"><label for="ld-term"><span class="en">Term</span><span class="tl">Term (taon)</span></label><select id="ld-term"><option value="5" selected>5 years (60 months) · AOR 1.55</option><option value="4">4 years (48 months) · 1.48</option><option value="3">3 years (36 months) · 1.32</option><option value="2">2 years (24 months) · 1.24</option><option value="1">1 year (12 months) · 1.22</option></select></div>
<div class="ld-res" id="ld-res" aria-live="polite"></div>
<p class="muted" style="font-size:13px;margin-top:10px"><span class="en">Standard formula: (SRP − DP) × AOR ÷ months, using the base-variant SRP. Estimate only; the all-in promo computation may differ.</span><span class="tl">Standard formula: (SRP − DP) × AOR ÷ months, gamit ang base-variant SRP. Estimate lang ito; puwedeng iba ang all-in promo computation.</span></p></div>
<div class="card pad"><h3><span class="en">2. Get the exact computation</span><span class="tl">2. Kunin ang eksaktong computation</span></h3>
<form id="ld-form" class="zform" novalidate>
<div class="fld"><label for="ld-name"><span class="en">Full name</span><span class="tl">Buong pangalan</span></label><input id="ld-name" autocomplete="name" required><p class="ferr" id="e_ld-name" hidden><span class="en">Please enter your name.</span><span class="tl">Pakilagay ang pangalan mo.</span></p></div>
<div class="fld"><label for="ld-mobile"><span class="en">Mobile number</span><span class="tl">Mobile number</span></label><input id="ld-mobile" type="tel" inputmode="tel" autocomplete="tel" placeholder="09XX XXX XXXX" required><p class="ferr" id="e_ld-mobile" hidden><span class="en">Enter a valid mobile number (09XXXXXXXXX).</span><span class="tl">Maglagay ng tamang mobile number (09XXXXXXXXX).</span></p></div>
<div class="fld"><label for="ld-email">Email</label><input id="ld-email" type="email" autocomplete="email" required><p class="ferr" id="e_ld-email" hidden><span class="en">Enter a valid email.</span><span class="tl">Maglagay ng tamang email.</span></p></div>
<label class="chk"><input type="checkbox" id="ld-consent"><span><span class="en">I agree to be contacted by Richard Cuagdan of Mitsubishi San Juan Motors about my chosen unit, and to the <a href="/privacy/">privacy policy</a>.</span><span class="tl">Pumapayag akong i-contact ni Richard Cuagdan ng Mitsubishi San Juan Motors tungkol sa napili kong unit, at sa <a href="/privacy/">privacy policy</a>.</span></span></label>
<p class="ferr" id="e_ld-consent" hidden><span class="en">Please tick the consent box.</span><span class="tl">Paki-check ang consent box.</span></p>
<button class="btn ld-btn" id="ld-btn" type="submit"><span class="en">Unlock my computation</span><span class="tl">I-unlock ang computation ko</span></button>
<p class="muted" style="font-size:13px;margin-top:10px">{e(DISC)}</p></form>
<div class="ld-ok" id="ld-ok" hidden aria-live="polite"></div></div></div></div></section>
<section class="sec"><div class="w"><p class="muted"><span class="en">Richard Cuagdan, sales executive at Mitsubishi San Juan Motors, serves buyers in San Jose del Monte (SJDM), Bulacan and Quezon City. See also <a href="/promos/">this month's promos</a> and the <a href="/budgetcalculator/">full monthly calculator</a>.</span><span class="tl">Si Richard Cuagdan, sales executive ng Mitsubishi San Juan Motors, ay nagse-serve sa San Jose del Monte (SJDM), Bulacan at Quezon City. Tingnan din ang <a href="/promos/">promos ngayong buwan</a> at ang <a href="/budgetcalculator/">monthly calculator</a>.</span></p>
<p class="ld-disc">{e(DISC)}</p></div></section></div>
<script type="application/json" id="ld-data">{json.dumps(data,ensure_ascii=False)}</script>
<script src="/assets/lead.js?v={lv}" defer></script><script src="/assets/lowdp.js?v={jv}" defer></script>'''
    page("/lowest-down-payment/","Unlock Lowest Down up to Zero Downpayment Promos | Mitsubishi Motors - San Juan Motors",
      "Lowest down payment range for every Mitsubishi, from ₱0 on select units, plus a standard amortization estimator. Pre-qualified only, subject to bank approval.",
      body,crumbs=[("/","Home"),("/promos/","Promos"),("/lowest-down-payment/","Lowest Down Payment")])
