D="https://mitsubishipromos.online"
FB="https://www.facebook.com/504759566043148"
MSG="https://m.me/504759566043148"
SITECHAT=False  # SHELVED 2026-10-29 (Messenger is the main chat route). Own site-wide chat bubble (needs webhook v8). One-line flip: True, then python3 _src/build.py
WEBHOOK="https://script.google.com/macros/s/AKfycbzP4moZ9QL3YB_liQsoqM80o9IfTBa-GMapQg1uLJF1xAOPLyvJ6PVhHb-nQ7A__hWsTA/exec"
PIXEL="1820790069172672"
def f(n): return "₱"+format(n,",")
# SRPs: official MMPC price list (mitsubishi-motors.com.ph/price-list, "As of August 2026"). srp=None -> "Ask for price".
# promo: dealer promo (gated, rendered only by JS on /promos/). opts=[(dp label, monthly)], fuel=int|None
def V(id,n,srp,img,promo=None,srpnote=None): return dict(id=id,n=n,srp=srp,img=img,promo=promo,srpnote=srpnote)
def P(opts,fuel=None,srp=None): return dict(opts=opts,fuel=fuel,srp=srp)
MODELS=[
 dict(slug="mirage-g4",name="Mirage G4",cat="Sedan",img="mg4gls_u17",
  blurb="A compact, fuel-sipping sedan that is easy to park around SJDM and Metro Manila and gentle on a first-car budget.",
  who="first-time buyers, daily commuters and young professionals",
  specs=[("Engine","1.2L (1,193 cc) D4 MPI VVT gasoline"),("Max power / torque","78 PS / 100 Nm"),("Transmission","5-speed manual or CVT"),("Seating","5")],
  variants=[V("mg4glxmt","Mirage G4 GLX 1.2G M/T",793000,"mg4glx_u17"),
            V("mg4glxat","Mirage G4 GLX 1.2G CVT",841000,"mg4glx_a66",P([("₱58K DP",15160)],20000)),
            V("mg4gls","Mirage G4 GLS 1.2G CVT",937000,"mg4gls_u17",P([("Zero DP",19303),("₱83K DP",16890)],20000))]),
 dict(slug="xpander",name="Xpander",cat="7-seater MPV",img="xpglx_x37",
  blurb="The family MPV built around Filipino life: seven seats, high ground clearance for flooded streets, and a cabin that handles provincial trips.",
  who="growing families, carpool parents, and OFW families who want one car for school runs and weekend trips",
  specs=[("Engine","1.5L in-line 4 DOHC 16-valve MIVEC gasoline"),("Max power / torque","105 PS / 141 Nm"),("Transmission","5-speed manual or 4-speed automatic"),("Seating","7")],
  variants=[V("xglxmt","Xpander GLX 1.5G 2WD M/T",1099000,"xpglx_u33",P([("Zero DP",22641),("₱148K DP",19811)],30000)),
            V("xglxat","Xpander GLX 1.5G 2WD A/T",1159000,"xpglx_x37",P([("Zero DP",23877),("₱138K DP",20892)],60000)),
            V("xglsat","Xpander GLS 1.5G 2WD A/T",1259000,"xpgls_c31",P([("Zero DP",25937),("₱148K DP",22695)],60000))]),
 dict(slug="xpander-cross",name="Xpander Cross",cat="7-seater crossover MPV",img="xc_x3n",
  blurb="Everything families like about the Xpander, with a rugged crossover look and a more premium cabin.",
  who="families who want MPV practicality with SUV styling",
  specs=[("Engine","1.5L in-line 4 DOHC 16-valve MIVEC gasoline"),("Max power / torque","105 PS / 141 Nm"),("Transmission","4-speed automatic"),("Seating","7")],
  variants=[V("xcross","Xpander Cross 1.5G 2WD A/T (Two-Tone)",1378000,"xc_x3n",P([("Zero DP",28389),("₱148K DP",24840)],60000))]),
 dict(slug="xforce",name="Xforce",cat="Compact SUV",img="xf_glx",
  blurb="A compact SUV with bold styling and a raised driving position, sized for city streets but ready for out-of-town weekends.",
  who="young families and professionals moving up from a sedan or hatchback",
  specs=[("Engine","1.5L gasoline"),("Transmission","CVT"),("Drivetrain","2WD")],
  variants=[V("xfglx","Xforce GLX 1.5G 2WD CVT",1119000,"xf_glx"),
            V("xfglsm","Xforce GLS 1.5G 2WD CVT (Monotone)",1299000,"xf_gls"),
            V("xfglst","Xforce GLS 1.5G 2WD CVT (Two-Tone)",1309000,"xf_gls"),
            V("xfgt","Xforce GT 1.5G 2WD CVT",1661000,"xf_gt")]),
 dict(slug="destinator",name="Destinator",cat="7-seater SUV",img="de_x3n",
  blurb="Mitsubishi's newest 7-seat SUV, with a turbocharged 1.5L engine and a roomy, tech-forward cabin.",
  who="families stepping up from an MPV who want more power, comfort and safety tech",
  specs=[("Engine","1.5L turbocharged gasoline (4B40), Euro 4"),("Max power / torque","163 PS / 250 Nm"),("Transmission","CVT"),("Seating","7")],
  variants=[V("dglx","Destinator GLX 1.5G Turbo 2WD CVT",1389000,"de_p26",P([("Zero DP",28615),("₱93K DP",26827)])),
            V("dgls","Destinator GLS 1.5G Turbo 2WD CVT",1599000,"de_d34",P([("Zero DP",32942),("₱123K DP",30883)],20000)),
            V("dgtm","Destinator GT 1.5G Turbo 2WD CVT (Monotone)",1929000,"de_jh3",P([("Zero DP",39740),("₱88K DP",37256)],40000)),
            V("dgtt","Destinator GT 1.5G Turbo 2WD CVT (Two-Tone)",1939000,"de_x3n",P([("Zero DP",39740),("₱88K DP",37256)],40000))]),
 dict(slug="outlander-phev",name="Outlander PHEV",cat="Plug-in hybrid SUV",img="op_gt",
  blurb="Mitsubishi's plug-in hybrid SUV: drive on electricity for everyday trips and let the gasoline engine take over for long ones.",
  who="buyers who want electrified driving without range worries",
  specs=[("Powertrain","2.4L gasoline plug-in hybrid"),("Drivetrain","AWD")],
  variants=[V("opgt","Outlander PHEV GT 2.4G AWD",2848000,"op_gt")]),
 dict(slug="montero-sport",name="Montero Sport",cat="7-seater diesel SUV",img="ms_white",
  blurb="The full-size diesel SUV, including the Black Series. Built on a ladder frame for long drives, rough roads and heavy loads.",
  who="executives, large families and anyone who drives far from the city often",
  specs=[("Engine","2.4L (2,442 cc) 4N15 MIVEC intercooled turbo diesel, Euro 4"),("Max power / torque","181 PS / 430 Nm"),("Transmission","6-speed manual or 8-speed automatic"),("Seating","7")],
  variants=[V("mglxmt","Montero Sport GLX 2.4D 2WD M/T",1568000,"ms_silver",P([("Zero DP",30284),("₱30K DP",28265)])),
            V("mgls","Montero Sport GLS 2.4D 2WD A/T",1927000,"ms_white",P([("Zero DP",39699),("₱138K DP",37218)],20000)),
            V("mbs2wd","Montero Sport Black Series 2.4D 2WD A/T",2190000,"msbs_jh3",P([("₱88K DP",45117),("₱218K DP",42297)],20000)),
            V("mbs4wd","Montero Sport Black Series 2.4D 4WD A/T",2530000,"msbs_x8w",P([("₱133K DP",52121),("₱283K DP",48864)],20000))]),
 dict(slug="triton",name="Triton",cat="Pickup",img="tr_gx_u28",
  blurb="A tough diesel pickup that works hard on weekdays and still feels comfortable for the family on weekends.",
  who="contractors, farm and resort owners, and anyone who needs a cargo bed",
  specs=[("Engine","2.4L 4N16 intercooled turbo diesel"),("Transmission","6-speed manual or automatic (by variant)"),("Drivetrain","2WD or 4WD (by variant)")],
  variants=[V("trglmt2","Triton GL 2.4D 2WD M/T",1266000,"tr_gl"),
            V("trglmt4","Triton GL 2.4D 4WD M/T",1292000,"tr_gl"),
            V("tritongxat","Triton GX 2.4D 2WD A/T",1430000,"tr_gx_u28",P([("Zero DP",28900),("₱140K DP",25200)],20000)),
            V("trglxmt2","Triton GLX 2.4D 2WD M/T",1649000,"tr_glx"),
            V("trglxat2","Triton GLX 2.4D 2WD A/T",1735000,"tr_glx"),
            V("trglxmt4","Triton GLX 2.4D 4WD M/T",1949000,"tr_glx"),
            V("trglsat","Triton GLS 2.4D 2WD A/T",1999000,"tr_gls"),
            V("trath","Triton Athlete 2.4D 4WD A/T",2359000,"tr_lineup")]),
 dict(slug="l300",name="L300",cat="Commercial",img="l300_fb",
  blurb="The workhorse of Philippine small businesses, available as a cab and chassis for custom bodies or as a ready-to-work dual-AC unit.",
  who="business owners in delivery, hauling, catering, hardware and retail",
  specs=[("Engine","2.2L 16-valve DOHC (4N14) turbo-intercooled diesel, Euro 4"),("Transmission","5-speed manual"),("Fuel","Diesel")],
  variants=[V("l300cc","L300 Cab & Chassis 2.2D M/T",829000,"l300_fb"),
            V("l300","2026 L300 Dual AC",None,"l300_fb",P([("Zero DP",21405),("₱123K DP",18789)],20000,srp=1039000))]),
 dict(slug="versa-van",name="Versa Van",cat="15-seater diesel van",img="vv_glx",
  blurb="A full-size diesel van for shuttle services, company transport and big families who travel together.",
  who="shuttle and tour operators, companies and large families",
  specs=[("Engine","2.5L (2,488 cc) DOHC 16-valve VGS turbo diesel"),("Max power / torque","129 PS / 356 Nm"),("Transmission","5-speed manual"),("Drivetrain","2WD"),("Seating","15 (including driver)"),("Colors","Silver Metallic, White Solid")],
  variants=[V("vvglx","2026 Versa Van GLX 2.5D 2WD M/T",1764000,"vv_glx",P([("₱33K DP",36340),("₱243K DP",31798)],20000,srp=1764000))]),
]
ALLIN=["3 years LTO registration","3 years TPL insurance","1 year comprehensive insurance, rate locked for 3 years","Chattel mortgage","Free labor up to 5,000 km","3 years warranty"]
FREEBIES=['Full tint','Floor mats','Seat cover (fabric seats)','Reverse camera','Early warning device','Basic tools','Umbrella','Microfiber cloth','Keychain']
NOTE="Promo valid for October 2026, subject to bank approval and change without notice."
SRPNOTE="SRPs from the official Mitsubishi Motors Philippines price list (as of August 2026), subject to change without notice; freight and handling not included."
def srp_txt(v): return f(v["srp"]) if v["srp"] else "Ask for price"
def srp_from(m):
    x=[v["srp"] for v in m["variants"] if v["srp"]]; return min(x) if x else None
UNITS=[v["n"] for m in MODELS for v in m["variants"]]
# ---- PROMO SOURCE OF TRUTH (Richard 2026-10-30): every variant's promo opts come from _src/optionAB_oct2026.json
# opts = [Option A (lowest DP; "Zero DP Promo" when DP is 0), Option B (30% DP, low monthly)], 60 months, subject to bank approval.
# The older hand-entered "Zero DP / ₱XK DP" pairs are replaced. Fuel points kept as entered above.
import json as _json, os as _os, re as _re
_AB=_json.load(open(_os.path.join(_os.path.dirname(__file__),"optionAB_oct2026.json")))
def _abk(x):
    x={"2026 L300 Dual AC":"L300 FB Body Dual AC 2.2D M/T","2026 Versa Van GLX 2.5D 2WD M/T":"Versa Van GLX 2.5D 2WD M/T"}.get(x,x)
    return _re.sub(r"[^a-z0-9]","",x.lower().replace("withdual","dual").replace("with single","single").replace("chasis","chassis"))
_ABM={_abk(r["unit"]):r for r in _AB}
def dplabel(dp): return "Zero DP Promo" if dp==0 else f"₱{dp/1000:g}K DP"
AB_UNMATCHED=[]
for _m in MODELS:
    for _v in _m["variants"]:
        _r=_ABM.get(_abk(_v["n"]))
        if not _r: AB_UNMATCHED.append(_v["n"]); continue
        _old=_v["promo"] or {}
        _v["promo"]=P([(dplabel(_r["a_dp"]),_r["a_mo"]),(dplabel(_r["b_dp"]),_r["b_mo"])],_old.get("fuel"),srp=_old.get("srp") or (None if _v["srp"] else _r["srp"]))
        _v["ab"]=dict(a_dp=_r["a_dp"],a_mo=_r["a_mo"],b_dp=_r["b_dp"],b_mo=_r["b_mo"],srp=_r["srp"])
