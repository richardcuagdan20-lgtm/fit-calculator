from data import PROMO_LABEL as _PL  # promo month (data.py)
# Wave 1-4 (DRAFT, branch draft-wave1, Nov 2026): hubs, model page upgrades, new and refreshed articles, site-wide design helpers.
# exec()'d inside build.py right before the model pages (uses page, img, e, f, MODELS, MSG, D, POSTS, FIGS, CALC, offers_ld, rx_alt ...).
# House rules: English only; low DP wording only; "Pre-qualified, subject to bank approval"; fuel points without a peso sign;
# Mitsubishi specs only as "according to Mitsubishi Motors" (MANUFACTURER_CLAIMS.md); no competitor prices; prices = Oct 2026 list (FRESH).
import re as _w_re
from drafts import BY
W_MOD="2026-11-05"
MSQ="Pre-qualified, subject to bank approval"
WM={m["slug"]:m for m in MODELS}
W_PATHS=[]  # every new or changed URL (scrubbed + checked)
def W_badge(): return f'<p class="fresh"><span>{e(FRESH)}</span></p>'
def W_short(v,m): return v["n"] if v["n"].startswith(m["name"]+" Cross") else v["n"].replace(m["name"]+" ","",1)  # Xpander Cross stays "Xpander Cross ..." (variant of the Xpander since 2026-11-15)
def W_trans(n):
    t="CVT" if "CVT" in n else "Automatic" if "A/T" in n else "Manual" if "M/T" in n else "Automatic"
    d="AWD" if "AWD" in n else "4WD" if "4WD" in n else "2WD"
    return t,d
def W_low(v):
    """lowest published promo option that has a down payment: (dp, monthly) or None"""
    ab=v.get("ab") or {}
    for dp,mo in ((ab.get("a_dp"),ab.get("a_mo")),(ab.get("b_dp"),ab.get("b_mo"))):
        if dp and mo: return dp,mo
    return None
def W_msg(slug,place,variant="",cls="btn sm ghost dk",label="Message Richard"):
    return f'<a class="{cls}" href="{MSG}" rel="noopener" data-inquire="{e(place)}" data-msgr="{e(slug)}-{e(place)}" data-track="msg" data-place="{e(place)}" data-variant="{e(variant)}">{label}</a>'
def W_pq(slug,place,cls="btn sm",label="Pre-qualify in 2 minutes"):
    return f'<a class="{cls}" href="/loan-assessment/?src={e(slug)}-{e(place)}" data-track="pq" data-model="{e(slug)}">{label}</a>'
def W_vtable(slug,place="variant-row"):
    m=WM[slug];rows=""
    for v in m["variants"]:
        t,d=W_trans(v["n"]);lo=W_low(v);fu=(v["promo"] or {}).get("fuel")
        dp=f(lo[0]) if lo else "Ask Richard";mo=(f'<b>{f(lo[1])}</b>/mo' if lo else "Ask Richard")
        fz=f'<br><small class="fpts">+ {fu:,} fuel points</small>' if fu else ""
        rows+=f'<tr><th scope="row">{e(W_short(v,m))}</th><td>{t}</td><td>{d}</td><td>{f(v["srp"])}</td><td>{dp}</td><td>{mo}{fz}</td><td>{W_msg(slug,place,v["n"],label="Ask about this")}</td></tr>'
    return (f'<div class="tw"><table class="pt vtab"><thead><tr><th scope="col">Variant</th><th scope="col">Transmission</th><th scope="col">Drive</th><th scope="col">SRP</th><th scope="col">Low DP</th><th scope="col">Sample monthly</th><th scope="col">Message</th></tr></thead><tbody>{rows}</tbody></table></div>'
            f'<p class="muted vnote">SRP from the official Mitsubishi Motors Philippines price list; freight and handling not included. Sample monthly: 60 months, all-in. {MSQ}. Promos change monthly; ask Richard for the current figures.</p>')
def W_ptab(slug,only=None):
    m=WM[slug];vs=[v for v in m["variants"] if (only is None or only in v["n"])]
    rows="".join(f'<tr><th scope="row">{e(W_short(v,m))}</th><td>{f(v["srp"])}</td><td>{f(W_low(v)[0]) if W_low(v) else "Ask Richard"}</td><td>{(f(W_low(v)[1])+"/mo") if W_low(v) else "Ask Richard"}</td></tr>' for v in vs)
    return f'{W_badge()}<div class="tw"><table class="pt"><thead><tr><th scope="col">Variant</th><th scope="col">SRP</th><th scope="col">Low DP</th><th scope="col">Sample monthly</th></tr></thead><tbody>{rows}</tbody></table></div><p class="muted">60 months, all-in. {MSQ}.</p>'
def W_from(slug): return f(srp_from(WM[slug]))
def W_FAQH(items):
    return '<section class="faqs" id="faq"><h2>Frequently asked questions</h2>'+"".join(f'<details class="faq"><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q,a in items)+'</section>'
def W_FAQLD(items): return {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in items]}
def W_vc(slug,ptype): return f'<div hidden data-vc data-model="{e(slug)}" data-ptype="{e(ptype)}"></div>'
def W_sbar(slug,label,frm=None):
    fr=f'<small>From {frm} ({e(FRESH_SHORT)})</small>' if frm else ""
    return (f'<div class="sbar" id="sbar" data-model="{e(slug)}"><div class="w sbi"><span class="sbm"><b>{e(label)}</b>{fr}</span>'
            +W_msg(slug,"sticky",cls="btn sm sbmsg")+W_pq(slug,"sticky",cls="btn sm ghost sbpq",label="Pre-qualify")+'</div></div>'
            '<script>(function(){var b=document.getElementById("sbar");if(!b)return;document.body.classList.add("has-sbar");var h=document.querySelector(".hd");'
            'function u(){var d=innerWidth>768;b.style.top=(d&&h)?h.offsetHeight+"px":"";b.classList.toggle("on",!d||scrollY>600)}'
            'function k(){var a=document.activeElement,f=a&&/^(INPUT|SELECT|TEXTAREA)$/.test(a.tagName),s=0;document.querySelectorAll("button[type=submit],form .btn").forEach(function(x){var r=x.getBoundingClientRect();if(x.offsetParent&&r.bottom>innerHeight-70&&r.top<innerHeight)s=1});b.classList.toggle("off",!!(f||s))}'
            'addEventListener("scroll",function(){u();k()},{passive:true});addEventListener("resize",u);document.addEventListener("focusin",k);document.addEventListener("focusout",function(){setTimeout(k,50)});u();k()})()</script>')
def W_trust(c="xpander"):
    b=f"/assets/img/richard/{c}-1x1-240"
    return (f'<section class="sec trust"><div class="w trs"><picture><source type="image/webp" srcset="{b}.webp"><img src="{b}.jpg" alt="{e(rx_alt(c))}" width="96" height="96" loading="lazy" decoding="async"></picture>'
            '<ul class="trl"><li><b>Richard Cuagdan</b>, authorized Mitsubishi sales executive, San Jose del Monte (SJDM)</li><li>'+MSQ+'</li><li>Replies personally on Messenger</li><li>Test drive in SJDM, Monday to Saturday</li></ul>'
            '<p class="row"><a class="btn sm ghost dk" href="/test-drive/">Book a test drive in SJDM</a></p></div></section>')
W_LOCAL='<p class="wloc">Buying in Bulacan? See <a href="/mitsubishi-sjdm-bulacan/">Mitsubishi San Jose del Monte (SJDM)</a>.</p>'
def W_cta(slug,name,unit=""):
    q=f"?unit={unit}" if unit else ""
    return (f'<h2>Your next step</h2><p>Compare the numbers, then see the {e(name)} in person in San Jose del Monte.</p>'
            f'<p class="row">{W_pq(slug,"article-end",cls="btn",label="Get my Pre-qualification (2 min)")} <a class="btn ghost dk" href="/budgetcalculator/">Compute my monthly</a> <a class="btn ghost dk" href="/test-drive/{q}">Book a test drive in SJDM</a></p>'
            f'<p class="row">{W_msg(slug,"article-end",cls="btn ghost dk",label="Message Richard about the "+e(name))}</p>{W_LOCAL}')
def W_cards(items):
    return '<div class="grid g3">'+"".join(f'<a class="card pad mc" href="{u}"><h3>{e(t)}</h3><p class="muted">{e(d)}</p></a>' for u,t,d in items)+'</div>'
def W_itemlist(name,items): return {"@type":"ItemList","name":name,"itemListElement":[{"@type":"ListItem","position":i+1,"url":D+u,"name":t} for i,(u,t,_) in enumerate(items)]}
def W_tiles(items): return '<div class="tiles">'+"".join(f'<div class="tile"><b>{e(a)}</b><span>{e(b)}</span></div>' for a,b in items)+'</div><p class="muted">According to Mitsubishi Motors Philippines.</p>'
def W_hero_extra(slug,name):
    return (f'<div class="pcard2"><p class="pfrom">SRP from <b>{W_from(slug)}</b></p>'
            f'<p class="row"><a class="btn sm" href="#calc">See my monthly</a></p></div>')
def W_vrow(slug,vid):
    v=next(x for x in WM[slug]["variants"] if x["id"]==vid);return v,W_low(v)

# ================= SPECS (MANUFACTURER_CLAIMS.md only)
SP_OP=[("Engine","2.4L 16-valve DOHC MIVEC (4B12) gasoline, 133 PS / 195 Nm"),("Front / rear motor","116 PS, 255 Nm / 136 PS, 195 Nm"),("Combined system output","306 PS, 450 N-m"),("Battery","Lithium-ion, 22.7 kWh"),("Pure electric range","Up to 100 km (no test cycle stated; actual range varies)"),("AC charging","AC Type 2; approx. 6.5 hours (230V-240V, 15A)"),("Drivetrain","All Wheel Drive with Super All-Wheel Control (S-AWC)"),("Fuel tank","53 L"),("Seating","5"),("Battery warranty","8 years or 160,000 km, whichever comes first")]
SP_DS=[("Engine","1.5L 4B40 turbocharged gasoline (Euro 4)"),("Max power / torque","163 PS / 250 N-m"),("Transmission / drive","CVT, 2WD (front-wheel drive)"),("Ground clearance","214 mm (best-in-class, per Mitsubishi Motors Philippines)"),("Drive modes","Normal, Wet, Gravel, Mud, Tarmac"),("Seating","7, three rows"),("Fuel tank / fuel","45 L, RON 95 and over")]
SP_MS=[("Engine","4N15 2.4L turbocharged direct injection diesel with MIVEC"),("Max power / torque","181 PS @ 3,500 rpm / 430 Nm @ 2,500 rpm"),("Transmission","8-speed automatic with Sport Mode; 6-speed manual (GLX)"),("4WD","Super Select 4WD-II (Black Series 4WD); other variants 2WD"),("Off-road (4WD)","Rear Differential Lock, Off-Road Mode, Hill Descent Control"),("Seating","7")]
SP_TR=[("Engine (Bi-Turbo)","4N16 2.4L diesel with Two-Stage Turbo: 204 PS, 470 Nm"),("Transmission","6-speed automatic or 6-speed manual (by variant)"),("4WD","Super Select 4WD-II with 7 drive modes (Athlete)"),("Safety rating","5-star, 2023 ASEAN NCAP"),("Fuel tank","75 L")]

# ================= MODEL PAGE UPGRADES (WUP, consumed by the model loop in build.py)
def W_related(items): return '<section class="sec"><div class="w"><h2>Related guides</h2>'+W_cards(items)+'</div></section>'
def W_calcsec(slug,name): return f'<section class="sec alt" id="calc"><div class="w"><h2>Compute your {e(name)} monthly</h2><p class="sub">Pick a variant, a down payment and a term. Estimate only; {MSQ}.</p>{CALC("model-"+slug)}</div></section>'
def W_vsec(slug,name): return f'<section class="sec" id="variants"><div class="w"><h2>{e(name)} variants, price and sample monthly</h2>{W_vtable(slug)}</div></section>'
FAQ_OP=[("How much is the Outlander PHEV in the Philippines?",f"The Outlander PHEV GT 2.4G AWD has an SRP of {W_from('outlander-phev')} ({FRESH}). Ask Richard for the current promo."),
 ("Is the Outlander PHEV a hybrid?","Yes. It is a plug-in hybrid (PHEV): according to Mitsubishi Motors, it pairs a 2.4L gasoline engine with front and rear electric motors and a 22.7 kWh battery you can charge from an outlet."),
 ("How far can the Outlander PHEV go on electricity?","According to Mitsubishi Motors Philippines, up to 100 km of pure electric range and almost 1,000 km combined. No test cycle is stated for these figures, and actual range varies with driving conditions."),
 ("How long does it take to charge?","According to Mitsubishi Motors, approximately 6.5 hours on AC (230V-240V, 15A). It supports the AC Type 2 charging protocol."),
 ("How many seats does the Outlander PHEV have?","Five, according to the Mitsubishi Motors Philippines brochure."),
 ("What is the battery warranty?","According to Mitsubishi Motors Philippines, 8 years or 160,000 km, whichever comes first."),
 ("Can I finance the Outlander PHEV?",f"Yes. Use the calculator or the 2-minute assessment. Results are {MSQ}."),
 ("Where can I test drive it near SJDM?","Book a test drive with Richard Cuagdan in San Jose del Monte (SJDM), Bulacan, Monday to Saturday.")]
FAQ_DS=[("How much is the Destinator?",f"SRP from {W_from('destinator')} for the GLX up to {f(1939000)} for the GT two-tone ({FRESH})."),
 ("What engine does the Destinator have?","According to Mitsubishi Motors Philippines, a 1.5L turbocharged gasoline engine (4B40) with 163 PS and 250 N-m, paired with a CVT."),
 ("How many seats does the Destinator have?","Seven, in three rows, according to Mitsubishi Motors Philippines."),
 ("Is the Destinator 4x4?","No. According to Mitsubishi Motors Philippines it is 2WD (front-wheel drive), with five drive modes including Gravel and Mud."),
 ("What is the Destinator ground clearance?","214 mm, which Mitsubishi Motors Philippines describes as best-in-class."),
 ("What is the lowest Destinator down payment?","See the variant table on this page for the low DP and sample monthly per variant. "+MSQ+"."),
 ("Can I test drive the Destinator in SJDM?","Yes. Book online and Richard will confirm your schedule in San Jose del Monte.")]
FAQ_MS=[("How much is the Montero Sport 2026?",f"SRP from {W_from('montero-sport')} (GLX 2WD M/T) to {f(2530000)} (Black Series 4WD A/T), {FRESH}."),
 ("Which Montero Sport is 4x4?","According to Mitsubishi Motors, the Black Series 4WD uses Super Select 4WD-II. The other variants are 2WD."),
 ("What engine does the Montero Sport have?","According to Mitsubishi Motors, a 4N15 2.4L turbo diesel with MIVEC: 181 PS and 430 Nm."),
 ("Is there a manual Montero Sport?","Yes, the GLX 2WD with a 6-speed manual. The other variants use an 8-speed automatic with Sport Mode."),
 ("How many seats does the Montero Sport have?","Seven, according to Mitsubishi Motors."),
 ("What is the Montero Sport monthly amortization?","See the variant table for the low DP and sample monthly per variant (60 months, all-in). "+MSQ+"."),
 ("Can I test drive a Montero Sport in SJDM?","Yes. Book a test drive with Richard in San Jose del Monte, Monday to Saturday.")]
FAQ_TR=[("How much is the Triton 2026?",f"SRP from {W_from('triton')} (GL 2WD M/T) to {f(2359000)} (Athlete 4WD A/T), {FRESH}."),
 ("How powerful is the Triton?","According to Mitsubishi Motors, the 2.4L Bi-Turbo diesel produces 204 PS and 470 Nm."),
 ("Is the Triton safe?","According to Mitsubishi Motors, the Triton earned a 5-star rating in the 2023 ASEAN NCAP."),
 ("Which Triton is automatic?","The GX 2WD, GLX 2WD A/T, GLS 2WD and Athlete 4WD come with an automatic; the GL and the other GLX variants are manual."),
 ("Which Triton is 4x4?","The GL 4WD M/T, GLX 4WD M/T and Athlete 4WD A/T. According to Mitsubishi Motors, the Athlete uses Super Select 4WD-II with 7 drive modes."),
 ("What is the Triton monthly installment?","See the variant table for the low DP and sample monthly per variant (60 months, all-in). "+MSQ+"."),
 ("Can a business owner finance a Triton?","Yes. Banks usually ask for business registration, permits, ITR or financial statements and bank statements.")]
WUP={
"outlander-phev":dict(title="Mitsubishi Outlander PHEV 2026 | SJDM San Jose del Monte",h1="Mitsubishi Outlander PHEV Plug-in Hybrid SUV",
 desc="Outlander PHEV GT AWD plug-in hybrid: 306 PS system output according to Mitsubishi Motors, Oct 2026 price, monthly. San Jose del Monte (SJDM).",
 specs=SP_OP,faq=FAQ_OP,c="xpander",
 rel=[("/mitsubishi-hybrid-phev/","How a Mitsubishi PHEV works","Plug-in hybrid explained"),("/blog/outlander-phev-price-philippines/","Outlander PHEV price Philippines","Price, low DP and monthly"),("/blog/outlander-phev-range-and-charging/","PHEV range and charging","Battery, range, charging time"),("/blog/outlander-phev-vs-montero-sport/","Outlander PHEV vs Montero Sport","Plug-in hybrid or diesel")]),
"destinator":dict(title="Destinator 2026 Variants & Promo | SJDM Bulacan",h1="Mitsubishi Destinator 2026 Variants, Promo & Monthly",
 desc="Destinator GLX, GLS, GT: Oct 2026 list prices, low DP and monthly, Pre-qualified, subject to bank approval. San Jose del Monte (SJDM).",
 specs=SP_DS,faq=FAQ_DS,c="destinator",
 rel=[("/destinator/","Destinator guide","Everything to know before you buy"),("/blog/destinator-price-philippines/","Destinator price Philippines","DP and monthly per variant"),("/blog/destinator-glx-vs-gls-vs-gt/","GLX vs GLS vs GT","Which variant fits you"),("/blog/destinator-vs-xforce/","Destinator vs XForce","Seats, size and features"),("/blog/destinator-fuel-consumption/","Destinator fuel consumption","Engine facts and saving tips"),("/blog/xpander-vs-destinator-family-car/","Xpander vs Destinator","Family car comparison")]),
"montero-sport":dict(title="Montero Sport 2026 Variants & Promo | SJDM Bulacan",h1="Mitsubishi Montero Sport 2026: Variants and Promo",
 desc="Montero Sport 2026 GLX, GLS, Black Series 2WD and 4WD: Oct 2026 prices and monthly, Pre-qualified, subject to bank approval. SJDM.",
 specs=SP_MS,faq=FAQ_MS,c="xpander",
 rel=[("/blog/montero-sport-price-philippines-2026/","Montero Sport price Philippines","DP and monthly per variant"),("/blog/montero-sport-black-series/","Black Series","2WD vs 4WD and what you get"),("/blog/montero-sport-vs-fortuner/","Montero Sport vs Fortuner","Features compared"),("/blog/montero-sport-fuel-consumption/","Montero Sport fuel consumption","Engine facts and tips"),("/blog/montero-sport-variants-explained/","GLX vs GLS vs Black Series","Variants explained"),("/blog/montero-sport-vs-destinator/","Montero Sport vs Destinator","Diesel SUV or turbo 7-seater"),("/tips/montero-sport-vs-triton/","Montero Sport vs Triton","SUV or pickup")]),
"triton":dict(title="Triton 2026 Variants & Promo | SJDM San Jose del Monte",h1="Mitsubishi Triton 2026: Variants, Promo and Monthly",
 desc="Triton GL to Athlete: 204 PS Bi-Turbo according to Mitsubishi Motors, Oct 2026 prices, monthly, Pre-qualified, subject to bank approval. SJDM.",
 specs=SP_TR,faq=FAQ_TR,c="xpander",
 rel=[("/blog/triton-price-philippines/","Triton price Philippines","Every variant, DP and monthly"),("/triton-downpayment-and-monthly/","Triton monthly installment","Down payment and monthly guide"),("/blog/triton-gx-2wd-at-first-pickup-guide/","Triton GX 2026","First pickup guide"),("/blog/triton-vs-hilux/","Triton vs Hilux","Pickup features compared"),("/blog/triton-for-business-and-farm/","Triton for business and farm","Work and farm use")]),
}
for _s,_u in WUP.items():
    _m=WM[_s]
    _u["hero_extra"]=W_hero_extra(_s,_m["name"])
    _u["top"]=W_vsec(_s,_m["name"])+W_calcsec(_s,_m["name"])
    _u["tail"]=W_trust(_u["c"])+W_related(_u["rel"])+'<section class="sec"><div class="w nar">'+W_FAQH(_u["faq"])+W_LOCAL+'</div></section>'
    _u["after"]=W_vc(_s,"model")+W_sbar(_s,_m["name"],W_from(_s))
    _u["ld"]=[W_FAQLD(_u["faq"])]
    W_PATHS.append(f"/cars/{_s}/")
_MG["outlander-phev"]=[("/mitsubishi-hybrid-phev/","How a Mitsubishi PHEV works")]+_MG.get("outlander-phev",[])
_MG["destinator"]=[("/destinator/","Destinator guide")]+_MG.get("destinator",[])

# ================= HUB: /destinator/
_dm=WM["destinator"]
DS_ART=[("/blog/destinator-price-philippines/","Destinator price Philippines","Price, DP and monthly per variant"),("/blog/destinator-vs-xforce/","Destinator vs XForce","Seats, size and features"),("/blog/destinator-fuel-consumption/","Destinator fuel consumption","Engine facts and saving tips"),("/blog/destinator-glx-vs-gls-vs-gt/","GLX vs GLS vs GT","Which variant fits you"),("/blog/xpander-vs-destinator-family-car/","Xpander vs Destinator","Family car comparison"),("/blog/montero-sport-vs-destinator/","Montero Sport vs Destinator","Diesel SUV or turbo 7-seater")]
DS_FAQ=FAQ_DS[:5]+[("What is the difference between GLX, GLS and GT?","All three share the 1.5L turbo and CVT. According to Mitsubishi Motors Philippines, the GT adds Forward Collision Mitigation (FCM). See the GLX vs GLS vs GT guide for details."),
 ("What fuel does the Destinator use?","According to Mitsubishi Motors Philippines, gasoline RON 95 and over, with a 45 L tank."),
 ("Does the Destinator have safety tech?","According to Mitsubishi Motors Philippines: Mitsubishi Motors Safety Sensing (MMSS), Multi-Around Monitor, Active Stability Control and Active Yaw Control, with FCM on the GT."),
 ("Can I get a Destinator with a low down payment?","Yes. The variants page shows the low DP and sample monthly per variant. "+MSQ+"."),
 ("Where can I see the Destinator near SJDM?","Message Richard Cuagdan, authorized Mitsubishi sales executive in San Jose del Monte (SJDM), to view and test drive a unit.")]
_dsrows="".join(f'<a class="card pad mc" href="/cars/destinator/#variants"><p class="kick">{e(W_short(v,_dm).split(" ")[0])}</p><h3>{e(W_short(v,_dm))}</h3><p class="low">SRP <b>{f(v["srp"])}</b></p></a>' for v in _dm["variants"][:3])
page("/destinator/","Mitsubishi Destinator 2026 Guide | SJDM Bulacan",
 "Mitsubishi Destinator 7-seater SUV guide: variants, specs, price links and test drive in San Jose del Monte (SJDM), Bulacan. Pre-qualify online.",
f'''<section class="ph"><div class="w hgrid"><div><p class="kick">Destinator · 7-seater SUV · SJDM</p><h1>Mitsubishi Destinator: Everything to Know Before You Buy</h1>
<p class="lead">According to Mitsubishi Motors Philippines, the Destinator is a 7-seater SUV with a 1.5L turbo engine (163 PS, 250 N-m) and 214 mm ground clearance. Here is everything in one place, from Richard Cuagdan, authorized Mitsubishi sales executive in San Jose del Monte (SJDM).</p>
<p class="row"><a class="btn" href="/cars/destinator/">See Destinator variants and promo</a> {W_msg("destinator","hero",cls="btn ghost dk")}</p></div>{img("de_x3n","Mitsubishi Destinator 7-seater SUV",eager=True,cls="himg")}</div></section>
<section class="sec"><div class="w"><h2>Destinator quick facts</h2>{W_tiles([("7 seats","Three rows"),("163 PS / 250 N-m","1.5L 4B40 turbo"),("214 mm","Ground clearance"),("5 drive modes","Normal, Wet, Gravel, Mud, Tarmac"),("CVT, 2WD","Front-wheel drive"),("45 L tank","RON 95 and over")])}</div></section>
<section class="sec alt"><div class="w"><h2>Which Destinator variant fits you?</h2><p class="sub">Same engine and CVT across the range; trim, comfort and safety features change. Read <a href="/blog/destinator-glx-vs-gls-vs-gt/">GLX vs GLS vs GT</a>.</p><div class="grid g3">{_dsrows}</div></div></section>
<section class="sec"><div class="w"><h2>Destinator guides</h2>{W_cards(DS_ART)}</div></section>
<section class="sec alt"><div class="w"><div class="card pad mini"><h2 class="h3">Destinator price</h2><p class="pfrom">SRP from <b>{W_from("destinator")}</b></p>{W_badge()}<p>Low DP and a sample monthly for every variant are on the variants page. {MSQ}.</p><p class="row"><a class="btn" href="/cars/destinator/">See Destinator variants and promo</a> <a class="btn ghost dk" href="/blog/destinator-price-philippines/">Destinator price Philippines</a></p></div></div></section>
{W_trust("destinator")}
<section class="sec"><div class="w nar">{W_FAQH(DS_FAQ)}
<div class="box"><h2 class="h3">Ready to see one?</h2><p class="row">{W_pq("destinator","hub-end",cls="btn",label="Get my Pre-qualification (2 min)")} <a class="btn ghost dk" href="/test-drive/?unit=destinator">Book a test drive in SJDM</a></p>{W_LOCAL}</div></div></section>
{W_vc("destinator","hub")}{W_sbar("destinator","Destinator",W_from("destinator"))}''',
 ld=[{"@type":"WebPage","@id":D+"/destinator/","name":"Mitsubishi Destinator: Everything to Know Before You Buy","url":D+"/destinator/","about":{"@id":D+"/#dealer"},"dateModified":W_MOD},W_itemlist("Destinator guides",DS_ART)]+offers_ld(_dm)+[W_FAQLD(DS_FAQ)],
 img="/assets/img/de_x3n.webp",og=rx_og("destinator"),crumbs=[("/","Home"),("/destinator/","Destinator")])
W_PATHS.append("/destinator/")

# ================= HUB: /mitsubishi-hybrid-phev/
PH_ART=[("/cars/outlander-phev/","Mitsubishi Outlander PHEV","Variant, promo and test drive"),("/blog/outlander-phev-price-philippines/","Outlander PHEV price","Price, low DP and monthly"),("/blog/outlander-phev-range-and-charging/","PHEV range and charging","Battery, range, charging"),("/blog/outlander-phev-vs-montero-sport/","PHEV vs diesel Montero Sport","Which SUV fits you")]
PH_FAQ=[("Does Mitsubishi sell a hybrid in the Philippines?","Yes. According to Mitsubishi Motors Philippines, the Outlander PHEV is the brand's first Plug-in Hybrid Electric Vehicle (PHEV) in the Philippine market."),
 ("What is the difference between a hybrid and a plug-in hybrid?","A conventional hybrid charges its small battery only while driving. A plug-in hybrid (PHEV) has a larger battery you can also charge from an outlet, so it can drive on electricity alone for everyday trips."),
 ("How far can the Outlander PHEV drive on electricity?","According to Mitsubishi Motors Philippines, up to 100 km of pure electric range and almost 1,000 km combined. No test cycle is stated, and actual range varies with driving conditions."),
 ("How do I charge a Mitsubishi PHEV?","According to Mitsubishi Motors, the Outlander PHEV supports AC Type 2 charging and takes approximately 6.5 hours on AC (230V-240V, 15A)."),
 ("Do I need to charge it to drive?","No. The 2.4L gasoline engine keeps the car going when the battery is low, so you can drive long trips without a charger."),
 ("How powerful is the Outlander PHEV?","According to Mitsubishi Motors, the combined system output is 306 PS and 450 N-m."),
 ("Is the Outlander PHEV all-wheel drive?","Yes. According to Mitsubishi Motors Philippines, it uses All Wheel Drive with Super All-Wheel Control (S-AWC)."),
 ("What is the battery warranty?","According to Mitsubishi Motors Philippines, 8 years or 160,000 km, whichever comes first."),
 ("How much is the Outlander PHEV?",f"SRP {W_from('outlander-phev')} for the GT 2.4G AWD ({FRESH})."),
 ("Can I test drive a Mitsubishi PHEV near SJDM?","Yes. Book with Richard Cuagdan, authorized Mitsubishi sales executive in San Jose del Monte (SJDM), Bulacan.")]
PH_SVG=('<figure class="fig phsvg"><svg viewBox="0 0 640 220" role="img" aria-label="How a plug-in hybrid works: charge from an outlet, the battery powers electric motors, the gasoline engine joins for long trips" width="640" height="220" style="width:100%;height:auto">'
 '<rect x="10" y="80" width="120" height="60" rx="10" fill="#f4f4f5" stroke="#0b0b0c"/><text x="70" y="115" text-anchor="middle" font-size="15" fill="#0b0b0c">AC outlet</text>'
 '<rect x="190" y="80" width="130" height="60" rx="10" fill="#fde8ea" stroke="#E60012"/><text x="255" y="108" text-anchor="middle" font-size="15" fill="#0b0b0c">Battery</text><text x="255" y="127" text-anchor="middle" font-size="12" fill="#6b6b73">22.7 kWh</text>'
 '<rect x="380" y="20" width="130" height="60" rx="10" fill="#fde8ea" stroke="#E60012"/><text x="445" y="47" text-anchor="middle" font-size="15" fill="#0b0b0c">Electric motors</text><text x="445" y="66" text-anchor="middle" font-size="12" fill="#6b6b73">front + rear</text>'
 '<rect x="380" y="140" width="130" height="60" rx="10" fill="#f4f4f5" stroke="#0b0b0c"/><text x="445" y="167" text-anchor="middle" font-size="15" fill="#0b0b0c">2.4L engine</text><text x="445" y="186" text-anchor="middle" font-size="12" fill="#6b6b73">gasoline</text>'
 '<rect x="560" y="80" width="70" height="60" rx="10" fill="#0b0b0c"/><text x="595" y="115" text-anchor="middle" font-size="14" fill="#fff">AWD</text>'
 '<path d="M130 110H186M320 100L376 55M320 120L376 165M510 50L556 100M510 170L556 120" stroke="#E60012" stroke-width="3" fill="none"/></svg>'
 '<figcaption class="muted">Simplified diagram. Battery capacity according to Mitsubishi Motors Philippines.</figcaption></figure>')
page("/mitsubishi-hybrid-phev/","Mitsubishi Hybrid & PHEV SUV Philippines | SJDM",
 "Mitsubishi PHEV SUV explained: how plug-in hybrid works, Outlander PHEV specs according to Mitsubishi Motors, and test drive in SJDM Bulacan.",
f'''<section class="ph"><div class="w hgrid"><div><p class="kick">Mitsubishi hybrid · PHEV SUV · SJDM</p><h1>Mitsubishi Hybrid and PHEV SUV in the Philippines</h1>
<p class="lead">According to Mitsubishi Motors Philippines, the Outlander PHEV is the brand's first Plug-in Hybrid Electric Vehicle in the Philippine market. It drives on electricity for everyday trips and uses its gasoline engine for long ones.</p>
<p class="row"><a class="btn" href="/cars/outlander-phev/">See the Outlander PHEV and price</a> {W_msg("outlander-phev","hero",cls="btn ghost dk")}</p></div>{img("op_gt","Mitsubishi Outlander PHEV plug-in hybrid SUV",eager=True,cls="himg")}</div></section>
<section class="sec"><div class="w"><h2>Outlander PHEV quick facts</h2>{W_tiles([("306 PS / 450 N-m","Combined system output"),("22.7 kWh","Lithium-ion battery"),("Up to 100 km","Pure electric range, no test cycle stated"),("AC Type 2","Approx. 6.5 hrs AC charging"),("S-AWC","All Wheel Drive"),("8 yrs / 160,000 km","Battery warranty")])}</div></section>
<section class="sec alt"><div class="w nar"><h2>How a plug-in hybrid works</h2>{PH_SVG}
<p>You charge the battery from an outlet at home or at a charging point. On everyday trips the electric motors drive the car. When the battery runs low, or when you need more power, the 2.4L gasoline engine joins in, so long trips need no charger. According to Mitsubishi Motors, the Outlander PHEV offers four EV drive modes: Normal, Save, Charge and EV Priority.</p>
<h2>PHEV vs hybrid</h2>
<div class="tw"><table class="pt"><thead><tr><th scope="col">Feature</th><th scope="col">Plug-in hybrid (PHEV)</th><th scope="col">Conventional hybrid</th></tr></thead><tbody>
<tr><th scope="row">Charge from an outlet</th><td>Yes</td><td>No</td></tr><tr><th scope="row">Drive on electricity alone</th><td>Yes, for everyday distances</td><td>Short distances only</td></tr><tr><th scope="row">Battery size</th><td>Larger</td><td>Smaller</td></tr><tr><th scope="row">Mitsubishi model in PH</th><td>Outlander PHEV</td><td>None listed by Mitsubishi Motors Philippines</td></tr></tbody></table></div>
<h2>Is a PHEV right for you?</h2>{W_cards([("/blog/outlander-phev-range-and-charging/","You can charge at home","Read range and charging"),("/blog/outlander-phev-vs-montero-sport/","You also want 7 seats or diesel","Compare with the Montero Sport"),("/blog/outlander-phev-price-philippines/","You want the numbers first","Outlander PHEV price")])}</div></section>
<section class="sec"><div class="w"><h2>Mitsubishi PHEV guides</h2>{W_cards(PH_ART)}</div></section>
<section class="sec alt"><div class="w"><div class="card pad mini"><h2 class="h3">Outlander PHEV price</h2><p class="pfrom">SRP <b>{W_from("outlander-phev")}</b></p>{W_badge()}<p class="row"><a class="btn" href="/cars/outlander-phev/">Mitsubishi Outlander PHEV</a> <a class="btn ghost dk" href="/blog/outlander-phev-price-philippines/">Outlander PHEV price</a></p></div></div></section>
{W_trust("xpander")}
<section class="sec"><div class="w nar">{W_FAQH(PH_FAQ)}
<div class="box"><h2 class="h3">Try electric driving in SJDM</h2><p class="row">{W_pq("outlander-phev","hub-end",cls="btn",label="Get my Pre-qualification (2 min)")} <a class="btn ghost dk" href="/test-drive/?unit=outlander-phev">Book a test drive in SJDM</a></p>{W_LOCAL}</div></div></section>
{W_vc("outlander-phev","hub")}{W_sbar("outlander-phev","Outlander PHEV",W_from("outlander-phev"))}''',
 ld=[{"@type":"WebPage","@id":D+"/mitsubishi-hybrid-phev/","name":"Mitsubishi Hybrid and PHEV SUV in the Philippines","url":D+"/mitsubishi-hybrid-phev/","about":{"@id":D+"/#dealer"},"dateModified":W_MOD},W_itemlist("Mitsubishi PHEV guides",PH_ART),W_FAQLD(PH_FAQ)],
 img="/assets/img/op_gt.webp",crumbs=[("/","Home"),("/cars/","Cars"),("/mitsubishi-hybrid-phev/","Mitsubishi PHEV / hybrid")])
W_PATHS.append("/mitsubishi-hybrid-phev/")

# ================= ARTICLES (new + refreshed). Rendered by build.articles() with w1=True (accordion FAQ, curated links, seo title, hub crumbs).
CR_DS=[("/","Home"),("/destinator/","Destinator")]
CR_PH=[("/","Home"),("/mitsubishi-hybrid-phev/","Mitsubishi PHEV / hybrid")]
CR_MS=[("/","Home"),("/cars/","Cars"),("/cars/montero-sport/","Montero Sport")]
CR_TR=[("/","Home"),("/cars/","Cars"),("/cars/triton/","Triton")]
def W_A(**k):
    k.setdefault("base","blog");k.setdefault("by",BY);k["w1"]=True;k.setdefault("date",W_MOD);k["mod"]=W_MOD
    assert len(k["seo"])<60,(k["slug"],len(k["seo"]));assert len(k["desc"])<155,(k["slug"],len(k["desc"]))
    W_PATHS.append(f"/{k['base']}/{k['slug']}/")
    return k
_glxl=W_vrow("destinator","dglx")[1];_opl=W_vrow("outlander-phev","opgt")[1];_trp=W_vrow("triton","trglmt2")[1];_msl=W_vrow("montero-sport","mglxmt")[1]
WA=[
W_A(slug="destinator-price-philippines",car="destinator",date="2026-10-22",img="de_jh3",alt="Mitsubishi Destinator GT, with 2026 price in the Philippines",crumbs=CR_DS,
 title="Destinator Price Philippines 2026: DP and Monthly per Variant",seo="Destinator Price Philippines 2026, DP & Monthly | SJDM",
 desc="Destinator price Philippines per variant, low DP and sample monthly (Oct 2026 list). Pre-qualified, subject to bank approval. SJDM Bulacan.",
 answer=f"The Destinator price in the Philippines starts at {f(1389000)} for the GLX, {f(1599000)} for the GLS, and {f(1929000)} (monotone) or {f(1939000)} (two-tone) for the GT ({FRESH}).",
 faq=[("How much is the Mitsubishi Destinator in the Philippines?",f"SRP: GLX {f(1389000)}, GLS {f(1599000)}, GT {f(1929000)} (monotone) or {f(1939000)} (two-tone), {FRESH}."),
  ("What is the Destinator DP and monthly?",f"From {f(_glxl[0])} DP and {f(_glxl[1])} a month on the GLX (60 months, all-in). {MSQ}."),
  ("Does the Destinator come with fuel points?","Selected variants come with fuel points in the current promo. Ask Richard for this month's freebies."),
  ("What engine does the Destinator have?","According to Mitsubishi Motors Philippines, a 1.5L turbocharged gasoline engine (4B40) with 163 PS and 250 N-m, paired with a CVT.")],
 more=[("/destinator/","Destinator guide"),("/blog/destinator-glx-vs-gls-vs-gt/","Destinator GLX vs GLS vs GT"),("/blog/destinator-vs-xforce/","Destinator vs XForce")],
 body=f'''<p>Here is the <a href="/destinator/">Mitsubishi Destinator</a> price in the Philippines for 2026, with a low DP and sample monthly for each variant. Want the full variant page? <a href="/cars/destinator/">Get a Destinator quote</a>.</p>
<h2>Destinator price per variant</h2>
{W_ptab("destinator")}
<p class="row">{W_pq("destinator","price-table",label="Compute my exact monthly")} <a class="btn sm ghost dk" href="/budgetcalculator/">Compute my monthly</a></p>
<h2>What "all-in" includes</h2>
<p>The promo packages bundle LTO registration, insurance and chattel mortgage. See <a href="/guides/what-all-in-includes/">what all-in includes</a>.</p>
<h2>Destinator DP and monthly</h2>
<p>A bigger down payment lowers the monthly and the total you pay. The table shows the lowest published DP per variant; Richard can compute other DP amounts for you. Every figure is {MSQ}, and the bank makes the final decision. See the <a href="/guides/car-loan-requirements/">car loan requirements</a>.</p>
<h2>Which variant?</h2>
<p>All variants share the 1.5L turbo (163 PS, 250 N-m), CVT, seven seats and 214 mm ground clearance, according to Mitsubishi Motors Philippines. Compare trims in <a href="/blog/destinator-glx-vs-gls-vs-gt/">Destinator GLX vs GLS vs GT</a>.</p>
'''+W_cta("destinator","Destinator","destinator")),
W_A(slug="outlander-phev-price-philippines",car="outlander-phev",img="op_gt",alt="Mitsubishi Outlander PHEV GT plug-in hybrid SUV",crumbs=CR_PH,
 title="Outlander PHEV Price Philippines 2026, DP and Monthly",seo="Outlander PHEV Price Philippines 2026 | SJDM Bulacan",
 desc="Outlander PHEV price Philippines (Oct 2026 list, November update pending), low DP and monthly, Pre-qualified, subject to bank approval. SJDM.",
 answer=f"The Mitsubishi Outlander PHEV GT 2.4G AWD has an SRP of {W_from('outlander-phev')} in the Philippines ({FRESH}).",
 faq=[("How much is the Outlander PHEV in the Philippines?",f"{W_from('outlander-phev')} SRP for the GT 2.4G AWD, {FRESH}."),
  ("What is the Outlander PHEV monthly?",f"From {f(_opl[1])} a month with {f(_opl[0])} DP, 60 months, all-in. {MSQ}."),
  ("How many variants are there?","One in the Philippines: the Outlander PHEV GT 2.4G AWD."),
  ("Is the Outlander PHEV battery covered by warranty?","According to Mitsubishi Motors Philippines, 8 years or 160,000 km, whichever comes first.")],
 more=[("/mitsubishi-hybrid-phev/","How a Mitsubishi PHEV works"),("/blog/outlander-phev-range-and-charging/","Outlander PHEV range and charging"),("/blog/outlander-phev-vs-montero-sport/","Outlander PHEV vs Montero Sport")],
 body=f'''<p>The <a href="/cars/outlander-phev/">Outlander PHEV</a> is Mitsubishi's plug-in hybrid SUV in the Philippines. Here is its price with a low DP and sample monthly. Get the <a href="/cars/outlander-phev/">Outlander PHEV promo and test drive</a>.</p>
<h2>Outlander PHEV price</h2>
{W_ptab("outlander-phev")}
<p class="row">{W_pq("outlander-phev","price-table",label="Compute my exact monthly")} <a class="btn sm ghost dk" href="/budgetcalculator/">Compute my monthly</a></p>
<h2>What you get</h2>
<ul class="ticks"><li>Combined system output of 306 PS and 450 N-m, according to Mitsubishi Motors</li><li>22.7 kWh battery with AC Type 2 charging, approx. 6.5 hours on AC</li><li>Up to 100 km of pure electric range, according to Mitsubishi Motors Philippines (no test cycle stated; actual range varies)</li><li>All Wheel Drive with S-AWC and seven drive modes</li><li>Five seats; battery warranty of 8 years or 160,000 km</li></ul>
<h2>Outlander PHEV DP and monthly</h2>
<p>The table shows the lowest published DP and its sample monthly. A bigger DP lowers the monthly. {MSQ}. See <a href="/guides/what-all-in-includes/">what all-in includes</a> and the <a href="/guides/car-loan-requirements/">car loan requirements</a>.</p>
<h2>New to plug-in hybrids?</h2>
<p>Read <a href="/mitsubishi-hybrid-phev/">how a Mitsubishi PHEV works</a> and <a href="/blog/outlander-phev-range-and-charging/">range and charging</a>.</p>
'''+W_cta("outlander-phev","Outlander PHEV","outlander-phev")),
W_A(slug="triton-price-philippines",car="triton",img="tr_lineup",alt="Mitsubishi Triton pickup lineup",crumbs=CR_TR,
 title="Triton Price Philippines 2026: Every Variant, DP, Monthly",seo="Triton Price Philippines 2026, All Variants | SJDM",
 desc="Triton price Philippines per variant (Oct 2026 list, November pending), low DP and sample monthly. Pre-qualified, subject to bank approval. SJDM.",
 answer=f"The Mitsubishi Triton price in the Philippines runs from {W_from('triton')} (GL 2WD M/T) to {f(2359000)} (Athlete 4WD A/T), {FRESH}.",
 faq=[("How much is the Triton in the Philippines?",f"From {W_from('triton')} for the GL 2WD M/T to {f(2359000)} for the Athlete 4WD A/T ({FRESH})."),
  ("What is the cheapest Triton automatic?",f"The Triton GX 2.4D 2WD A/T at {f(1430000)} SRP."),
  ("What is the Triton monthly installment?",f"From {f(_trp[1])} a month with {f(_trp[0])} DP on the GL 2WD M/T (60 months, all-in). {MSQ}."),
  ("Which Triton has the Bi-Turbo engine?","According to Mitsubishi Motors, the 2.4L Bi-Turbo diesel makes 204 PS and 470 Nm. Ask Richard which variant carries it.")],
 more=[("/triton-downpayment-and-monthly/","Triton monthly installment"),("/blog/triton-gx-2wd-at-first-pickup-guide/","Triton GX 2026"),("/blog/triton-vs-hilux/","Triton vs Hilux")],
 body=f'''<p>Here is the <a href="/cars/triton/">Triton</a> price in the Philippines for every 2026 variant, with a low DP and sample monthly. See all <a href="/cars/triton/">Triton 2026 variants</a>.</p>
<h2>Triton price per variant</h2>
{W_ptab("triton")}
<p class="row">{W_pq("triton","price-table",label="Compute my exact monthly")} <a class="btn sm ghost dk" href="/budgetcalculator/">Compute my monthly</a></p>
<h2>Manual or automatic, 2WD or 4WD</h2>
<ul class="ticks"><li><b>Manual</b>: GL 2WD and 4WD, GLX 2WD and 4WD</li><li><b>Automatic</b>: GX 2WD, GLX 2WD, GLS 2WD and Athlete 4WD</li><li><b>4WD</b>: GL 4WD, GLX 4WD and Athlete. According to Mitsubishi Motors, the Athlete uses Super Select 4WD-II with 7 drive modes.</li></ul>
<h2>Triton DP and monthly</h2>
<p>The table shows the lowest published DP per variant with its sample monthly. For a different DP or term, see the <a href="/triton-downpayment-and-monthly/">Triton monthly installment</a> guide. {MSQ}.</p>
<h2>What every Triton buyer should know</h2>
<p>According to Mitsubishi Motors, the Triton earned a 5-star rating in the 2023 ASEAN NCAP and has a 75 L fuel tank. Using it for work? Read <a href="/blog/triton-for-business-and-farm/">Triton for business and farm</a>.</p>
'''+W_cta("triton","Triton","triton")),
W_A(slug="montero-sport-price-philippines-2026",car="montero-sport",date="2026-10-22",img="msbs_x8w",alt="Mitsubishi Montero Sport Black Series 4WD, with 2026 price in the Philippines",crumbs=CR_MS,
 title="Montero Sport Price Philippines 2026, DP and Monthly",seo="Montero Sport Price Philippines 2026 | SJDM",
 desc="Montero Sport price Philippines per variant, low DP and monthly amortization (Oct 2026 list). Pre-qualified, subject to bank approval. SJDM.",
 answer=f"The Montero Sport price in the Philippines for 2026 is {f(1568000)} (GLX 2WD M/T), {f(1927000)} (GLS 2WD A/T), {f(2190000)} (Black Series 2WD A/T) and {f(2530000)} (Black Series 4WD A/T), {FRESH}.",
 faq=[("How much is the Montero Sport in the Philippines in 2026?",f"SRP: GLX 2WD M/T {f(1568000)}, GLS 2WD A/T {f(1927000)}, Black Series 2WD A/T {f(2190000)}, Black Series 4WD A/T {f(2530000)} ({FRESH})."),
  ("What is the Montero Sport monthly amortization?",f"From {f(_msl[1])} a month with {f(_msl[0])} DP on the GLX M/T (60 months, all-in). {MSQ}."),
  ("How much is the Montero Sport automatic?",f"The GLS 2WD A/T is {f(1927000)} SRP; the Black Series 2WD A/T is {f(2190000)}."),
  ("Which Montero Sport is 4x4?","The Black Series 4WD A/T, with Super Select 4WD-II according to Mitsubishi Motors.")],
 more=[("/cars/montero-sport/","Montero Sport 2026 variants"),("/blog/montero-sport-black-series/","Montero Sport Black Series"),("/blog/montero-sport-variants-explained/","Montero Sport GLX vs GLS vs Black Series")],
 body=f'''<p>Here is the <a href="/cars/montero-sport/">Montero Sport</a> price in the Philippines for 2026, with a low DP and monthly amortization per variant. See all <a href="/cars/montero-sport/">Montero Sport 2026 variants</a>.</p>
<h2>Montero Sport price per variant</h2>
{W_ptab("montero-sport")}
<p class="row">{W_pq("montero-sport","price-table",label="Pre-qualify in 2 minutes")} <a class="btn sm ghost dk" href="/budgetcalculator/">Compute my monthly</a></p>
<h2>Montero Sport monthly amortization</h2>
<p>The sample monthly in the table uses the lowest published DP on 60 months, all-in. A bigger DP lowers the monthly. {MSQ}; the bank makes the final decision. See <a href="/guides/what-all-in-includes/">what all-in includes</a> and the <a href="/guides/car-loan-requirements/">car loan requirements</a>.</p>
<h2>Manual or automatic, 2WD or 4WD</h2>
<ul class="ticks"><li><b>Manual</b>: GLX, 6-speed</li><li><b>Automatic</b>: GLS and Black Series, 8-speed with Sport Mode</li><li><b>4WD</b>: Black Series 4WD only, with Super Select 4WD-II</li></ul>
<p>According to Mitsubishi Motors, every variant has the 2.4L 4N15 turbo diesel (181 PS, 430 Nm) and seven seats. More in <a href="/blog/montero-sport-variants-explained/">Montero Sport GLX vs GLS vs Black Series</a> and <a href="/blog/montero-sport-black-series/">Black Series</a>.</p>
'''+W_cta("montero-sport","Montero Sport","montero-sport")),
]
# ---- Wave 3
_bs=W_vrow("montero-sport","mbs2wd")[1]
WA+=[
W_A(slug="destinator-vs-xforce",car="destinator",img="de_d34",alt="Mitsubishi Destinator 7-seater SUV",crumbs=CR_DS,
 title="Mitsubishi Destinator vs XForce: Seats, Size and Features",seo="Destinator vs XForce: Which Mitsubishi Fits You? | SJDM",
 desc="Destinator vs XForce compared by seats, engine and features, according to Mitsubishi Motors. Test drive both in San Jose del Monte (SJDM).",
 answer="Choose the Destinator if you need seven seats and turbo power; choose the XForce if five seats are enough and you want a compact SUV for the city.",
 faq=[("Is the XForce a 7-seater?","No. The XForce is a 5-seat compact SUV. The Destinator has seven seats in three rows."),
  ("Which one has a turbo?","According to Mitsubishi Motors Philippines, the Destinator's 1.5L turbo makes 163 PS and 250 N-m. The XForce uses a 1.5L gasoline engine; ask Richard for its full spec sheet."),
  ("Do both have a CVT?","Yes, both use a CVT and are 2WD."),
  ("Where can I test drive both?","In San Jose del Monte (SJDM) with Richard Cuagdan. Book a test drive online.")],
 more=[("/destinator/","Destinator guide"),("/tips/xforce-2026-price-philippines/","XForce 2026 price: GLX vs GLS vs GT"),("/blog/destinator-fuel-consumption/","Destinator fuel consumption")],
 body='''<div class="box verdict"><p><b>Choose the Destinator if</b> you carry six or seven people and want the turbo engine and extra ground clearance.</p><p><b>Choose the XForce if</b> five seats are enough and you mostly drive and park in the city.</p><p class="row"><a class="btn sm" href="/test-drive/?unit=destinator">Test drive the Destinator in SJDM</a></p></div>
<p>Both are Mitsubishi SUVs with a 1.5L gasoline engine and a CVT, but they suit different families. More in the <a href="/destinator/">Destinator guide</a>.</p>
<h2>Feature comparison</h2>
<div class="tw"><table class="pt"><thead><tr><th scope="col">Feature</th><th scope="col">Destinator</th><th scope="col">XForce</th></tr></thead><tbody>
<tr><th scope="row">Body type</th><td>7-seater SUV</td><td>Compact SUV</td></tr>
<tr><th scope="row">Seats</th><td>7, three rows</td><td>5</td></tr>
<tr><th scope="row">Engine</th><td>1.5L 4B40 turbo gasoline, 163 PS / 250 N-m</td><td>1.5L gasoline</td></tr>
<tr><th scope="row">Transmission / drive</th><td>CVT, 2WD</td><td>CVT, 2WD</td></tr>
<tr><th scope="row">Ground clearance</th><td>214 mm</td><td>See the XForce spec sheet</td></tr>
<tr><th scope="row">Drive modes</th><td>Normal, Wet, Gravel, Mud, Tarmac</td><td>See the XForce spec sheet</td></tr>
<tr><th scope="row">Variants</th><td>GLX, GLS, GT</td><td>GLX, GLS, GT</td></tr></tbody></table></div>
<p class="muted">Destinator figures according to Mitsubishi Motors Philippines. Prices: <a href="/blog/destinator-price-philippines/">Destinator price Philippines</a> and <a href="/tips/xforce-2026-price-philippines/">XForce 2026 price</a>.</p>
<h2>Who each one suits</h2>
<ul class="ticks"><li><b>Destinator</b>: growing families, provincial trips, carpool runs, and drivers who want turbo power with a full load</li><li><b>XForce</b>: couples and small families, city commuting, easy parking</li></ul>
'''+W_cta("destinator","Destinator","destinator")),
W_A(slug="destinator-fuel-consumption",car="destinator",img="de_p26",alt="Mitsubishi Destinator on the road",crumbs=CR_DS,
 title="Destinator Fuel Consumption: Engine Facts and Saving Tips",seo="Destinator Fuel Consumption: What to Expect | SJDM",
 desc="What affects Destinator fuel consumption: 1.5L turbo facts according to Mitsubishi Motors, driving tips and a test drive in SJDM, Bulacan.",
 answer="Mitsubishi Motors Philippines does not publish an official km/L figure for the Destinator. Fuel use depends on traffic, load, speed and driving style; a test drive with the trip computer gives you a real-world feel.",
 faq=[("What is the official Destinator km/L?","Mitsubishi Motors Philippines does not publish an official fuel economy figure for the Destinator, so this page does not quote one."),
  ("What fuel does the Destinator use?","Gasoline, RON 95 and over, according to Mitsubishi Motors Philippines. The tank holds 45 L."),
  ("Does the turbo use more fuel?","It depends on how you drive. Smooth, steady driving uses less fuel; hard acceleration uses more."),
  ("How can I check fuel use before buying?","Ask for a test drive in SJDM and watch the trip computer on your usual route.")],
 more=[("/destinator/","Destinator guide"),("/tips/fuel-saving-tips-diesel-vs-gasoline/","Fuel saving tips"),("/blog/destinator-vs-xforce/","Destinator vs XForce")],
 body='''<p>Fuel cost is a fair question before buying a 7-seater. Here is what we know about the <a href="/destinator/">Destinator</a> engine and what affects how much fuel you use. Get a Destinator quote on the <a href="/cars/destinator/">variants page</a>.</p>
<h2>Engine facts</h2>
<ul class="ticks"><li>1.5L 4B40 turbocharged gasoline engine, Euro 4</li><li>163 PS and 250 N-m</li><li>CVT, front-wheel drive</li><li>45 L fuel tank, RON 95 and over</li></ul>
<p class="muted">According to Mitsubishi Motors Philippines. No official km/L figure is published, so this page does not quote one.</p>
<h2>What affects fuel consumption</h2>
<ul class="ticks"><li><b>Traffic</b>: stop-and-go city traffic uses more fuel than steady NLEX driving</li><li><b>Load</b>: seven passengers and luggage add weight</li><li><b>Speed</b>: steady, moderate speeds use less fuel</li><li><b>Tires and maintenance</b>: correct tire pressure and on-time PMS help</li><li><b>Aircon and idling</b>: long idling with the AC on adds up</li></ul>
<h2>Saving tips</h2>
<p>Accelerate smoothly, anticipate stops, and plan trips outside peak hours. More in <a href="/tips/fuel-saving-tips-diesel-vs-gasoline/">fuel saving tips</a>.</p>
<h2>See it on the trip computer</h2>
<p>The best answer is your own route. Ask for a test drive in San Jose del Monte and watch the trip computer.</p>
'''+W_cta("destinator","Destinator","destinator")),
W_A(slug="montero-sport-black-series",car="montero-sport",img="msbs_jh3",alt="Mitsubishi Montero Sport Black Series",crumbs=CR_MS,
 title="Montero Sport Black Series: 2WD vs 4WD and What You Get",seo="Montero Sport Black Series 2026 Guide | SJDM",
 desc="Montero Sport Black Series 2WD and 4WD: features according to Mitsubishi Motors, Oct 2026 price, monthly. Test drive in San Jose del Monte (SJDM).",
 answer=f"The Montero Sport Black Series comes as a 2WD A/T ({f(2190000)}) and a 4WD A/T ({f(2530000)}), {FRESH}. According to Mitsubishi Motors, the 4WD adds Super Select 4WD-II, Rear Differential Lock, Off-Road Mode and Hill Descent Control.",
 faq=[("How much is the Montero Sport Black Series?",f"Black Series 2WD A/T {f(2190000)}; Black Series 4WD A/T {f(2530000)} ({FRESH})."),
  ("What does the 4WD add?","According to Mitsubishi Motors: Super Select 4WD-II, Rear Differential Lock, Off-Road Mode and Hill Descent Control."),
  ("What engine does the Black Series have?","The same 4N15 2.4L turbo diesel as the rest of the range: 181 PS and 430 Nm, with an 8-speed automatic, according to Mitsubishi Motors."),
  ("What is the Black Series monthly?",f"From {f(_bs[1])} a month with {f(_bs[0])} DP on the 2WD (60 months, all-in). {MSQ}.")],
 more=[("/cars/montero-sport/","Montero Sport 2026 variants"),("/blog/montero-sport-price-philippines-2026/","Montero Sport price Philippines"),("/blog/montero-sport-vs-fortuner/","Montero Sport vs Fortuner")],
 body=f'''<p>The Black Series sits at the top of the <a href="/cars/montero-sport/">Montero Sport 2026 variants</a>. Here is how the 2WD and 4WD differ.</p>
<h2>Black Series price</h2>
{W_ptab("montero-sport","Black")}
<h2>2WD vs 4WD</h2>
<div class="tw"><table class="pt"><thead><tr><th scope="col">Feature</th><th scope="col">Black Series 2WD A/T</th><th scope="col">Black Series 4WD A/T</th></tr></thead><tbody>
<tr><th scope="row">Engine</th><td>2.4L 4N15 turbo diesel, 181 PS / 430 Nm</td><td>2.4L 4N15 turbo diesel, 181 PS / 430 Nm</td></tr>
<tr><th scope="row">Transmission</th><td>8-speed A/T with Sport Mode</td><td>8-speed A/T with Sport Mode</td></tr>
<tr><th scope="row">Drive</th><td>2WD</td><td>Super Select 4WD-II</td></tr>
<tr><th scope="row">Off-road aids</th><td>Not listed</td><td>Rear Differential Lock, Off-Road Mode, Hill Descent Control</td></tr>
<tr><th scope="row">Seats</th><td>7</td><td>7</td></tr></tbody></table></div>
<p class="muted">According to Mitsubishi Motors Philippines (Montero Sport brochure).</p>
<h2>Which one should you get?</h2>
<ul class="ticks"><li><b>2WD</b>: city and highway driving, the occasional provincial road</li><li><b>4WD</b>: steep, muddy or unpaved roads, beach or farm access</li></ul>
<p>Compare all variants in <a href="/blog/montero-sport-variants-explained/">GLX vs GLS vs Black Series</a>.</p>
'''+W_cta("montero-sport","Montero Sport Black Series","mbs4wd")),
W_A(slug="montero-sport-vs-fortuner",car="montero-sport",img="ms_white",alt="Mitsubishi Montero Sport",crumbs=CR_MS,
 title="Montero Sport vs Fortuner: Features That Matter to Buyers",seo="Montero Sport vs Fortuner: Feature Comparison | SJDM",
 desc="Montero Sport vs Fortuner compared by features only: engine, 4WD system, seats. Montero facts according to Mitsubishi Motors. SJDM test drive.",
 answer="Both are 7-seat diesel SUVs. This comparison covers features only. Montero Sport figures are according to Mitsubishi Motors; for the Fortuner, check the manufacturer's official spec sheet.",
 faq=[("Is the Montero Sport a 7-seater?","Yes, seven seats according to Mitsubishi Motors."),
  ("Does the Montero Sport have 4WD?","The Black Series 4WD has Super Select 4WD-II, according to Mitsubishi Motors. The other variants are 2WD."),
  ("Why no Fortuner prices here?","This page compares features only. For the Montero Sport price, see the Montero Sport price article."),
  ("Can I test drive the Montero Sport in SJDM?","Yes. Book online with Richard Cuagdan in San Jose del Monte.")],
 more=[("/cars/montero-sport/","Montero Sport 2026 variants"),("/blog/montero-sport-black-series/","Montero Sport Black Series"),("/blog/montero-sport-fuel-consumption/","Montero Sport fuel consumption")],
 body='''<div class="box verdict"><p><b>Choose the Montero Sport if</b> you want an 8-speed automatic, Super Select 4WD-II on the 4WD variant, and a manual option on the GLX.</p><p><b>Choose the other if</b> its features suit you better after comparing both official spec sheets side by side.</p><p class="row"><a class="btn sm" href="/test-drive/?unit=montero-sport">Test drive the Montero Sport in SJDM</a></p></div>
<p>Two popular 7-seat diesel SUVs, compared by features only. See the <a href="/cars/montero-sport/">Montero Sport 2026 variants</a> for prices.</p>
<h2>Feature comparison</h2>
<div class="tw"><table class="pt"><thead><tr><th scope="col">Feature</th><th scope="col">Montero Sport</th><th scope="col">Fortuner</th></tr></thead><tbody>
<tr><th scope="row">Body type</th><td>7-seat SUV</td><td>7-seat SUV</td></tr>
<tr><th scope="row">Engine</th><td>2.4L 4N15 turbo diesel with MIVEC, 181 PS / 430 Nm</td><td>Check the manufacturer's spec sheet</td></tr>
<tr><th scope="row">Transmission</th><td>8-speed A/T with Sport Mode; 6-speed M/T (GLX)</td><td>Check the manufacturer's spec sheet</td></tr>
<tr><th scope="row">4WD system</th><td>Super Select 4WD-II (Black Series 4WD)</td><td>Check the manufacturer's spec sheet</td></tr>
<tr><th scope="row">Off-road aids</th><td>Rear Differential Lock, Off-Road Mode, Hill Descent Control (4WD)</td><td>Check the manufacturer's spec sheet</td></tr>
<tr><th scope="row">Driver assistance</th><td>FCM, BSW with LCA, UMS, RCTA, Adaptive Cruise Control (higher variants)</td><td>Check the manufacturer's spec sheet</td></tr></tbody></table></div>
<p class="muted">Montero Sport features according to Mitsubishi Motors Philippines. Montero Sport prices: <a href="/blog/montero-sport-price-philippines-2026/">Montero Sport price Philippines</a>.</p>
<h2>What to compare on a test drive</h2>
<ul class="ticks"><li>Third-row space and how the seats fold</li><li>Ride comfort on rough roads</li><li>Visibility and parking aids in tight streets</li><li>How the automatic responds in traffic and on NLEX</li></ul>
'''+W_cta("montero-sport","Montero Sport","montero-sport")),
W_A(slug="montero-sport-fuel-consumption",car="montero-sport",img="ms_silver",alt="Mitsubishi Montero Sport on the road",crumbs=CR_MS,
 title="Montero Sport Fuel Consumption: Engine Facts and Tips",seo="Montero Sport Fuel Consumption: What Affects It | SJDM",
 desc="What affects Montero Sport fuel consumption: 2.4L diesel facts according to Mitsubishi Motors, driving tips, and a test drive in SJDM.",
 answer="Mitsubishi Motors Philippines does not publish an official km/L figure for the Montero Sport. Fuel use depends on traffic, load, speed and driving style.",
 faq=[("What is the official Montero Sport km/L?","Mitsubishi Motors Philippines does not publish an official fuel economy figure, so this page does not quote one."),
  ("Is the Montero Sport diesel?","Yes. According to Mitsubishi Motors, a 4N15 2.4L turbocharged direct injection diesel with MIVEC."),
  ("Does 4WD use more fuel?","Driving in 4WD on rough roads usually uses more fuel than 2WD on pavement; use 4WD when conditions need it."),
  ("How can I check before buying?","Ask for a test drive in SJDM and watch the trip computer on your usual route.")],
 more=[("/cars/montero-sport/","Montero Sport 2026 variants"),("/tips/fuel-saving-tips-diesel-vs-gasoline/","Fuel saving tips"),("/blog/montero-sport-vs-fortuner/","Montero Sport vs Fortuner")],
 body='''<p>Here is what drives fuel use in the <a href="/cars/montero-sport/">Montero Sport</a> and how to keep it down. See the <a href="/cars/montero-sport/">Montero Sport 2026 variants</a> for prices.</p>
<h2>Engine facts</h2>
<ul class="ticks"><li>4N15 2.4L turbocharged direct injection diesel with MIVEC</li><li>181 PS at 3,500 rpm, 430 Nm at 2,500 rpm</li><li>8-speed automatic with Sport Mode, or 6-speed manual (GLX)</li></ul>
<p class="muted">According to Mitsubishi Motors Philippines. No official km/L figure is published, so this page does not quote one.</p>
<h2>What affects fuel consumption</h2>
<ul class="ticks"><li><b>Traffic</b>: stop-and-go driving uses more fuel than steady highway runs</li><li><b>Load and towing</b>: a full cabin or a trailer adds work</li><li><b>Drive mode</b>: use 4WD only when the road needs it</li><li><b>Maintenance</b>: tire pressure, clean filters and on-time PMS</li></ul>
<h2>Saving tips</h2>
<p>Drive smoothly, keep a steady speed on NLEX, and avoid long idling. More in <a href="/tips/fuel-saving-tips-diesel-vs-gasoline/">fuel saving tips</a>.</p>
'''+W_cta("montero-sport","Montero Sport","montero-sport")),
W_A(slug="triton-vs-hilux",car="triton",img="tr_glx",alt="Mitsubishi Triton pickup",crumbs=CR_TR,
 title="Triton vs Hilux vs Ranger: Pickup Features Compared",seo="Triton vs Hilux (and Ranger): Features | SJDM",
 desc="Triton vs Hilux, plus Ranger, compared by features only. Triton facts according to Mitsubishi Motors, 5-star ASEAN NCAP. SJDM test drive.",
 answer="This is a feature-only comparison. According to Mitsubishi Motors, the Triton's 2.4L Bi-Turbo diesel makes 204 PS and 470 Nm, and the Triton earned a 5-star 2023 ASEAN NCAP rating. For the Hilux and Ranger, check each manufacturer's spec sheet.",
 faq=[("How powerful is the Triton?","According to Mitsubishi Motors, the 2.4L Bi-Turbo diesel produces 204 PS and 470 Nm."),
  ("Does the Triton have a 5-star safety rating?","According to Mitsubishi Motors, it earned a 5-star rating in the 2023 ASEAN NCAP."),
  ("Why no Hilux or Ranger prices?","This page compares features only. For Triton prices, see the Triton price article."),
  ("Which Triton is 4x4?","GL 4WD M/T, GLX 4WD M/T and Athlete 4WD A/T.")],
 more=[("/cars/triton/","Triton 2026 variants"),("/blog/triton-price-philippines/","Triton price Philippines"),("/blog/triton-for-business-and-farm/","Triton for business and farm")],
 body='''<div class="box verdict"><p><b>Choose the Triton if</b> you want the 204 PS Bi-Turbo diesel, Super Select 4WD-II on the Athlete, and a 5-star 2023 ASEAN NCAP rating.</p><p><b>Choose another pickup if</b> its features suit your work better after comparing official spec sheets.</p><p class="row"><a class="btn sm" href="/test-drive/?unit=triton">Test drive the Triton in SJDM</a></p></div>
<p>Pickup buyers in Bulacan often compare these three. Here is a feature-only look. See the <a href="/cars/triton/">Triton 2026 variants</a> for prices.</p>
<h2>Triton vs Hilux</h2>
<div class="tw"><table class="pt"><thead><tr><th scope="col">Feature</th><th scope="col">Triton</th><th scope="col">Hilux</th></tr></thead><tbody>
<tr><th scope="row">Body type</th><td>Pickup</td><td>Pickup</td></tr>
<tr><th scope="row">Engine (top)</th><td>4N16 2.4L Bi-Turbo diesel, 204 PS / 470 Nm</td><td>Check the manufacturer's spec sheet</td></tr>
<tr><th scope="row">Transmission</th><td>6-speed A/T or 6-speed M/T</td><td>Check the manufacturer's spec sheet</td></tr>
<tr><th scope="row">4WD system</th><td>Super Select 4WD-II with 7 drive modes (Athlete)</td><td>Check the manufacturer's spec sheet</td></tr>
<tr><th scope="row">Safety rating</th><td>5-star, 2023 ASEAN NCAP</td><td>Check the manufacturer's spec sheet</td></tr>
<tr><th scope="row">Fuel tank</th><td>75 L</td><td>Check the manufacturer's spec sheet</td></tr></tbody></table></div>
<p class="muted">Triton features according to Mitsubishi Motors Philippines.</p>
<h2>Triton vs Ranger</h2>
<p>The Ranger is another popular pickup. Compare the same rows (engine, 4WD system, safety rating, bed size) using its official spec sheet, then drive both. Triton figures above are according to Mitsubishi Motors.</p>
<h2>What to check on a test drive</h2>
<ul class="ticks"><li>Bed size against your usual cargo</li><li>Rear seat comfort for family use</li><li>Turning and parking in tight streets</li><li>Automatic vs manual for your daily route</li></ul>
<p>Triton prices: <a href="/blog/triton-price-philippines/">Triton price Philippines</a>.</p>
'''+W_cta("triton","Triton","triton")),
]
# ---- Wave 4
WA+=[
W_A(slug="outlander-phev-range-and-charging",car="outlander-phev",img="op_gt",alt="Mitsubishi Outlander PHEV plug-in hybrid",crumbs=CR_PH,
 title="Outlander PHEV Range and Charging: Home and Public",seo="Outlander PHEV Range & Charging Guide | SJDM",
 desc="Outlander PHEV range and charging according to Mitsubishi Motors: 22.7 kWh battery, AC Type 2, approx. 6.5 hrs AC charge. Ask in SJDM Bulacan.",
 answer="According to Mitsubishi Motors Philippines, the Outlander PHEV offers up to 100 km of pure electric range and almost 1,000 km combined (no test cycle stated; actual range varies). It charges on AC Type 2 in approximately 6.5 hours (230V-240V, 15A).",
 faq=[("What is the Outlander PHEV electric range?","Up to 100 km of pure electric range, according to Mitsubishi Motors Philippines. No test cycle is stated, and actual range varies with driving conditions."),
  ("How long does charging take?","Approximately 6.5 hours on AC (230V-240V, 15A), according to Mitsubishi Motors."),
  ("What charging type does it use?","AC Type 2, according to Mitsubishi Motors Philippines. The supplied cable uses an AC industrial plug (2P+E) 16A and is 6.0 m long."),
  ("Does it support DC fast charging?","DC fast charging is not listed on the Mitsubishi Motors Philippines page. Ask Richard to confirm."),
  ("What if the battery runs out?","The 2.4L gasoline engine keeps the car going, so you can continue your trip.")],
 more=[("/mitsubishi-hybrid-phev/","How a Mitsubishi PHEV works"),("/blog/outlander-phev-price-philippines/","Outlander PHEV price"),("/blog/outlander-phev-vs-montero-sport/","Outlander PHEV vs Montero Sport")],
 body=W_tiles([("22.7 kWh","Lithium-ion battery"),("AC Type 2","Charging protocol"),("Approx. 6.5 hrs","AC charge, 230V-240V, 15A")])+'''
<p>Thinking about the <a href="/cars/outlander-phev/">Outlander PHEV</a>? Here is how far it goes on electricity and how charging works. See the <a href="/cars/outlander-phev/">Outlander PHEV promo and test drive</a>.</p>
<h2>Range</h2>
<p>According to Mitsubishi Motors Philippines, the Outlander PHEV offers up to 100 km of pure electric range and a combined driving range of almost 1,000 km. Mitsubishi Motors Philippines does not state a test cycle for these figures, and actual range varies with traffic, speed, load, aircon use and weather.</p>
<h2>Charging</h2>
<ol class="steps"><li><h3>Park near a suitable outlet</h3><p>The supplied cable is 6.0 m with an AC industrial plug (2P+E) 16A, according to Mitsubishi Motors Philippines.</p></li><li><h3>Connect the cable to the car</h3><p>The car supports the AC Type 2 charging protocol.</p></li><li><h3>Charge</h3><p>Approximately 6.5 hours on AC (230V-240V, 15A), according to Mitsubishi Motors.</p></li></ol>
<h2>Before you set up home charging</h2>
<ul class="ticks"><li>Have a licensed electrician check your home's wiring and outlet</li><li>Confirm where you will park and how the cable reaches</li><li>Ask Richard about the charging equipment that comes with the unit</li></ul>
<h2>EV drive modes</h2>
<p>According to Mitsubishi Motors Philippines, the Outlander PHEV has four EV drive modes: Normal, Save, Charge and EV Priority. Learn more in <a href="/mitsubishi-hybrid-phev/">how a Mitsubishi PHEV works</a>.</p>
'''+W_cta("outlander-phev","Outlander PHEV","outlander-phev")),
W_A(slug="outlander-phev-vs-montero-sport",car="outlander-phev",img="op_gt",alt="Mitsubishi Outlander PHEV plug-in hybrid SUV",crumbs=CR_PH,
 title="Outlander PHEV vs Montero Sport: Plug-in Hybrid or Diesel?",seo="Outlander PHEV vs Montero Sport: Which SUV? | SJDM",
 desc="Outlander PHEV vs Montero Sport compared by powertrain, seats and use case, according to Mitsubishi Motors. Test drive in San Jose del Monte.",
 answer="Choose the Outlander PHEV for electric driving on everyday trips and AWD; choose the Montero Sport for seven seats, a diesel engine and a 4WD option.",
 faq=[("Which has more seats?","The Montero Sport has seven seats; the Outlander PHEV has five, according to Mitsubishi Motors."),
  ("Which is more powerful?","According to Mitsubishi Motors, the Outlander PHEV's combined output is 306 PS and 450 N-m; the Montero Sport's 2.4L diesel makes 181 PS and 430 Nm."),
  ("Which one can drive on electricity?","Only the Outlander PHEV, with up to 100 km of pure electric range according to Mitsubishi Motors Philippines (no test cycle stated)."),
  ("Can I test drive both in SJDM?","Yes, book with Richard Cuagdan in San Jose del Monte.")],
 more=[("/mitsubishi-hybrid-phev/","How a Mitsubishi PHEV works"),("/blog/outlander-phev-range-and-charging/","Outlander PHEV range and charging"),("/blog/montero-sport-price-philippines-2026/","Montero Sport price Philippines")],
 body='''<div class="box verdict"><p><b>Choose the Outlander PHEV if</b> you can charge at home, drive mostly short daily trips and want AWD.</p><p><b>Choose the Montero Sport if</b> you need seven seats, often drive long provincial routes, or want a 4WD option.</p><p class="row"><a class="btn sm" href="/test-drive/?unit=outlander-phev">Test drive the Outlander PHEV in SJDM</a></p></div>
<p>Two very different Mitsubishi SUVs. See the <a href="/cars/outlander-phev/">Outlander PHEV</a> and the <a href="/cars/montero-sport/">Montero Sport</a>.</p>
<h2>Feature comparison</h2>
<div class="tw"><table class="pt"><thead><tr><th scope="col">Feature</th><th scope="col">Outlander PHEV</th><th scope="col">Montero Sport</th></tr></thead><tbody>
<tr><th scope="row">Powertrain</th><td>2.4L gasoline plug-in hybrid, front and rear motors</td><td>2.4L 4N15 turbo diesel</td></tr>
<tr><th scope="row">Output</th><td>306 PS / 450 N-m combined</td><td>181 PS / 430 Nm</td></tr>
<tr><th scope="row">Drive</th><td>AWD with S-AWC</td><td>2WD, or Super Select 4WD-II (Black Series 4WD)</td></tr>
<tr><th scope="row">Seats</th><td>5</td><td>7</td></tr>
<tr><th scope="row">Electric driving</th><td>Up to 100 km (no test cycle stated)</td><td>No</td></tr></tbody></table></div>
<p class="muted">According to Mitsubishi Motors Philippines. Prices: <a href="/blog/outlander-phev-price-philippines/">Outlander PHEV price</a> and <a href="/blog/montero-sport-price-philippines-2026/">Montero Sport price</a>.</p>
<h2>Who each one suits</h2>
<ul class="ticks"><li><b>Outlander PHEV</b>: daily commutes that fit the electric range, home charging, all-weather AWD</li><li><b>Montero Sport</b>: big families, long provincial trips, rough roads with the 4WD variant</li></ul>
'''+W_cta("outlander-phev","Outlander PHEV","outlander-phev")),
]
# ---- Triton GX guide: retitle + refresh (Wave 3), keeps its URL
for _a in POSTS:
    if _a["slug"]=="triton-gx-2wd-at-first-pickup-guide":
        _gx=W_vrow("triton","tritongxat")[1]
        _a.update(title="Triton GX 2026: Is It the Right First Pickup?",seo="Triton GX 2026: First Pickup Guide | SJDM Bulacan",
          desc="Triton GX 2026 2WD AT for first-time pickup owners: features, Oct 2026 price and monthly. Test drive in San Jose del Monte (SJDM).",
          answer=f"The Triton GX 2.4D 2WD A/T is an automatic double-cab pickup with an SRP of {f(1430000)} ({FRESH}). The automatic makes the switch from a sedan or MPV easier.",
          w1=True,mod=W_MOD,crumbs=CR_TR,more=[("/cars/triton/","Triton 2026 variants"),("/blog/triton-price-philippines/","Triton price Philippines"),("/triton-downpayment-and-monthly/","Triton monthly installment")])
        _b=_a["body"];_i=_b.find("<h2>The "+_PL+" promo</h2>");_j=_b.find("<h2>Driving and parking tips</h2>")
        assert _i>0 and _j>_i
        _b=_b[:_i]+f'<h2>Triton GX 2026 price and monthly</h2>\n<p>SRP {f(1430000)}. Low DP from {f(_gx[0])} with a sample monthly of {f(_gx[1])} (60 months, all-in). {MSQ}.</p>{W_badge()}\n'+_b[_j:]
        _b=_w_re.sub(r"<h2>Related reading</h2>.*$","",_b,flags=_w_re.S);_b=_w_re.sub(r"<p>See also:.*$","",_b,flags=_w_re.S);_b=_w_re.sub(r"<h2>Your next step</h2>.*$","",_b,flags=_w_re.S)
        _b=_b.replace("Unang pickup mo? Congrats, it's","Buying your first pickup? It's")
        _a["body"]=_b+'<p>Compare every variant in the <a href="/blog/triton-price-philippines/">Triton price Philippines</a> guide and the <a href="/triton-downpayment-and-monthly/">Triton monthly installment</a> guide.</p>\n'+W_cta("triton","Triton GX","tritongxat")
        _a["faq"]=list(_a["faq"])+[("How much is the Triton GX 2026?",f"{f(1430000)} SRP for the GX 2.4D 2WD A/T ({FRESH}). Financing is {MSQ}.")]
        W_PATHS.append("/blog/triton-gx-2wd-at-first-pickup-guide/")
for _k in ("triton-gx-2wd-at-first-pickup-guide","destinator-price-philippines","montero-sport-price-philippines-2026"): FIGS.pop(_k,None)
# ================= ARTICLE: Xpander Hybrid (Xpander HEV / Xpander Cross HEV) "what we know" (DRAFT 2026-11-16). Not sold in PH, no SRP: Message CTA only.
# Official editorial photos from the Mitsubishi Motors newsroom (Feb 1, 2024 release; editorial use only, not for ads).
CR_GT=[("/","Home"),("/tips/","Guides & Tips")]
XH_SRC=[("https://www.mitsubishi-motors.com/en/newsroom/newsrelease/2024/20240201_1.html","Mitsubishi Motors news release, Feb 1, 2024: Xpander and Xpander Cross HEV premiere in Thailand"),
 ("https://www.mitsubishi-motors.com/en/newsroom/newsrelease/2026/20260406_2.html","Mitsubishi Motors news release, Apr 6, 2026: intention to join the Philippine EVIS program"),
 ("https://www.mitsubishi-motors.com.ph/articles/mmpc-official-statement","Mitsubishi Motors Philippines: official statement on the EVIS program, Oct 2026"),
 ("https://www.mitsubishi-motors.com.ph/guides/mitsubishi-xpander-eco-friendly-7-seater-philippines-2026","Mitsubishi Motors Philippines: Xpander 2026 guide (hybrid not yet available locally)"),
 ("https://www.mitsubishi-motors.co.th/en/news-activity/news/MMTh-XPANDER-XPANDER-CROSS-HEV-First-Ever-Debut-Motor-Expo-2025-0-interest","Mitsubishi Motors Thailand: New Xpander HEV and Xpander Cross HEV debut, Nov 28, 2025"),
 ("https://www.mitsubishi-motors.co.th/en/buy/all-models-price","Mitsubishi Motors Thailand: official price list"),
 ("https://www.mitsubishi-motors.co.th/en/cars/xpanderhev","Mitsubishi Motors Thailand: New Xpander HEV"),
 ("https://www.mitsubishi-motors.co.th/en/cars/xpandercrosshev","Mitsubishi Motors Thailand: New Xpander Cross HEV"),
 ("https://www.mitsubishi-motors.co.th/content/dam/mitsubishi-motors-th/images/site-images/vehicle-page-assets/xpanderhev/2024/manuals_and_guides/xpander-hev-owner-manual-en.pdf","Mitsubishi Motors Thailand: Xpander HEV owner's manual (English, PDF)"),
 ("https://www.mitsubishi-motors.com/en/newsroom/stories/phev4/index.html","Mitsubishi Motors story: the HEV system and its NEDC fuel consumption claims"),
 ("https://toyota.com.ph/zenix","Toyota Motor Philippines: Zenix"),
 ("https://content.toyota.com.ph/uploads/vehicles/49/001_49_1724138891546_000.pdf","Toyota Motor Philippines: Zenix brochure and specifications (PDF)"),
 ("https://www.mitsubishi-motors.com.ph/cars/outlander-phev","Mitsubishi Motors Philippines: Outlander PHEV"),
 ("https://www.mitsubishi-motors.com.ph/articles/mmpc-introduces-new-outlander-phev","Mitsubishi Motors Philippines: MMPC introduces the new Outlander PHEV, Aug 20, 2026"),
 ("https://www.mitsubishi-motors.com.ph/guides/enriching-life-with-outlander-phev","Mitsubishi Motors Philippines: Enriching life with the Outlander PHEV (battery and charging)")]
def XH_fig(k,alt,w,h,cap="Official photo: Mitsubishi Motors (2024 launch model)."):
    return f'<figure class="fig"><img src="/assets/img/{k}.webp" alt="{e(alt)}" width="{w}" height="{h}" loading="lazy" decoding="async"><figcaption class="zsm">{e(cap)}</figcaption></figure>'
def XH_msg(place,cls="btn",label="Message Richard for Xpander Hybrid updates"):
    return f'<a class="{cls}" href="{MSG}" rel="noopener" data-msgr="xpander-hybrid-{e(place)}" data-track="msg" data-place="{e(place)}">{label}</a>'
def XH_watch():
    """Lite YouTube Short facade (9:16): poster + play button, iframe loads on click."""
    import json as _json
    vid="G7ooToxPNQU"
    name="Xpander Hybrid Philippines: Fuel Consumption, Specs & PH Release (2026)"
    desc="A 60-second explainer of the Mitsubishi Xpander Hybrid (HEV): official specs, fuel consumption, and Philippine release status. The model is not sold in the Philippines yet; Mitsubishi Motors Philippines has not announced a local launch date or SRP."
    poster=f"https://i.ytimg.com/vi/{vid}/oardefault.jpg"  # official 9:16 thumb; hqdefault is 16:9 and crops poorly
    hq=f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg"
    embed=f"https://www.youtube-nocookie.com/embed/{vid}"
    watch=f"https://www.youtube.com/shorts/{vid}"
    ld=_json.dumps({"@context":"https://schema.org","@type":"VideoObject","name":name,"description":desc,
        "thumbnailUrl":[poster,hq],"uploadDate":"2026-11-17","embedUrl":embed,"contentUrl":watch},ensure_ascii=False)
    css=(
        ".xh-watch{margin:32px 0 8px}.xh-watch .muted,.xh-watch noscript{text-align:center;max-width:360px;margin-left:auto;margin-right:auto}"
        ".xh-yt{position:relative;margin:0 auto;max-width:360px;width:100%;aspect-ratio:9/16;background:#0b0b0c;border-radius:var(--r);overflow:hidden}"
        ".xh-yt iframe,.xh-yt-facade{position:absolute;inset:0;width:100%;height:100%;border:0;display:block}"
        ".xh-yt-facade{padding:0;background:#0b0b0c;cursor:pointer}"
        ".xh-yt-facade img{width:100%;height:100%;object-fit:cover;object-position:center}"
        ".xh-yt-play{position:absolute;left:50%;top:50%;width:68px;height:48px;margin:-24px 0 0 -34px;background:var(--red);border-radius:14px;box-shadow:0 4px 16px rgba(0,0,0,.35);pointer-events:none;transition:background .15s,transform .15s}"
        ".xh-yt-play:before{content:\"\";position:absolute;left:26px;top:14px;border-style:solid;border-width:10px 0 10px 16px;border-color:transparent transparent transparent #fff}"
        ".xh-yt-facade:hover .xh-yt-play,.xh-yt-facade:focus-visible .xh-yt-play{background:var(--redd);transform:scale(1.06);transform-origin:center}"
        ".xh-yt-facade:focus-visible{outline:3px solid var(--red);outline-offset:3px}"
    )
    js=(
        "(function(){var r=document.getElementById(\"xh-yt\");if(!r)return;var b=r.querySelector(\"[data-yt]\");if(!b)return;"
        "b.addEventListener(\"click\",function(){var f=document.createElement(\"iframe\");"
        "f.src=\"https://www.youtube-nocookie.com/embed/\"+b.getAttribute(\"data-yt\")+\"?autoplay=1\";"
        "f.title="+_json.dumps(name)+";"
        "f.setAttribute(\"allow\",\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\");"
        "f.setAttribute(\"allowfullscreen\",\"\");f.setAttribute(\"loading\",\"lazy\");"
        "f.setAttribute(\"referrerpolicy\",\"strict-origin-when-cross-origin\");b.replaceWith(f);f.focus();});})();"
    )
    return (
        f"<style>{css}</style>"
        f'<section class="xh-watch" aria-label="{e(name)}">'
        f"<h2>Watch: Xpander Hybrid in 60 seconds</h2>"
        f"<p>A short explainer of the official specs, fuel consumption, and what Mitsubishi Motors has announced about a Philippine release.</p>"
        f'<div class="xh-yt" id="xh-yt">'
        f'<button type="button" class="xh-yt-facade" data-yt="{vid}" aria-label="Play video: {e(name)}">'
        f'<img src="{poster}" alt="{e(name)}" width="360" height="640" loading="lazy" decoding="async">'
        f'<span class="xh-yt-play" aria-hidden="true"></span></button></div>'
        f'<p class="muted">Also on <a href="{watch}" rel="noopener" target="_blank">YouTube</a>.</p>'
        f'<noscript><p><a href="{watch}" rel="noopener" target="_blank">Watch on YouTube</a></p></noscript>'
        f"</section>"
        f'<script type="application/ld+json">{ld}</script>'
        f"<script>{js}</script>"
    )

_xh=W_A(slug="xpander-hybrid-philippines",car="xpander",date="2026-11-16",img="xh_hero",
 alt="Mitsubishi Xpander HEV hybrid MPV in White Diamond, official Mitsubishi Motors launch photo",crumbs=CR_GT,
 title="Xpander Hybrid Philippines: Specs, Fuel Consumption | SJDM, San Jose del Monte",seo="Xpander Hybrid Fuel Consumption | SJDM San Jose del Monte",
 desc="Xpander Hybrid (HEV): fuel consumption, electric specs, hybrid 7-seater comparison and PH status. No PH SRP yet. Richard, SJDM, San Jose del Monte.",
 answer="The Xpander Hybrid (Xpander HEV and Xpander Cross HEV) has been on sale in Thailand since February 1, 2024. Mitsubishi Motors Philippines has not announced a local launch date or SRP, so it is not available in the Philippines yet.",
 faq=[("Is the Xpander Hybrid available in the Philippines?","Not yet. Mitsubishi Motors Philippines (MMPC) sells the Xpander and Xpander Cross with a 1.5L gasoline engine. The hybrid versions are sold in Thailand, and MMPC has not announced a Philippine launch."),
  ("When will the Xpander Hybrid come to the Philippines?","There is no announced date. In April 2026, Mitsubishi Motors said MMPC plans to start building a new hybrid model at its Santa Rosa, Laguna plant around mid-2028, subject to approval under the government's EVIS program. Mitsubishi Motors has not said which model it will be."),
  ("How much is the Xpander Hybrid in the Philippines?","There is no Philippine SRP. In Thailand, the official price is THB 935,000 for the Xpander HEV and THB 953,000 for the Xpander Cross HEV. That is about ₱1,755,000 and ₱1,789,000 at the BSP reference rate of November 12, 2026, for reference only. A future Philippine price could be quite different."),
  ("What engine does the Xpander HEV have?","According to Mitsubishi Motors Thailand, a 1.6L MIVEC gasoline engine (95 PS, 134 Nm) works with an 85 kW (116 PS) electric motor with 255 Nm of torque and a lithium-ion hybrid battery, driving the front wheels."),
  ("What is the Xpander Hybrid's fuel consumption?","According to Mitsubishi Motors, fuel consumption is about 34% better in urban driving and about 15% better in combined driving than its gasoline CVT model, on the NEDC lab test used in Thailand. Mitsubishi Motors hasn't published a km/L figure in the official sources I checked, so I don't quote one. Real-world results depend on how and where you drive."),
  ("Do you need to charge the Xpander Hybrid? Is it a plug-in hybrid?","No. It is a full hybrid (HEV), not a plug-in. According to the Xpander HEV owner's manual, the drive battery is charged by the engine and by regenerative braking, so it doesn't need charging from an outside source. There is no charging port."),
  ("What battery does the Xpander Hybrid use?","A lithium-ion drive battery placed under the front seats, according to Mitsubishi Motors. Mitsubishi Motors hasn't published the battery capacity in the brochure or owner's manual I checked."),
  ("How far can the Xpander Hybrid run on electricity alone?","Mitsubishi Motors doesn't publish an EV-only range for the Xpander HEV. The owner's manual says EV drive is mainly used when starting off, the EV cruising range varies with driving conditions, and it gets shorter at high speed or uphill."),
  ("Xpander Hybrid vs Toyota Zenix Hybrid: what's the difference?","Both are seven-seat full hybrids that don't plug in. On official specs, the Xpander HEV (Thailand) has a 1.6L engine and an 85 kW (116 PS), 255 Nm motor. The Zenix 2.0 Q HEV sold by Toyota Motor Philippines has a 2.0L engine (152 PS), a 113 PS motor generator and 186 PS total system output, and it is longer and wider. Only the Zenix is sold in the Philippines today."),
  ("Is there a 7-seater hybrid in the Philippines?","Yes. For example, Toyota Motor Philippines sells the Zenix 2.0 Q HEV, a seven-seat full hybrid. The Xpander Hybrid isn't sold here yet. Mitsubishi Motors Philippines' Outlander PHEV is a plug-in hybrid, but it seats five."),
  ("HEV vs PHEV: which is better?","It depends on how you drive. An HEV like the Xpander HEV charges itself and never needs a plug. A PHEV like the Outlander PHEV has a much bigger battery you charge from a socket: Mitsubishi Motors Philippines quotes up to 100 km of pure electric range. If you can't charge at home, an HEV is simpler. If you can, a PHEV can cover short daily trips on electricity."),
  ("Can I reserve an Xpander Hybrid with Richard now?","Not yet, because there are no Philippine variants or prices to reserve. Message me and I will update you when MMPC announces local details. If you need a seven-seater now, the current Xpander and Xpander Cross are available.")],
 more=[("/cars/xpander/","Mitsubishi Xpander 2026"),
      ("/blog/xpander-variants-explained/","Xpander variants explained"),
      ("/blog/best-7-seater-for-filipino-families-2026/","Best 7-seater for Filipino families 2026")],
 body=f'''<p>Many of you in San Jose del Monte (SJDM) and around Bulacan have asked me about the <b>Xpander Hybrid</b>. Mitsubishi calls it the <b>Xpander HEV</b> (hybrid electric vehicle), and there is also an <b>Xpander Cross HEV</b>. This page puts what Mitsubishi Motors has officially announced in one place: where it is sold, the key specs, its official Thai prices converted to pesos for reference, and how it compares with the Xpander we sell here today.</p>
<div class="box ans"><p><b>Not available in the Philippines yet:</b> Mitsubishi Motors Philippines (MMPC) has not announced a local launch date, variants or SRP for the Xpander Hybrid. It is not in Philippine showrooms, so I can't quote a local price or take reservations for it yet. I'll update this page when MMPC announces local details.</p></div>
{XH_watch()}
<h2>What is the Xpander Hybrid?</h2>
<p>According to Mitsubishi Motors, the Xpander HEV and Xpander Cross HEV are full hybrid versions of the Xpander seven-seater. They don't need charging from a plug: a 1.6L gasoline engine and a generator make electricity, and an electric motor drives the front wheels. Mitsubishi Motors says the system was newly developed from its plug-in hybrid (PHEV) technology.</p>
<p>The car runs on the battery alone when starting off and at low speeds. It switches to hybrid driving when climbing or accelerating, the engine helps at high speeds, and braking recovers energy back into the battery. Mitsubishi Motors put the drive battery under the front seats, so the three-row, seven-seat cabin is kept.</p>
{XH_fig("xh_cross","Mitsubishi Xpander Cross HEV hybrid in Graphite Gray, official Mitsubishi Motors photo",1200,800,"Xpander Cross HEV. Official photo: Mitsubishi Motors (2024 launch model).")}
<h2>Philippine release status</h2>
<div class="tw"><table class="pt"><thead><tr><th scope="col">Date</th><th scope="col">What Mitsubishi announced</th></tr></thead><tbody>
<tr><th scope="row">Feb 1, 2024</th><td>Global debut of the Xpander HEV and Xpander Cross HEV, on sale in Thailand the same day. Built at the Laem Chabang Plant in Thailand.</td></tr>
<tr><th scope="row">Nov 28, 2025</th><td>Mitsubishi Motors Thailand shows the updated 2026 model year Xpander HEV and Xpander Cross HEV, with six airbags and Diamond Sense driver-assist features.</td></tr>
<tr><th scope="row">Apr 6, 2026</th><td>Mitsubishi Motors announces its intention to join the Philippine government's Electric Vehicle Incentive Strategy (EVIS). Subject to approval, MMPC plans to start building a <b>new hybrid model</b> in Santa Rosa, Laguna around mid-2028. The model was not named.</td></tr>
<tr><th scope="row">Oct 2026</th><td>MMPC reaffirms its EVIS commitment and says it is preparing for registration under the program.</td></tr>
<tr><th scope="row">As of Nov 16, 2026</th><td>No Philippine launch date, variants or SRP for the Xpander Hybrid. MMPC's lineup lists the Xpander and Xpander Cross with gasoline engines only.</td></tr>
</tbody></table></div>
<p>Please don't assume the hybrid that MMPC plans to build in Laguna will be the Xpander. Mitsubishi Motors hasn't said which model it is. Treat any Philippine launch month you see online as unconfirmed until MMPC announces it.</p>
<h2>Key specs, according to Mitsubishi Motors</h2>
<p>These are the official Thailand figures for the 2026 model year. Specs may vary by market, and Philippine specs have not been announced.</p>
<div class="tw"><table class="pt"><thead><tr><th scope="col">Item</th><th scope="col">Official figure (Thailand)</th></tr></thead><tbody>
<tr><th scope="row">Engine</th><td>1.6L (1,590 cc) 4-cylinder DOHC 16-valve MIVEC gasoline, Atkinson cycle: 95 PS at 5,100 rpm, 134 Nm at 4,500 rpm</td></tr>
<tr><th scope="row">Electric motor</th><td>85 kW (116 PS), 255 Nm</td></tr>
<tr><th scope="row">Hybrid battery</th><td>Lithium-ion</td></tr>
<tr><th scope="row">Transmission and drive</th><td>Transaxle, front-wheel drive, with Active Yaw Control (AYC)</td></tr>
<tr><th scope="row">Drive modes</th><td>7: Normal, Wet, Gravel, Tarmac and Mud, plus EV Priority and Charge</td></tr>
<tr><th scope="row">Seating</th><td>Three rows, seven seats</td></tr>
<tr><th scope="row">Length × width × height</th><td>4,595 × 1,750 × 1,750 mm (Xpander Cross HEV: 1,790 mm wide)</td></tr>
<tr><th scope="row">Wheelbase</th><td>2,775 mm</td></tr>
<tr><th scope="row">Ground clearance</th><td>205 mm</td></tr>
<tr><th scope="row">Wheels and brakes</th><td>17-inch alloys (205/55 R17); disc brakes front and rear</td></tr>
<tr><th scope="row">Fuel tank</th><td>40 L</td></tr>
<tr><th scope="row">Safety</th><td>Six airbags; Lane Departure Warning, Blind Spot Warning with Lane Change Assist, and Rear Cross Traffic Alert. Mitsubishi Motors Thailand lists a 4-star ASEAN NCAP rating.</td></tr>
<tr><th scope="row">Cabin</th><td>10-inch touchscreen with Apple CarPlay and Android Auto, 8-inch LCD meter, Heat Guard synthetic leather seats. The Cross HEV adds a Multi Around Monitor.</td></tr>
</tbody></table></div>
<p class="muted">Thailand specification, from Mitsubishi Motors Thailand's 2026 model year brochures and website.</p>
{XH_fig("xh_cabin","Dashboard and front seats of the Mitsubishi Xpander HEV, official Mitsubishi Motors photo",1200,800)}
<h2>Overseas prices in pesos (reference only)</h2>
<div class="box ans"><p><b>Not a Philippine price.</b> These are official Thailand prices converted to pesos for reference only. They are not the Philippine SRP and not a prediction of it. Only MMPC sets the Philippine SRP.</p></div>
<div class="tw"><table class="pt"><thead><tr><th scope="col">Model (Thailand)</th><th scope="col">Official price</th><th scope="col">Approx. in pesos</th></tr></thead><tbody>
<tr><th scope="row">Xpander HEV</th><td>THB 935,000</td><td>≈ ₱1,755,000</td></tr>
<tr><th scope="row">Xpander Cross HEV</th><td>THB 953,000</td><td>≈ ₱1,789,000</td></tr>
</tbody></table></div>
<p class="muted">Mitsubishi Motors Thailand says these prices exclude dealer accessories and installation (THB 14,000 on the Xpander HEV and THB 26,000 on the Cross HEV), for totals of THB 949,000 (≈ ₱1,782,000) and THB 979,000 (≈ ₱1,838,000). Two-tone colors add THB 15,000. Prices are from the official Thai price list as of November 16, 2026.</p>
<p class="muted"><b>Exchange rate:</b> BSP reference rate published November 12, 2026: THB 1 = ₱1.8774. Rounded to the nearest thousand pesos. These peso figures will move with the exchange rate.</p>
<p>Why these are not a Philippine price:</p>
<ul class="ticks">
<li>Exchange rates, import duties, taxes and what is included in the price differ by market.</li>
<li>Thai prices include Thai taxes and Thai-spec equipment.</li>
<li>Any future Philippine version could have different specs, variants and inclusions.</li>
</ul>
<h2>Xpander Hybrid vs the Xpander on sale here today</h2>
<p>Feature comparison only. The hybrid figures are Mitsubishi Motors Thailand's; the current Xpander figures are Mitsubishi Motors Philippines'.</p>
<div class="tw"><table class="pt"><thead><tr><th scope="col">Feature</th><th scope="col">Xpander HEV (Thailand)</th><th scope="col">Xpander (Philippines today)</th></tr></thead><tbody>
<tr><th scope="row">Power source</th><td>1.6L gasoline engine plus electric motor (full hybrid)</td><td>1.5L MIVEC gasoline engine</td></tr>
<tr><th scope="row">Output</th><td>Engine 95 PS / 134 Nm; motor 116 PS / 255 Nm</td><td>105 PS / 141 Nm</td></tr>
<tr><th scope="row">Transmission</th><td>Transaxle</td><td>4-speed AT or 5-speed MT</td></tr>
<tr><th scope="row">Battery-only (EV) driving</th><td>Yes, with EV Priority mode</td><td>No</td></tr>
<tr><th scope="row">Drive modes</th><td>7, including EV Priority and Charge</td><td>Not offered</td></tr>
<tr><th scope="row">Seating</th><td>7</td><td>7</td></tr>
<tr><th scope="row">Length and wheelbase</th><td>4,595 mm; 2,775 mm</td><td>4,595 mm; 2,775 mm</td></tr>
<tr><th scope="row">Ground clearance</th><td>205 mm</td><td>225 mm</td></tr>
<tr><th scope="row">Available in the Philippines</th><td>Not yet</td><td>Yes, four variants including the Xpander Cross</td></tr>
</tbody></table></div>
<p>The current Xpander lineup and its official promos are on the <a href="/cars/xpander/">Mitsubishi Xpander 2026</a> page.</p>
<h2>Xpander Hybrid fuel consumption and electric specs</h2>
<div class="box ans"><p><b>Fuel consumption, according to Mitsubishi Motors:</b> about <b>34% better in urban driving</b> and about <b>15% better combined</b> than its gasoline CVT model, on the NEDC lab test commonly used in Thailand. Mitsubishi Motors also says the engine on its own is about 10% more fuel efficient. These are percentages, not km/L. Mitsubishi Motors hasn't published a km/L figure in the official sources I checked.</p></div>
<p>New cars in Thailand also carry a government Eco Sticker label with fuel and CO2 figures. I couldn't confirm the Xpander HEV's label figure from an official source, so I haven't listed a km/L number. km/L figures you see online vary by source and test.</p>
<div class="tw"><table class="pt"><thead><tr><th scope="col">Item</th><th scope="col">According to Mitsubishi Motors (Thailand)</th></tr></thead><tbody>
<tr><th scope="row">Electric motor</th><td>S91 motor: 85 kW (116 PS) maximum output, 255 N·m; maximum 30-minute power 40 kW</td></tr>
<tr><th scope="row">Engine</th><td>4A92 1.6L (1,590 cc): 70 kW (95 PS) at 5,100 rpm, 134 N·m at 4,500 rpm. Its main job is to generate power.</td></tr>
<tr><th scope="row">Drive battery</th><td>Lithium-ion, under the front seats. Capacity not published.</td></tr>
<tr><th scope="row">Charging</th><td>No plug. The battery is charged by the engine and by regenerative braking.</td></tr>
<tr><th scope="row">EV (battery-only) driving</th><td>Mainly when starting off and at low speeds. No official EV-only range. It gets shorter at high speed or uphill.</td></tr>
<tr><th scope="row">EV Priority mode</th><td>Runs on the battery without starting the engine. Not available when the battery is low, cruise control is on or the battery is too cold.</td></tr>
<tr><th scope="row">Charge mode</th><td>Runs the engine to charge the battery to nearly full, while driving or stopped. Use it only in a well-ventilated space.</td></tr>
<tr><th scope="row">Regenerative braking</th><td>Recovers energy when you lift off the accelerator or brake. The "B" selector position gives stronger regenerative braking.</td></tr>
<tr><th scope="row">Top speed and weight</th><td>155 km/h; kerb weight 1,455 to 1,460 kg</td></tr>
<tr><th scope="row">Fuel tank</th><td>40 L</td></tr>
</tbody></table></div>
<p class="muted">From the Xpander HEV owner's manual and 2026 model year brochure (Mitsubishi Motors Thailand) and Mitsubishi Motors' Feb 1, 2024 news release.</p>
<p>The engine can also start on its own. According to the owner's manual, the car switches from EV to hybrid drive when you accelerate hard, climb or drive on an expressway with a heavy foot, use the air conditioning, or when the system is too hot or too cold.</p>
<h2>How it compares with other hybrid 7-seaters</h2>
<p>This is a spec comparison only, using each maker's official figures. The Zenix 2.0 Q HEV is a seven-seat full hybrid that Toyota Motor Philippines sells here. The gasoline Xpander is shown as a baseline.</p>
<div class="tw"><table class="pt"><thead><tr><th scope="col">Spec</th><th scope="col">Xpander HEV (Thailand)</th><th scope="col">Toyota Zenix 2.0 Q HEV (PH)</th><th scope="col">Xpander gasoline (PH)</th></tr></thead><tbody>
<tr><th scope="row">Sold in the Philippines</th><td>Not yet</td><td>Yes</td><td>Yes</td></tr>
<tr><th scope="row">Type</th><td>Full hybrid, self-charging</td><td>Full hybrid, self-charging</td><td>Gasoline</td></tr>
<tr><th scope="row">Engine</th><td>1.6L (1,590 cc), 95 PS, 134 Nm</td><td>2.0L (1,987 cc), 152 PS, 188 Nm</td><td>1.5L (1,499 cc), 105 PS, 141 Nm</td></tr>
<tr><th scope="row">Electric motor</th><td>116 PS (85 kW), 255 Nm</td><td>113 PS (motor generator)</td><td>None</td></tr>
<tr><th scope="row">Total system output</th><td>Not published</td><td>186 PS</td><td>105 PS</td></tr>
<tr><th scope="row">Drive battery</th><td>Lithium-ion</td><td>Not listed in the brochure</td><td>None</td></tr>
<tr><th scope="row">Plug-in charging</th><td>No</td><td>No</td><td>Not applicable</td></tr>
<tr><th scope="row">EV-only driving</th><td>Yes, EV Priority mode</td><td>Yes, EV Mode</td><td>No</td></tr>
<tr><th scope="row">Transmission and drive</th><td>Transaxle, front-wheel drive</td><td>CVT, front-wheel drive</td><td>4-speed AT or 5-speed MT</td></tr>
<tr><th scope="row">Seats</th><td>7</td><td>7</td><td>7</td></tr>
<tr><th scope="row">Length × width × height</th><td>4,595 × 1,750 × 1,750 mm</td><td>4,755 × 1,850 × 1,790 mm</td><td>4,595 × 1,750 × 1,750 mm</td></tr>
<tr><th scope="row">Fuel tank</th><td>40 L</td><td>52 L</td><td>Not listed here</td></tr>
<tr><th scope="row">Official fuel consumption claim</th><td>About 34% better urban and 15% better combined vs its gasoline CVT model (NEDC)</td><td>Not stated in the brochure</td><td>Not stated</td></tr>
</tbody></table></div>
<p class="muted">Sources: Mitsubishi Motors Thailand (Xpander HEV), Toyota Motor Philippines' Zenix brochure (Zenix 2.0 Q HEV) and Mitsubishi Motors Philippines (Xpander). Makers test and publish figures in different ways, and the Xpander HEV figures are for Thailand, so these numbers aren't directly comparable. Fuel consumption figures from different tests (NEDC, WLTP or others) shouldn't be compared side by side.</p>
<h2>HEV vs PHEV vs gas: what's the difference?</h2>
<p>People often search "hybrid vs PHEV". Here's the difference, using three Mitsubishi models: the gasoline Xpander, the Xpander HEV and the Outlander PHEV.</p>
<div class="tw"><table class="pt"><thead><tr><th scope="col">Question</th><th scope="col">Gas (Xpander, PH)</th><th scope="col">HEV (Xpander HEV, Thailand)</th><th scope="col">PHEV (Outlander PHEV, PH)</th></tr></thead><tbody>
<tr><th scope="row">What moves the car</th><td>1.5L gasoline engine</td><td>Mostly the electric motor. The 1.6L engine generates power and helps at high speed.</td><td>Front and rear electric motors (116 PS and 136 PS) with a 2.4L gasoline engine</td></tr>
<tr><th scope="row">Drive battery</th><td>None</td><td>Lithium-ion, capacity not published</td><td>Lithium-ion, 22.7 kWh</td></tr>
<tr><th scope="row">Do you plug it in?</th><td>No</td><td>No, it charges itself</td><td>Yes: Type 2 AC charging and CHAdeMO DC quick charging</td></tr>
<tr><th scope="row">Pure electric driving</th><td>None</td><td>Short distances, mainly starting off and at low speeds</td><td>Up to 100 km, according to MMPC (test cycle not stated; actual range varies)</td></tr>
<tr><th scope="row">Seats</th><td>7</td><td>7</td><td>5</td></tr>
<tr><th scope="row">Sold in the Philippines</th><td>Yes</td><td>Not yet</td><td>Yes</td></tr>
</tbody></table></div>
<ul class="ticks">
<li><b>Gas:</b> the simplest setup, with one engine and no drive battery.</li>
<li><b>HEV (full hybrid):</b> nothing changes in your routine. You fill up with gasoline, and the car uses its battery and motor to save fuel, especially in stop-and-go traffic.</li>
<li><b>PHEV (plug-in hybrid):</b> a much bigger battery that you charge from a socket. If you can charge at home, many daily trips can be electric, and the engine is there for long drives.</li>
</ul>
<p>Want to see the plug-in option? Read the <a href="/cars/outlander-phev/">Outlander PHEV</a> page.</p>
{XH_fig("xh_drive","Mitsubishi Xpander Cross HEV driving on a gravel road with headlights on, official Mitsubishi Motors photo",1200,800,"Xpander Cross HEV. Official photo: Mitsubishi Motors (2024 launch model).")}
<h2>Fun facts about the Xpander Hybrid</h2>
<ul class="ticks">
<li><b>Built from plug-in hybrid know-how.</b> Mitsubishi Motors says the HEV system was newly developed from its PHEV technology, the same family as the Outlander PHEV.</li>
<li><b>A quiet mode for early mornings.</b> EV Priority mode runs on the battery without starting the engine, which Mitsubishi Motors pitches for quiet drives through residential areas early in the morning. If the battery is low, Charge mode tops it up, whether moving or stopped.</li>
<li><b>255 Nm from the electric motor.</b> That torque arrives quickly from a standstill, which Mitsubishi Motors says helps with merging and U-turns in city traffic.</li>
<li><b>A Mitsubishi first under the hood.</b> The 1.6L engine uses the first electric water pump ever fitted to a Mitsubishi Motors engine, to cut mechanical losses.</li>
<li><b>Better city fuel consumption.</b> According to Mitsubishi Motors, it's about 34% better in urban driving and about 15% better combined than its gasoline CVT model, on the NEDC lab test.</li>
<li><b>Seven seats kept.</b> The drive battery sits under the front seats, so the hybrid keeps the Xpander's three rows.</li>
<li><b>Made in Thailand.</b> The Xpander HEV and Xpander Cross HEV are built at Mitsubishi Motors' Laem Chabang Plant in Thailand.</li>
</ul>
<h2>What you can do now</h2>
<p>If you're waiting for the Xpander Hybrid, tap the Messenger button on this page and I'll update you when Mitsubishi Motors Philippines announces local details such as the launch date, variants and SRP.</p>
<p class="row">{XH_msg("article")}</p>
<p>If your family needs a seven-seater now, the current <a href="/cars/xpander/">Xpander and Xpander Cross</a> are on sale in the Philippines. You can see every variant there, or read <a href="/blog/xpander-variants-explained/">Xpander variants explained</a>.</p>
<h2>Official sources</h2>
<ul class="links">{"".join(f'<li><a href="{u}" rel="noopener" target="_blank">{e(t)}</a></li>' for u,t in XH_SRC)}</ul>
<p class="muted">Photos: official Mitsubishi Motors newsroom images of the 2024 launch model, used here for editorial purposes. I'll update this page when Mitsubishi Motors Philippines announces local details.</p>
<p class="row">{XH_msg("article-end",cls="btn ghost dk",label="Message Richard")}</p>{W_LOCAL}
''')
_xh["mod"]="2026-11-17"
_xh["no_finance_cta"]=True  # not sold in PH; loan/monthly CTAs would send people to another car
WA.append(_xh)
_WS={a["slug"] for a in WA}
XL.pop("triton-gx-2wd-at-first-pickup-guide",None) if "XL" in globals() else None
POSTS[:]=[a for a in POSTS if a["slug"] not in _WS]+WA
def W_SCRUB(R):
    """changed pages only: remove no-DP promo labels injected by shared modules (promosab) and stray links to the no-DP guides"""
    for p in W_PATHS+["/triton-downpayment-and-monthly/","/mitsubishi-sjdm-bulacan/"]:
        fp=R+p+"index.html"
        if not os.path.exists(fp): continue
        s=open(fp).read();o=s
        s=s.replace('<span class="ab-zt">Zero DP Promo</span>','').replace('<b class="ab-z">Zero DP Promo</b>','<b class="ab-z">Low DP</b>')
        s=_w_re.sub(r',? up to Zero DP','',s);s=_w_re.sub(r',? hanggang Zero DP','',s)
        s=_w_re.sub(r'<li><a href="/(?:mitsubishi-zero-down-payment-promo|guides/zero-dp-vs-low-dp|blog/zero-down-payment-car-philippines)/">[^<]*</a></li>','',s)
        if s!=o: open(fp,"w").write(s)
# price pages also get the sticky action bar + ViewContent marker (strategy 3.0.1)
for _a in WA:
    if "price-philippines" in _a["slug"]: _a["after"]=W_vc(_a["car"],"price")+W_sbar(_a["car"],WM[_a["car"]]["name"],W_from(_a["car"]))
