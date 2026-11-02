# SJDM / Bulacan local guides (branch draft-seo2, 2026-11-02). Brand = Richard Cuagdan, authorized Mitsubishi sales executive.
# Figures come ONLY from data.py / promosab (via seo2026 helpers). No street address, no fake branches, no travel-time claims.
from seo2026 import MODELS, f, ALLIN, M, ZDP, B, zl, rng, table, CTA, DISC, VALID, MON, ALLIN_UL
BY="Mitsubishi Sales Executive"; DT="2026-11-02"
P=[]
def low(slug):
    z=zl(slug); return f"{f(z)}/mo at Zero DP" if z else "see the promos page"
def srp0(slug):
    s=[v["srp"] or (v["promo"] or {}).get("srp") for v in M(slug)["variants"]]; s=[x for x in s if x]; return f(min(s)) if s else "message me"
AREAS=[("Caloocan (North) and Novaliches","Quirino Highway and the Bagong Silang / Camarin side are the usual way up to SJDM.","/blog/mitsubishi-near-caloocan-novaliches/"),
 ("Fairview and Quezon City","Commonwealth Avenue and Regalado/Quirino Highway connect Fairview to SJDM.","/blog/mitsubishi-near-fairview-quezon-city/"),
 ("Marilao and Meycauayan","Most buyers come via NLEX or the Marilao–SJDM roads; both are next-door towns.","/blog/mitsubishi-near-bulacan-towns/"),
 ("Bocaue and Santa Maria","Reachable through Santa Maria and the Norzagaray–SJDM roads or via NLEX.","/blog/mitsubishi-near-bulacan-towns/"),
 ("Norzagaray","Directly east of SJDM; many buyers here look at pickups and 7-seaters for mixed roads.","/blog/mitsubishi-near-bulacan-towns/"),
 ("Montalban (Rodriguez), Rizal","Southeast neighbour of SJDM; I coordinate viewing and paperwork online first.",None),
 ("Malolos and central Bulacan","Farther north via NLEX/MacArthur; most of the process (quote, documents, pre-qualification) can be done online.","/blog/mitsubishi-near-bulacan-towns/")]
AREA_UL="<ul class='ticks'>"+"".join(f"<li><b>{a}</b>: {d}"+(f' <a href="{u}">Read more</a>' if u else "")+"</li>" for a,d,u in AREAS)+"</ul>"
NOTE_AREAS='<p class="muted">These are areas I serve. I am one authorized Mitsubishi sales executive based in San Jose del Monte; I do not have branches in these towns. Routes are general; check live traffic before you drive.</p>'

# 1 buying guide
P.append(dict(base="tips",car="xpander",slug="mitsubishi-buying-guide-sjdm-bulacan",date=DT,by=BY,img="xpglx_x37",
alt="Mitsubishi Xpander, a popular choice for SJDM and Bulacan families",
title="Buying a Mitsubishi in SJDM, San Jose del Monte: 2026 Guide",
kw=("Mitsubishi San Jose del Monte",["Mitsubishi SJDM Bulacan","Mitsubishi Bulacan price list","Mitsubishi SJDM promo","buy Mitsubishi Bulacan"]),
desc="How to buy a Mitsubishi in San Jose del Monte (SJDM), Bulacan: price list, October 2026 promos, financing, test drive, documents and release, step by step.",
answer=f"To buy a Mitsubishi in San Jose del Monte, Bulacan: pick a unit from the 2026 price list (SRPs from {srp0('mirage-g4')} for the Mirage G4), compare this month's two all-in promo options, check if you're Pre-qualified, book a test drive, submit documents for bank evaluation, then schedule release. Financing is subject to bank approval.",
faq=[("Where can I buy a Mitsubishi in San Jose del Monte?","I'm Richard Cuagdan, an authorized Mitsubishi sales executive in San Jose del Monte (SJDM), Bulacan. Message or call me and I'll guide you from quote to release."),
("What is the cheapest Mitsubishi in Bulacan?",f"By SRP, the Mirage G4 starts at {srp0('mirage-g4')}. On {MON} promos its Zero DP monthly starts at {low('mirage-g4')}, 60 months, all-in, subject to bank approval."),
("Can I process everything online?","Most of it: the quote, document checklist and pre-qualification. You'll still sign the bank and release documents and receive the unit in person."),
("How long does the whole process take?","It depends on the bank's evaluation and unit availability. Complete documents are the biggest thing you control.")],
body=f'''<p>Most of my buyers live in San Jose del Monte or nearby Bulacan towns and work in Quezon City, Caloocan or Manila. This guide is the process I walk them through, in order, so you know what happens at each step and what you need to prepare.</p>
<h2>Step 1: Pick a unit from the 2026 price list</h2>
<p>Start with the official SRP. Every model and variant is on the <a href="/cars/">Mitsubishi 2026 price list</a>. A quick view of where each model starts:</p>
<ul class="ticks">'''+"".join(f'<li><a href="/cars/{m["slug"]}/">{m["name"]}</a>: SRP from {srp0(m["slug"])}</li>' for m in MODELS)+f'''</ul>
<p>Not sure which body type fits? Families usually compare the <a href="/cars/xpander/">Xpander</a> and <a href="/cars/destinator/">Destinator</a>; business owners look at the <a href="/cars/l300/">L300</a> and <a href="/cars/triton/">Triton</a>. If you drive to Manila daily, read <a href="/tips/best-mitsubishi-for-sjdm-manila-commute/">which Mitsubishi fits the SJDM to Manila commute</a>.</p>
<h2>Step 2: Compare this month's promo options</h2>
<p>Each unit has two all-in options on the <a href="/promos/">promos page</a>: Option A with the lowest down payment, and Option B with a 30% down payment and a lower monthly. Popular units this month:</p>
{table(["mirage-g4","xpander","triton"])}
<p>See <a href="/tips/option-a-vs-option-b-mitsubishi-promo/">Option A vs Option B</a> to decide which suits your cash flow.</p>
<h2>Step 3: Check your budget and pre-qualify</h2>
<p>Keep the monthly at about 30–35% of gross monthly income. Use the <a href="/budgetcalculator/">monthly calculator</a>, then the free <a href="/loan-assessment/">loan pre-qualification check</a>. A result is "Pre-qualified, subject to bank approval"; the bank makes the final decision.</p>
<h2>Step 4: Test drive in SJDM</h2>
<p><a href="/test-drive/">Book a test drive</a> for a Monday to Saturday slot. Bring your driver's license. Here's <a href="/tips/mitsubishi-test-drive-sjdm/">what to check on a test drive</a>.</p>
<h2>Step 5: Documents and bank evaluation</h2>
<p>Prepare IDs, proof of income and proof of billing (see the <a href="/guides/car-loan-requirements/">car loan requirements</a>). I submit to the bank and follow up for you. Details for local buyers are in <a href="/tips/car-financing-bulacan/">car financing in Bulacan</a>.</p>
<h2>Step 6: Release</h2>
<p>All-in promos bundle the main fees:</p>{ALLIN_UL}
<p>Use the <a href="/tips/new-car-release-day-checklist/">release day checklist</a> before you drive home.</p>
<h2>Areas I serve</h2>
<p>Besides SJDM, I help buyers from nearby towns. See <a href="/tips/mitsubishi-bulacan-areas-served/">areas I serve in Bulacan and north Metro Manila</a>.</p>
'''+CTA("Message me with the unit you're eyeing and I'll send this month's computation for SJDM.")))

# 2 financing in Bulacan
P.append(dict(base="tips",car="xpander",slug="car-financing-bulacan",date=DT,by=BY,img="xpglx_u33",
alt="Mitsubishi Xpander, often financed by Bulacan buyers on 60 months",
title="Car Financing SJDM, San Jose del Monte Bulacan: Low DP Guide",
kw=("low down payment Mitsubishi Bulacan",["car loan Bulacan","Mitsubishi financing SJDM","Mitsubishi promo Bulacan","car financing San Jose del Monte"]),
desc="Car financing in SJDM, San Jose del Monte and Bulacan for Mitsubishi buyers: low down payment and Zero DP Promo options, income guide, documents and how bank approval works. October 2026.",
answer=f"For Bulacan buyers, most Mitsubishi units are financed through a bank auto loan on up to 60 months. {MON} promos give two all-in options per unit: the lowest down payment (Zero DP Promo on select units) or 30% down for a lower monthly. Everything is subject to bank approval.",
faq=[("What is the lowest down payment for a Mitsubishi in Bulacan?",f"It depends on the unit. Option A ranges this month: Mirage G4 {rng('mirage-g4')}, Xpander {rng('xpander')}, Triton {rng('triton')}. Subject to bank approval."),
("Do I need to go to a bank branch in Bulacan?","Usually not. I submit your application to partner banks and coordinate the verification. The bank may call you or your employer."),
("Can self-employed buyers or online sellers apply?","Yes. Banks look at business documents, bank statements and how long the business has run. See the requirements guide."),
("Is in-house financing better?","Bank financing is the common route for new cars. Compare total cost and terms in writing before deciding.")],
body=f'''<p>"Magkano ang down?" and "Pasok ba ako?" are the two questions I hear most from buyers in SJDM, Marilao, Meycauayan and the rest of Bulacan. Here's how financing actually works, with this month's real promo figures.</p>
<h2>How a bank auto loan works</h2>
<p>You pay a down payment; the bank pays the rest and you repay it monthly over the term. On all-in promos, registration, insurance and chattel mortgage are bundled, so the monthly you see is close to what you'll actually pay. More detail: <a href="/guides/how-car-financing-works-philippines/">how car financing works</a>.</p>
<h2>Low down payment options this month</h2>
<p>Option A is the lowest down payment per unit. Ranges for {MON}:</p>
<ul class="ticks">'''+"".join(f'<li><a href="/cars/{s}/">{M(s)["name"]}</a>: {rng(s)}</li>' for s in ["mirage-g4","xpander","xforce","destinator","triton","montero-sport","l300"])+f'''</ul>
<p>Exact figures per variant are on the <a href="/promos/">promos page</a>. Zero DP is explained in <a href="/tips/zero-dp-mitsubishi-bank-approval/">Zero DP and bank approval</a>.</p>
<h2>Monthly and income guide</h2>
{table(["mirage-g4","xpander","l300"])}
<h2>Documents</h2>
<p>Employed: IDs, payslips or certificate of employment, proof of billing. Self-employed: DTI/SEC papers, bank statements, ITR. OFWs: contract and remittance proof, plus an SPA or co-borrower. Full list: <a href="/guides/car-loan-requirements/">car loan requirements</a> and the <a href="/tips/ofw-car-loan-requirements-mitsubishi/">OFW checklist</a>.</p>
<h2>Improving your chances</h2>
<p>A bigger down payment, a co-borrower, clean existing loans and complete documents all help. See <a href="/tips/car-loan-approval-tips/">car loan approval tips</a>. Any result from my tools is "Pre-qualified, subject to bank approval".</p>
'''+CTA("Tell me your unit and target monthly, and I'll compute the best option for you.")))

# 3 commute fit
P.append(dict(base="tips",car="xforce",slug="best-mitsubishi-for-sjdm-manila-commute",date=DT,by=BY,img="xf_gls",
alt="Mitsubishi Xforce, a compact SUV option for the SJDM to Manila commute",
title="Best Mitsubishi for the SJDM (San Jose del Monte)–Manila Commute",
kw=("best car for SJDM to Manila commute",["Mitsubishi for daily commute","fuel efficient Mitsubishi","Mirage G4 commute","Xforce Bulacan"]),
desc="Which Mitsubishi fits the daily San Jose del Monte (SJDM) to Manila commute: Mirage G4, Xforce, Xpander or Triton, compared on size, transmission, use and October 2026 monthly.",
answer=f"For a solo or couple commute from SJDM to Quezon City or Manila, the Mirage G4 CVT is the easiest on budget ({low('mirage-g4')}). If you want SUV height for flooded roads, the Xforce fits. Families who also commute pick the Xpander A/T. Promo figures are for {MON}, subject to bank approval.",
faq=[("Manual or automatic for the SJDM to Manila drive?","Stop-and-go traffic on Quirino Highway, Commonwealth or NLEX approaches makes an automatic or CVT far less tiring for daily use."),
("Is a diesel worth it for commuting?","Diesel pickups and SUVs suit heavy loads and long drives. For pure city commuting, a smaller gasoline car is usually cheaper to run."),
("Which unit handles flooded streets better?","Higher ground clearance helps. The Xforce, Xpander Cross, Triton and Montero Sport sit higher than a sedan; never drive through deep flood water.")],
body=f'''<p>Many of my SJDM buyers drive to Quezon City, Caloocan or Manila every weekday. The right unit depends on who rides with you, where you park and what you can comfortably pay monthly. (For route and timing habits, see <a href="/tips/sjdm-to-manila-commute-tips/">SJDM to Manila commute tips</a>.)</p>
<h2>Solo or couple commuter: Mirage G4</h2>
<p>A compact sedan with a CVT option. Easy to park in the city and the lowest monthly in the lineup. <a href="/mirage-g4-downpayment-and-monthly/">Mirage G4 down payment and monthly</a>.</p>
<h2>Want SUV height: Xforce</h2>
<p>Compact SUV with a CVT across variants. Good if your route floods during the rainy season. <a href="/tips/xforce-2026-price-philippines/">Xforce 2026 price guide</a>.</p>
<h2>Family plus commute: Xpander</h2>
<p>Seven seats for school runs and weekend trips, A/T variants for traffic. <a href="/cars/xpander/">Xpander prices</a>.</p>
<h2>Commute plus work: Triton</h2>
<p>If you also haul for a business, a pickup does double duty. <a href="/triton-downpayment-and-monthly/">Triton down payment and monthly</a>.</p>
<h2>Monthly comparison</h2>
{table(["mirage-g4","xforce","xpander","triton"])}
'''+CTA("Tell me your daily route and who rides with you; I'll suggest a unit and a monthly that fits.","xforce")))

# 4 areas served
P.append(dict(base="tips",car="xpander",slug="mitsubishi-bulacan-areas-served",date=DT,by=BY,img="xc_x3n",
alt="Mitsubishi Xpander Cross for buyers across Bulacan and north Metro Manila",
title="Areas I Serve from SJDM, San Jose del Monte: Bulacan & North MM",
kw=("Mitsubishi Bulacan",["Mitsubishi Marilao","Mitsubishi Meycauayan","Mitsubishi Norzagaray","Mitsubishi Caloocan","Mitsubishi Montalban"]),
desc="Mitsubishi sales help from San Jose del Monte for buyers in SJDM, Caloocan, Quezon City, Marilao, Meycauayan, Bocaue, Norzagaray, Montalban and Malolos: how it works from your town.",
answer="I'm based in San Jose del Monte (SJDM), Bulacan, and I help Mitsubishi buyers from nearby towns: Caloocan and Novaliches, Fairview and Quezon City, Marilao, Meycauayan, Bocaue, Santa Maria, Norzagaray, Montalban (Rodriguez) and Malolos. Quotes, documents and pre-qualification can be done online.",
faq=[("Do you have branches in these towns?","No. I'm one authorized Mitsubishi sales executive based in San Jose del Monte. I serve buyers from these areas by phone, Messenger and scheduled meetings."),
("Can I get the same promo if I live outside SJDM?","Promos apply to the unit and the month, not your town. Bank approval depends on your application."),
("Where will I do PMS?","You can have your car serviced at any authorized Mitsubishi service center convenient to you. Ask me and I'll explain your options.")],
body=f'''<p>Buyers find me from all over Bulacan and the north of Metro Manila. Here's how I can help depending on where you are.</p>
<h2>Towns and cities I serve</h2>
{AREA_UL}
{NOTE_AREAS}
<h2>What we can do online first</h2>
<ul class="ticks"><li>Send this month's computation for your unit (<a href="/promos/">promos</a>)</li><li>Check your budget with the <a href="/budgetcalculator/">calculator</a></li><li>See if you're Pre-qualified with the <a href="/loan-assessment/">loan check</a></li><li>Go over your documents before submission</li></ul>
<h2>What happens in person</h2>
<p>A <a href="/test-drive/">test drive</a> (optional but recommended), signing the bank and release documents, and receiving your unit.</p>
<h2>Start here</h2>
<p>New to the process? Read the <a href="/tips/mitsubishi-buying-guide-sjdm-bulacan/">SJDM buying guide</a> and <a href="/tips/car-financing-bulacan/">car financing in Bulacan</a>.</p>
'''+CTA("Message me your town and the unit you're looking at; I'll send the computation and next steps.")))
