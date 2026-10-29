# /promos/ Option A / Option B (2026-10-29, Richard): every unit shows two options.
# Option A = lowest DP + monthly (LOCKED until the visitor unlocks with name/mobile/email+consent; one unlock reveals all units).
# Option B = 30% DP + low monthly, public (same figures as the saved replies). Source: /workspace/loanapp/pricelist/optionAB.json (Oct 2026).
import json, hashlib, base64, os
SRC="/workspace/loanapp/pricelist/optionAB.json"
CACHE=os.path.join(os.path.dirname(__file__),"optionAB_oct2026.json")
FAM=[("Mirage Hatchback","mirage","Mirage"),("Mirage G4","mirage-g4","Mirage G4"),("Xpander","xpander","Xpander"),("Xpander Cross","xpander-cross","Xpander Cross"),
 ("Xforce","xforce","Xforce"),("Destinator","destinator","Destinator"),("Triton","triton","Triton"),("Montero Sport","montero-sport","Montero Sport"),
 ("L300","l300","L300"),("Versa Van","versa-van","Versa Van"),("Outlander PHEV","outlander-phev","Outlander PHEV")]
# Richard's lowest-DP range per family (2026-10-29). Mirage hatchback / Xpander Cross unknown -> no range line.
RANGE={"mirage-g4":(0,18000),"xpander":(18000,33000),"xforce":(18000,48000),"destinator":(0,33000),"triton":(0,18000),
 "montero-sport":(0,33000),"l300":(18000,53000),"versa-van":(18000,48000),"outlander-phev":(68000,183000)}
# fuel points only where the current site already shows the same figure
FUEL={"Xpander GLX 1.5G 2WD M/T":30000,"L300 FB BODY WITHDUAL AC 2.2D M/T":20000}
NICE={"L300 CAB & CHASIS 2.2D M/T":"L300 Cab & Chassis 2.2D M/T","L300 FB BODY WITH SINGLE AC 2.2D M/T":"L300 FB Body Single AC 2.2D M/T",
 "L300 FB BODY WITHDUAL AC 2.2D M/T":"L300 FB Body Dual AC 2.2D M/T","OUTLANDER PHEV GT 2.4G AWD":"Outlander PHEV GT 2.4G AWD"}
# card photos (2026-10-29): same image each /cars/ page uses per variant; Mirage hatchback has none -> no photo
IMG={"Mirage G4 GLX 1.2G M/T":"mg4glx_u17","Mirage G4 GLX 1.2G CVT":"mg4glx_a66","Mirage G4 GLS 1.2G CVT":"mg4gls_u17",
 "Xpander GLX 1.5G 2WD M/T":"xpglx_u33","Xpander GLX 1.5G 2WD A/T":"xpglx_x37","Xpander GLS 1.5G 2WD A/T":"xpgls_c31",
 "Xpander Cross 1.5G 2WD A/T (Two-Tone)":"xc_x3n","XFORCE GLX 1.5G 2WD CVT":"xf_glx","XFORCE GLS 1.5G 2WD CVT (Monotone)":"xf_gls",
 "XFORCE GLS 1.5G 2WD CVT (Two-Tone)":"xf_gls","XFORCE GT 1.5G 2WD CVT":"xf_gt","Destinator GLX 1.5G Turbo 2WD CVT":"de_p26",
 "Destinator GLS 1.5G Turbo 2WD CVT":"de_d34","Destinator GT 1.5G Turbo 2WD CVT (Monotone)":"de_jh3","Destinator GT 1.5G Turbo 2WD CVT (Two-Tone)":"de_x3n",
 "Triton GL 2.4D 2WD M/T":"tr_gl","Triton GX 2.4D 2WD A/T":"tr_gx_u28","Triton GLX 2.4D 2WD M/T":"tr_glx","Triton GLX 2.4D 2WD A/T":"tr_glx",
 "Triton GLS 2.4D 2WD A/T":"tr_gls","Triton GL 2.4D 4WD M/T":"tr_gl","Triton GLX 2.4D 4WD M/T":"tr_glx","Triton Athlete 2.4D 4WD A/T":"tr_lineup",
 "Montero Sport GLX 2.4D 2WD M/T":"ms_silver","Montero Sport GLS 2.4D 2WD A/T":"ms_white","Montero Sport Black Series 2.4D 2WD A/T":"msbs_jh3",
 "Montero Sport Black Series 2.4D 4WD A/T":"msbs_x8w","L300 CAB & CHASIS 2.2D M/T":"l300_fb","L300 FB BODY WITH SINGLE AC 2.2D M/T":"l300_fb",
 "L300 FB BODY WITHDUAL AC 2.2D M/T":"l300_fb","Versa Van GLX 2.5D 2WD M/T":"vv_glx","Versa Van GLX 2.5D 2WD M/T (UPGRADED) 18 SEATER":"vv_glx",
 "OUTLANDER PHEV GT 2.4G AWD":"op_gt"}
def rows():
    p=SRC if os.path.exists(SRC) else CACHE
    d=json.load(open(p))
    if p==SRC: json.dump(d,open(CACHE,"w"),ensure_ascii=False,indent=1)
    return [r for r in d if not any(k in r["unit"] for k in ("Quartz White","White Diamond","(White)"))]  # base colors, like the saved replies
def build(page,e,f,R,hero_cta,ALLIN_HTML,FREE_HTML,NOTE,MSG):
    rs=rows(); A=[]; EAG=[0]; secs=""; nav=[]
    for fam,slug,name in FAM:
        vs=[r for r in rs if r["family"]==fam]
        if not vs: continue
        nav.append(f'<a href="#{slug}">{e(name)}</a>')
        rg=RANGE.get(slug)
        if rg and rg[0]==0:  # Richard 2026-10-29: show "Zero DP Promo" instead of ₱0 (still subject to approval)
            rl=f'<p class="ab-rng"><b class="ab-z">Zero DP Promo</b><span class="en">, up to <b>{f(rg[1])}</b> DP</span><span class="tl">, hanggang <b>{f(rg[1])}</b> DP</span> <small class="muted">· <span class="en">Pre-qualified, subject to bank approval</span><span class="tl">Pre-qualified, subject to bank approval</span></small></p>'
        else:
            rl=f'<p class="ab-rng"><span class="en">Lowest DP range</span><span class="tl">Lowest DP range</span> <b>{f(rg[0])} – {f(rg[1])}</b></p>' if rg else ""
        cards=""
        for r in vs:
            i=len(A); A.append([r["a_dp"],r["a_mo"]]); n=NICE.get(r["unit"],r["unit"].replace("XFORCE","Xforce"))
            fu=f'<p class="fuel"><span class="en">Plus <b>{FUEL[r["unit"]]:,} fuel points</b></span><span class="tl">May <b>{FUEL[r["unit"]]:,} fuel points</b></span></p>' if r["unit"] in FUEL else ""
            im=IMG.get(r["unit"]); ph=""
            if im:
                EAG[0]+=1
                w,h=__import__("PIL.Image",fromlist=["x"]).open(f"{R}/assets/img/{im}.webp").size
                iv=hashlib.md5(open(f"{R}/assets/img/{im}.webp","rb").read()).hexdigest()[:8]
                ph=f'<div class="ab-ph"><img src="/assets/img/{im}.webp?v={iv}" width="{w}" height="{h}" alt="Mitsubishi {e(n)}" {'fetchpriority="high"' if EAG[0]<=3 else 'loading="lazy"'} decoding="async"></div>'
            cards+=f'''<article class="card pad pcard ab">{ph}<h3>{e(n)}</h3><p class="srp">SRP <b>{f(r["srp"])}</b></p>
<div class="ab-o ab-a" data-a="{i}"><p class="ab-k">Option A <span class="en">· Lowest DP</span><span class="tl">· Pinakamababang DP</span></p><div class="ab-v"><span class="ab-dp">DP <b class="ab-x">₱••,•••</b></span><span class="ab-mo"><b class="ab-x">₱••,•••</b><small>/mo</small></span></div><button type="button" class="ab-ul" data-unlock><span class="en">🔒 Unlock</span><span class="tl">🔒 I-unlock</span></button></div>
<div class="ab-o ab-b"><p class="ab-k">Option B <span class="en">· Low monthly</span><span class="tl">· Mababang monthly</span></p><div class="ab-v"><span class="ab-dp">DP <b>{f(r["b_dp"])}</b></span><span class="ab-mo"><b>{f(r["b_mo"])}</b><small>/mo</small></span></div></div>
{fu}<p class="muted ab-s"><span class="en">60 months, all-in. Pre-qualified, subject to bank approval.</span><span class="tl">60 months, all-in. Pre-qualified, subject to bank approval.</span></p><p class="row"><a class="btn sm" href="/budgetcalculator/">Compare with my own DP</a> <a class="btn sm ghost dk" href="/loan-assessment/">Check my chances</a></p></article>'''
        secs+=f'<section class="pm" id="{slug}"><h2>{e(name)}</h2>{rl}<div class="grid g3">{cards}</div></section>'
    blob=base64.b64encode(json.dumps(A).encode()).decode()
    lv=hashlib.md5(open(R+"/assets/lead.js","rb").read()).hexdigest()[:8]
    jv=hashlib.md5(open(R+"/assets/promos.js","rb").read()).hexdigest()[:8]
    css='''<style>html[data-lang=tl] .abw .en,html:not([data-lang=tl]) .abw .tl{display:none!important}
.ab-lang{display:flex;gap:8px;margin:0 0 14px}.ab-lang button{background:none;border:1px solid #52525b;color:inherit;border-radius:999px;padding:8px 14px;min-height:40px;font:inherit;font-size:14px;cursor:pointer}html[data-lang=tl] .ab-lang [data-setlang=tl],html:not([data-lang=tl]) .ab-lang [data-setlang=en]{background:#0b0b0c;color:#fff}
.ab-ph{margin:-4px -4px 12px;aspect-ratio:3/2;background:#fff;border-radius:10px;overflow:hidden;display:flex;align-items:center;justify-content:center}.ab-ph img{width:100%;height:100%;object-fit:contain;display:block}
.ab-rng{margin:-4px 0 14px;font-size:15px;color:#3f3f46}.ab-rng b{color:var(--redd);white-space:nowrap}
.ab-o{border:1px solid var(--ln);border-radius:12px;padding:12px 14px;margin:0 0 10px;position:relative}.ab-a{background:linear-gradient(135deg,#0b0b0c,#27272a);color:#fff;border:0}
.ab-k{margin:0 0 6px;font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--redd)}.ab-a .ab-k{color:#fca5a5}
.ab-v{display:flex;justify-content:space-between;align-items:baseline;gap:8px;flex-wrap:wrap}.ab-dp{font-size:15px}.ab-mo b{font-size:22px}.ab-mo small{font-weight:400;opacity:.7}
.ab-x{filter:blur(6px);user-select:none}html.ab-open .ab-x{filter:none}html.ab-open .ab-ul{display:none}
.ab-ul{margin-top:10px;width:100%;background:var(--red);color:#fff;border:0;border-radius:999px;padding:10px 14px;min-height:44px;font:inherit;font-size:15px;font-weight:700;cursor:pointer}.ab-ul:hover{background:var(--redd)}
.ab-s{font-size:13px}.ab-box{border-left:5px solid var(--red)}.ab-box .chk{font-size:14px;display:flex;gap:10px;align-items:flex-start;margin:6px 0 14px}.ab-box .chk input{width:20px;height:20px;flex:none;margin-top:2px}.ab-box .ferr{color:#b8000e;font-size:13px;margin:4px 0 0}
.ab-ok{background:#f0fdf4;border:1px solid #bbf7d0;border-radius:14px;padding:16px}.ab-btn{width:100%;font-size:17px}.ab-fg{display:grid;gap:0 16px}@media(min-width:900px){.ab-fg{grid-template-columns:1fr 1fr 1fr}}.ab-fg>*{min-width:0}
html.ab-open .ab-lockonly{display:none}html:not(.ab-open) .ab-openonly{display:none}</style>
<script>try{if(localStorage.getItem("promos_optA_unlocked")==="1")document.documentElement.classList.add("ab-open")}catch(_){}</script>'''
    form=f'''<section class="sec" id="unlock" style="padding-bottom:0"><div class="w"><div class="card pad ab-box">
<div class="ab-lockonly"><h2 class="h3" style="margin:0 0 6px"><span class="en">Unlock Option A: the lowest down payment for every unit</span><span class="tl">I-unlock ang Option A: pinakamababang down payment ng bawat unit</span></h2>
<p class="muted" style="margin:0 0 12px"><span class="en">Option B is shown below for every unit. Leave your details once to reveal Option A (lowest DP and monthly, including Zero DP Promo on select units) on all units.</span><span class="tl">Nakalista sa baba ang Option B ng bawat unit. Iwan ang details mo isang beses para makita ang Option A (lowest DP at monthly, kasama ang Zero DP Promo sa piling units) ng lahat ng unit.</span></p>
<form id="ab-form" novalidate><div class="ab-fg">
<div class="fld"><label for="ab-name"><span class="en">Full name</span><span class="tl">Buong pangalan</span></label><input id="ab-name" autocomplete="name" required><p class="ferr" id="e_ab-name" hidden><span class="en">Please enter your name.</span><span class="tl">Pakilagay ang pangalan mo.</span></p></div>
<div class="fld"><label for="ab-mobile">Mobile number</label><input id="ab-mobile" type="tel" inputmode="tel" autocomplete="tel" placeholder="09XX XXX XXXX" required><p class="ferr" id="e_ab-mobile" hidden><span class="en">Enter a valid mobile number (09XXXXXXXXX).</span><span class="tl">Maglagay ng tamang mobile number (09XXXXXXXXX).</span></p></div>
<div class="fld"><label for="ab-email">Email</label><input id="ab-email" type="email" autocomplete="email" required><p class="ferr" id="e_ab-email" hidden><span class="en">Enter a valid email.</span><span class="tl">Maglagay ng tamang email.</span></p></div></div>
<label class="chk"><input type="checkbox" id="ab-consent"><span><span class="en">I agree to be contacted by Richard Cuagdan of Mitsubishi San Juan Motors about these promos, and to the <a href="/privacy/">privacy policy</a>.</span><span class="tl">Pumapayag akong i-contact ni Richard Cuagdan ng Mitsubishi San Juan Motors tungkol sa promos na ito, at sa <a href="/privacy/">privacy policy</a>.</span></span></label>
<p class="ferr" id="e_ab-consent" hidden><span class="en">Please tick the consent box.</span><span class="tl">Paki-check ang consent box.</span></p>
<button class="btn ab-btn" id="ab-btn" type="submit"><span class="en">Unlock Option A</span><span class="tl">I-unlock ang Option A</span></button>
<p class="muted ab-s" style="margin-top:10px">Pre-qualified, subject to bank approval. Rates, promos and DP may change without prior notice.</p></form></div>
<div class="ab-openonly ab-ok" id="ab-ok" aria-live="polite"><p style="margin:0"><b><span class="en">Option A is unlocked for every unit.</span><span class="tl">Na-unlock na ang Option A ng bawat unit.</span></b> <span class="en">Richard can send the exact all-in computation for your chosen unit.</span><span class="tl">Puwedeng i-send ni Richard ang eksaktong all-in computation ng unit na gusto mo.</span></p><p class="muted ab-s" style="margin:6px 0 0">Pre-qualified, subject to bank approval.</p></div>
</div></div></section>'''
    body=css+f'''<div class="abw"><section class="ph"><div class="w"><div class="ab-lang" role="group" aria-label="Language / Wika"><button type="button" data-setlang="en">English</button><button type="button" data-setlang="tl">Taglish</button></div>
<p class="kick">October 2026</p><h1><span class="en">Mitsubishi promos this month</span><span class="tl">Mitsubishi promos ngayong buwan</span></h1><p class="lead"><span class="en">Every unit comes with two all-in options on 60 months: <b>Option A</b>, the lowest down payment (unlock to see), and <b>Option B</b>, a 30% down payment with a lower monthly.</span><span class="tl">Bawat unit may dalawang all-in option sa 60 months: <b>Option A</b>, ang pinakamababang down payment (i-unlock para makita), at <b>Option B</b>, 30% down payment na mas mababa ang monthly.</span></p>
{hero_cta("#list",src="promos")}</div></section>
{form}
<section class="sec" id="list"><div class="w"><nav class="pnav" aria-label="Jump to model">{" ".join(nav)}</nav>
{secs}
<p class="note">{NOTE}</p><p class="muted"><span class="en">Other down payment options: </span><span class="tl">Ibang DP options: </span><a href="{MSG}" rel="noopener" data-msgr="promos-other">message Richard on Messenger</a>.</p></div></section>
<section class="sec alt"><div class="w"><h2>How to use this month's promo</h2><ol class="psteps"><li><b>Pick a unit and Option A or B</b> above.</li><li><b>Estimate your own plan</b> with the <a href="/budgetcalculator/">monthly calculator</a> (standard formula: (SRP − DP) × add-on rate ÷ months; 5 years at 1.55).</li><li><b>Check your chances</b> with the free <a href="/loan-assessment/">Loan Application Assessment</a> (Pre-qualified, subject to bank approval).</li><li><b>Apply or ask</b>: <a href="/apply/">apply online</a> or <a href="{MSG}" rel="noopener" data-msgr="promos-steps">message Richard on Messenger</a>.</li></ol></div></section>
<section class="sec"><div class="w split"><div><h2>All-in includes</h2>{ALLIN_HTML}</div><div><h2>Freebies</h2>{FREE_HTML}</div></div></section></div>
<script type="text/plain" id="ab-a">{blob}</script>
<script src="/assets/lead.js?v={lv}" defer></script><script src="/assets/promos.js?v={jv}" defer></script>'''
    page("/promos/","October 2026 Promos | Mitsubishi Motors - San Juan Motors",
     "October 2026 Mitsubishi promos from San Juan Motors: two all-in options per unit on 60 months, lowest down payment or a lower monthly, with freebies. Subject to bank approval.",
     body, crumbs=[("/","Home"),("/promos/","Promos")])
    return [r["unit"] for r in rs]
