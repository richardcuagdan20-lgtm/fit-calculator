D="https://mitsubishipromos.online"
MSG="https://m.me/504759566043148"
def f(n): return "₱"+format(n,",")
# variant: name, srp (int or str label), srp_num, options [(dp label, monthly)], fuel (int or None), img
MODELS=[
 dict(slug="mirage-g4",name="Mirage G4",cat="Sedan",img="mg4gls_u17",
  blurb="A compact, fuel-sipping sedan that is easy to park around SJDM and Metro Manila and gentle on a first-car budget.",
  who="first-time buyers, daily commuters, young professionals and Grab-style city driving",
  specs=[("Engine","1.2L (1,193 cc) D4 MPI VVT gasoline"),("Max power / torque","78 PS / 100 Nm"),("Transmission","CVT"),("Seating","5")],
  variants=[dict(n="Mirage G4 GLX AT",srp=841000,opts=[("₱58K DP",15160)],fuel=20000,img="mg4glx_a66"),
            dict(n="Mirage G4 GLS",srp=937000,opts=[("Zero DP",19303),("₱83K DP",16890)],fuel=20000,img="mg4gls_u17")]),
 dict(slug="xpander",name="Xpander",cat="7-seater MPV",img="xpglx_x37",
  blurb="The family MPV built around Filipino life: seven seats, high ground clearance for flooded streets, and a cabin that handles provincial trips.",
  who="growing families, carpool parents, and OFW families who want one car for school runs and weekend trips",
  specs=[("Engine","1.5L in-line 4 DOHC 16-valve MIVEC gasoline"),("Max power / torque","105 PS / 141 Nm"),("Transmission","5-speed manual or 4-speed automatic"),("Seating","7")],
  variants=[dict(n="Xpander GLX MT",srp=1099000,opts=[("Zero DP",22641),("₱148K DP",19811)],fuel=30000,img="xpglx_u33"),
            dict(n="Xpander GLX AT",srp=1159000,opts=[("Zero DP",23877),("₱138K DP",20892)],fuel=60000,img="xpglx_x37"),
            dict(n="Xpander GLS AT",srp=1259000,opts=[("Zero DP",25937),("₱148K DP",22695)],fuel=60000,img="xpgls_c31")]),
 dict(slug="xpander-cross",name="Xpander Cross",cat="7-seater crossover MPV",img="xc_x3n",
  blurb="Everything families like about the Xpander, with a rugged crossover look and a more premium cabin.",
  who="families who want MPV practicality with SUV styling",
  specs=[("Engine","1.5L in-line 4 DOHC 16-valve MIVEC gasoline"),("Max power / torque","105 PS / 141 Nm"),("Transmission","4-speed automatic"),("Seating","7")],
  variants=[dict(n="Xpander Cross",srp=1378000,opts=[("Zero DP",28389),("₱148K DP",24840)],fuel=60000,img="xc_x3n")]),
 dict(slug="destinator",name="Destinator",cat="7-seater SUV",img="de_x3n",
  blurb="Mitsubishi's newest 7-seat SUV, with a turbocharged 1.5L engine and a roomy, tech-forward cabin.",
  who="families stepping up from an MPV who want more power, comfort and safety tech",
  specs=[("Engine","1.5L turbocharged gasoline (4B40), Euro 4"),("Max power / torque","163 PS / 250 Nm"),("Transmission","CVT"),("Seating","7")],
  variants=[dict(n="Destinator GLX",srp=1389000,opts=[("Zero DP",28615),("₱93K DP",26827)],fuel=None,img="de_p26"),
            dict(n="Destinator GLS",srp=1599000,opts=[("Zero DP",32942),("₱123K DP",30883)],fuel=20000,img="de_d34"),
            dict(n="Destinator GT",srp=1929000,srpl="₱1,929,000 (mono-tone) / ₱1,939,000 (two-tone)",opts=[("Zero DP",39740),("₱88K DP",37256)],fuel=40000,img="de_x3n")]),
 dict(slug="l300",name="L300",cat="Commercial",img="l300_fb",
  blurb="The workhorse of Philippine small businesses, now with dual air-conditioning for the crew in front and behind.",
  who="business owners in delivery, hauling, catering, hardware and retail",
  specs=[("Engine","2.2L 16-valve DOHC (4N14) turbo-intercooled diesel, Euro 4"),("Transmission","5-speed manual"),("Fuel","Diesel")],
  variants=[dict(n="2026 L300 Dual AC",srp=1039000,opts=[("Zero DP",21405),("₱123K DP",18789)],fuel=20000,img="l300_fb")]),
 dict(slug="triton",name="Triton",cat="Pickup",img="tr_gx_u28",
  blurb="A tough diesel pickup that works hard on weekdays and still feels comfortable for the family on weekends.",
  who="contractors, farm and resort owners, and anyone who needs a cargo bed",
  specs=[("Engine","2.4L (2,440 cc) 4N16 D4 intercooled turbo diesel"),("Transmission","6-speed automatic with Sport Mode"),("Drivetrain","2WD")],
  variants=[dict(n="Triton GX AT",srp=1430000,opts=[("Zero DP",28900),("₱140K DP",25200)],fuel=20000,img="tr_gx_u28")]),
 dict(slug="montero-sport",name="Montero Sport",cat="7-seater diesel SUV",img="ms_white",
  blurb="The full-size diesel SUV, now including the Black Series. Built on a ladder frame for long drives, rough roads and heavy loads.",
  who="executives, large families and anyone who drives far from the city often",
  specs=[("Engine","2.4L (2,442 cc) 4N15 MIVEC intercooled turbo diesel, Euro 4"),("Max power / torque","181 PS / 430 Nm"),("Transmission","6-speed manual or 8-speed automatic"),("Seating","7")],
  variants=[dict(n="Montero Sport GLX MT",srp=1568000,opts=[("Zero DP",30284),("₱30K DP",28265)],fuel=None,img="ms_silver"),
            dict(n="Montero Sport GLS",srp=1927000,opts=[("Zero DP",39699),("₱138K DP",37218)],fuel=20000,img="ms_white"),
            dict(n="Montero Sport Black Series AT 2WD",srp=2190000,opts=[("₱88K DP",45117),("₱218K DP",42297)],fuel=20000,img="msbs_jh3"),
            dict(n="Montero Sport Black Series AT 4WD",srp=2530000,srpl="₱2,530,000 (₱2,545,000 in White Diamond)",opts=[("₱133K DP",52121),("₱283K DP",48864)],fuel=20000,img="msbs_x8w")]),
]
OTHER=[("Xforce","Compact SUV"),("Outlander PHEV","Plug-in hybrid SUV"),("Versa Van","Passenger and cargo van")]
ALLIN=["3 years LTO registration","3 years TPL insurance","1 year comprehensive insurance, rate locked for 3 years","Chattel mortgage","Free labor up to 5,000 km","3 years warranty"]
FREEBIES=['Full tint','Floor mats','Seat cover (fabric seats)','Reverse camera','Early warning device','Basic tools','Umbrella','Microfiber cloth','Keychain']
NOTE="Promo valid for October 2026, subject to bank approval and change without notice."
def lowest(m): return min(o[1] for v in m["variants"] for o in v["opts"])
