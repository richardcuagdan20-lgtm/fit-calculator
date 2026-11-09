# Evergreen landing pages. exec()'d inside build.py (uses page, img, e, MODELS, ILLS, D, MSG, TEL, TELD, ADDR).
# ONE data source for promo figures: data.MODELS (promo fields). Promo month: data.PROMO_YM / PROMO_UPDATED.
PROMO_MONTH=PROMO_LABEL  # local alias (label, e.g. "November 2026") from data.py
# Which verified options to show per variant id (count of options); fuel shown only where verified.
SHOW={"mg4glxat":1,"mg4gls":2,"tritongxat":2,"l300":2,"xglxmt":2,"xglxat":2,"xglsat":2,"xcross":2,
      "dglx":2,"dgls":2,"dgtm":2,"mglxmt":2,"mgls":2,"mbs2wd":1,"mbs4wd":1,"vvglx":2}
FUEL_OK={"tritongxat","l300","vvglx","mg4glxat","mg4gls"}
VBY={v["id"]:(m,v) for m in MODELS for v in m["variants"]}
def prow(i):
    m,v=VBY[i]; p=v["promo"]; srp=p["srp"] or v["srp"]
    return dict(id=i,n=v["n"],srp=srp,opts=p["opts"][:2],fuel=(p["fuel"] if i in FUEL_OK else None))
def inc(mo): return f"₱{mo/0.35/1000:.1f}K–₱{mo/0.30/1000:.1f}K"
def ptable(ids,caption,extra=""):
    rows="".join(f'<tr><th scope="row">{e(r["n"])}<br><span class="muted">SRP {f(r["srp"])}</span></th><td>{o[0]}</td><td><b>{f(o[1])}</b>/mo</td><td>{inc(o[1])}</td><td>{format(r["fuel"],",")+" fuel points" if r["fuel"] else "—"}</td></tr>' for r in map(prow,ids) for o in r["opts"])
    return f'''<div class="box" id="promo-table" style="margin-top:24px"><h2 class="h3" style="margin-top:0">{PROMO_MONTH} promo table</h2><p class="muted">{caption} Updated {PROMO_UPDATED}. 5-year (60-month) term, all-in, subject to bank approval and change without notice.</p>
<div style="overflow-x:auto"><table class="spec"><tr><th scope="col">Unit</th><th scope="col">Down payment</th><th scope="col">Monthly</th><th scope="col">Gross income guide (30–35%)</th><th scope="col">Freebie</th></tr>{rows}</table></div>{extra}</div>'''
ALLIN_E=["LTO registration","TPL insurance","Comprehensive insurance for the first year","Chattel mortgage","Free PMS labor up to 5,000 km","Factory warranty"]
ALLIN_EH="<ul class='ticks'>"+"".join(f"<li>{x}</li>" for x in ALLIN_E)+"</ul>"
DOCS='''<ul class="ticks"><li><b>Everyone:</b> two valid government IDs with matching signatures, and proof of billing</li>
<li><b>Employed:</b> certificate of employment with compensation, recent payslips or latest ITR</li>
<li><b>Business owner / self-employed:</b> DTI or SEC registration, business or mayor's permit, latest ITR or financial statements, bank statements</li>
<li><b>OFW / seafarer:</b> employment or crew contract, payslips or proof of remittance, and SPA or co-borrower details for the family member in the Philippines</li></ul>
<p class="muted">Each bank can ask for more. Full list: <a href="/guides/car-loan-requirements/">car loan requirements</a>. OFW? See the <a href="/blog/ofw-car-buying-guide/">OFW car loan guide</a>.</p>'''
INCOME='''<p>A sensible guide: keep the monthly amortization at about <b>30–35% of your gross monthly income</b>. Divide the monthly by 0.35 for a minimum income and by 0.30 for a comfortable one. A spouse or family member can sometimes join as a <a href="/tips/co-borrower-car-loan-philippines/">co-borrower</a> so the bank considers combined income. The bank always makes the final call. Try the <a href="/budgetcalculator/">budget calculator</a> to match a unit to your income in a minute.</p>'''
HOW='''<p>Every financed car comes down to four numbers:</p>
<ul class="ticks"><li><b>SRP</b>: the suggested retail price of the unit.</li><li><b>Down payment (DP)</b>: what you pay upfront. On a Zero DP promo, none; a bigger DP means a smaller loan and a lower monthly.</li><li><b>Term</b>: how long you pay. The promos here are computed on 5 years (60 months); shorter terms mean higher monthlies but less interest overall.</li><li><b>Monthly amortization</b>: the fixed amount you pay the bank each month until the loan is done.</li></ul>
<p>Compare all four together, not just the monthly. More on this in <a href="/guides/how-car-financing-works-philippines/">how car financing works</a> and <a href="/guides/zero-dp-vs-low-dp/">Zero DP vs low DP</a>.</p>'''
def CTAX(lead,unit=""):
    q=f"?unit={unit}" if unit else ""
    return f'''<h2>Your next step</h2><p>{lead}</p>
<p class="row"><a class="btn" href="/budgetcalculator/">Compute my monthly</a> <a class="btn ghost dk" href="/test-drive/{q}">Book a Test Drive</a> <a class="btn ghost dk" href="tel:{TEL}">Call or text {TELD}</a></p>
<p class="muted">{ADDR}. <a href="{MSG}" rel="noopener">Message Richard for showroom visits and directions</a>.</p>'''
LANDINGS=[]
def L(**k): LANDINGS.append(k)

L(slug="mitsubishi-sjdm-bulacan",kw="San Jose del Monte",img="xc_x3n",alt="Mitsubishi Xpander Cross, available with Richard Cuagdan in San Jose del Monte (SJDM), Bulacan",
 title="Mitsubishi SJDM: San Jose del Monte, Bulacan",
 h1="Mitsubishi in San Jose del Monte (SJDM), Bulacan",
 desc="Mitsubishi SJDM sales executive in San Jose del Monte, Bulacan: price list, low DP, test drive and Pre-qualify online, subject to bank approval.",
 kick="Mitsubishi SJDM · San Jose del Monte, Bulacan",
 lead="Richard Cuagdan is an authorized Mitsubishi sales executive and car agent in San Jose del Monte (SJDM), Bulacan. See a unit, book a test drive, get the current all-in promo and Pre-qualify online, subject to bank approval.",
 figs=[],table=[],tcap="",
 body=lambda T:f'''<p class="row">{W_msg("sjdm","local-hero",cls="btn",label="Message Richard")} {W_pq("sjdm","local-hero",cls="btn ghost dk",label="Pre-qualify")}</p>
<h2>Areas served</h2>
<p class="chips">SJDM barangays · Norzagaray · Santa Maria · Marilao · Meycauayan · Bocaue · Malolos · Caloocan / Novaliches · Fairview, Quezon City · Montalban (Rodriguez)</p>
<p>No branches in those towns: Richard serves them from San Jose del Monte. See <a href="/tips/mitsubishi-bulacan-areas-served/">areas served</a> and the <a href="/blog/mitsubishi-dealer-bulacan/">Mitsubishi Bulacan buyer guide</a>.</p>
<h2>Featured higher models</h2>
<div class="grid g2">
<a class="card pad mc" href="/destinator/"><h3>Destinator</h3><p class="muted">7-seater SUV, SRP from {W_from("destinator")}</p></a>
<a class="card pad mc" href="/cars/montero-sport/"><h3>Montero Sport</h3><p class="muted">7-seat diesel SUV, SRP from {W_from("montero-sport")}</p></a>
<a class="card pad mc" href="/cars/triton/"><h3>Triton</h3><p class="muted">Pickup, SRP from {W_from("triton")}</p></a>
<a class="card pad mc" href="/mitsubishi-hybrid-phev/"><h3>Outlander PHEV</h3><p class="muted">Plug-in hybrid SUV, SRP {W_from("outlander-phev")}</p></a></div>
{W_badge()}
<p>Every model and price: <a href="/cars/">Mitsubishi price list 2026</a>.</p>
<h2>What you can do</h2>
<ul class="ticks"><li><b>See the 2026 lineup</b>: message first so Richard can tell you which unit and color are available to view.</li>
<li><b>Test drive</b>: book a schedule on the <a href="/test-drive/">test drive page</a>, Monday to Saturday. Bring your driver's license.</li>
<li><b>Get the all-in promo</b>: low DP options with freebies, explained side by side.</li>
<li><b>Pre-check your documents</b>: Richard reviews your requirements before they go to the bank.</li></ul>
<h2>Documents to prepare</h2>
{DOCS}
'''+W_cta("sjdm","Mitsubishi lineup"),
 faq=[("Is there a Mitsubishi sales executive in San Jose del Monte?","Yes. Richard Cuagdan is an authorized Mitsubishi sales executive serving San Jose del Monte (SJDM), Bulacan and Quezon City."),
 ("Can I test drive a Mitsubishi in SJDM?","Yes. Book online on the test drive page, Monday to Saturday, 8:00 AM to 5:00 PM."),
 ("Can I get a low down payment in SJDM?","Yes. Every unit has low DP options in the current all-in promo. Pre-qualified, subject to bank approval."),
 ("Which towns do you serve?","San Jose del Monte, Norzagaray, Santa Maria, Marilao, Meycauayan, Bocaue, Malolos, Caloocan and Novaliches, Fairview and Montalban."),
 ("How do I get directions?","Message Richard on Messenger or call 0954 291 1201 for showroom visits and directions.")])

L(slug="mitsubishi-casa-bulacan",kw="Mitsubishi casa Bulacan",img="xpglx_x37",alt="Mitsubishi Xpander GLX at a Mitsubishi casa in Bulacan",
 title="Mitsubishi Casa Bulacan: SJDM, San Jose del Monte Guide",
 h1="Mitsubishi casa Bulacan: what a casa is and how to buy in SJDM (San Jose del Monte)",
 desc="Mitsubishi casa Bulacan guide: what \"casa\" means, buying brand-new in San Jose del Monte (SJDM), test drives, PMS and arranging a showroom visit.",
 kick="Richard Cuagdan · Authorized Mitsubishi Sales Executive · SJDM",
 lead="Searching \"Mitsubishi casa Bulacan\"? \"Casa\" is what most Filipinos call the brand's authorized dealership, ang mismong Mitsubishi dealer. In San Jose del Monte, that's Richard Cuagdan, an authorized Mitsubishi sales executive in San Jose del Monte. Here's what buying at a casa looks like, step by step.",
 figs=[("What \"casa\" means","cs-what","What is a casa: the authorized dealership for sales, service and genuine parts"),("Buying at the casa","cs-buy","Buying a car at the casa: from inquiry to release day"),("PMS at an authorized casa","cs-pms","Why owners bring their car back to an authorized casa for PMS"),("Directions","cs-photo","Mitsubishi Xpander on the road")],
 table=["mg4gls","xglxmt","dglx","tritongxat","l300"],tcap="Sample units.",
 body=lambda T:f'''<h2>What "casa" means</h2>
<p>In Philippine car talk, the <b>casa</b> is the brand's authorized dealership, as opposed to a second-hand lot or an independent shop. When people say "sa casa ko binili" or "sa casa ko pina-PMS," they mean an authorized dealer of the brand. A casa sells brand-new units on official SRPs, arranges bank financing, and handles service and warranty work under the brand's standards.</p>
<h2>Buying at the casa</h2>
<ol class="steps"><li><h3>Choose a unit and test drive it</h3><p>Compare models on the <a href="/cars/">cars page</a>, then <a href="/test-drive/">book a test drive</a>.</p></li>
<li><h3>Pick cash or financing</h3><p>For financing, choose Zero DP or a down payment. See <a href="/guides/zero-dp-vs-low-dp/">Zero DP vs low DP</a>.</p></li>
<li><h3>Submit documents</h3><p>I pre-check them before they go to the bank.</p></li>
<li><h3>Bank approval</h3><p>The bank evaluates your application; approval is always the bank's decision.</p></li>
<li><h3>Release day</h3><p>Inspect the unit, check the documents and freebies, then drive home. Use my <a href="/tips/new-car-release-day-checklist/">release day checklist</a>.</p></li></ol>
<h2>What the all-in package covers</h2>
<p>Casa promos are usually quoted "all-in", meaning the main fees are bundled so your cash-out is clear:</p>
{ALLIN_EH}
<p>Details vary by unit and promo. See <a href="/guides/what-all-in-includes/">what all-in includes</a>.</p>
{T}
<h2>Documents to prepare</h2>
{DOCS}
<h2>PMS at an authorized casa</h2>
<p>PMS (preventive maintenance service) follows the schedule in your owner's manual, by kilometers or months, whichever comes first. Many owners keep PMS at an authorized casa because the work follows the brand's schedule, uses genuine parts and fluids, and leaves a service record that supports warranty claims and resale value. Ask about the free PMS labor included in the all-in package. Read the <a href="/tips/pms-schedule-guide/">PMS schedule guide</a>.</p>
<h2>Will the monthly fit?</h2>
{INCOME}
<h2>Directions</h2>
<p><b>Richard Cuagdan, Mitsubishi SJDM</b>, serving San Jose del Monte (SJDM), Bulacan and Quezon City. Message or call Richard for a showroom visit and directions.</p>
<p class="row"><a class="btn ghost dk" href="{MSG}" rel="noopener">Message Richard for directions</a></p>
<p>More for SJDM buyers: <a href="/mitsubishi-sjdm-bulacan/">Mitsubishi SJDM Bulacan</a> and <a href="/brochures/">official Mitsubishi brochures (PDF)</a>.</p>
'''+CTAX("Message or call me before you go to the casa so I can have your unit ready."),
 faq=[("What does casa mean for cars in the Philippines?","Casa is the common term for a brand's authorized dealership, where you buy brand-new units and bring your car for service and warranty work."),
 ("Where is the Mitsubishi casa in San Jose del Monte?","Richard Cuagdan, authorized Mitsubishi sales executive, serves San Jose del Monte (SJDM), Bulacan and Quezon City. Message or call him for a showroom visit and directions."),
 ("Is it better to buy a car at the casa?","Buying at an authorized casa gives you a brand-new unit on official SRP, bank financing, an all-in package and warranty coverage."),
 ("Do I need to do PMS at the casa?","Follow the PMS schedule in your owner's manual. Many owners use an authorized casa to keep genuine parts and a service record that supports warranty claims."),
 ("Can I get Zero DP at the casa?","Yes, on selected units. Check the dated promo table on this page and confirm with Richard. Subject to bank approval.")])

L(slug="mirage-g4-downpayment-and-monthly",kw="Mirage G4 downpayment and monthly",img="mg4gls_u17",alt="Mitsubishi Mirage G4 GLS sedan, with downpayment and monthly options",car="mirage-g4",
 title="Mirage G4 Downpayment and Monthly: How It Works",
 h1="Mirage G4 downpayment and monthly: a plain-language guide",
 desc="Mirage G4 downpayment and monthly explained: how DP, term and monthly work, the documents, all-in inclusions, income guide, plus a dated promo table.",
 kick="Mitsubishi Mirage G4 · Sedan",
 lead="Planning your first car? This Mirage G4 downpayment and monthly guide explains how the down payment, the 5-year term and the monthly fit together, what the all-in package covers, the documents you need and the income that fits. Current promo figures sit in one dated table below, para madaling i-check.",
 figs=[("How downpayment and monthly work","mg-how","Mirage G4 downpayment and monthly: SRP, down payment, term and monthly explained"),("Documents","mg-docs","Car loan documents commonly required for a Mirage G4"),("Income guide","mg-income","Income guide: keep the car monthly at 30 to 35 percent of gross income"),("Which variant","mg-photo","Mitsubishi Mirage G4 GLX CVT sedan")],
 table=["mg4glxat","mg4gls"],tcap="Mirage G4 promos.",textra=f'<p class="muted">Mirage G4 GLX M/T and other DP options: <a href="{MSG}" rel="noopener">message Richard for the latest Mirage G4 promo</a>.</p>',
 body=lambda T:f'''<h2>How downpayment and monthly work</h2>
{HOW}
<p>For a compact sedan like the <a href="/cars/mirage-g4/">Mirage G4</a>, a down payment lowers the monthly noticeably, while Zero DP keeps your savings intact. Both are valid; it depends on whether cash on hand or a lower monthly matters more to you.</p>
<h2>Current Mirage G4 promo</h2>
{T}
<h2>What all-in covers</h2>
{ALLIN_EH}
<p>Freebies like tint, mats and a reverse camera usually come too. See <a href="/guides/what-all-in-includes/">what all-in includes</a>.</p>
<h2>Documents</h2>
{DOCS}
<h2>Income guide</h2>
{INCOME}
<h2>Which variant</h2>
<p>The Mirage G4 comes as the GLX (manual or CVT) and the GLS (CVT), all with the 1.2L gasoline engine. The CVT is easier in SJDM and EDSA traffic; the GLS adds more features. Compare them on the <a href="/cars/mirage-g4/">Mirage G4 page</a>, and read <a href="/tips/manual-vs-automatic-car-philippines/">manual vs automatic</a> if you're torn. First car? Use my <a href="/tips/first-time-car-buyer-checklist/">first-time buyer checklist</a>.</p>
'''+CTAX("Check what fits your budget, then test drive the Mirage G4 in SJDM.","mirage-g4"),
 faq=[("How much is the Mirage G4 downpayment and monthly?","See the dated promo table on this page for the current all-in options on a 5-year term. For variants or DP amounts not listed, message Richard for the latest Mirage G4 promo."),
 ("Is there a Zero DP Mirage G4?",f"Not this month. In {PROMO_MONTH} every Mirage G4 variant has Option A with a {__import__('promotext').V['mg4glxmt']['promo']['opts'][0][0].replace(' DP','')} down payment, shown in the promo table. Subject to bank approval."),
 ("What salary do I need for a Mirage G4?","As a guide, keep the monthly at about 30–35% of your gross monthly income. Divide the monthly by 0.35 for a minimum income. The bank makes the final assessment."),
 ("What documents do I need for a Mirage G4 car loan?","Two valid IDs and proof of billing, plus income documents: COE and payslips or ITR if employed, business documents if self-employed, and contract and remittance proof if you're an OFW."),
 ("Can I pay the Mirage G4 in less than 5 years?","Yes, shorter terms are available. The monthly will be higher, but you pay less interest overall. Ask Richard for a computation.")])

L(slug="triton-downpayment-and-monthly",kw="Triton down payment",img="tr_gx_u28",alt="Mitsubishi Triton GX pickup, with down payment and monthly installment options",car="triton",
 title="Triton Down Payment & Monthly Installment | SJDM",
 h1="Triton Down Payment and Monthly Installment",
 desc="Triton down payment and monthly installment per variant, Pre-qualified, subject to bank approval. Compute yours in San Jose del Monte (SJDM).",
 kick="Mitsubishi Triton · Pickup financing · SJDM",
 lead=("Here is how the Triton down payment and monthly installment work for every 2026 variant, whether the pickup is for the family, the farm or your business. Prices use the "+_PLS+" list, November update pending."),
 figs=[],table=[],tcap="",
 body=lambda T:f'''<h2>Triton monthly installment per variant</h2>
{W_vtable("triton","lp-row")}
<p class="row">{W_pq("triton","lp-table",label="Get my Pre-qualification (2 min)")} <a class="btn sm ghost dk" href="/budgetcalculator/">Compute my monthly</a></p>
<h2>How the down payment changes the monthly</h2>
<p>Every financed pickup comes down to four numbers: the SRP, the down payment, the term and the monthly. A bigger down payment means a smaller loan, a lower monthly and less interest overall. For business buyers, a lower DP keeps cash in the business for stock or payroll, while a bigger DP keeps the monthly light on cash flow. See <a href="/guides/how-car-financing-works-philippines/">how car financing works</a>.</p>
<h2>What all-in covers</h2>
{ALLIN_EH}
<h2>Documents</h2>
{DOCS}
<h2>Income guide</h2>
<p>A sensible guide: keep the monthly at about 30 to 35% of gross monthly income. For self-employed buyers, banks look at business records, so keep your ITR, financial statements and bank statements consistent. The bank always makes the final decision.</p>
<h2>Which Triton</h2>
<p>See the <a href="/cars/triton/">Triton 2026 variants</a>, the <a href="/blog/triton-price-philippines/">Triton price Philippines</a> guide, <a href="/blog/triton-gx-2wd-at-first-pickup-guide/">Triton GX 2026</a>, and <a href="/blog/triton-for-business-and-farm/">Triton for business and farm</a>.</p>
'''+W_cta("triton","Triton","triton"),
 faq=[("How much is the Triton down payment?",("The variant table shows the lowest published down payment for each Triton variant ("+_PLS+" list, November update pending). Richard can compute any other amount.")),
 ("What is the Triton monthly installment?","See the sample monthly per variant in the table: 60 months, all-in. Pre-qualified, subject to bank approval."),
 ("Can a business owner finance a Triton?","Yes. Banks typically ask for DTI or SEC registration, permits, ITR or financial statements and bank statements."),
 ("What income do I need for a Triton?","As a guide, keep the monthly at about 30 to 35% of gross monthly income."),
 ("Is the Triton 4x4 available on financing?","Yes. The GL 4WD, GLX 4WD and Athlete 4WD are in the table with their sample monthly.")])

L(slug="l300-monthly-installment",kw="L300 monthly installment",img="l300_fb",alt="Mitsubishi L300 Dual AC, with monthly installment options",car="l300",
 title="L300 Monthly Installment: Financing Guide for Negosyo",
 h1="L300 monthly installment: how it's computed and what you need",
 desc="L300 monthly installment guide: how DP and term change the monthly, business documents, all-in inclusions, income guide and a dated L300 Dual AC promo table.",
 kick="Mitsubishi L300 · Commercial",
 lead="Planning an L300 for your negosyo? This L300 monthly installment guide shows how the down payment and 5-year term set your monthly, what the all-in package covers, which documents business owners need, and how to check the monthly against your income. Current promo figures are in one dated table.",
 figs=[("How the monthly is computed","l3-how","L300 monthly installment: how SRP, down payment and term set the monthly"),("What all-in covers","l3-allin","L300 all-in package: LTO registration, TPL, comprehensive insurance, chattel mortgage"),("Documents","l3-docs","Documents for L300 financing for business owners"),("Is the L300 right","l3-photo","Mitsubishi L300 side view")],
 table=["l300"],tcap="L300 promos.",textra=f'<p class="muted">L300 Cab &amp; Chassis, FB and other body types: <a href="{MSG}" rel="noopener">message Richard for the latest promo</a>.</p>',
 body=lambda T:f'''<h2>How the monthly is computed</h2>
{HOW}
<p>For a work vehicle, think of the monthly as a business expense. Compare it with what you now pay for deliveries or rentals. My <a href="/blog/l300-negosyo-guide/">L300 negosyo guide</a> walks through simple ROI thinking.</p>
<h2>Current L300 promo</h2>
{T}
<h2>What all-in covers</h2>
{ALLIN_EH}
<h2>Documents</h2>
{DOCS}
<h2>Income guide</h2>
{INCOME}
<h2>Is the L300 right for you?</h2>
<p>The <a href="/cars/l300/">L300</a> uses a 2.2L turbo-intercooled diesel with a 5-speed manual. The Dual AC is ready to work; other body types suit custom cargo. Compare with a pickup in <a href="/blog/l300-vs-triton-for-negosyo/">L300 vs Triton</a>, and see the <a href="/blog/l300-price-philippines-2026/">L300 price 2026</a> article.</p>
'''+CTAX("Check if the L300 fits your negosyo budget, then test drive it in SJDM.","l300"),
 faq=[("How much is the L300 monthly installment?","The current all-in options on a 5-year term are in the dated promo table on this page. Other body types: message Richard for the latest promo."),
 ("Is there a Zero DP L300?","Yes, the L300 Dual AC has a Zero DP option this month, shown in the promo table, subject to bank approval."),
 ("Can I lower the L300 monthly?","A bigger down payment lowers the monthly. A shorter term raises the monthly but cuts total interest."),
 ("What documents does a business need for an L300 loan?","DTI or SEC registration, business or mayor's permit, latest ITR or financial statements, bank statements, two valid IDs and proof of billing."),
 ("Is the L300 Cab & Chassis on promo?","Message Richard for the latest Cab & Chassis and FB promo.")])

L(slug="mitsubishi-zero-down-payment-promo",kw="Mitsubishi zero down payment promo",img="xpglx_u33",alt="Mitsubishi Xpander GLX, available on a zero down payment promo",
 title="Mitsubishi Zero Down Payment Promo: How It Works",
 h1="Mitsubishi zero down payment promo: how it works and who qualifies",
 desc="Mitsubishi zero down payment promo explained: what Zero DP covers, documents, income guide, approval tips, and a dated table of this month's Zero DP units.",
 kick="Zero DP · All-in",
 lead="A Mitsubishi zero down payment promo lets you drive home a brand-new unit without a down payment, with the main fees bundled in an all-in package. Here's what Zero DP really means, who usually qualifies, the documents, and the income that fits. This month's Zero DP units are in one dated table.",
 figs=[("What zero down payment means","zp-what","Mitsubishi zero down payment promo: Zero DP vs with DP compared"),("How to avail","zp-steps","How to avail a Mitsubishi zero down payment promo in 4 steps"),("Who qualifies","zp-income","What the bank checks for Zero DP approval"),("Approval tips","zp-tips","Tips to strengthen a Zero DP car loan application")],
 table=__import__("promotext").zero_ids(),tcap="Zero DP Promo units (Option A), lowest monthly first, with Option B (30% DP) shown too.",
 textra=f'<p class="muted">Other units have Option A with a low down payment this month; see the <a href="/promos/">promos page</a>. Subject to bank approval.</p>',
 body=lambda T:f'''<h2>What zero down payment means</h2>
<p>Zero DP means you don't pay a down payment on the unit; the bank finances the full amount over the term (5 years on these promos). Because the loan is bigger, the monthly is higher than with a DP. "All-in" means the main fees are bundled:</p>
{ALLIN_EH}
<p>Always ask for the written breakdown of what, if anything, you'll pay at signing. More in <a href="/guides/what-all-in-includes/">what all-in includes</a> and <a href="/guides/zero-dp-vs-low-dp/">Zero DP vs low DP</a>.</p>
<h2>This month's Zero DP units</h2>
{T}
<h2>How to avail</h2>
<ol class="steps"><li><h3>Check your budget</h3><p>Use the <a href="/budgetcalculator/">budget calculator</a>.</p></li><li><h3>Pick a unit and test drive it</h3><p><a href="/test-drive/">Book online</a>.</p></li><li><h3>Submit documents</h3><p>I pre-check them first.</p></li><li><h3>Bank approval and release</h3><p>Approval is always the bank's decision.</p></li></ol>
<h2>Who qualifies</h2>
<p>Zero DP isn't about a special status; it's about whether the bank sees that the higher monthly fits your income and your documents check out.</p>
{INCOME}
<h2>Documents</h2>
{DOCS}
<h2>Approval tips</h2>
<ul class="ticks"><li>Pick a unit whose monthly fits the 30–35% guide.</li><li>Submit complete, consistent documents.</li><li>Settle small debts and pay cards on time.</li><li>Add a co-borrower or a small DP if the monthly is tight.</li><li>Answer the bank's verification call.</li></ul>
<p>More: <a href="/tips/car-loan-approval-tips/">car loan approval tips</a>, <a href="/blog/zero-down-payment-car-philippines/">zero down payment car list</a>, and the <a href="/blog/xpander-monthly-amortization/">Xpander monthly amortization</a> breakdown.</p>
'''+CTAX("See which Zero DP unit fits your income, then book a test drive in SJDM."),
 faq=[("Does Mitsubishi have a zero down payment promo?","Yes, on selected units each month. This month's Zero DP units are in the dated promo table on this page. Subject to bank approval."),
 ("Is zero down payment really zero?","There's no down payment on the unit, and the all-in package bundles the main fees. Ask for the written breakdown of anything due at signing."),
 ("Is Zero DP harder to get approved?","The monthly is higher, so the bank checks more closely that it fits your income. Complete documents and a realistic unit help."),
 ("What's the cheapest Mitsubishi on Zero DP?","See the promo table, sorted by Zero DP monthly, lowest first."),
 ("Can OFWs get Zero DP?","Yes, OFWs can apply. Banks usually ask for a contract, proof of remittance and an SPA or co-borrower in the Philippines.")])

L(slug="transfer-of-approval",kw="Transfer of Approval",img="xpglx_x37",alt="Mitsubishi Xpander GLX, available through Transfer of Approval with Richard Cuagdan in San Jose del Monte (SJDM), Bulacan",
 title="Transfer of Approval: Mitsubishi SJDM, San Jose del Monte",
 h1="Transfer of Approval for Mitsubishi in SJDM (San Jose del Monte), Bulacan",
 desc="Have a car loan approval from another dealer or brand? I accept Transfer of Approval for Mitsubishi in SJDM, San Jose del Monte. Subject to bank approval.",
 kick="We accept Transfer of Approval · SJDM",
 lead="May bank approval ka na from another dealer, agent or even another brand, and gusto mo nang ituloy sa Mitsubishi? I accept Transfer of Approval for buyers in San Jose del Monte (SJDM), Bulacan and nearby Quezon City. Send your approval details and I'll tell you the clear next step. Final financing is always subject to bank approval.",
 figs=[],table=[],tcap="",
 body=lambda T:f'''<p class="row">{W_msg("transfer-of-approval","toa-hero",cls="btn",label="Message Richard")} <a class="btn ghost dk" href="tel:{TEL}">Call or text {TELD}</a></p>
<h2>Who this page is for</h2>
<ul class="ticks"><li>May approval ka na, pero mabagal or hindi ka comfortable sa previous agent.</li>
<li>You were approved for one unit, but now you want a different Mitsubishi.</li>
<li>Your approval is from another brand or casa, and you want to move it to Mitsubishi with me.</li>
<li>The original dealer is far, and an SJDM or Quezon City follow-through is more practical for you.</li></ul>
<h2>How Transfer of Approval usually works</h2>
<ol class="steps"><li><h3>Send your approval details</h3><p>A clear photo or screenshot of your approval or credit advice, the bank or financing company, the original dealer or brand, and the unit you want now.</p></li>
<li><h3>I check what can move</h3><p>I review whether your file can be transferred as is or needs a new computation for the Mitsubishi unit you picked. Policies vary per bank.</p></li>
<li><h3>Sign a short transfer request letter</h3><p>Most transfers use a simple letter asking the bank to move your approval so you can continue with me. I can share a template.</p></li>
<li><h3>Bank coordination, then release</h3><p>Once the bank confirms the new quotation, we continue with your down payment, documents and release. Timelines vary, and the final decision is always the bank's.</p></li></ol>
<h2>What usually stays and what can change</h2>
<div class="grid g2"><div class="card pad"><h3>Usually stays</h3><ul class="ticks"><li>Your identity and most of your income documents, if still current</li><li>The fact that a bank already evaluated you</li><li>A faster start than applying from zero, when the bank cooperates</li></ul></div>
<div class="card pad"><h3>Can change</h3><ul class="ticks"><li>Down payment and monthly, if the price, term or promo package is different</li><li>Insurance, chattel mortgage and other items on the new quotation</li><li>The dealer and agent handling your release</li><li>Whether a more expensive unit still fits after the bank recomputes</li></ul></div></div>
<h2>What to send me</h2>
<ul class="ticks"><li><b>Required:</b> your approval letter, credit advice or a clear screenshot with the bank name visible</li>
<li><b>Required:</b> the original dealer or brand and the unit on the approval</li>
<li><b>Required:</b> the Mitsubishi unit you want now, or your shortlist</li>
<li><b>Usually needed:</b> one or two valid government IDs</li>
<li><b>If the bank asks:</b> proof of billing, and your latest payslips, COE, ITR or business documents</li>
<li><b>Later:</b> a signed transfer request letter (I'll send the template)</li></ul>
<p class="row">{W_msg("transfer-of-approval","toa-checklist",cls="btn",label="Send my approval details")}</p>
<h2>Choose your Mitsubishi and check the numbers</h2>
<p>See this month's <a href="/promos/">Mitsubishi promos</a>, browse <a href="/cars/">all models and prices</a>, or estimate your new monthly with the <a href="/budgetcalculator/">budget calculator</a>. No approval yet? Start with the free <a href="/loan-assessment/">loan application assessment</a> or the <a href="/apply/">application form</a>.</p>
'''+CTAX("May approval ka na? Message me with the checklist above and I'll give you a clear, no-pressure next step in San Jose del Monte (SJDM)."),
 faq=[("What is Transfer of Approval?","It means moving an existing car loan approval from one dealer, agent, brand or unit so you can continue with another agent or unit before the car is released. It is not the same as transferring ownership of a car that is already financed."),
 ("Pwede bang i-transfer ang approval sa ibang dealer?","Often yes, with a signed transfer request and coordination with the bank. The bank's policy decides the outcome, so send your approval details first and I'll check."),
 ("Pwede ba from another brand papuntang Mitsubishi?","Many buyers do this. The bank usually recomputes the loan for the new Mitsubishi unit against your income. Subject to bank approval."),
 ("Gaano katagal valid ang approval?","It depends on the bank and what your approval letter says. Check the date on your letter and message me early if it is close to expiring."),
 ("Ilang araw ang transfer process?","It varies per bank and on whether your unit and documents are ready. I'll give you a realistic timeline after I see your approval details."),
 ("Magbabago ba ang DP at monthly?","If the unit, price, term or promo package changes, yes. Your previous monthly does not automatically carry over to a different car."),
 ("Kailangan ko pa bang magsubmit ulit ng documents?","Sometimes the bank reuses your existing file. Have your IDs and approval copy ready either way; the bank may ask for updated income documents if the file is old or the loan amount changes a lot."),
 ("Paano kung in-house financing ang approval ko?","In-house and brand financing have their own transfer rules. Send me the approval details first so I can check what is possible."),
 ("Ano ang next step kung may approval na ako ngayon?","Message me on Messenger or call 0954 291 1201 with your approval screenshot, your preferred Mitsubishi unit and your IDs.")])

for _k in LANDINGS: _k["faq"]=list(_k["faq"])+C_LFAQ.get(_k["slug"],[])  # draft-cars A17
LAND_PATHS=[]
for a in LANDINGS:
    path=f"/{a['slug']}/"; LAND_PATHS.append((path,a)); GT_LAND.add(path)
    kw=a["kw"].lower()
    assert all(kw in a[x].lower() for x in ("title","h1","desc","lead")),(a["slug"],[x for x in ("title","h1","desc","lead") if kw not in a[x].lower()])
    assert 140<=len(a["desc"])<=160,(a["slug"],len(a["desc"]))
    assert len(a["title"])<=65,(a["slug"],len(a["title"]))
    T=ptable(a["table"],a["tcap"],a.get("textra",""))
    body=a["body"](T)
    for key,k,alt in a["figs"]:
        w,h=ILLS[k];tag=f'<figure class="fig"><img src="/assets/img/ill/{k}.webp" alt="{e(alt)}" width="{w}" height="{h}" loading="lazy" decoding="async"></figure>\n'
        i=body.find("<h2>"+key);assert i>=0,(a["slug"],key);body=body[:i]+tag+body[i:]
    fq='<h2>Frequently asked questions</h2>'+"".join(f'<h3>{e(q)}</h3><p>{e(x)}</p>' for q,x in a["faq"])
    ld=[{"@type":"WebPage","@id":D+path,"name":a["title"],"description":a["desc"],"url":D+path,"dateModified":PROMO_UPDATED,"about":{"@id":D+"/#dealer"},"author":{"@id":D+"/#richard"},"primaryImageOfPage":D+f"/assets/img/{a['img']}.webp"},
        {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":x}} for q,x in a["faq"]]}]
    if a.get("car"):
        for i in a["table"]:
            r=prow(i);ld.append({"@type":"Product","name":"Mitsubishi "+r["n"],"brand":{"@type":"Brand","name":"Mitsubishi"},"offers":{"@type":"Offer","price":r["srp"],"priceCurrency":"PHP","priceValidUntil":PROMO_END,"itemCondition":"https://schema.org/NewCondition","availability":"https://schema.org/InStock","seller":{"@id":D+"/#dealer"},"url":D+path}})
    page(path,a["title"],a["desc"],f'''<article class="art"><div class="w nar"><header><p class="kick">{e(a["kick"])}</p><h1>{e(a["h1"])}</h1><p class="muted">By <a href="/about/">Richard Cuagdan</a>, Car Sales Executive · Updated <time datetime="{PROMO_UPDATED}">{PROMO_UPDATED}</time></p></header>
{img(a["img"],a["alt"],eager=True,cls="aimg")}
<p class="lead" style="color:inherit">{e(a["lead"])}</p>
{hero_cta(lang=a.get("lang","en"),src="lp-"+a["slug"])}
{body}
{rx_bio(rx_pick(a["slug"]))}
{LACTA}
{fq}
<aside class="box"><h2 class="h3">More guides</h2><ul class="links">{"".join(f'<li><a href="/{b["slug"]}/">{e(b["title"])}</a></li>' for b in LANDINGS if b is not a)}</ul></aside></div></article>''',ld=ld,ogtype="article",img=f"/assets/img/{a['img']}.webp",og=rx_og(rx_pick(a["slug"])) if rx_pick(a["slug"]) else None,
    crumbs=[("/","Home"),(GT,GT_EN),(path,a["kw"])])
