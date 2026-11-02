# SEO/GenAI draft posts (2026-10-30, branch draft-seo). Figures come ONLY from data.py (SRP, Option A/B, fuel points)
# and promosab rows (Option B, as shown on /promos/) + promosab.RANGE (Option A range). Nothing here is live until merged.
from data import MODELS, f, ALLIN, FREEBIES
import promosab as _pab
BY="Mitsubishi Sales Executive"; DT="2026-10-30"; MON="October 2026"
VALID="Promo figures are for "+MON+" only, 60 months, all-in, subject to bank approval and change without notice. SRPs are from the official Mitsubishi Motors Philippines price list (as of August 2026)."
DISC='<p class="muted">This is Richard Cuagdan\'s personal sales website, not the official Mitsubishi Motors Philippines website. Results of any assessment are Pre-qualified, subject to bank approval.</p>'
_B={r["unit"].replace("XFORCE","Xforce").upper():r for r in _pab.rows()}
def B(n):
    r=_B.get(n.upper()); return (r["b_dp"],r["b_mo"]) if r and _pab.b_ok(r) else None
def ZDP(v):
    # Option A (lowest DP) monthly from data.py (mirrors optionAB_oct2026.json)
    return v["promo"]["opts"][0][1] if v["promo"] else None
def ADP(v): return v["promo"]["opts"][0][0] if v["promo"] else None
def ISZ(v): return bool(v["promo"]) and v["promo"]["opts"][0][0]=="Zero DP Promo"
def SRP(v): return (v["promo"] or {}).get("srp") or v["srp"]
def M(slug): return next(m for m in MODELS if m["slug"]==slug)
def inc(mo): return f"{f(round(mo/0.35/100)*100)}–{f(round(mo/0.30/100)*100)}"
def rng(slug):
    import re as _r
    ds=[]
    for v in M(slug)["variants"]:
        if not v["promo"]: continue
        l=v["promo"]["opts"][0][0]; ds.append(0 if l=="Zero DP Promo" else int(_r.sub(r"[^0-9]","",l))*1000)
    if not ds: return "message me"
    lo,hi=min(ds),max(ds)
    t=lambda x:"Zero DP Promo" if x==0 else f(x)
    return t(lo) if lo==hi else f"{t(lo)} to {f(hi)} DP"
def fuel(v): return f'{v["promo"]["fuel"]:,} fuel points' if v["promo"] and v["promo"]["fuel"] else "—"
def table(slugs,cols=("srp","zdp","b","inc")):
    h={"srp":"SRP","zdp":"Option A (lowest DP / monthly)","b":"Option B (DP / monthly)","inc":"Gross income guide*","fuel":"Freebie","a":"Option A range"}
    rows=""
    for s in slugs:
        m=M(s)
        for v in m["variants"]:
            if not SRP(v): continue
            z=ZDP(v); b=B(v["n"])
            c={"srp":f(SRP(v)),"zdp":(ADP(v)+" / "+f(z)+"/mo") if z else "—","b":(f"{f(b[0])} / {f(b[1])}/mo" if b else "—"),
               "inc":inc(z or (b[1] if b else 0)) if (z or b) else "—","fuel":fuel(v),"a":rng(s)}
            rows+="<tr><th scope='row'>"+v["n"]+"</th>"+"".join(f"<td>{c[k]}</td>" for k in cols)+"</tr>"
    return (f'<table class="spec"><thead><tr><th scope="col">Unit</th>'+"".join(f'<th scope="col">{h[k]}</th>' for k in cols)+f'</tr></thead><tbody>{rows}</tbody></table>'
            f'<p class="note">Updated {DT}. {VALID} *Income guide = the monthly at 30–35% of gross monthly income; banks decide.</p>')
ALLIN_UL="<ul class='ticks'>"+"".join(f"<li>{x}</li>" for x in ALLIN)+"</ul>"
def CTA(lead,unit=""):
    q=f"?unit={unit}" if unit else ""
    return f'''<h2>Your next step</h2>
<p>{lead}</p>
<p class="row"><a class="btn" href="/budgetcalculator/">Compute my monthly</a> <a class="btn ghost dk" href="/loan-assessment/">See if you're Pre-qualified</a> <a class="btn ghost dk" href="/test-drive/{q}">Book a Test Drive</a></p>
<p class="muted">Questions muna? Call or text 0954 291 1201. Financing is always subject to bank approval.</p>{DISC}'''
def zl(slug):
    v=[x for x in M(slug)["variants"] if ZDP(x)]
    return min(ZDP(x) for x in v) if v else None
P=[]
LOW4=", ".join(f"{v['n']} ({f(ZDP(v))}/mo)" for v in sorted([v for m in MODELS for v in m["variants"] if ZDP(v)],key=ZDP)[:4])
# ---------------------------------------------------------------- 1 monthly amortization (all models)
_ALLS=["mirage-g4","xpander","xpander-cross","xforce","destinator","triton","montero-sport","l300","versa-van","outlander-phev"]
P.append(dict(base="tips",car="xpander",slug="mitsubishi-monthly-amortization-philippines",date=DT,by=BY,img="xpglx_x37",
alt="Mitsubishi Xpander GLX, one of the most-asked monthly amortization questions in SJDM",
title="Mitsubishi Monthly Amortization Philippines (October 2026)",
kw=("Mitsubishi monthly amortization",["magkano monthly ng Mitsubishi","Mitsubishi monthly payment","Xpander monthly","Mitsubishi promo monthly 2026"]),
desc="Mitsubishi monthly amortization for October 2026: every model's SRP, Option A lowest-DP monthly, Option B 30% DP monthly and income guide in one dated table.",
answer=f"For {MON}, the lowest Mitsubishi monthly amortization on a 60-month all-in promo is {f(zl('mirage-g4'))}/mo for the Mirage G4 GLX M/T (Option A, lowest DP), {f(zl('l300'))}/mo for the L300 and {f(zl('xpander'))}/mo for the Xpander (Option A). Your actual monthly depends on the unit, your down payment, the term and the bank. Promos are subject to bank approval.",
faq=[("Magkano ang monthly ng Mitsubishi?",f"For {MON}, Option A (lowest DP) monthlies on 60 months start at {f(zl('mirage-g4'))} (Mirage G4) and go up to {f(max(ZDP(v) or 0 for m in MODELS for v in m["variants"]))} for the Outlander PHEV. Option B with a bigger down payment lowers the monthly. All subject to bank approval."),
("What is the difference between Option A and Option B?","Option A is the lowest down payment for a unit (shown on /promos/ after a short unlock form). Option B is a 30% down payment with a lower monthly. Both are all-in and subject to bank approval."),
("Is the monthly amortization fixed?","On a standard bank auto loan the monthly is fixed for the whole term once the bank approves your loan. Ask your bank to confirm before signing."),
("How much salary do I need?","A common bank guide is that the monthly should be about 30% to 35% of gross monthly income. The table shows that range for each unit; the bank makes the final decision."),
("Does the monthly include insurance and registration?","On all-in promos, the main fees (LTO registration, TPL, first-year comprehensive insurance and chattel mortgage) are bundled. Ask for the written breakdown.")],
body=f'''<p>"Magkano ang monthly?" is the first question I get on Messenger, almost every day. So here it is in one place: every Mitsubishi model, its official SRP, the {MON} Option A (lowest DP) monthly, and the Option B monthly (30% down payment) that is shown on the <a href="/promos/">promos page</a>. The figures come from the same price list the showroom uses this month, and the table is dated so you know when it was last checked.</p>
<h2>How a Mitsubishi monthly amortization is computed</h2>
<p>Your monthly amortization is the amount financed (unit price less down payment, plus the bundled all-in charges) spread over the term with the bank's add-on rate. Three things move it:</p>
<ul class="ticks"><li><b>Down payment.</b> Bigger DP, smaller loan, lower monthly. The lowest DP has the highest monthly.</li><li><b>Term.</b> The promos below are 60 months (5 years). Shorter terms raise the monthly but lower the total interest.</li><li><b>Unit and variant.</b> A GLS costs more than a GLX of the same model, so its monthly is higher.</li></ul>
<p>Want to try your own DP and term? Use the <a href="/budgetcalculator/">monthly estimate calculator</a>. It also shows the official promo for the same unit so you can compare.</p>
<h2>{MON} Mitsubishi monthly amortization table</h2>
<p>Units listed by model. "—" means there is no promo of that type for the unit this month; message me for the latest.</p>
{table(_ALLS)}
<h2>Option A: the lowest down payment</h2>
<p>Every unit on the promos page also has an <b>Option A</b>, the lowest down payment for that unit. On some units this is a <b>Zero DP Promo</b>; on others it is a small DP (for example, the Mirage G4 is "{rng('mirage-g4')}"), subject to bank approval. Option A figures are unlocked with a short form on the <a href="/promos/">promos page</a> so I can send you the exact computation for your profile.</p>
<h2>What the all-in package includes</h2>
<p>All-in means the main charges are bundled into the deal, so you are not surprised at signing:</p>
{ALLIN_UL}
<p>Read <a href="/guides/what-all-in-includes/">what all-in includes</a> for the details, and always ask for the written breakdown.</p>
<h2>How to read the income guide</h2>
<p>Banks in the Philippines usually want the car monthly to be no more than about 30% to 35% of gross monthly income, after looking at your other loans. The income column shows that range. If you are slightly below it, a co-borrower or a bigger down payment often helps. See <a href="/blog/how-much-car-can-i-afford-philippines/">how much car can I afford</a> and <a href="/tips/co-borrower-car-loan-philippines/">co-borrower car loans</a>.</p>
<h2>Tips para bumaba ang monthly</h2>
<ul class="ticks"><li>Pick the variant you actually need. A GLX with the right features is often the smarter buy.</li><li>Add even a small DP. Option B shows how much a 30% DP lowers the monthly.</li><li>Clear small debts and credit card balances before you apply.</li><li>Prepare complete documents so the bank evaluates you on your best profile. See <a href="/guides/car-loan-requirements/">car loan requirements</a>.</li></ul>
<h2>Which units have the lowest monthly this month?</h2>
<p>By Option A monthly this month: {LOW4}. For families, the Xpander is the most common choice; for business, the L300. For a 7-seat SUV, compare the <a href="/cars/destinator/">Destinator</a> and the <a href="/cars/montero-sport/">Montero Sport</a>.</p>
'''+CTA("Tell me your budget and I'll match it with a unit and the right option. Check your monthly first, then see if you're Pre-qualified in 2 minutes.")))
# ---------------------------------------------------------------- 2 zero DP & bank approval
_Z=[(v["n"],ZDP(v)) for m in MODELS for v in m["variants"] if ISZ(v)]
P.append(dict(base="tips",car="xpander",slug="zero-dp-mitsubishi-bank-approval",date=DT,by=BY,img="xpglx_u33",
alt="Mitsubishi Xpander, a popular low down payment unit in SJDM, Bulacan",
title="Zero DP Mitsubishi: What It Means and How Bank Approval Works",
kw=("zero DP Mitsubishi",["Mitsubishi zero down payment","zero DP car Bulacan","walang DP na sasakyan","zero DP bank approval"]),
desc="Zero DP Mitsubishi explained: what Zero DP Promo really covers, how the bank evaluates you, timeline, documents, and why it is subject to bank approval.",
answer="Zero DP Promo means the bank may finance the full unit price so you don't pay a down payment, with the main fees bundled in an all-in package. It is never automatic: the bank checks your income, credit record and documents first. On this site, a good result is shown as Pre-qualified, subject to bank approval.",
faq=[("Is Zero DP really zero cash out?","Zero DP means no down payment on the unit. Ask for the written breakdown of anything due at signing, such as the first monthly or reservation, because terms can vary per bank and month."),
("Why is Zero DP subject to bank approval?","Because the bank lends the full amount, it takes more risk, so it checks income, existing loans and credit history more closely. No seller can promise the result."),
("How long does bank approval take?","Usually a few working days after complete documents are submitted, longer if the bank needs more papers or verification. Incomplete documents are the main cause of delay."),
("What if the bank does not approve Zero DP?","Often the bank will offer approval with a down payment instead. Option B (30% DP) or a co-borrower are common alternatives."),
("Which Mitsubishi units have Zero DP this month?",f"In {MON}: "+", ".join(sorted({n.split(' 1.')[0].split(' 2.')[0] for n,_ in _Z}))+". See the dated table below.")],
body=f'''<p>"Zero DP" is the most searched promo term I see for Mitsubishi in Bulacan, and also the most misunderstood. It is real, and many of my clients drive home with it, but it works only when the bank says yes. This guide explains exactly what the <b>Zero DP Promo</b> is, what the bank checks, and what you can do to improve your chances.</p>
<h2>What Zero DP means (and what it doesn't)</h2>
<p>Zero DP means you do not pay a down payment on the unit. The bank finances the full unit price over the term (60 months on this month's promos). Because there is no DP, the loan is bigger and the monthly is higher than with a down payment.</p>
<p>It does <b>not</b> mean "automatic approval" or "no requirements". On the <a href="/promos/">promos page</a>, units with this option show <b>Zero DP Promo</b> as Option A, subject to bank approval, because the final DP depends on how the bank evaluates you.</p>
<h2>How bank approval works, step by step</h2>
<ol><li><b>Pre-qualification.</b> You share your income type, monthly income and existing loans. The free <a href="/loan-assessment/">AI Car Loan Application Assessment</a> gives a result in minutes: at best, Pre-qualified, subject to bank approval.</li>
<li><b>Application and documents.</b> You fill out the <a href="/apply/">application form</a> and submit IDs, proof of income and proof of billing. See <a href="/guides/car-loan-requirements/">car loan requirements</a>.</li>
<li><b>Credit investigation.</b> The bank checks your credit records and may call you, your employer or references.</li>
<li><b>Bank decision.</b> The bank may approve the loan as applied, approve with a down payment, or decline.</li>
<li><b>Signing and release.</b> Once the bank approves your loan, you sign the loan papers and we schedule the release.</li></ol>
<h2>What the bank looks at</h2>
<table class="spec"><thead><tr><th scope="col">Factor</th><th scope="col">What helps</th></tr></thead><tbody>
<tr><th scope="row">Income vs monthly</th><td>Monthly at about 30–35% of gross income or less</td></tr>
<tr><th scope="row">Stability</th><td>Regular employment, an active business with records, or a current OFW contract</td></tr>
<tr><th scope="row">Credit record</th><td>On-time payments on cards and loans, no unpaid accounts</td></tr>
<tr><th scope="row">Documents</th><td>Complete, consistent names, addresses and income figures</td></tr>
<tr><th scope="row">Reachability</th><td>Answering the bank's verification call</td></tr></tbody></table>
<h2>{MON} Option A (lowest DP) by unit</h2>
{table(["mirage-g4","xpander","xpander-cross","destinator","triton","montero-sport","l300"],cols=("srp","zdp","inc","fuel"))}
<h2>Zero DP vs paying a down payment</h2>
<p>Zero DP keeps your savings intact, which matters if you need an emergency fund. A down payment lowers the monthly and the total paid. Option B on the promos page shows a 30% DP version for every unit. For a deeper comparison, read <a href="/guides/zero-dp-vs-low-dp/">Zero DP vs low DP</a> and the <a href="/mitsubishi-zero-down-payment-promo/">Mitsubishi zero down payment promo</a> guide.</p>
<h2>Paano tumaas ang chance ma-approve</h2>
<ul class="ticks"><li>Choose a unit whose monthly fits the 30–35% guide.</li><li>Pay off or reduce small debts first.</li><li>Add a co-borrower (spouse or immediate family) if income is tight.</li><li>Submit complete documents the first time.</li><li>Keep your phone on for the verification call.</li></ul>
'''+CTA("Curious if Zero DP fits your profile? See if you're Pre-qualified in about 2 minutes, then I'll guide your bank application.")))
# ---------------------------------------------------------------- 3 OFW requirements
P.append(dict(base="tips",car="xpander",slug="ofw-car-loan-requirements-mitsubishi",date=DT,by=BY,img="xpgls_c31",
alt="Mitsubishi Xpander GLS, a common choice for OFW families in Bulacan",
title="OFW Car Loan Requirements for a Mitsubishi (2026 Checklist)",
kw=("OFW car loan requirements",["OFW car loan Mitsubishi","seafarer car loan","car loan for OFW Philippines","SPA car loan OFW"]),
desc="OFW car loan requirements for a Mitsubishi: land-based and seafarer documents, SPA vs co-borrower, remittance proof, and how to apply from abroad.",
answer="For an OFW car loan on a Mitsubishi, banks usually ask for a valid passport or government IDs, your current employment contract or certificate of employment, recent proof of remittance, and proof of billing at your Philippine address. Seafarers add their contract and sea service record. Requirements vary per bank, and approval is always the bank's decision.",
faq=[("Can I apply for a car loan while working abroad?","Yes. You can send documents online, and a family member in the Philippines can sign for you through a Special Power of Attorney (SPA) or join as a co-borrower, depending on the bank."),
("How many months of remittance do banks ask for?","It varies per bank, commonly the last 3 to 6 months. Use the same remittance channel and recipient consistently."),
("What is the difference between SPA and co-borrower?","An SPA lets someone act and sign for you. A co-borrower shares the loan obligation and their income may be counted. Banks decide which they accept for your case."),
("Can my family use the car while I'm abroad?","Yes, many OFW families do. The registered owner and insurance details should be set up correctly; ask me during the application."),
("Can I do the test drive online?","A family member can test drive in SJDM for you, and I can send video walk-arounds on Messenger.")],
body=f'''<p>Many of my clients are OFWs and seafarers buying a car for the family back home in Bulacan or Metro Manila. The process is very doable from abroad, as long as the documents are complete and the bank can reach you. Here is the checklist I send to OFW clients. For the full process (SPA, release, registration while you're away), read the <a href="/blog/ofw-car-buying-guide/">OFW car loan guide</a>.</p>
<h2>OFW car loan requirements checklist</h2>
<table class="spec"><thead><tr><th scope="col">Document</th><th scope="col">Land-based OFW</th><th scope="col">Seafarer</th></tr></thead><tbody>
<tr><th scope="row">Application form</th><td>Yes</td><td>Yes</td></tr>
<tr><th scope="row">Valid passport or 2 government IDs</th><td>Yes</td><td>Yes</td></tr>
<tr><th scope="row">Employment contract or COE with salary</th><td>Yes</td><td>Latest contract</td></tr>
<tr><th scope="row">Sea service record / work history</th><td>—</td><td>Often required</td></tr>
<tr><th scope="row">Proof of remittance (recent months)</th><td>Yes</td><td>Yes</td></tr>
<tr><th scope="row">Proof of billing (PH address)</th><td>Yes</td><td>Yes</td></tr>
<tr><th scope="row">SPA or co-borrower documents</th><td>If someone signs for you</td><td>If someone signs for you</td></tr></tbody></table>
<p class="note">This is a general checklist. Each bank sets its own list, and some ask for more. I'll confirm the exact list for your bank before you send anything. Updated {DT}.</p>
<h2>SPA or co-borrower?</h2>
<p>A <b>Special Power of Attorney (SPA)</b> lets a trusted person in the Philippines sign and process papers for you. A <b>co-borrower</b> shares the loan, and the bank may consider combined income. If your spouse has income here, a co-borrower setup can strengthen the application. Read <a href="/tips/co-borrower-car-loan-philippines/">co-borrower car loans</a>.</p>
<h2>How to apply from abroad, step by step</h2>
<ol><li>Check what fits your budget with the <a href="/budgetcalculator/">calculator</a>.</li><li>Take the free <a href="/loan-assessment/">assessment</a>; a good result reads Pre-qualified, subject to bank approval.</li><li>Fill out the <a href="/apply/">application</a> and send clear scans of your documents.</li><li>Answer the bank's verification call or email, even if you're on a different time zone.</li><li>Once the bank approves, your SPA or co-borrower signs, and your family picks up the unit in SJDM.</li></ol>
<h2>Popular units for OFW families this month</h2>
{table(["xpander","xpander-cross","destinator","mirage-g4"],cols=("srp","zdp","b"))}
<h2>Common reasons OFW applications get delayed</h2>
<ul class="ticks"><li>Expired or soon-to-expire contract.</li><li>Remittances to different recipients every month.</li><li>Names spelled differently across IDs and documents.</li><li>The bank cannot reach the applicant for verification.</li></ul>
<h2>Timing tips</h2>
<p>If you want the unit ready before you come home for Christmas, start the application early so there is time for documents, bank evaluation and release. Message me with your target date and I'll work backwards from it.</p>
'''+CTA("Working abroad? Send your target release date and I'll plan the documents and timeline with you.","xpander")))
# ---------------------------------------------------------------- 4 Montero vs Triton
ms=M("montero-sport"); tr=M("triton")
def sp(m,k): return dict(m["specs"]).get(k,"—")
P.append(dict(base="tips",car="montero-sport",slug="montero-sport-vs-triton",date=DT,by=BY,img="ms_white",
alt="Mitsubishi Montero Sport GLS, compared with the Triton pickup for work and family use",
title="Montero Sport vs Triton: Which Fits Work vs Family?",
kw=("Montero Sport vs Triton",["Triton vs Montero Sport","SUV or pickup Philippines","Triton for family","Montero Sport monthly"]),
desc="Montero Sport vs Triton: diesel SUV or pickup? Seats, cargo, engines, October 2026 SRPs and monthlies, and who each one fits, from an SJDM sales executive.",
answer=f"Choose the Montero Sport if you mainly carry people: it seats 7, has a closed, quieter cabin and an 8-speed automatic on most variants. Choose the Triton if you carry cargo for work: it has an open bed and more variants for business, with SRPs from {f(1266000)}. Both are diesel and built for rough roads.",
faq=[("Can the Triton be a family car?","Yes, the double-cab Triton seats 5 and many families use it. But cargo in the open bed is exposed to rain, and it seats fewer than the 7-seat Montero Sport."),
("Which is cheaper, Montero Sport or Triton?",f"The Triton starts lower: {f(1266000)} SRP for the GL 2WD M/T vs {f(1568000)} for the Montero Sport GLX M/T (August 2026 price list)."),
("Which has a Zero DP option this month?",f"In {MON}: "+", ".join(v["n"] for s_ in ("triton","montero-sport") for v in M(s_)["variants"] if ISZ(v))+" have a Zero DP Promo option; other variants have a low DP. Subject to bank approval."),
("Is a pickup better for business taxes or registration?","That depends on your business setup; ask your accountant. I can help with business financing documents."),
("Which is better for flooded roads?","Both are body-on-frame diesels with good ground clearance. Always avoid deep floodwater regardless of vehicle.")],
body=f'''<p>Business owners and growing families in Bulacan often narrow it down to these two diesels. They share Mitsubishi's tough reputation, but they are built for different jobs. Here's how I explain the choice on the showroom floor.</p>
<h2>Quick comparison</h2>
<table class="spec"><thead><tr><th scope="col"></th><th scope="col">Montero Sport</th><th scope="col">Triton</th></tr></thead><tbody>
<tr><th scope="row">Body</th><td>7-seat SUV, closed cabin</td><td>Pickup with open cargo bed</td></tr>
<tr><th scope="row">Engine</th><td>{sp(ms,"Engine")}</td><td>{sp(tr,"Engine")}</td></tr>
<tr><th scope="row">Transmission</th><td>{sp(ms,"Transmission")}</td><td>{sp(tr,"Transmission")}</td></tr>
<tr><th scope="row">Seating</th><td>7</td><td>5 (double cab)</td></tr>
<tr><th scope="row">SRP range</th><td>{f(1568000)} – {f(2530000)}</td><td>{f(1266000)} – {f(2359000)}</td></tr>
<tr><th scope="row">Best for</th><td>{ms["who"]}</td><td>{tr["who"]}</td></tr></tbody></table>
<p class="note">Specs summarized from Mitsubishi Motors Philippines; SRPs from the official price list as of August 2026.</p>
<h2>Choose the Montero Sport if…</h2>
<ul class="ticks"><li>You regularly carry 5 to 7 people, including kids and seniors.</li><li>You want luggage inside a closed, air-conditioned cabin.</li><li>You drive long distances (Baguio, La Union, Bicol) and want a quieter ride.</li><li>You want the Black Series look or 4WD for provincial roads.</li></ul>
<h2>Choose the Triton if…</h2>
<ul class="ticks"><li>You carry tools, produce, materials or stock for your negosyo.</li><li>You want a lower starting price and more variant choices (GL, GX, GLX, GLS, Athlete).</li><li>You need 4WD on a manual for farm or resort roads.</li><li>You want one vehicle for weekday work and weekend family trips with 5 seats.</li></ul>
<h2>{MON} prices and monthlies</h2>
{table(["montero-sport","triton"])}
<h2>Financing for business owners</h2>
<p>Self-employed buyers usually submit business registration, recent bank statements and IDs. Banks look at the business's cash flow, so keep deposits regular. See <a href="/blog/triton-for-business-and-farm/">Triton for business and farm</a>, <a href="/triton-downpayment-and-monthly/">Triton downpayment and monthly</a>, and <a href="/blog/montero-sport-variants-explained/">Montero Sport variants explained</a>.</p>
<h2>Test drive both back-to-back</h2>
<p>The fastest way to decide is to drive both the same day in SJDM, with the people who'll ride most often. Sit in the second and third rows of the Montero, and load-test the Triton bed with what you actually carry.</p>
'''+CTA("Book a back-to-back test drive of the Montero Sport and Triton in SJDM.","montero-sport")))
# ---------------------------------------------------------------- 5 Option A vs B
P.append(dict(base="tips",car="destinator",slug="option-a-vs-option-b-mitsubishi-promo",date=DT,by=BY,img="de_x3n",
alt="Mitsubishi Destinator GT two-tone, shown with Option A and Option B promo choices",
title="Option A vs Option B: Choosing Your Mitsubishi Promo",
kw=("Mitsubishi promo Option A vs Option B",["lowest DP or low monthly","Mitsubishi promo SJDM","30% down payment car","all-in DP Mitsubishi"]),
desc="Option A (lowest down payment) vs Option B (30% DP, lower monthly) on Mitsubishi promos in SJDM: how each works, examples, and how to choose for your budget.",
answer="On the promos page, every Mitsubishi unit has two all-in options. Option A is the lowest down payment (Zero DP Promo on select units, subject to bank approval), with a higher monthly. Option B is a 30% down payment with a lower monthly. Pick A to keep your cash; pick B to lower the monthly and total paid.",
faq=[("Why is Option A locked?","Option A figures are shown after a short form so I can send the exact computation and confirm it for your profile. The form does not commit you to anything."),
("Is Option B exactly 30%?","Option B is the 30% DP package shown on the promos page; the exact peso DP and monthly per unit are in the table."),
("Can I choose a DP between A and B?","Yes. Use the monthly estimate calculator to try your own DP, then I'll confirm the official computation."),
("Are both options all-in?","Yes, both bundle the main fees like LTO registration, insurance and chattel mortgage. Ask for the written breakdown."),
("Is either option guaranteed?","No. Both are subject to bank approval.")],
body=f'''<p>When I rebuilt the <a href="/promos/">promos page</a>, I simplified every unit into two choices, because that's how most buyers decide anyway: "Gusto ko maliit ang ilalabas" or "Gusto ko maliit ang monthly." Here's how to choose.</p>
<h2>The two options in one table</h2>
<table class="spec"><thead><tr><th scope="col"></th><th scope="col">Option A</th><th scope="col">Option B</th></tr></thead><tbody>
<tr><th scope="row">Down payment</th><td>Lowest for the unit (Zero DP Promo on select units)</td><td>30% DP</td></tr>
<tr><th scope="row">Monthly</th><td>Higher</td><td>Lower</td></tr>
<tr><th scope="row">Total paid over 60 months</th><td>Higher</td><td>Lower</td></tr>
<tr><th scope="row">Best for</th><td>Buyers who want to keep savings</td><td>Buyers with cash ready who want a lighter monthly</td></tr>
<tr><th scope="row">Bank approval</th><td>Required</td><td>Required</td></tr></tbody></table>
<h2>Option A ranges by model</h2>
<table class="spec"><thead><tr><th scope="col">Model</th><th scope="col">Option A (lowest DP)</th></tr></thead><tbody>'''+"".join(f"<tr><th scope='row'>{M(s)['name']}</th><td>{rng(s)}</td></tr>" for s in ["mirage-g4","xpander","xforce","destinator","triton","montero-sport","l300","versa-van","outlander-phev"])+f'''</tbody></table>
<p class="note">As shown on the promos page, {MON}, subject to bank approval. Exact Option A figures per variant are on the promos page after the short unlock form.</p>
<h2>Option B examples ({MON})</h2>
{table(["xpander","destinator","triton","l300"],cols=("srp","b","inc"))}
<h2>How to choose</h2>
<ul class="ticks"><li><b>Keep an emergency fund first.</b> If paying 30% would empty your savings, Option A is usually safer.</li><li><b>Check the monthly against your income.</b> If Option A's monthly goes above about 35% of gross income, Option B or a co-borrower may get a better bank result.</li><li><b>Think total cost.</b> A bigger DP means less interest over 60 months.</li><li><b>Business owners:</b> compare with your cash flow cycle, not just the monthly.</li></ul>
<p>Still unsure? Try your own numbers in the <a href="/budgetcalculator/">calculator</a> or read <a href="/guides/zero-dp-vs-low-dp/">Zero DP vs low DP</a>.</p>
'''+CTA("Unlock Option A on the promos page, or ask me to compute a DP in between.")))
# ---------------------------------------------------------------- 6 Xforce price
xf=M("xforce")
P.append(dict(base="tips",car="xforce",slug="xforce-2026-price-philippines",date=DT,by=BY,img="xf_gls",
alt="Mitsubishi Xforce GLS compact SUV",
title="Mitsubishi Xforce 2026 Price Philippines: GLX vs GLS vs GT",
kw=("Xforce price Philippines",["Xforce 2026 price","Xforce GLX vs GLS","Xforce GT price","Xforce monthly"]),
desc="Mitsubishi Xforce 2026 price Philippines: GLX, GLS and GT SRPs, Option B monthly, what changes per variant, and who the compact SUV fits best.",
answer=f"The Mitsubishi Xforce 2026 SRP in the Philippines is {f(1119000)} for the GLX, {f(1299000)} for the GLS monotone, {f(1309000)} for the GLS two-tone and {f(1661000)} for the GT, all 1.5L gasoline CVT 2WD (official price list as of August 2026). Option A is a lowest DP of {rng('xforce')}, subject to bank approval.",
faq=[("What engine does the Xforce have?","A 1.5L gasoline engine with a CVT and front-wheel drive (2WD) across the lineup."),
("Is the Xforce a 7-seater?","No, it's a 5-seat compact SUV. For 7 seats, look at the Xpander, Xpander Cross or Destinator."),
("Xforce or Xpander Cross?","The Xforce is a 5-seat compact SUV with a more car-like drive; the Xpander Cross is a 7-seat crossover MPV. Choose by how many people you carry."),
("Does the Xforce have Zero DP this month?",f"For {MON}, the Xforce Option A on the promos page is {rng('xforce')}, subject to bank approval."),
("Where can I test drive the Xforce near SJDM?","Book online and I'll prepare a unit in San Jose del Monte, Bulacan.")],
body=f'''<p>The Xforce is Mitsubishi's compact SUV for buyers moving up from a sedan or hatchback: raised seating, bold styling, and a size that still parks easily in SM San Jose del Monte or Fairview. Here are the 2026 prices and how the variants differ.</p>
<h2>Xforce 2026 prices (SRP)</h2>
{table(["xforce"],cols=("srp","b","inc"))}
<h2>Key specs</h2>
<table class="spec"><tbody>'''+"".join(f"<tr><th scope='row'>{a}</th><td>{b}</td></tr>" for a,b in xf["specs"])+f'''<tr><th scope="row">Seating</th><td>5</td></tr></tbody></table>
<p class="note">Specs summarized from Mitsubishi Motors Philippines. Ask me for the full spec sheet of a specific variant.</p>
<h2>GLX vs GLS vs GT: how to choose</h2>
<ul class="ticks"><li><b>GLX</b> is the entry point and the lowest monthly, good for first SUV owners watching the budget.</li><li><b>GLS</b> (monotone or two-tone) is the middle trim most buyers look at for a more premium feel; the two-tone adds a contrasting roof for {f(10000)} more on SRP.</li><li><b>GT</b> is the top variant for buyers who want the most equipment.</li></ul>
<p>Feature lists change by model year, so I'll send you the official spec sheet for the exact variant before you decide. Don't rely on a feature unless it's on that sheet.</p>
<h2>Who the Xforce fits</h2>
<p>A good fit for {xf["who"]}. If you regularly carry more than 5 people, compare the <a href="/cars/xpander-cross/">Xpander Cross</a> or the <a href="/cars/destinator/">Destinator</a>; read <a href="/guides/xpander-vs-xpander-cross-vs-destinator/">Xpander vs Xpander Cross vs Destinator</a>.</p>
<h2>Financing the Xforce</h2>
<p>On the <a href="/promos/">promos page</a>, every Xforce variant has Option A (lowest DP, {rng('xforce')}) and Option B (30% DP, lower monthly), both all-in and subject to bank approval. Freebies vary per variant and month; ask me for this month's list.</p>
'''+CTA("Want to see the Xforce in person? Book a test drive in SJDM.","xforce")))
# 7 FAQ hub (/tips/mitsubishi-sjdm-buyer-faq/) HELD BACK until the FAQ list from Fina and Mark is approved (see branch draft-seo for the old draft).
