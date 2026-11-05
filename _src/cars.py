# Other-models plan (DRAFT, branch draft-cars, Nov 2026): OTHER_CARS_STRATEGY.md assets A1-A17.
# exec()'d inside build.py right after wave1.py (reuses W_* helpers, page, img, e, f, MODELS, MSG, D, POSTS, TIPS, GUIDES, FIGS, CALC, offers_ld).
# House rules: English only; Low DP wording only (lowest option WITH a down payment); "Pre-qualified, subject to bank approval";
# Mitsubishi specs only "according to Mitsubishi Motors" (MANUFACTURER_CLAIMS_OTHER_MODELS.md; items marked not found are skipped);
# no fuel economy figures; no competitor prices; prices = FRESH label (data.py). No peso figure is invented: all come from data.py / optionAB.
C_PATHS=[]   # every new or changed URL of this plan (scrubbed + checked)
def C_chk(t,d,where):
    assert len(t)<60,(where,"title",len(t),t); assert len(d)<155,(where,"desc",len(d),d)
def C_srp(v): return v["srp"] or (v["promo"] or {}).get("srp") or (v.get("ab") or {}).get("srp")
def C_short(v,m): return W_short(v,m).replace("2026 ","")
def C_vtable(slug,place="variant-row"):
    m=WM[slug];rows=""
    for v in m["variants"]:
        t,d=W_trans(v["n"]);lo=W_low(v);fu=(v["promo"] or {}).get("fuel")
        dp=f(lo[0]) if lo else "Ask Richard";mo=(f'<b>{f(lo[1])}</b>/mo' if lo else "Ask Richard")
        fz=f'<br><small class="fpts">+ {fu:,} fuel points</small>' if fu else ""
        rows+=f'<tr><th scope="row">{e(C_short(v,m))}</th><td>{t}</td><td>{f(C_srp(v))}</td><td>{dp}</td><td>{mo}{fz}</td><td>{W_msg(slug,place,v["n"],label="Ask about this")}</td></tr>'
    return (f'{W_badge()}<div class="tw"><table class="pt vtab"><thead><tr><th scope="col">Variant</th><th scope="col">Transmission</th><th scope="col">SRP</th><th scope="col">Low DP</th><th scope="col">Sample monthly</th><th scope="col">Message</th></tr></thead><tbody>{rows}</tbody></table></div>'
            f'<p class="muted vnote">SRP: {e(FRESH)}; freight and handling not included. Low DP: lowest published promo option with a down payment. Sample monthly: 60 months, all-in. {MSQ}.</p>')
def C_ptab(slug):
    m=WM[slug];rows=""
    for v in m["variants"]:
        lo=W_low(v)
        rows+=f'<tr><th scope="row">{e(C_short(v,m))}</th><td>{f(C_srp(v))}</td><td>{f(lo[0]) if lo else "Ask Richard"}</td><td>{(f(lo[1])+"/mo") if lo else "Ask Richard"}</td></tr>'
    return f'{W_badge()}<div class="tw"><table class="pt"><thead><tr><th scope="col">Variant</th><th scope="col">SRP</th><th scope="col">Low DP</th><th scope="col">Sample monthly</th></tr></thead><tbody>{rows}</tbody></table></div><p class="muted">SRP: {e(FRESH)}; freight and handling not included. 60 months, all-in. {MSQ}.</p>'
def C_lo(vid):
    for m in MODELS:
        for v in m["variants"]:
            if v["id"]==vid: return v,W_low(v)
def C_tiles(items): return W_tiles(items).replace("According to Mitsubishi Motors Philippines.","Specs according to Mitsubishi Motors Philippines.")
def C_cta(slug,name,unit,biz=False):
    return (f'<h2>Your next step</h2><p>Compare the numbers, then see the {e(name)} in person in San Jose del Monte (SJDM).</p>'
            f'<p class="row">{W_pq(slug,"article-end",cls="btn",label="Get my "+e(name)+" Pre-qualification (2 min)")} <a class="btn ghost dk" href="/budgetcalculator/?m={unit}">Compute my {e(name)} monthly</a> <a class="btn ghost dk" href="/test-drive/?unit={unit}">Book a test drive in SJDM</a></p>'
            f'<p class="row">{W_msg(slug,"article-end",cls="btn ghost dk",label=("Business buyer? Message Richard" if biz else "Message Richard about the "+e(name)))}</p>'
            '<p class="wloc">Buying in Bulacan? See <a href="/mitsubishi-sjdm-bulacan/">Mitsubishi San Jose del Monte (SJDM)</a> and the <a href="/mitsubishi-price-list-philippines/">full Mitsubishi price list</a>.</p>')
PL_LINK='<a href="/mitsubishi-price-list-philippines/">Full Mitsubishi price list</a>'

# ================= SPECS (MANUFACTURER_CLAIMS_OTHER_MODELS.md only; "not found" items skipped)
SP_XP=[("Engine","1.5L in-line 4 DOHC 16V MIVEC gasoline (4A91), 1,499 cc"),("Max power / torque","105 PS @ 6,000 rpm / 141 Nm @ 4,000 rpm"),("Transmission","4-speed AT or 5-speed MT"),("Seating","7"),("Dimensions (L x W x H)","4,595 x 1,750 x 1,750 mm; wheelbase 2,775 mm"),("Ground clearance","225 mm"),("Safety","Driver and passenger airbags, ABS with EBD, ISO-Fix; the GLS adds ASC, Traction Control, Active Yaw Control, Hill Start Assist and Multi-Around Monitor")]
SP_XC=[("Engine","1.5L MIVEC DOHC 16-valve gasoline"),("Transmission / drive","4-speed AT, front-wheel drive (2WD)"),("Seating","7 (family-friendly crossover MPV)"),("Ground clearance","225 mm"),("Safety","Dual front airbags, ABS with EBD, Brake Assist, ASC, Traction Control, AYC, HSA, Multi-Around Monitor, ISO-Fix")]
SP_MI=[("Engine","1.2L 12-valve inline 3-cylinder DOHC MIVEC (3A92)"),("Transmission","INVECS III CVT or 5-speed manual"),("Seating","Space for 5 adults"),("Dimensions (L x W x H)","3,795 x 1,665 x 1,500 mm"),("Turning radius","4.6 m"),("Safety","Front SRS airbags; front 3-point ELR seatbelts with pretensioner")]
SP_G4=[("Engine","1.2L in-line 3 DOHC MIVEC (3A92), 1,193 cc"),("Max power / torque","78 PS @ 6,000 rpm / 100 Nm @ 4,000 rpm"),("Transmission","CVT or 5-speed MT"),("Seating / fuel tank","5 / 42 L"),("Dimensions (L x W x H)","4,305 x 1,670 x 1,515 mm; wheelbase 2,550 mm"),("Ground clearance","170 mm"),("Safety","Driver and passenger airbags, ABS with EBD, ASC, Hill Start Assist, ISO-Fix")]
SP_XF=[("Engine","1.5L 4 in-line DOHC 16V MIVEC gasoline (4A91), Euro 4"),("Max power / torque","105 PS @ 6,000 rpm / 141 Nm @ 4,000 rpm"),("Transmission","CVT"),("Seating / fuel tank","5 / 42 L"),("Dimensions (L x W x H)","4,390 x 1,810 x 1,660 mm; wheelbase 2,650 mm"),("Ground clearance","193 mm"),("Drive modes","Normal, Wet, Gravel, Mud (higher variants)"),("Safety","ASC/TCL, AYC, HSA, Emergency Stop Signal; the GT adds MMSS (FCM, LCDN, BSW, RCTA, AHB, Adaptive Cruise Control) and TPMS")]
SP_L3=[("Engine (Cab and Chassis)","4N14 2.2L 16V DOHC turbo intercooler common-rail diesel, Euro 4, 2,268 cc"),("Max power / torque","99.25 PS @ 3,500 rpm / 200 Nm @ 1,000-3,500 rpm"),("Transmission","5-speed manual"),("Dimensions (L x W x H)","4,440 x 1,695 x 1,915 mm; wheelbase 2,350 mm"),("Ground clearance / GVW","195 mm / 2,345 kg"),("Fuel tank","55 L")]
SP_VV=[("Engine","YD25 DDTI 2.5L inline-4 DOHC 16V variable turbo diesel, 2,488 cc"),("Max power / torque","129 PS @ 3,200 rpm / 356 Nm @ 1,400-2,000 rpm"),("Transmission","5-speed manual"),("Seating","15"),("Dimensions (L x W x H)","4,710 x 1,695 x 1,990 mm; wheelbase 2,555 mm"),("Ground clearance / fuel tank","195 mm / 65 L"),("Safety","Driver and passenger airbags, ABS with EBD, Vehicle Dynamic Control (VDC)")]
def _lo_txt(vid):
    v,lo=C_lo(vid); return (f"{f(lo[0])} DP and {f(lo[1])} a month" if lo else "Ask Richard")
FAQ_XP=[("How much is the Mitsubishi Xpander 2026?",f"SRP from {W_from('xpander')} (GLX M/T) to {f(1259000)} (GLS A/T), {FRESH}. See the variant table for each variant's low DP and sample monthly."),
 ("What is the lowest Xpander down payment?",f"On the GLX M/T, {_lo_txt('xglxmt')} (60 months, all-in). {MSQ}."),
 ("How many seats does the Xpander have?","Seven, according to Mitsubishi Motors Philippines."),
 ("What engine does the Xpander have?","According to Mitsubishi Motors Philippines, a 1.5L MIVEC gasoline engine (4A91) with 105 PS and 141 Nm, with a 4-speed AT or 5-speed MT."),
 ("What is the Xpander ground clearance?","225 mm, according to Mitsubishi Motors Philippines."),
 ("What does the GLS add over the GLX?","According to Mitsubishi Motors Philippines, the GLS adds ASC, Traction Control, Active Yaw Control, Hill Start Assist and the Multi-Around Monitor."),
 ("Is it Xpander or 'Expander'?","The official name is Xpander. Many buyers search for 'Expander', but it is the same Mitsubishi 7-seater MPV."),
 ("Can I test drive the Xpander in SJDM?","Yes. Book online and Richard will confirm your schedule in San Jose del Monte (SJDM), Monday to Saturday.")]
FAQ_XC=[("How much is the Xpander Cross 2026?",f"{f(1378000)} SRP for the Xpander Cross 1.5G 2WD A/T Two-Tone ({FRESH})."),
 ("What is the Xpander Cross low DP?",f"{_lo_txt('xcross')} (60 months, all-in). {MSQ}."),
 ("How many seats does the Xpander Cross have?","Seven. Mitsubishi Motors Philippines calls it a family-friendly 7-seater crossover MPV."),
 ("What is the Xpander Cross ground clearance?","225 mm, which Mitsubishi Motors Philippines describes as class-leading."),
 ("Is the Xpander Cross automatic?","Yes. According to Mitsubishi Motors Philippines, it uses a 4-speed AT with front-wheel drive."),
 ("Can I test drive it in SJDM?","Yes. Book a test drive with Richard in San Jose del Monte (SJDM).")]
FAQ_MI=[("How much is the Mirage 2026?",f"SRP {f(720000)} (GLX M/T) or {f(781000)} (GLX CVT), {FRESH}."),
 ("What is the Mirage low DP?",f"GLX M/T: {_lo_txt('mirglxmt')}; GLX CVT: {_lo_txt('mirglxcvt')} (60 months, all-in). {MSQ}."),
 ("What engine does the Mirage have?","According to Mitsubishi Motors Philippines, a 1.2L 3-cylinder DOHC MIVEC engine (3A92) with a CVT or 5-speed manual."),
 ("Is the Mirage easy to park?","According to Mitsubishi Motors Philippines, it has a 4.6-meter turning radius and seats up to five adults."),
 ("Mirage or Mirage G4?","The Mirage is the hatchback; the Mirage G4 is the sedan with a separate trunk. Compare both prices on the price list."),
 ("Can I test drive a Mirage in SJDM?","Yes. Book online and Richard will confirm in San Jose del Monte (SJDM).")]
FAQ_G4=[("How much is the Mirage G4 2026?",f"SRP from {f(793000)} (GLX M/T) to {f(937000)} (GLS CVT), {FRESH}."),
 ("What is the Mirage G4 low DP?",f"GLX M/T: {_lo_txt('mg4glxmt')} (60 months, all-in). {MSQ}."),
 ("What engine does the Mirage G4 have?","According to Mitsubishi Motors Philippines, a 1.2L MIVEC engine (3A92) with 78 PS and 100 Nm."),
 ("What safety features does it have?","According to Mitsubishi Motors Philippines: driver and passenger airbags, ABS with EBD, ASC, Hill Start Assist and ISO-Fix."),
 ("How big is the fuel tank?","42 L, according to Mitsubishi Motors Philippines."),
 ("Can I test drive the Mirage G4 in SJDM?","Yes. Book a test drive with Richard in San Jose del Monte (SJDM).")]
FAQ_XF=[("How much is the Xforce 2026?",f"SRP from {W_from('xforce')} (GLX) to {f(1661000)} (GT), {FRESH}."),
 ("What is the Xforce low DP?",f"GLX: {_lo_txt('xfglx')} (60 months, all-in). {MSQ}."),
 ("What engine does the Xforce have?","According to Mitsubishi Motors Philippines, a 1.5L MIVEC gasoline engine (4A91) with 105 PS and 141 Nm and a CVT."),
 ("How many seats does the Xforce have?","Five, according to Mitsubishi Motors Philippines."),
 ("What is the Xforce ground clearance?","193 mm, according to Mitsubishi Motors Philippines."),
 ("What does the GT add?","According to Mitsubishi Motors Philippines, Mitsubishi Motors Safety Sensing (FCM, LCDN, BSW, RCTA, AHB, Adaptive Cruise Control), TPMS and a Dynamic Sound Yamaha Premium audio with 8 speakers."),
 ("Can I test drive the Xforce in SJDM?","Yes. Book a test drive with Richard in San Jose del Monte (SJDM).")]
FAQ_L3=[("How much is the L300 2026?",f"L300 Cab and Chassis {f(829000)}; L300 Dual AC {f(1039000)} ({FRESH})."),
 ("What is the L300 low DP?",f"Cab and Chassis: {_lo_txt('l300cc')}; Dual AC: {_lo_txt('l300')} (60 months, all-in). {MSQ}."),
 ("What engine does the L300 have?","According to Mitsubishi Motors Philippines, a 2.2L Euro 4 turbo diesel (4N14) with 99.25 PS and 200 Nm, and a 5-speed manual."),
 ("Can a business owner finance an L300?","Yes. Banks usually ask for business registration, permits, ITR or financial statements and bank statements."),
 ("Can I get a custom body on the Cab and Chassis?","Yes, the Cab and Chassis is meant for a body built to your business. Ask Richard about body options and timelines."),
 ("Can I test drive an L300 in SJDM?","Yes. Book a test drive with Richard in San Jose del Monte (SJDM).")]
FAQ_VV=[("How much is the Versa Van?",f"{f(1764000)} SRP for the Versa Van GLX 2.5D 2WD M/T ({FRESH})."),
 ("What is the Versa Van low DP?",f"{_lo_txt('vvglx')} (60 months, all-in). {MSQ}."),
 ("How many seats does the Versa Van have?","15, according to Mitsubishi Motors Philippines."),
 ("What engine does the Versa Van have?","According to Mitsubishi Motors Philippines, a 2.5L YD25 DDTI turbo diesel with 129 PS and 356 Nm, and a 5-speed manual."),
 ("Is the Versa Van good for a shuttle business?","It is built for group transport. Message Richard for business financing documents and a quote."),
 ("Can I see a Versa Van in SJDM?","Yes. Message Richard to arrange a viewing in San Jose del Monte (SJDM).")]
def _md(name): return f"{name} 2026 variants, Oct 2026 list prices, low DP and monthly in SJDM, Bulacan. Pre-qualified, subject to bank approval. Book a test drive."
CUP={
"xpander":dict(title="Mitsubishi Xpander 2026 | SJDM, San Jose del Monte",h1="Mitsubishi Xpander 2026 in San Jose del Monte (SJDM)",
 desc="Xpander 2026 variants, Oct 2026 list prices, low DP and monthly in SJDM, Bulacan. Pre-qualified, subject to bank approval. Book a test drive.",specs=SP_XP,faq=FAQ_XP,c="xpander",unit="xpander",
 rel=[("/blog/xpander-price-philippines-2026/","Xpander price Philippines","Every variant's SRP, low DP and monthly"),("/blog/xpander-monthly-amortization/","Xpander monthly installment","DP and amortization"),("/cars/xpander-cross/","Xpander Cross 2026","The crossover version"),("/blog/xpander-vs-avanza/","Xpander vs Avanza","Feature comparison"),("/blog/xforce-vs-xpander/","Xforce vs Xpander","SUV or MPV"),("/blog/xpander-variants-explained/","Xpander variants explained","GLX vs GLS")]),
"xpander-cross":dict(title="Mitsubishi Xpander Cross 2026 | SJDM Bulacan",h1="Mitsubishi Xpander Cross 2026 in San Jose del Monte (SJDM)",desc=_md("Xpander Cross"),specs=SP_XC,faq=FAQ_XC,c="xpander",unit="xcross",
 rel=[("/blog/xpander-cross-2026-price-philippines/","Xpander Cross price Philippines","SRP, low DP and monthly"),("/cars/xpander/","Xpander 2026","The family MPV"),("/guides/xpander-vs-xpander-cross-vs-destinator/","Xpander vs Cross vs Destinator","Which 7-seater")]),
"mirage":dict(title="Mitsubishi Mirage 2026 Hatchback | SJDM Bulacan",h1="Mitsubishi Mirage 2026 in San Jose del Monte (SJDM)",desc=_md("Mirage"),specs=SP_MI,faq=FAQ_MI,c="mirage",unit="mirage",
 rel=[("/blog/mirage-price-philippines-2026/","Mirage price Philippines","Hatchback SRP, low DP, monthly"),("/tips/mirage-hatchback-down-payment-monthly-sjdm/","Mirage down payment and monthly","DP and monthly guide"),("/tips/mirage-hatchback-vs-mirage-g4/","Mirage vs Mirage G4","Hatchback or sedan")]),
"mirage-g4":dict(title="Mitsubishi Mirage G4 2026 Sedan | SJDM Bulacan",h1="Mitsubishi Mirage G4 2026 in San Jose del Monte (SJDM)",desc=_md("Mirage G4"),specs=SP_G4,faq=FAQ_G4,c="mirage",unit="mirage-g4",
 rel=[("/blog/mirage-g4-price-philippines-2026/","Mirage G4 price Philippines","Sedan SRP, low DP, monthly"),("/mirage-g4-downpayment-and-monthly/","Mirage G4 downpayment and monthly","DP and monthly guide"),("/tips/mirage-hatchback-vs-mirage-g4/","Mirage vs Mirage G4","Hatchback or sedan")]),
"xforce":dict(title="Mitsubishi Xforce 2026 | SJDM, San Jose del Monte",h1="Mitsubishi Xforce 2026 in San Jose del Monte (SJDM)",desc=_md("Xforce"),specs=SP_XF,faq=FAQ_XF,c="xforce",unit="xforce",
 rel=[("/tips/xforce-2026-price-philippines/","Xforce price Philippines","GLX vs GLS vs GT"),("/blog/xforce-vs-xpander/","Xforce vs Xpander","SUV or MPV"),("/blog/destinator-vs-xforce/","Destinator vs Xforce","Seats, size and features")]),
"l300":dict(title="Mitsubishi L300 2026 | SJDM, San Jose del Monte",h1="Mitsubishi L300 2026 in San Jose del Monte (SJDM)",desc=_md("L300"),specs=SP_L3,faq=FAQ_L3,c="xpander",unit="l300",biz=True,
 rel=[("/blog/l300-price-philippines-2026/","L300 price Philippines","SRP, low DP and monthly"),("/l300-monthly-installment/","L300 monthly installment","DP and monthly guide"),("/blog/l300-negosyo-guide/","L300 negosyo guide","Cab and chassis vs Dual AC"),("/blog/l300-vs-triton-for-negosyo/","L300 vs Triton","For business")]),
"versa-van":dict(title="Mitsubishi Versa Van Price 2026 | SJDM Bulacan",h1="Mitsubishi Versa Van 2026 Price in San Jose del Monte (SJDM)",desc=_md("Versa Van"),specs=SP_VV,faq=FAQ_VV,c="xpander",unit="vvglx",biz=True,
 rel=[("/mitsubishi-price-list-philippines/","Mitsubishi price list","Every model and variant"),("/budgetcalculator/?m=vvglx","Car loan calculator","Compute your monthly"),("/guides/car-loan-requirements/","Car loan requirements","Documents checklist")]),
}
for _s,_u in CUP.items():
    _m=WM[_s];C_chk(_u["title"],_u["desc"],_s)
    _u["hero_extra"]=W_hero_extra(_s,_m["name"])
    _u["top"]=f'<section class="sec" id="variants"><div class="w"><h2>{e(_m["name"])} variants, price and sample monthly</h2>{C_vtable(_s)}</div></section>'+W_calcsec(_s,_m["name"])
    _box=(f'<section class="sec"><div class="w nar"><div class="box"><h2 class="h3">Ready for the {e(_m["name"])}?</h2><p class="row">{W_pq(_s,"model-end",cls="btn",label="Get my "+e(_m["name"])+" Pre-qualification (2 min)")} <a class="btn ghost dk" href="/test-drive/?unit={_u["unit"]}">Book {"an" if _m["name"][0] in "AEIOUX" else "a"} {e(_m["name"])} test drive in SJDM</a></p>'
          +(f'<p class="row">{W_msg(_s,"model-end-biz",cls="btn ghost dk",label="Business buyer? Message Richard")}</p>' if _u.get("biz") else "")+f'<p class="muted">{PL_LINK} · <a href="/budgetcalculator/?m={_u["unit"]}">Car loan calculator</a></p></div></div></section>')
    _u["tail"]=W_trust(_u["c"])+'<section class="sec"><div class="w"><h2>Key facts</h2>'+C_tiles(_u["specs"][:6])+'</div></section>'+W_related(_u["rel"])+'<section class="sec"><div class="w nar">'+W_FAQH(_u["faq"])+W_LOCAL+'</div></section>'+_box
    _u["after"]=W_vc(_s,"model")+W_sbar(_s,_m["name"],W_from(_s))
    _u["ld"]=[W_FAQLD(_u["faq"])]
    WUP[_s]=_u; C_PATHS.append(f"/cars/{_s}/")

# ================= ARTICLES
CR_C=lambda s,n:[("/","Home"),("/cars/","Cars"),(f"/cars/{s}/",n)]
def C_A(**k):
    k=W_A(**k); C_PATHS.append(f"/{k['base']}/{k['slug']}/"); return k
_xl=C_lo("xglxmt")[1];_ml=C_lo("mirglxmt")[1];_gl=C_lo("mg4glxmt")[1];_fl=C_lo("xfglx")[1];_cl=C_lo("xcross")[1];_ll=C_lo("l300cc")[1];_la=C_lo("l300")[1]
CA=[
C_A(slug="xpander-price-philippines-2026",car="xpander",img="xpglx_x37",alt="Mitsubishi Xpander GLX, with 2026 price in the Philippines",crumbs=CR_C("xpander","Xpander"),
 title="Mitsubishi Xpander Price Philippines 2026",seo="Mitsubishi Xpander Price Philippines 2026: All Variants",
 desc="Xpander 2026 SRP per variant from the Oct 2026 list, plus low DP and sample monthly. Pre-qualified, subject to bank approval. Richard, SJDM.",
 answer=f"The Mitsubishi Xpander price in the Philippines is {f(1099000)} for the GLX M/T, {f(1159000)} for the GLX A/T and {f(1259000)} for the GLS A/T ({FRESH}).",
 faq=[("How much is the Xpander in the Philippines?",f"SRP: GLX M/T {f(1099000)}, GLX A/T {f(1159000)}, GLS A/T {f(1259000)} ({FRESH})."),
  ("What is the cheapest Xpander?",f"The GLX 1.5G 2WD M/T at {f(1099000)} SRP."),
  ("What is the lowest Xpander down payment?",f"On the GLX M/T, {f(_xl[0])} DP with a sample monthly of {f(_xl[1])} (60 months, all-in). {MSQ}."),
  ("Is the SRP the final price?","The SRP excludes freight and handling. The promo package is all-in; ask Richard for the current breakdown."),
  ("How often do prices change?","Mitsubishi Motors Philippines updates its price list from time to time and promos change monthly. This page shows the "+FRESH+".")],
 more=[("/cars/xpander/","Mitsubishi Xpander 2026"),("/blog/xpander-monthly-amortization/","Xpander monthly installment"),("/blog/xpander-cross-2026-price-philippines/","Xpander Cross price Philippines"),("/mitsubishi-price-list-philippines/","Full Mitsubishi price list")],
 body=f'''<p>Here is the 2026 Mitsubishi Xpander price for every variant, with the lowest published down payment and a sample monthly. For colors, specs and a test drive, see the <a href="/cars/xpander/">Mitsubishi Xpander 2026</a> page.</p>
<h2>Xpander price per variant</h2>
{C_ptab("xpander")}
<p class="row"><a class="btn sm" href="/budgetcalculator/?m=xpander">Compute my Xpander monthly</a> {W_msg("xpander","price-table",label="Message Richard about the Xpander")}</p>
<h2>GLX or GLS?</h2>
<p>All three variants share the 1.5L MIVEC engine (105 PS, 141 Nm) and seven seats, according to Mitsubishi Motors Philippines. The GLX comes with a manual or automatic; the GLS is automatic and, according to Mitsubishi Motors Philippines, adds ASC, Traction Control, Active Yaw Control, Hill Start Assist and the Multi-Around Monitor. More in <a href="/blog/xpander-variants-explained/">Xpander variants explained</a>.</p>
<h2>Xpander DP and monthly</h2>
<p>A bigger down payment lowers the monthly and the total you pay. The table shows the lowest published promo option with a down payment; Richard can compute any other amount. See the <a href="/blog/xpander-monthly-amortization/">Xpander monthly installment</a> guide. Every figure is {MSQ}.</p>
<h2>Xpander Cross</h2>
<p>Want the crossover look? See the <a href="/blog/xpander-cross-2026-price-philippines/">Xpander Cross price Philippines</a> guide, or compare every model in the {PL_LINK.replace("Full M","full M")}.</p>
'''+C_cta("xpander","Xpander","xpander"),
 after=W_vc("xpander","price_article")+W_sbar("xpander","Xpander",W_from("xpander"))),
C_A(slug="mirage-price-philippines-2026",car="mirage",img="mir_glx_red",alt="Mitsubishi Mirage GLX hatchback, with 2026 price in the Philippines",crumbs=CR_C("mirage","Mirage"),
 title="Mitsubishi Mirage Hatchback Price Philippines 2026",seo="Mitsubishi Mirage Price Philippines 2026 (Hatchback)",
 desc="Mirage hatchback 2026 SRP by variant (Oct 2026 list), low DP and sample monthly. Pre-qualified, subject to bank approval. Richard in SJDM.",
 answer=f"The Mitsubishi Mirage hatchback price in the Philippines is {f(720000)} for the GLX M/T and {f(781000)} for the GLX CVT ({FRESH}).",
 faq=[("How much is the Mirage hatchback in the Philippines?",f"SRP: GLX M/T {f(720000)}, GLX CVT {f(781000)} ({FRESH})."),
  ("What is the Mirage low DP?",f"On the GLX M/T, {f(_ml[0])} DP with a sample monthly of {f(_ml[1])} (60 months, all-in). {MSQ}."),
  ("Is the Mirage good for the city?","According to Mitsubishi Motors Philippines, it seats up to five adults and has a 4.6-meter turning radius."),
  ("Is the SRP the final price?","The SRP excludes freight and handling. Ask Richard for the current all-in promo.")],
 more=[("/cars/mirage/","Mitsubishi Mirage 2026"),("/tips/mirage-hatchback-down-payment-monthly-sjdm/","Mirage down payment and monthly"),("/blog/mirage-g4-price-philippines-2026/","Mirage G4 price Philippines"),("/mitsubishi-price-list-philippines/","Full Mitsubishi price list")],
 body=f'''<p>Here is the 2026 Mitsubishi Mirage hatchback price per variant, with the lowest published down payment and a sample monthly. For specs and a test drive, see the <a href="/cars/mirage/">Mitsubishi Mirage 2026</a> page.</p>
<h2>Mirage price per variant</h2>
{C_ptab("mirage")}
<p class="row"><a class="btn sm" href="/budgetcalculator/?m=mirage">Compute my Mirage monthly</a> {W_msg("mirage","price-table",label="Message Richard")}</p>
<h2>Manual or CVT?</h2>
<p>According to Mitsubishi Motors Philippines, both variants use the 1.2L 3-cylinder MIVEC engine (3A92); you choose a 5-speed manual or the INVECS III CVT. The CVT suits stop-and-go traffic; the manual has the lower SRP.</p>
<h2>Mirage DP and monthly</h2>
<p>For more down payment amounts, read the <a href="/tips/mirage-hatchback-down-payment-monthly-sjdm/">Mirage down payment and monthly</a> guide. Every figure is {MSQ}.</p>
<h2>Hatchback or sedan?</h2>
<p>Compare with the <a href="/blog/mirage-g4-price-philippines-2026/">Mirage G4 price Philippines</a> guide, or read <a href="/tips/mirage-hatchback-vs-mirage-g4/">Mirage vs Mirage G4</a>.</p>
'''+C_cta("mirage","Mirage","mirage"),
 after=W_vc("mirage","price_article")+W_sbar("mirage","Mirage",W_from("mirage"))),
C_A(slug="mirage-g4-price-philippines-2026",car="mirage-g4",img="mg4gls_u17",alt="Mitsubishi Mirage G4 GLS sedan, with 2026 price in the Philippines",crumbs=CR_C("mirage-g4","Mirage G4"),
 title="Mitsubishi Mirage G4 Price Philippines 2026",seo="Mirage G4 Price Philippines 2026: Sedan Variants",
 desc="Mirage G4 sedan 2026 SRP per variant from the Oct 2026 list, low DP and sample monthly. Pre-qualified, subject to bank approval. SJDM.",
 answer=f"The Mitsubishi Mirage G4 price in the Philippines is {f(793000)} for the GLX M/T, {f(841000)} for the GLX CVT and {f(937000)} for the GLS CVT ({FRESH}).",
 faq=[("How much is the Mirage G4 in the Philippines?",f"SRP: GLX M/T {f(793000)}, GLX CVT {f(841000)}, GLS CVT {f(937000)} ({FRESH})."),
  ("What is the Mirage G4 low DP?",f"On the GLX M/T, {f(_gl[0])} DP with a sample monthly of {f(_gl[1])} (60 months, all-in). {MSQ}."),
  ("What engine does the Mirage G4 have?","According to Mitsubishi Motors Philippines, a 1.2L MIVEC engine making 78 PS and 100 Nm."),
  ("Is the SRP the final price?","The SRP excludes freight and handling. Ask Richard for the current all-in promo.")],
 more=[("/cars/mirage-g4/","Mitsubishi Mirage G4 2026"),("/mirage-g4-downpayment-and-monthly/","Mirage G4 downpayment and monthly"),("/blog/mirage-price-philippines-2026/","Mirage hatchback price Philippines"),("/mitsubishi-price-list-philippines/","Full Mitsubishi price list")],
 body=f'''<p>Here is the 2026 Mitsubishi Mirage G4 sedan price per variant, with the lowest published down payment and a sample monthly. For specs and a test drive, see the <a href="/cars/mirage-g4/">Mitsubishi Mirage G4 2026</a> page.</p>
<h2>Mirage G4 price per variant</h2>
{C_ptab("mirage-g4")}
<p class="row"><a class="btn sm" href="/budgetcalculator/?m=mirage-g4">Compute my Mirage G4 monthly</a> {W_msg("mirage-g4","price-table",label="Message Richard")}</p>
<h2>GLX or GLS?</h2>
<p>According to Mitsubishi Motors Philippines, every Mirage G4 uses the 1.2L MIVEC engine (78 PS, 100 Nm) and comes with driver and passenger airbags, ABS with EBD, ASC, Hill Start Assist and ISO-Fix. The GLX is offered as a manual or CVT; the GLS is CVT only. Ask Richard to walk you through the trim differences in person.</p>
<h2>Mirage G4 DP and monthly</h2>
<p>For more down payment amounts, read the <a href="/mirage-g4-downpayment-and-monthly/">Mirage G4 downpayment and monthly</a> guide. Every figure is {MSQ}.</p>
'''+C_cta("mirage-g4","Mirage G4","mirage-g4"),
 after=W_vc("mirage-g4","price_article")+W_sbar("mirage-g4","Mirage G4",W_from("mirage-g4"))),
C_A(slug="xpander-vs-avanza",car="xpander",img="xpgls_c31",alt="Mitsubishi Xpander GLS family MPV",crumbs=[("/","Home"),("/cars/","Cars"),("/cars/xpander/","Xpander")],
 title="Mitsubishi Xpander vs Avanza: Which Family MPV Fits You?",seo="Xpander vs Avanza: Feature Comparison for Families",
 desc="A feature-based look at the Xpander and Avanza: seating, engine, safety and practicality, with Xpander facts according to Mitsubishi Motors.",
 answer="Both are seven-seat-class family MPVs with 1.5L-class gasoline engines. According to Mitsubishi Motors Philippines, the Xpander offers 225 mm ground clearance and 105 PS from its 1.5L MIVEC engine. For Avanza details not listed below, check the manufacturer's spec sheet.",
 faq=[("Which has more ground clearance?","According to Mitsubishi Motors Philippines, the Xpander has 225 mm. The Avanza figure was not published on the official page we checked, so check the manufacturer's spec sheet."),
  ("Do both come with an automatic?","Yes. According to Mitsubishi Motors Philippines, the Xpander has a 4-speed AT or 5-speed MT; according to Toyota Motor Philippines, the Avanza has a CVT or 5-speed MT depending on variant."),
  ("Where can I see Xpander prices?","See the Xpander price Philippines guide. This comparison does not list competitor prices."),
  ("Can I test drive the Xpander in SJDM?","Yes. Book with Richard Cuagdan, authorized Mitsubishi sales executive in San Jose del Monte (SJDM).")],
 more=[("/cars/xpander/","Mitsubishi Xpander 2026"),("/blog/xpander-price-philippines-2026/","Xpander price Philippines"),("/blog/xforce-vs-xpander/","Xforce vs Xpander")],
 body='''<div class="box verdict"><p><b>Choose the Xpander if</b> you want high ground clearance for flooded streets (225 mm, according to Mitsubishi Motors Philippines), seven seats and the Multi-Around Monitor on the GLS.</p><p><b>Look at the spec sheets side by side if</b> you are deciding on cabin details: we list only features both makers publish.</p><p class="row"><a class="btn sm" href="/test-drive/?unit=xpander">Test drive the Xpander in SJDM</a> '''+W_msg("xpander","verdict",label="Message Richard")+'''</p></div>
<p>The <a href="/cars/xpander/">Mitsubishi Xpander</a> and the Avanza are both family MPVs. This guide compares published features only, neutrally and without competitor prices.</p>
<h2>Feature comparison</h2>
<div class="tw"><table class="pt"><thead><tr><th scope="col">Feature</th><th scope="col">Mitsubishi Xpander</th><th scope="col">Avanza</th></tr></thead><tbody>
<tr><th scope="row">Engine</th><td>1.5L MIVEC DOHC 16V gasoline (4A91)</td><td>1.3L (1NR-VE) or 1.5L (2NR-VE) 4-cylinder 16-valve DOHC Dual VVT-i, by variant</td></tr>
<tr><th scope="row">Power / torque</th><td>105 PS / 141 Nm</td><td>Check the manufacturer's spec sheet</td></tr>
<tr><th scope="row">Transmission</th><td>4-speed AT or 5-speed MT</td><td>CVT or 5-speed MT, by variant</td></tr>
<tr><th scope="row">Seating</th><td>7</td><td>Check the manufacturer's spec sheet</td></tr>
<tr><th scope="row">Ground clearance</th><td>225 mm</td><td>Check the manufacturer's spec sheet</td></tr>
<tr><th scope="row">Safety highlights</th><td>Driver and passenger airbags, ABS with EBD, ISO-Fix; GLS adds ASC, Traction Control, AYC, HSA, Multi-Around Monitor</td><td>SRS airbags; back camera on selected variants</td></tr>
</tbody></table></div>
<p class="muted">Xpander: according to Mitsubishi Motors Philippines (2026 Xpander flyer). Avanza: according to Toyota Motor Philippines' official Avanza page, checked November 4, 2026. Specifications change; confirm with each manufacturer's current spec sheet. No competitor prices are shown.</p>
<h2>Who the Xpander suits</h2>
<ul class="ticks"><li>Families who drive through flood-prone streets and want 225 mm of ground clearance</li><li>Buyers who want a manual or a conventional automatic</li><li>Those who want the Multi-Around Monitor (GLS) for tight parking</li></ul>
<h2>Xpander price</h2>
<p>See the <a href="/blog/xpander-price-philippines-2026/">Xpander price Philippines</a> guide for each variant's SRP, low DP and sample monthly.</p>
'''+C_cta("xpander","Xpander","xpander")),
C_A(slug="xforce-vs-xpander",car="xforce",img="xf_gls",alt="Mitsubishi Xforce GLS compact SUV",crumbs=[("/","Home"),("/cars/","Cars"),("/cars/xforce/","Xforce")],
 title="Mitsubishi Xforce vs Xpander: Which One Suits You?",seo="Xforce vs Xpander: Crossover SUV or Family MPV?",
 desc="Xforce vs Xpander by seating, size, engine and driving needs, according to Mitsubishi Motors. See prices, then test drive in SJDM, San Jose del Monte.",
 answer="Choose the Xpander for seven seats and 225 mm ground clearance; choose the Xforce for a five-seat compact SUV with a CVT, drive modes and, on the GT, Mitsubishi Motors Safety Sensing (according to Mitsubishi Motors Philippines).",
 faq=[("Which has more seats?","The Xpander seats seven; the Xforce seats five, according to Mitsubishi Motors Philippines."),
  ("Do they share an engine?","Both use a 1.5L MIVEC gasoline engine (4A91) with 105 PS and 141 Nm, according to Mitsubishi Motors Philippines. The Xforce uses a CVT; the Xpander a 4-speed AT or 5-speed MT."),
  ("Which has more ground clearance?","The Xpander has 225 mm and the Xforce 193 mm, according to Mitsubishi Motors Philippines."),
  ("Can I test drive both in SJDM?","Yes. Book with Richard in San Jose del Monte (SJDM) and ask to try both on the same visit.")],
 more=[("/cars/xforce/","Mitsubishi Xforce 2026"),("/cars/xpander/","Mitsubishi Xpander 2026"),("/tips/xforce-2026-price-philippines/","Xforce price Philippines"),("/blog/xpander-price-philippines-2026/","Xpander price Philippines")],
 body='''<div class="box verdict"><p><b>Choose the Xforce if</b> you mostly carry up to five people and want an SUV look, a CVT and drive modes.</p><p><b>Choose the Xpander if</b> you need seven seats or often drive through flood-prone streets.</p><p class="row"><a class="btn sm" href="/test-drive/?unit=xforce">Test drive both in SJDM</a></p></div>
<p>Same engine family, two different shapes. See the <a href="/cars/xforce/">Xforce</a> and the <a href="/cars/xpander/">Xpander</a>.</p>
<h2>Feature comparison</h2>
<div class="tw"><table class="pt"><thead><tr><th scope="col">Feature</th><th scope="col">Xforce</th><th scope="col">Xpander</th></tr></thead><tbody>
<tr><th scope="row">Body</th><td>Compact SUV</td><td>7-seater MPV</td></tr>
<tr><th scope="row">Seats</th><td>5</td><td>7</td></tr>
<tr><th scope="row">Engine</th><td colspan="2">1.5L MIVEC gasoline (4A91), 105 PS / 141 Nm</td></tr>
<tr><th scope="row">Transmission</th><td>CVT</td><td>4-speed AT or 5-speed MT</td></tr>
<tr><th scope="row">Length</th><td>4,390 mm</td><td>4,595 mm</td></tr>
<tr><th scope="row">Ground clearance</th><td>193 mm</td><td>225 mm</td></tr>
<tr><th scope="row">Drive modes</th><td>Normal, Wet, Gravel, Mud (higher variants)</td><td>Not listed</td></tr>
<tr><th scope="row">Advanced safety</th><td>MMSS on the GT (FCM, LCDN, BSW, RCTA, AHB, Adaptive Cruise Control)</td><td>GLS: ASC, Traction Control, AYC, HSA, Multi-Around Monitor</td></tr>
</tbody></table></div>
<p class="muted">According to Mitsubishi Motors Philippines (Xforce brochure and 2026 Xpander flyer). Prices: <a href="/tips/xforce-2026-price-philippines/">Xforce price Philippines</a> and <a href="/blog/xpander-price-philippines-2026/">Xpander price Philippines</a>.</p>
<h2>Who each one suits</h2>
<ul class="ticks"><li><b>Xforce</b>: couples and young families, city driving with weekend trips, buyers moving up from a sedan</li><li><b>Xpander</b>: larger families, carpools, school runs and provincial trips</li></ul>
'''+C_cta("xforce","Xforce","xforce")),
]
# ---- refreshed / upgraded existing articles
def C_find(slug):
    for L_ in (POSTS,TIPS,GUIDES):
        for a in L_:
            if a["slug"]==slug: return a
    raise KeyError(slug)
def C_ref(slug,**k):
    a=C_find(slug);faq_add=k.pop("faq_add",[]);a.update(k);a["w1"]=True;a["mod"]=W_MOD
    if faq_add: a["faq"]=list(a.get("faq") or [])+faq_add
    if "seo" in a: C_chk(a["seo"],a["desc"],slug)
    FIGS[slug]=[x for x in FIGS.get(slug,[]) if "zero" not in x[2].lower()]
    if "body" in k: FIGS.pop(slug,None)
    base=a.get("base") or ("guides" if a in GUIDES else "blog"); C_PATHS.append(f"/{base}/{slug}/"); return a
C_ref("xforce-2026-price-philippines",title="Mitsubishi Xforce Price Philippines 2026",seo="Mitsubishi Xforce Price Philippines 2026: All Variants",
 desc="Xforce 2026 SRP per variant from the Oct 2026 list, low DP and sample monthly. Pre-qualified, subject to bank approval. Ask Richard in SJDM.",
 answer=f"The Mitsubishi Xforce price in the Philippines starts at {f(1119000)} for the GLX, {f(1299000)} (monotone) or {f(1309000)} (two-tone) for the GLS, and {f(1661000)} for the GT ({FRESH}).",
 crumbs=CR_C("xforce","Xforce"),
 faq=[("How much is the Xforce in the Philippines?",f"SRP: GLX {f(1119000)}, GLS {f(1299000)} (monotone) or {f(1309000)} (two-tone), GT {f(1661000)} ({FRESH})."),
  ("What is the Xforce low DP?",f"On the GLX, {f(_fl[0])} DP with a sample monthly of {f(_fl[1])} (60 months, all-in). {MSQ}."),
  ("What does the GT add?","According to Mitsubishi Motors Philippines, Mitsubishi Motors Safety Sensing (FCM, LCDN, BSW, RCTA, AHB, Adaptive Cruise Control), TPMS and a Dynamic Sound Yamaha Premium audio with 8 speakers."),
  ("Is the Xforce a 7-seater?","No. It seats five, according to Mitsubishi Motors Philippines. For seven seats, compare the Xpander.")],
 more=[("/cars/xforce/","Mitsubishi Xforce 2026"),("/blog/xforce-vs-xpander/","Xforce vs Xpander"),("/mitsubishi-price-list-philippines/","Full Mitsubishi price list")],
 body=f'''<h2>Xforce price per variant</h2>
{C_ptab("xforce")}
<p class="row"><a class="btn sm" href="/budgetcalculator/?m=xforce">Compute my Xforce monthly</a> {W_msg("xforce","price-table",label="Message Richard")}</p>
<p>All Xforce variants share a 1.5L MIVEC engine (105 PS, 141 Nm), a CVT, five seats and 193 mm ground clearance, according to Mitsubishi Motors Philippines. See the <a href="/cars/xforce/">Mitsubishi Xforce 2026</a> page for specs and a test drive.</p>
<h2>GLX vs GLS vs GT</h2>
<ul class="ticks"><li><b>GLX</b>: the entry point, with the same engine and CVT</li><li><b>GLS</b>: monotone or two-tone; according to Mitsubishi Motors Philippines, higher variants add drive modes (Normal, Wet, Gravel, Mud) and side and curtain airbags</li><li><b>GT</b>: according to Mitsubishi Motors Philippines, adds Mitsubishi Motors Safety Sensing, TPMS and the Dynamic Sound Yamaha Premium audio (8 speakers)</li></ul>
<p class="muted">Confirm the exact equipment of each variant with Richard before you decide.</p>
<h2>Xforce or Xpander?</h2>
<p>Need seven seats? Read <a href="/blog/xforce-vs-xpander/">Xforce vs Xpander</a>.</p>
'''+C_cta("xforce","Xforce","xforce"),after=W_vc("xforce","price_article")+W_sbar("xforce","Xforce",W_from("xforce")))
C_ref("xpander-cross-2026-price-philippines",title="Mitsubishi Xpander Cross Price Philippines 2026",seo="Xpander Cross Price Philippines 2026: SRP and Monthly",
 desc="Xpander Cross 2026 SRP from the Oct 2026 list, low DP and sample monthly. Pre-qualified, subject to bank approval. Richard, San Jose del Monte.",
 answer=f"The Xpander Cross 1.5G 2WD A/T (Two-Tone) has an SRP of {f(1378000)} ({FRESH}).",crumbs=CR_C("xpander-cross","Xpander Cross"),
 faq=FAQ_XC[:4],more=[("/cars/xpander-cross/","Mitsubishi Xpander Cross 2026"),("/blog/xpander-price-philippines-2026/","Xpander price Philippines"),("/guides/xpander-vs-xpander-cross-vs-destinator/","Xpander vs Xpander Cross vs Destinator")],
 body=f'''<h2>Xpander Cross price</h2>
{C_ptab("xpander-cross")}
<p class="row"><a class="btn sm" href="/budgetcalculator/?m=xcross">Compute my Xpander Cross monthly</a> {W_msg("xpander-cross","price-table",label="Message Richard")}</p>
<p>See the <a href="/cars/xpander-cross/">Mitsubishi Xpander Cross 2026</a> page for specs and a test drive, or compare with the regular Xpander in the <a href="/blog/xpander-price-philippines-2026/">Xpander price Philippines</a> guide.</p>
<h2>What you get</h2>
<p>According to Mitsubishi Motors Philippines, the Xpander Cross is a family-friendly 7-seater crossover MPV with a 1.5L MIVEC engine, a 4-speed AT and a class-leading 225 mm ground clearance. Safety equipment includes dual front airbags, ABS with EBD, Brake Assist, ASC, Traction Control, AYC, HSA, the Multi-Around Monitor and ISO-Fix.</p>
<h2>For probinsya trips</h2>
<p>If your family often drives home to the province, the high ground clearance helps on rough or flooded roads, and seven seats fit relatives and pasalubong. Book a test drive on the routes you know in and around San Jose del Monte. Compare all three family 7-seaters in <a href="/guides/xpander-vs-xpander-cross-vs-destinator/">Xpander vs Xpander Cross vs Destinator</a>.</p>
'''+C_cta("xpander-cross","Xpander Cross","xcross"),after=W_vc("xpander-cross","price_article")+W_sbar("xpander-cross","Xpander Cross",W_from("xpander-cross")))
def C_dpterm(slug):
    m=WM[slug];rows=""
    for v in m["variants"]:
        ab=v.get("ab") or {}
        opts=[(ab.get(k+"_dp"),ab.get(k+"_mo")) for k in ("a","b") if ab.get(k+"_dp") and ab.get(k+"_mo")]
        for dp,mo in opts: rows+=f'<tr><th scope="row">{e(C_short(v,m))}</th><td>{f(C_srp(v))}</td><td>{f(dp)}</td><td><b>{f(mo)}</b>/mo</td></tr>'
    return f'{W_badge()}<div class="tw"><table class="pt"><thead><tr><th scope="col">Variant</th><th scope="col">SRP</th><th scope="col">Down payment</th><th scope="col">Monthly (60 months)</th></tr></thead><tbody>{rows}</tbody></table></div><p class="muted">Published promo options with a down payment, 60 months, all-in. November promo pending; figures change monthly. {MSQ}.</p>'
C_ref("xpander-monthly-amortization",title="Mitsubishi Xpander Monthly Installment 2026",seo="Xpander Monthly Installment 2026: DP and Amortization",
 desc="Sample Xpander monthly installment per variant and down payment (Oct 2026 promo basis). Pre-qualified, subject to bank approval. SJDM.",
 answer=f"On the Oct 2026 promo basis, the Xpander GLX M/T starts at {f(_xl[0])} DP and {f(_xl[1])} a month for 60 months, all-in. November promo pending.",crumbs=CR_C("xpander","Xpander"),
 faq=[("What is the Xpander monthly installment?",f"From {f(_xl[1])} a month on the GLX M/T with {f(_xl[0])} DP (60 months, all-in, Oct 2026 promo basis). {MSQ}."),
  ("Does a bigger down payment lower the monthly?","Yes. The table shows two published options per variant; a larger DP gives a lower monthly and a smaller total."),
  ("Can I choose a shorter term?","Yes. Use the calculator on this page to compare terms; the bank confirms the final figures."),
  ("What income do I need?","A common guide is a monthly installment of about 30 to 35 percent of gross monthly income. Take the 2-minute assessment for a Pre-qualified estimate.")],
 more=[("/blog/xpander-price-philippines-2026/","Xpander price Philippines"),("/cars/xpander/","Mitsubishi Xpander 2026"),("/loan-assessment/","Pre-qualify in 2 minutes")],
 body=f'''<p>Here is the sample Xpander monthly installment per variant and down payment. For SRPs only, see the <a href="/blog/xpander-price-philippines-2026/">Xpander price Philippines</a> guide.</p>
<h2>Xpander monthly by down payment</h2>
{C_dpterm("xpander")}
<h2>Compute your own Xpander monthly</h2>
{CALC("article-xpander-monthly")}
<h2>How to lower your monthly</h2>
<ul class="ticks"><li>Put down a bigger down payment</li><li>Choose the GLX M/T, the variant with the lowest SRP</li><li>Ask Richard about a co-borrower if your income is close to the guide</li></ul>
<p>Ready to check your chances? <a href="/loan-assessment/?src=xpander-monthly">Pre-qualify in 2 minutes</a>. Results are {MSQ}.</p>
'''+C_cta("xpander","Xpander","xpander"))
C_ref("l300-price-philippines-2026",title="Mitsubishi L300 Price Philippines 2026",seo="Mitsubishi L300 Price Philippines 2026: SRP and DP",
 desc="L300 2026 SRP from the Oct 2026 list, low DP and sample monthly for negosyo buyers. Pre-qualified, subject to bank approval. SJDM.",
 answer=f"The Mitsubishi L300 price in the Philippines is {f(829000)} for the Cab and Chassis and {f(1039000)} for the L300 Dual AC ({FRESH}).",crumbs=CR_C("l300","L300"),
 faq=[("How much is the L300 in the Philippines?",f"L300 Cab and Chassis {f(829000)}; L300 Dual AC {f(1039000)} ({FRESH})."),
  ("What is the L300 low DP?",f"Cab and Chassis: {f(_ll[0])} DP, {f(_ll[1])} a month. Dual AC: {f(_la[0])} DP, {f(_la[1])} a month (60 months, all-in). {MSQ}."),
  ("What documents does a business owner need?","Usually DTI or SEC registration, business or mayor's permit, latest ITR or financial statements and bank statements. Each bank can ask for more."),
  ("What engine does the L300 have?","According to Mitsubishi Motors Philippines, a 2.2L Euro 4 turbo diesel (4N14) with 99.25 PS and 200 Nm and a 5-speed manual.")],
 more=[("/cars/l300/","Mitsubishi L300 2026"),("/l300-monthly-installment/","L300 monthly installment"),("/blog/l300-negosyo-guide/","L300 negosyo guide")],
 body=f'''<h2>L300 price per variant</h2>
{C_ptab("l300")}
<p class="row"><a class="btn sm" href="/budgetcalculator/?m=l300">Compute my L300 monthly</a> {W_msg("l300","price-table",label="Business buyer? Message Richard")}</p>
<p>For specs and a test drive, see the <a href="/cars/l300/">Mitsubishi L300 2026</a> page. For more DP and term combinations, read the <a href="/l300-monthly-installment/">L300 monthly installment</a> guide.</p>
<h2>Cab and Chassis or Dual AC?</h2>
<p>The Cab and Chassis is the starting point for a body built to your business, such as a dropside or aluminum van. The Dual AC is a ready-to-work unit. Compare both in the <a href="/blog/l300-negosyo-guide/">L300 negosyo guide</a>.</p>
<h2>Engine and capacity</h2>
<p>According to Mitsubishi Motors Philippines, the L300 uses a 2.2L Euro 4 turbo diesel making 99.25 PS and 200 Nm, with a 5-speed manual and a gross vehicle weight of 2,345 kg (Cab and Chassis).</p>
'''+C_cta("l300","L300","l300",biz=True),after=W_vc("l300","price_article")+W_sbar("l300","L300",W_from("l300")))
# local refresh + hub
C_ref("mitsubishi-near-fairview-quezon-city",title="Mitsubishi Near Fairview: San Jose del Monte (SJDM)",seo="Mitsubishi Fairview Buyers | SJDM, San Jose del Monte",
 desc="From Fairview? Get Mitsubishi prices, low DP and a test drive with Richard in San Jose del Monte (SJDM). Pre-qualified, subject to bank approval.",
 more=[("/mitsubishi-quezon-city/","Mitsubishi for Quezon City buyers"),("/mitsubishi-sjdm-bulacan/","Mitsubishi San Jose del Monte (SJDM)"),("/mitsubishi-price-list-philippines/","Full Mitsubishi price list")],
 faq_add=[("I live in another part of Quezon City. Can Richard still help?","Yes. See the Quezon City page for buyers outside Fairview; the process is the same.")])
C_ref("mitsubishi-near-bulacan-towns",title="Mitsubishi Near Bulacan Towns: Meycauayan, Sta. Maria",seo="Mitsubishi Near Bulacan Towns: Meycauayan, Sta. Maria",
 more=[("/mitsubishi-malolos/","Mitsubishi for Malolos buyers"),("/mitsubishi-marilao/","Mitsubishi for Marilao buyers"),("/mitsubishi-sjdm-bulacan/","Mitsubishi San Jose del Monte (SJDM)")])
_tb=C_find("mitsubishi-near-bulacan-towns");_tb["body"]='<p class="box">Buying from Malolos or Marilao? See the dedicated pages: <a href="/mitsubishi-malolos/">Mitsubishi for Malolos buyers</a> and <a href="/mitsubishi-marilao/">Mitsubishi for Marilao buyers</a>.</p>\n'+_tb["body"]
# finance guide
C_ref("how-car-financing-works-philippines",title="Car Loan Philippines: How Car Financing Works in 2026",seo="Car Loan Philippines: How Financing Works (2026)",
 desc="How a car loan works in the Philippines: down payment, terms, requirements and bank review. Pre-qualified, subject to bank approval. From SJDM.",
 crumbs=[("/","Home"),(GT,GT_EN)],more=[("/budgetcalculator/","Car loan calculator Philippines"),("/guides/car-loan-requirements/","Car loan requirements"),("/loan-assessment/","Pre-qualify in 2 minutes")],
 faq_add=[("How does a car loan work in the Philippines?","You pay a down payment, the bank finances the rest, and you repay it monthly over the term you choose. The bank reviews your income, documents and credit before it decides."),
  ("Where can I compute my monthly?","Use the car loan calculator. Figures are estimates; results are "+MSQ+".")])
_hg=C_find("how-car-financing-works-philippines");_hg["body"]='<p class="box">Want numbers first? Try the <a href="/budgetcalculator/">car loan calculator</a>, check the <a href="/guides/car-loan-requirements/">car loan requirements</a>, then <a href="/loan-assessment/?src=finance-guide">pre-qualify in 2 minutes</a>.</p>\n'+_hg["body"]
# A17 FAQ batch (articles)
C_ref("car-loan-requirements",seo="Car Loan Requirements Philippines: 2026 Checklist",desc="Car loan requirements in the Philippines for employed, self-employed and OFW buyers: IDs, proof of income, bank documents. Pre-qualify from SJDM.",
 faq_add=[("What are the car loan requirements in the Philippines?","Two valid IDs and proof of billing for everyone, plus proof of income: payslips and a certificate of employment if employed, business documents and ITR if self-employed, or a contract and remittance proof if you work abroad.")])
C_ref("car-financing-bulacan",faq_add=[("Can I get a car loan in Bulacan?","Yes. Richard Cuagdan in San Jose del Monte (SJDM) helps Bulacan buyers prepare documents and submit to partner banks. Results are "+MSQ+"."),
  ("Does Mitsubishi offer financing?","Mitsubishi units are financed through banks with monthly promo packages. Ask Richard for this month's options per model.")])
C_ref("mitsubishi-test-drive-sjdm",faq_add=[("How do I book a Mitsubishi test drive?","Use the online form: pick a unit, a date and a time, and Richard will confirm by message.")])
C_ref("mitsubishi-dealer-bulacan",faq_add=[("Is there a Mitsubishi in Bulacan?","Yes. Richard Cuagdan is an authorized Mitsubishi sales executive in San Jose del Monte (SJDM), Bulacan.")])
_CS={a["slug"] for a in CA}
POSTS[:]=[a for a in POSTS if a["slug"] not in _CS]+CA
C_LFAQ={"mitsubishi-sjdm-bulacan":[("Who will assist me?","Richard Cuagdan, authorized Mitsubishi sales executive and car agent in San Jose del Monte (SJDM), from inquiry to release."),
 ("Is there a Mitsubishi near me in SJDM?","Yes. Richard serves San Jose del Monte (SJDM), nearby Bulacan towns and Quezon City. Message him for directions.")]}
C_PATHS.append("/mitsubishi-sjdm-bulacan/")

# ================= A1 /mitsubishi-price-list-philippines/
PL_GROUPS=[("Hatchback and sedan",["mirage","mirage-g4"]),("MPV",["xpander","xpander-cross"]),("SUV",["xforce","destinator","outlander-phev","montero-sport"]),("Pickup",["triton"]),("Commercial",["l300","versa-van"])]
def _plrows():
    out=""
    for g,ss in PL_GROUPS:
        out+=f'<tr class="plg"><th scope="rowgroup" colspan="5">{e(g)}</th></tr>'
        for s in ss:
            m=WM[s]
            for i,v in enumerate(m["variants"]):
                lo=W_low(v)
                out+=(f'<tr{" id=pl-"+s if i==0 else ""}><th scope="row"><a href="/cars/{s}/">{e(C_short(v,m) if not v["n"].startswith(m["name"]) else v["n"])}</a></th><td>{f(C_srp(v))}</td><td>{f(lo[0]) if lo else "Ask Richard"}</td><td>{(f(lo[1])+"/mo") if lo else "Ask Richard"}</td>'
                      f'<td><a class="btn sm ghost dk" href="{MSG}?ref=pricelist-{v["id"]}" rel="noopener" data-msgr="pricelist-{v["id"]}" data-track="msg" data-place="pricelist-row" data-prow="{e(s)}|{e(v["n"])}">Get a quote</a></td></tr>')
    return out
PL_FAQ=[("What is the Mitsubishi price list 2026?",f"The table on this page lists every 2026 Mitsubishi model and variant sold in the Philippines with its SRP ({FRESH})."),
 ("Which Mitsubishi car for sale in the Philippines is the cheapest?",f"The Mirage GLX 1.2G M/T hatchback, at {f(720000)} SRP ({FRESH})."),
 ("Are freight and handling included in the SRP?","No. SRPs exclude freight and handling. The monthly promo packages are all-in; ask Richard for the breakdown of your unit."),
 ("How often do Mitsubishi prices change?","Mitsubishi Motors Philippines updates its price list from time to time, and promos change monthly. This page will be updated when the November list is confirmed."),
 ("What does 'Low DP' mean in the table?","It is the lowest published promo option that has a down payment, with its sample monthly for 60 months, all-in. "+MSQ+"."),
 ("Can I get a quote for one variant?","Yes. Tap Get a quote on any row to message Richard, authorized Mitsubishi sales executive in San Jose del Monte (SJDM).")]
_plchips="".join(f'<a class="chip" href="#pl-{s}">{e(WM[s]["name"])}</a>' for _,ss in PL_GROUPS for s in ss)
_plt="Mitsubishi Price List Philippines 2026: All Models";_pld="Every 2026 Mitsubishi model and variant SRP in one table, with low DP and sample monthly. Pre-qualified, subject to bank approval. Ask Richard in SJDM."
C_chk(_plt,_pld,"pricelist")
_plart=[(f"/cars/{s}/",f"{WM[s]['name']} variants and promo","Model page") for _,ss in PL_GROUPS for s in ss]
_plprice=[("/blog/xpander-price-philippines-2026/","Xpander price Philippines","SRP, low DP, monthly"),("/blog/mirage-price-philippines-2026/","Mirage price Philippines","Hatchback"),("/blog/mirage-g4-price-philippines-2026/","Mirage G4 price Philippines","Sedan"),("/tips/xforce-2026-price-philippines/","Xforce price Philippines","Compact SUV"),("/blog/xpander-cross-2026-price-philippines/","Xpander Cross price Philippines","Crossover MPV"),("/blog/l300-price-philippines-2026/","L300 price Philippines","Commercial"),("/blog/destinator-price-philippines/","Destinator price Philippines","7-seater SUV"),("/blog/montero-sport-price-philippines-2026/","Montero Sport price Philippines","Diesel SUV"),("/blog/triton-price-philippines/","Triton price Philippines","Pickup")]
page("/mitsubishi-price-list-philippines/",_plt,_pld,
f'''<section class="ph"><div class="w"><p class="kick">Price list · 2026 · SJDM</p><h1>Mitsubishi Price List Philippines 2026 (Oct 2026 List)</h1>
<p class="lead">Every Mitsubishi model and variant in one table, with the lowest published down payment and a sample monthly. From Richard Cuagdan, authorized Mitsubishi sales executive in San Jose del Monte (SJDM).</p>
<p class="row">{W_msg("pricelist","hero",cls="btn",label="Get a quote for my variant")} {W_pq("pricelist","hero",cls="btn ghost dk",label="Pre-qualify in 2 minutes")}</p>
<nav class="chips" aria-label="Jump to model">{_plchips}</nav></div></section>
<section class="sec" id="price-list"><div class="w"><h2>Mitsubishi price list 2026</h2>
<div class="tw pltw"><table class="pt pltab"><caption>{W_badge()}</caption><thead><tr><th scope="col">Model and variant</th><th scope="col">SRP</th><th scope="col">Low DP</th><th scope="col">Sample monthly</th><th scope="col">Quote</th></tr></thead><tbody>{_plrows()}</tbody></table></div>
<p class="muted">SRP: {e(FRESH)}, from the official Mitsubishi Motors Philippines price list; freight and handling not included; subject to change without notice. Low DP: lowest published promo option with a down payment. Sample monthly: 60 months, all-in. {MSQ}.</p>
<p class="row"><a class="btn sm" href="/budgetcalculator/">Car loan calculator</a> <a class="btn sm ghost dk" href="/loan-assessment/?src=pricelist-table">Pre-qualify in 2 minutes</a></p></div></section>
<section class="sec alt"><div class="w"><h2>Price guides per model</h2>{W_cards(_plprice)}</div></section>
<section class="sec"><div class="w"><h2>Model pages</h2>{W_cards(_plart)}</div></section>
{W_trust("xpander")}
<section class="sec"><div class="w nar">{W_FAQH(PL_FAQ)}{W_LOCAL}</div></section>
<script>document.addEventListener("click",function(ev){{var a=ev.target.closest&&ev.target.closest("[data-prow]");if(!a)return;var p=a.dataset.prow.split("|");try{{if(window.gtag)gtag("event","pricelist_row_click",{{model:p[0],variant:p[1],page_type:"price_list"}})}}catch(_){{}}}});</script>
{W_vc("pricelist","price_list")}{W_sbar("pricelist","Mitsubishi price list",W_from("mirage"))}''',
 ld=[{"@type":"WebPage","@id":D+"/mitsubishi-price-list-philippines/","name":"Mitsubishi Price List Philippines 2026","url":D+"/mitsubishi-price-list-philippines/","about":{"@id":D+"/#dealer"},"dateModified":W_MOD},
     {"@type":"ItemList","name":"Mitsubishi price list Philippines 2026","itemListElement":[{"@type":"ListItem","position":i+1,"item":p} for i,p in enumerate([x for _,ss in PL_GROUPS for s in ss for x in offers_ld(WM[s])])]},W_FAQLD(PL_FAQ)],
 crumbs=[("/","Home"),("/cars/","Cars"),("/mitsubishi-price-list-philippines/","Mitsubishi price list")])
C_PATHS.append("/mitsubishi-price-list-philippines/")

# ================= A15 local pages (served from SJDM; no showroom claim in the town, no travel times)
def C_local(slug,town,title,h1,lead,why,models,faq,extra,img_,alt_):
    d=f"From {town}? Get Mitsubishi prices, low DP and a test drive with Richard in San Jose del Monte (SJDM). Pre-qualified, subject to bank approval."
    C_chk(title,d,slug)
    cards="".join(f'<a class="card pad mc" href="/cars/{s}/"><p class="kick">{e(WM[s]["cat"])}</p><h3>Mitsubishi {e(WM[s]["name"])}</h3><p class="low">SRP from <b>{W_from(s)}</b></p><p class="muted">{e(t)}</p></a>' for s,t in models)
    page(f"/{slug}/",title,d,
f'''<section class="ph"><div class="w hgrid"><div><p class="kick">{e(town)} · served from San Jose del Monte (SJDM)</p><h1>{e(h1)}</h1><p class="lead">{lead}</p>
<p class="row">{W_msg("local-"+slug,"hero",cls="btn",label="Message Richard")} <a class="btn ghost dk" href="/test-drive/">Book a test drive in SJDM</a></p></div>{img(img_,alt_,eager=True,cls="himg")}</div></section>
<section class="sec"><div class="w nar"><h2>How buying from {e(town)} works</h2>
<ol class="steps"><li><h3>Get prices and a quote online</h3><p>Check the <a href="/mitsubishi-price-list-philippines/">Mitsubishi price list</a>, then message Richard for the current promo on your variant.</p></li>
<li><h3>Pre-qualify from home</h3><p>Take the <a href="/loan-assessment/?src=local-{slug}">2-minute assessment</a> and send your documents for a pre-check. Results are {MSQ}.</p></li>
<li><h3>Test drive in San Jose del Monte</h3><p>Book a schedule online. Richard sends directions; check a live map before you leave because traffic changes by hour and day.</p></li>
<li><h3>Release</h3><p>Richard coordinates the bank, payment and release schedule with you.</p></li></ol>
{why}</div></section>
<section class="sec alt"><div class="w"><h2>Popular with {e(town)} buyers</h2><div class="grid g3">{cards}</div><p class="muted">SRP: {e(FRESH)}.</p></div></section>
{extra}
{W_trust("xpander")}
<section class="sec"><div class="w nar">{W_FAQH(faq)}<p class="wloc">See <a href="/mitsubishi-sjdm-bulacan/">Mitsubishi San Jose del Monte (SJDM)</a> · <a href="/mitsubishi-price-list-philippines/">price list</a> · <a href="/test-drive/">test drive</a>.</p></div></section>
{W_vc("local-"+slug,"local")}{W_sbar("local-"+slug,"Richard, Mitsubishi SJDM")}''',
     ld=[{"@type":"WebPage","@id":D+f"/{slug}/","name":h1,"url":D+f"/{slug}/","about":{"@id":D+"/#dealer"},"spatialCoverage":{"@type":"Place","name":town},"dateModified":W_MOD},
         {"@type":"Service","name":f"Mitsubishi sales assistance for {town} buyers","provider":{"@id":D+"/#dealer"},"areaServed":{"@type":"Place","name":town}},W_FAQLD(faq)],
     img=f"/assets/img/{img_}.webp",crumbs=[("/","Home"),("/mitsubishi-sjdm-bulacan/","Mitsubishi SJDM"),(f"/{slug}/",town)])
    C_PATHS.append(f"/{slug}/")
C_local("mitsubishi-malolos","Malolos","Mitsubishi Malolos Buyers | SJDM, San Jose del Monte","Mitsubishi for Malolos Buyers: Served from SJDM",
 "Live or work in Malolos, the capital city of Bulacan? Richard Cuagdan, authorized Mitsubishi sales executive in San Jose del Monte (SJDM), handles your quote, pre-qualification and test drive, with most steps done online before you travel.",
 '<h2>Good to know for Malolos buyers</h2><ul class="ticks"><li><b>Government and office employees</b>: prepare a certificate of employment with compensation and recent payslips; these are the documents banks ask for most.</li><li><b>Family business owners</b>: bring DTI or SEC registration, a mayor\'s permit and bank statements. The <a href="/cars/l300/">L300</a> and <a href="/cars/triton/">Triton</a> are common work vehicles.</li><li><b>One trip, not three</b>: send documents online first so your SJDM visit covers the test drive and signing together.</li></ul>',
 [("xpander","Seven seats for family trips"),("triton","Pickup for work and weekends"),("l300","Commercial workhorse")],
 [("Is there a Mitsubishi showroom in Malolos?","This page is not a Malolos showroom. Richard Cuagdan serves Malolos buyers from San Jose del Monte (SJDM), Bulacan; there are other authorized Mitsubishi dealers in the region, so choose the one that serves you best."),
  ("Can I finish most of the process without traveling?","Yes. Quotes, pre-qualification and document pre-checks happen online or on Messenger. You visit SJDM for the test drive and signing."),
  ("What documents should a Malolos government employee prepare?","Two valid IDs, proof of billing, a certificate of employment with compensation and recent payslips or the latest ITR. Each bank can ask for more."),
  ("Which Mitsubishi suits a family business?","The L300 for deliveries and the Triton for mixed work and family use. Compare them in the L300 vs Triton guide."),
  ("Where will I service my car?","Ask Richard about authorized service options nearest your home; the warranty schedule is the same.")],
 '<section class="sec"><div class="w nar"><h2>Business buyer from Malolos?</h2><p>Read the <a href="/blog/l300-vs-triton-for-negosyo/">L300 vs Triton for negosyo</a> guide and the <a href="/blog/l300-price-philippines-2026/">L300 price Philippines</a> guide.</p></div></section>',
 "tr_gx_u28","Mitsubishi Triton for Malolos buyers")
C_local("mitsubishi-marilao","Marilao","Mitsubishi Marilao Buyers | SJDM, San Jose del Monte","Mitsubishi for Marilao Buyers: Served from SJDM",
 "Driving from Marilao? Richard Cuagdan, authorized Mitsubishi sales executive in San Jose del Monte (SJDM), prepares your quote, pre-qualification and test drive so your visit is short and planned.",
 '<h2>Good to know for Marilao buyers</h2><ul class="ticks"><li><b>NLEX commuters</b>: an automatic such as the <a href="/cars/xpander/">Xpander GLX A/T</a> or the <a href="/cars/xforce/">Xforce CVT</a> makes stop-and-go traffic easier.</li><li><b>Flood-prone streets</b>: according to Mitsubishi Motors Philippines, the Xpander has 225 mm ground clearance.</li><li><b>Shift workers</b>: message Richard any time; he replies personally on Messenger and schedules test drives Monday to Saturday.</li></ul>',
 [("xpander","225 mm ground clearance, seven seats"),("xforce","Compact SUV with a CVT"),("mirage-g4","Sedan with the lowest monthly")],
 [("Is there a Mitsubishi showroom in Marilao?","This page is not a Marilao showroom. Richard Cuagdan serves Marilao buyers from San Jose del Monte (SJDM), Bulacan; there are other authorized Mitsubishi dealers in the region, so choose the one that serves you best."),
  ("Which Mitsubishi is best for the NLEX commute?","An automatic is easier in traffic: the Xpander GLX A/T or GLS A/T for families, the Xforce CVT or Mirage G4 CVT for smaller households."),
  ("Can I get a quote without visiting?","Yes. Message Richard with your preferred variant and down payment and he will send the current promo."),
  ("Can I schedule a test drive after work?","Test drives run Monday to Saturday. Book online and Richard will confirm the best slot."),
  ("Is financing available for first-time buyers?","Yes. Start with the 2-minute assessment; results are "+MSQ+".")],
 "", "xpglx_x37","Mitsubishi Xpander for Marilao families")
C_local("mitsubishi-quezon-city","Quezon City","Mitsubishi Quezon City Buyers | SJDM Bulacan","Mitsubishi for Quezon City Buyers: San Jose del Monte (SJDM)",
 "San Jose del Monte borders Quezon City, so many QC buyers in Fairview, Novaliches and nearby areas work with Richard Cuagdan, authorized Mitsubishi sales executive in SJDM. Get your quote and pre-qualification online, then test drive in SJDM.",
 '<h2>Good to know for Quezon City buyers</h2><ul class="ticks"><li><b>From Fairview</b>: see <a href="/blog/mitsubishi-near-fairview-quezon-city/">Mitsubishi near Fairview</a> for buyers along Quirino Highway.</li><li><b>From Novaliches or Caloocan</b>: see <a href="/blog/mitsubishi-near-caloocan-novaliches/">Mitsubishi near Caloocan and Novaliches</a>.</li><li><b>Condo or tight parking</b>: according to Mitsubishi Motors Philippines, the Mirage has a 4.6-meter turning radius and the Xpander GLS adds the Multi-Around Monitor.</li></ul>',
 [("mirage","City-size hatchback, 4.6 m turning radius"),("xpander","Family 7-seater"),("destinator","7-seater SUV with a turbo engine")],
 [("Does Richard serve Quezon City buyers?","Yes. Richard Cuagdan serves San Jose del Monte (SJDM), Bulacan and Quezon City, from SJDM. This page is not a Quezon City showroom."),
  ("Can I register the car in Quezon City?","Registration follows your address on the documents. Ask Richard how the LTO registration in the all-in package is handled for QC addresses."),
  ("Which Mitsubishi suits city parking?","The Mirage hatchback, with a 4.6-meter turning radius according to Mitsubishi Motors Philippines."),
  ("I'm from Fairview. Which page should I read?","See the Mitsubishi near Fairview guide; it covers buyers along Quirino Highway."),
  ("How do I start?","Message Richard or take the 2-minute assessment. Results are "+MSQ+".")],
 "", "de_x3n","Mitsubishi Destinator for Quezon City families")

# ================= A12/A17 FAQ blocks injected into non-article pages + scrub of every changed path
C_INJ={"/loan-assessment/":("Mitsubishi car loan: common questions",[("Can I apply for a Mitsubishi car loan online?","Yes. This free assessment gives a Pre-qualified estimate in a few minutes; the final decision is the bank's (Pre-qualified, subject to bank approval)."),("Which documents will the bank ask for?","Two valid IDs, proof of billing and proof of income for your employment type. See the car loan requirements guide."),("Does the assessment affect my credit?","No. It is an estimate based on your answers; no bank application is filed until you decide to proceed.")]),
 "/brochures/":("Mitsubishi brochure download: common questions",[("How do I download a Mitsubishi brochure?","Tap Download official brochure (PDF) on any model. The file opens from the official Mitsubishi Motors Philippines website."),("Do brochures show the current price?","No. Brochures cover features and specs. For prices, see the Mitsubishi price list; for this month's promo, message Richard."),("Can I get a brochure for a specific variant?","Message Richard and he will send the spec sheet for the variant you are considering.")]),
 "/promos/":("Promo terms",[("How long is a promo valid?","Each promo is valid for the stated month only, subject to bank approval and change without notice. November update pending."),("Are the promo prices all-in?","Promo packages bundle LTO registration, insurance and chattel mortgage on a 60-month term. Ask Richard for your unit's breakdown."),("What are fuel points?","Selected variants come with fuel points (for example, 10K Fuel Points) in the promo. Ask Richard which variants qualify this month."),("Is a promo the same as bank approval?","No. Promos are Pre-qualified, subject to bank approval.")])}
C_PATHS+=["/loan-assessment/","/brochures/","/promos/"]
def C_SCRUB(R):
    import re as _r
    for p in C_PATHS:
        fp=R+p+"index.html"
        if not os.path.exists(fp): continue
        s=open(fp).read();o=s
        if p in C_INJ:
            h,it=C_INJ[p]
            sec=f'<section class="sec"><div class="w nar"><h2>{e(h)}</h2>'+W_FAQH(it).replace('<h2>Frequently asked questions</h2>','')+'</div></section>'
            s=s.replace('<footer class="ft">',sec+'<footer class="ft">',1)
            s=s.replace('</head>','<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org",**W_FAQLD(it)},ensure_ascii=False)+'</script>\n</head>',1)
        s=s.replace('<span class="ab-zt">Zero DP Promo</span>','').replace('<b class="ab-z">Zero DP Promo</b>','<b class="ab-z">Low DP</b>')
        s=_r.sub(r',? up to Zero DP','',s);s=_r.sub(r',? hanggang Zero DP','',s)
        s=_r.sub(r'<li><a href="/(?:mitsubishi-zero-down-payment-promo|guides/zero-dp-vs-low-dp|blog/zero-down-payment-car-philippines|[a-z]+/[a-z0-9-]*zero[a-z0-9-]*)/">[^<]*</a></li>','',s)
        s=_r.sub(r'<p>See also: the <a href="/mitsubishi-zero-down-payment-promo/">[^<]*</a>\.</p>\n?','',s)
        if s!=o: open(fp,"w").write(s)
