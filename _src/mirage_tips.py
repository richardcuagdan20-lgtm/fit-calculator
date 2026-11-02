# Mirage hatchback guides (branch draft-mirage, 2026-11-03). Facts ONLY from the official Mitsubishi Motors Philippines
# Mirage and Mirage G4 brochures (PDF linked on /brochures/) and the official price list (as of August 2026).
# Promo figures ONLY from data.py (optionAB_oct2026.json). Unconfirmed Option B (flags) -> "Ask for latest", never a number.
from seo2026 import MODELS, f, CTA, VALID, MON, ALLIN_UL
from data import BASK
BY="Mitsubishi Sales Executive"; DT="2026-11-03"
V={v["id"]:v for m in MODELS for v in m["variants"]}
def srp(i): return f(V[i]["srp"])
def a(i): x=V[i]["ab"]; return (f(x["a_dp"]),f(x["a_mo"]))
def b(i): x=V[i]["ab"]; return (f(x["b_dp"]),f(x["b_mo"])) if x["b_mo"] else None
def bt(i):
    x=b(i); return f"{x[0]} DP / {x[1]}/mo" if x else f"<b>{BASK}</b> (being confirmed)"
def at(i): x=a(i); return f"{x[0]} DP / {x[1]}/mo"
def row(i,label=None): return f"<tr><th scope='row'>{label or V[i]['n']}</th><td>{srp(i)}</td><td>{at(i)}</td><td>{bt(i)}</td></tr>"
def ptable(ids):
    return ('<table class="spec"><thead><tr><th scope="col">Variant</th><th scope="col">SRP</th><th scope="col">Option A (lowest DP)</th><th scope="col">Option B (30% DP)</th></tr></thead><tbody>'
            +"".join(row(i) for i in ids)+f'</tbody></table><p class="note">Updated {DT}. {VALID} Pre-qualified, subject to bank approval.</p>')
BRO='<a href="/brochures/#mirage">official Mirage brochure (PDF)</a>'
CHK=f'<p class="muted">Specs are taken from the {BRO} and the Mirage G4 brochure from Mitsubishi Motors Philippines. Mitsubishi may change specifications without prior notice, so check the brochure for latest specs.</p>'
P=[]
SPEC=('<table class="spec"><thead><tr><th scope="col"></th><th scope="col">Mirage (hatchback)</th><th scope="col">Mirage G4 (sedan)</th></tr></thead><tbody>'
 +"".join(f"<tr><th scope='row'>{k}</th><td>{x}</td><td>{y}</td></tr>" for k,x,y in [
 ("Overall length","3,795 mm","4,305 mm"),("Overall width","1,665 mm","1,670 mm"),("Overall height","1,500 mm","1,515 mm"),
 ("Wheelbase","2,450 mm","2,550 mm"),("Minimum ground clearance","160 mm","170 mm"),("Fuel tank","35 L","42 L"),
 ("Engine","1.2L 3-cylinder MIVEC gasoline","1.2L gasoline"),("Max power / torque","77.52 PS / 100 Nm","78 PS / 100 Nm"),
 ("Transmission","5-speed manual or INVECS-III CVT","5-speed manual or CVT"),("Tires","175/55 R15","185/55 R15"),("Seating","5","5")])
 +'</tbody></table>')

# 1 hatchback vs G4
P.append(dict(base="tips",car="mirage",slug="mirage-hatchback-vs-mirage-g4",date=DT,by=BY,img="mir_glx_red",
alt="Mitsubishi Mirage GLX hatchback in Red Metallic, from the official Mirage brochure",
title="Mirage Hatchback vs Mirage G4: Which Should You Buy?",
kw=("Mirage hatchback vs Mirage G4",["Mirage vs Mirage G4","Mitsubishi Mirage hatchback price","Mirage G4 price","best first car Philippines"]),
desc=f"Mitsubishi Mirage hatchback vs Mirage G4 sedan: size, engine, trunk vs tailgate, official SRP and {MON} promo, and who each one suits in SJDM, San Jose del Monte.",
answer=f"Choose the Mirage hatchback if you mostly drive and park in the city and want the lowest entry price (SRP from {srp('mirglxmt')}). Choose the Mirage G4 sedan if you want a separate trunk, a longer wheelbase and more cabin length for passengers (SRP from {srp('mg4glxmt')}). Both use a 1.2L gasoline engine with manual or CVT. Promos are subject to bank approval.",
faq=[("Is the Mirage hatchback the same engine as the Mirage G4?","Both use a 1.2L gasoline engine with 100 Nm of torque. The hatchback brochure lists 77.52 PS; the G4 brochure lists 78 PS. Check the brochure for latest specs."),
("Which is easier to park?","The hatchback. It is 510 mm shorter overall (3,795 mm vs 4,305 mm) and the brochure quotes a 4.6-meter minimum turning radius."),
("Which is cheaper?",f"By official SRP, the Mirage GLX 1.2G M/T hatchback at {srp('mirglxmt')} is the most affordable Mitsubishi in the current price list; the Mirage G4 starts at {srp('mg4glxmt')}."),
("Can I get the CVT on both?","Yes. The hatchback comes as GLX M/T and GLX CVT; the G4 comes as GLX M/T, GLX CVT and GLS CVT.")],
body=f'''<p>The Mirage name covers two body styles: the <a href="/cars/mirage/">Mirage hatchback</a> and the <a href="/cars/mirage-g4/">Mirage G4 sedan</a>. They share the same basic recipe, a light body and a frugal 1.2L gasoline engine, but they suit slightly different owners. Here is a clear comparison using the official brochures and price list, so you can decide before visiting the showroom in San Jose del Monte.</p>
<h2>Size and practicality</h2>
<p>The biggest difference is length. The hatchback measures 3,795 mm overall; the G4 sedan is 4,305 mm. Width and height are almost identical, so the extra length on the G4 goes into a longer wheelbase (2,550 mm vs 2,450 mm) and a separate trunk. The hatchback answers with a tailgate and a rear bench with a fold function, which is handy for bulky items like a balikbayan box or a folded stroller.</p>
{SPEC}
{CHK}
<h2>Driving in the city</h2>
<p>For narrow subdivision streets, mall parking and U-turn slots, the shorter hatchback is the easier car. The Mirage brochure highlights a 4.6-meter minimum turning radius, one of the tightest in its class, and a low drag coefficient for fuel efficiency. If most of your driving is inside SJDM, Caloocan or Quezon City, that compact footprint is a daily advantage.</p>
<p>The G4 sits on a longer wheelbase and has slightly more ground clearance (170 mm vs 160 mm), which some owners prefer for longer highway trips and for passengers in the back.</p>
<h2>Engine and transmission</h2>
<p>Both cars use a 1.2-liter gasoline engine with 100 Nm of torque and offer a 5-speed manual or a CVT. The hatchback runs the 3A92 three-cylinder DOHC MIVEC engine (77.52 PS) and the INVECS-III CVT, which the brochure says selects the optimal gear ratio for efficient performance and a smooth ride. If you sit in stop-and-go traffic every day, the CVT is the more relaxed choice; read <a href="/tips/manual-vs-automatic-car-philippines/">manual vs automatic</a> if you are undecided.</p>
<h2>Safety and features</h2>
<p>The Mirage hatchback brochure lists dual SRS airbags, the RISE (Reinforced Impact Safety Evolution) body, side impact beams, a child-proof lock and an ASEAN NCAP Grand Prix Award (2014) for adult occupant protection in the mini car category. Inside, the GLX has a 7-inch touch screen with Bluetooth and USB, 15-inch black alloy wheels and a tailgate spoiler. Features differ by variant on both cars, so compare the exact variant in each brochure.</p>
<h2>Price and this month's promo</h2>
<p>Official SRPs (price list as of August 2026) and the {MON} all-in promo on 60 months:</p>
{ptable(["mirglxmt","mirglxcvt","mg4glxmt","mg4glxat","mg4gls"])}
<p>Option A is the lowest down payment for each unit; Option B is a 30% down payment with a lower monthly. For the Mirage GLX CVT, the Option B monthly is still being confirmed, so I show it as "{BASK}" rather than publish a figure I cannot stand behind. Message me and I will send the confirmed computation.</p>
<h2>Who should pick which</h2>
<ul class="ticks"><li><b>Mirage hatchback</b>: solo commuters, first-time owners, city driving, easy parking, the lowest SRP in the lineup.</li><li><b>Mirage G4</b>: small families, frequent rear passengers, people who want a separate locked trunk, more highway driving.</li></ul>
<p>Still torn? Drive both. See the <a href="/tips/mirage-hatchback-down-payment-monthly-sjdm/">Mirage hatchback down payment and monthly guide</a> and the <a href="/mirage-g4-downpayment-and-monthly/">Mirage G4 downpayment and monthly guide</a> before you decide.</p>
'''+CTA("Tell me how you drive and who rides with you; I'll line up both Mirage body styles for a back-to-back test drive in SJDM.","mirage")))

# 2 down payment and monthly
P.append(dict(base="tips",car="mirage",slug="mirage-hatchback-down-payment-monthly-sjdm",date=DT,by=BY,img="mir_glx_red",
alt="Mitsubishi Mirage GLX hatchback, the most affordable Mitsubishi in the 2026 price list",
title="Mirage Hatchback Down Payment & Monthly Guide (SJDM)",
kw=("Mirage hatchback down payment and monthly",["Mitsubishi Mirage monthly amortization","Mirage GLX price Philippines","Mirage hatchback SJDM","Mirage CVT monthly"]),
desc=f"Mitsubishi Mirage hatchback down payment and monthly amortization in SJDM, San Jose del Monte, Bulacan: official SRP, {MON} Option A and Option B, income guide and documents.",
answer=f"For {MON}, the Mirage GLX 1.2G M/T (SRP {srp('mirglxmt')}) is {a('mirglxmt')[0]} DP and {a('mirglxmt')[1]}/mo on Option A, or {b('mirglxmt')[0]} DP and {b('mirglxmt')[1]}/mo on Option B, 60 months all-in. The GLX CVT (SRP {srp('mirglxcvt')}) is {a('mirglxcvt')[0]} DP and {a('mirglxcvt')[1]}/mo on Option A; its Option B is being confirmed, so ask for the latest. Pre-qualified, subject to bank approval.",
faq=[("What is the lowest down payment for the Mirage hatchback?",f"For {MON}, Option A is {a('mirglxmt')[0]} for the GLX M/T and {a('mirglxcvt')[0]} for the GLX CVT, on 60 months, all-in, subject to bank approval."),
("Why is the CVT Option B shown as 'Ask for latest'?","The Option B monthly for the CVT is being re-checked against the official computation. Rather than publish a number that may change, I send the confirmed figure directly when you message me."),
("What income do I need?",f"Banks usually like the monthly to stay around 30–35% of gross monthly income. At {a('mirglxmt')[1]}/mo that is roughly {f(round(V['mirglxmt']['ab']['a_mo']/0.35/100)*100)}–{f(round(V['mirglxmt']['ab']['a_mo']/0.30/100)*100)} gross a month. The bank makes the final decision."),
("What does all-in include?","LTO registration, TPL and comprehensive insurance, chattel mortgage and more. See the list on this page.")],
body=f'''<p>The <a href="/cars/mirage/">Mitsubishi Mirage hatchback</a> is the most affordable way into a brand-new Mitsubishi. This guide covers the official SRP, this month's two promo options, how much income banks usually look for and what to prepare if you are buying in San Jose del Monte (SJDM) or nearby Bulacan and Quezon City.</p>
<h2>Official SRP</h2>
<ul class="ticks"><li><b>Mirage GLX 1.2G M/T</b>: {srp('mirglxmt')}</li><li><b>Mirage GLX 1.2G CVT</b>: {srp('mirglxcvt')}</li></ul>
<p>SRPs are from the official Mitsubishi Motors Philippines price list (as of August 2026). Freight and handling are not included, and prices can change without notice.</p>
<h2>{MON} promo: Option A and Option B</h2>
<p>Every unit has two all-in options on 60 months. <b>Option A</b> is the lowest down payment. <b>Option B</b> is a 30% down payment with a lower monthly.</p>
{ptable(["mirglxmt","mirglxcvt"])}
<div class="box"><p><b>About the CVT Option B:</b> the Option B monthly for the Mirage GLX CVT is still being confirmed, so it is shown as "{BASK}". I will send you the confirmed down payment and monthly on request. The GLX M/T figures above are confirmed for {MON}.</p></div>
<h2>How the monthly works</h2>
<ol class="steps"><li><h3>SRP</h3><p>The official price of the variant you choose.</p></li><li><h3>Down payment</h3><p>A smaller DP keeps more cash in your pocket; a bigger DP lowers the monthly.</p></li><li><h3>Term</h3><p>These promos are on 60 months (5 years).</p></li><li><h3>Monthly</h3><p>A fixed amortization to the bank for the whole term.</p></li></ol>
<p>Want to try your own down payment? Use the <a href="/budgetcalculator/">monthly calculator</a>. It shows an estimate next to the official promo for the same unit.</p>
<h2>Manual or CVT?</h2>
<p>The manual has the lower SRP and the lower monthly. The INVECS-III CVT costs more but is far less tiring in daily traffic on Quirino Highway, Commonwealth or EDSA. If you are a new driver, the CVT is usually worth the difference. More in <a href="/tips/manual-vs-automatic-car-philippines/">manual vs automatic</a>.</p>
<h2>Income guide</h2>
<p>Most banks prefer the monthly amortization to stay around 30–35% of your gross monthly income, after other loans. Use that as a rough guide, then check your chances with the free <a href="/loan-assessment/">Loan Application Assessment</a>. Results are Pre-qualified, subject to bank approval.</p>
<h2>What all-in includes</h2>
{ALLIN_UL}
<h2>Documents to prepare</h2>
<ul class="ticks"><li>Two valid government IDs</li><li>Proof of income: payslips and certificate of employment, or business documents and bank statements if self-employed</li><li>Proof of billing for your address</li><li>For OFWs: contract or employment certificate and remittance records; see the <a href="/blog/ofw-car-buying-guide/">OFW car loan guide</a></li></ul>
<p>Requirements vary by bank; I will tell you exactly which ones apply to your situation. Comparing body styles? Read <a href="/tips/mirage-hatchback-vs-mirage-g4/">Mirage hatchback vs Mirage G4</a>.</p>
'''+CTA("Send me your preferred variant and down payment; I'll prepare the exact all-in computation for the Mirage hatchback.","mirage")))

# 3 first car / commute
P.append(dict(base="tips",car="mirage",slug="mirage-hatchback-first-car-bulacan-manila-commute",date=DT,by=BY,img="mir_int",
alt="Mitsubishi Mirage hatchback dashboard with 7-inch touch screen, from the official Mirage brochure",
title="Is the Mirage a Good First Car for the Bulacan–Manila Commute?",
kw=("Mirage good first car",["best city car Philippines","Mirage hatchback review Philippines","SJDM to Manila commute car","fuel efficient car Bulacan"]),
desc="Is the Mitsubishi Mirage hatchback a good first car or city car for the SJDM, San Jose del Monte, Bulacan to Manila commute? Size, CVT, safety, costs and limits, from the official brochure.",
answer=f"For a solo or couple commuter, yes: the Mirage hatchback is compact (3,795 mm long, 4.6 m turning radius), has a frugal 1.2L MIVEC engine, a CVT option for traffic and dual airbags, and it is the lowest SRP in the Mitsubishi lineup ({srp('mirglxmt')}). If you regularly carry five adults or heavy loads, look at a bigger unit. Check the brochure for latest specs.",
faq=[("Is the Mirage fuel efficient?","The brochure highlights the 1.2L MIVEC engine, the INVECS-III CVT and a low drag coefficient for fuel efficiency. Real consumption depends on traffic, load and driving style, so I don't quote a fixed km/L figure."),
("Can the Mirage handle NLEX and long drives?","It is designed mainly as a city car, but it is a regular highway-legal 1.2L car. For frequent long trips with a full load, a bigger engine is more relaxed."),
("Is it safe for a new driver?","The brochure lists dual SRS airbags, the RISE body, side impact beams and an ASEAN NCAP Grand Prix Award (2014) for adult occupant protection in the mini car category."),
("Manual or CVT for the commute?","For daily stop-and-go traffic between Bulacan and Metro Manila, the CVT is the easier choice.")],
body=f'''<p>Many of my first-time buyers in San Jose del Monte (SJDM) ask the same question: is a small car enough for the daily drive to Quezon City, Caloocan or Manila? Here is an honest look at the <a href="/cars/mirage/">Mitsubishi Mirage hatchback</a> as a first car and city car, using only what Mitsubishi publishes in the official brochure.</p>
<h2>Why it works as a first car</h2>
<ul class="ticks"><li><b>Easy to place on the road</b>: 3,795 mm long and 1,665 mm wide, so lane positioning and parking are less stressful while you build confidence.</li><li><b>Tight turning</b>: the brochure quotes a 4.6-meter minimum turning radius for narrow streets and parking spots.</li><li><b>Simple to drive</b>: a CVT option, electric power steering and a tilt-adjustable steering wheel.</li><li><b>Lowest entry price</b>: SRP from {srp('mirglxmt')}, the most affordable Mitsubishi in the current price list.</li></ul>
<h2>The daily commute from Bulacan</h2>
<p>Routes from SJDM to Metro Manila, whether via Quirino Highway, Commonwealth Avenue or NLEX, mix slow traffic with short faster stretches. That is where a small, light car shines: the CVT handles stop-and-go without a clutch, and the compact body slips into tight parking at the office or the mall. For timing and route habits, see <a href="/tips/sjdm-to-manila-commute-tips/">SJDM to Manila commute tips</a>.</p>
<h2>Fuel efficiency</h2>
<p>Mitsubishi describes the Mirage's (3A92) 1.2L in-line 3 DOHC MIVEC engine as tuned for high output with low fuel consumption and lower emissions, paired with the INVECS-III CVT for fuel economy and a smooth ride, and an aerodynamic body with a low drag coefficient. The fuel tank holds 35 liters. Actual consumption depends on your route, traffic and habits, so treat any km/L claim you hear with caution; <a href="/tips/fuel-saving-tips-diesel-vs-gasoline/">these fuel saving habits</a> matter as much as the car.</p>
<h2>Safety for new drivers</h2>
<p>Standard safety listed in the brochure includes dual SRS airbags for the driver and front passenger, the RISE body structure with crumple zones, side impact beams, a child-proof lock and three-point seatbelts with pretensioners in front. The Mirage also won the ASEAN NCAP Grand Prix Award (2014) for adult occupant protection in the mini car category.</p>
<h2>Comfort and tech</h2>
<p>Mitsubishi says the cabin offers ample leg and headroom for up to five adults, with a driver's seat that adjusts for height, slide and recline. The GLX has a 7-inch touch screen with Bluetooth, USB and Mirror Link, plus manual air-conditioning and a 12V socket.</p>
<h2>Where it is not the best fit</h2>
<ul class="ticks"><li>You carry five adults every day or often load heavy cargo: consider the <a href="/cars/xpander/">Xpander</a>.</li><li>Your street floods often: a higher unit like the <a href="/cars/xforce/">Xforce</a> gives more clearance than the Mirage's 160 mm.</li><li>You want a separate trunk: the <a href="/cars/mirage-g4/">Mirage G4 sedan</a> is the sister model.</li></ul>
<h2>What it costs each month</h2>
<p>For {MON}, the Mirage GLX M/T is {at('mirglxmt')} on Option A, 60 months all-in; the GLX CVT is {at('mirglxcvt')} on Option A, with its Option B shown as "{BASK}" while it is being confirmed. Full details are in the <a href="/tips/mirage-hatchback-down-payment-monthly-sjdm/">Mirage hatchback down payment and monthly guide</a>. Pre-qualified, subject to bank approval.</p>
{CHK}
'''+CTA("Want to feel how the Mirage handles your actual route? Book a test drive in SJDM and bring your usual passengers.","mirage")))
