# Evergreen landing pages. exec()'d inside build.py (uses page, img, e, MODELS, ILLS, D, MSG, TEL, TELD, ADDR, MAPQ).
# ONE data source for promo figures: data.MODELS (promo fields). Update the month there + PROMO_MONTH below.
PROMO_MONTH="October 2026"; PROMO_UPDATED="2026-10-22"
# Which verified options to show per variant id (count of options); fuel shown only where verified.
SHOW={"mg4glxat":1,"mg4gls":2,"tritongxat":2,"l300":2,"xglxmt":2,"xglxat":2,"xglsat":2,"xcross":2,
      "dglx":2,"dgls":2,"dgtm":2,"mglxmt":2,"mgls":2,"mbs2wd":1,"mbs4wd":1,"vvglx":2}
FUEL_OK={"tritongxat","l300","vvglx","mg4glxat","mg4gls"}
VBY={v["id"]:(m,v) for m in MODELS for v in m["variants"]}
def prow(i):
    m,v=VBY[i]; p=v["promo"]; srp=p["srp"] or v["srp"]
    return dict(id=i,n=v["n"],srp=srp,opts=p["opts"][:SHOW[i]],fuel=(p["fuel"] if i in FUEL_OK else None))
def inc(mo): return f"₱{mo/0.35/1000:.1f}K–₱{mo/0.30/1000:.1f}K"
def ptable(ids,caption,extra=""):
    rows="".join(f'<tr><th scope="row">{e(r["n"])}<br><span class="muted">SRP {f(r["srp"])}</span></th><td>{o[0]}</td><td><b>{f(o[1])}</b>/mo</td><td>{inc(o[1])}</td><td>{f(r["fuel"])+" fuel" if r["fuel"] else "—"}</td></tr>' for r in map(prow,ids) for o in r["opts"])
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
<p class="muted">Showroom: {ADDR}. <a href="https://www.google.com/maps/dir/?api=1&amp;destination={MAPQ}" target="_blank" rel="noopener">Get directions on Google Maps</a>.</p>'''
LANDINGS=[]
def L(**k): LANDINGS.append(k)

L(slug="mitsubishi-sjdm-bulacan",kw="Mitsubishi SJDM Bulacan",img="xc_x3n",alt="Mitsubishi Xpander Cross, available at Mitsubishi SJ Legacy Motors in SJDM, Bulacan",
 title="Mitsubishi SJDM Bulacan: SJ Legacy Motors Sales & Promos",
 h1="Mitsubishi SJDM Bulacan: buy your Mitsubishi in San Jose del Monte",
 desc="Mitsubishi SJDM Bulacan: Mitsubishi SJ Legacy Motors on Quirino Highway, San Jose del Monte. Promos, test drive, financing help and directions in one place.",
 kick="San Jose del Monte, Bulacan",
 lead="Searching for Mitsubishi SJDM Bulacan? Mitsubishi SJ Legacy Motors is an authorized Mitsubishi dealer on Quirino Highway in Sto. Cristo, San Jose del Monte, and I'm Richard Cuagdan, one of its sales executives. Here's how to see a unit, test drive it, get the current all-in promo and finance it, kahit first time mo pa lang.",
 figs=[("Where to find us","sj-loc","Mitsubishi SJDM Bulacan: Mitsubishi SJ Legacy Motors on Quirino Highway, Sto. Cristo, San Jose del Monte"),("What you can do","sj-what","What you can do at the Mitsubishi dealership in SJDM: see units, test drive, get the promo, pre-check documents"),("Plan your visit","sj-plan","Three steps to plan a Mitsubishi showroom visit in SJDM"),("Popular units","sj-photo","Mitsubishi Xpander Cross 7-seater")],
 table=["mg4gls","xglxat","xcross","dglx","tritongxat","l300","vvglx","mglxmt"],tcap="Popular units at SJ Legacy Motors.",
 body=lambda T:f'''<h2>Where to find us</h2>
<p><b>Mitsubishi SJ Legacy Motors</b>, Lot 9 Ebenezer Christian Academy, Sitio Gitna, Sto. Cristo, Quirino Highway, San Jose del Monte, Bulacan. It's along the main Quirino Highway corridor, so it's a straightforward drive from the rest of SJDM, Norzagaray, Santa Maria and the northern edge of Metro Manila (Fairview, Novaliches, Caloocan North).</p>
<p class="row"><a class="btn ghost dk" href="https://www.google.com/maps/dir/?api=1&amp;destination={MAPQ}" target="_blank" rel="noopener">Get directions on Google Maps</a> <a class="btn ghost dk" href="tel:{TEL}">Call or text {TELD}</a></p>
<h2>What you can do</h2>
<ul class="ticks"><li><b>See the 2026 lineup</b>: <a href="/cars/mirage-g4/">Mirage G4</a>, <a href="/cars/xpander/">Xpander</a>, <a href="/cars/xpander-cross/">Xpander Cross</a>, <a href="/cars/destinator/">Destinator</a>, <a href="/cars/montero-sport/">Montero Sport</a>, <a href="/cars/triton/">Triton</a>, <a href="/cars/l300/">L300</a> and more. Message me first so I can tell you which unit and color are available to view.</li>
<li><b>Test drive</b>: book a schedule online on the <a href="/test-drive/">test drive page</a>. Bring your driver's license.</li>
<li><b>Get the all-in promo</b>: Zero DP and low-DP options with freebies, explained side by side.</li>
<li><b>Pre-check your documents</b>: I review your requirements before they go to the bank, so there are fewer back-and-forths.</li></ul>
<h2>Popular units</h2>
<p>These are the units SJDM families and negosyo owners ask about most. The figures live in one dated table so they're easy to check against the latest promo.</p>
{T}
<p>For variants not shown (Mirage G4 GLX MT, other Triton variants, L300 Cab &amp; Chassis, Xforce, Outlander PHEV), <a href="{MSG}" rel="noopener">message Richard for the latest promo</a>.</p>
<h2>How financing works here</h2>
{HOW}
<h2>Documents to prepare</h2>
{DOCS}
<h2>Will the monthly fit?</h2>
{INCOME}
<h2>Plan your visit</h2>
<ol class="steps"><li><h3>Check your budget</h3><p>Use the <a href="/budgetcalculator/">budget calculator</a> to see which units fit.</p></li><li><h3>Book a test drive</h3><p>Pick the unit and time on the <a href="/test-drive/">test drive page</a>.</p></li><li><h3>Message or call me</h3><p>Call or text {TELD} so the unit is ready when you arrive. Coming from the city? Read <a href="/blog/mitsubishi-near-fairview-quezon-city/">Mitsubishi near Fairview</a> or <a href="/blog/mitsubishi-near-caloocan-novaliches/">near Caloocan and Novaliches</a>.</p></li></ol>
<p>Want to know what "casa" means and what to expect at an authorized dealership? See <a href="/mitsubishi-casa-bulacan/">Mitsubishi casa Bulacan</a>. Bulacan buyers can also read <a href="/blog/mitsubishi-dealer-bulacan/">Mitsubishi dealer Bulacan</a>.</p>
'''+CTAX("Check your budget, then book a test drive in SJDM. I'll have your unit ready."),
 faq=[("Where is Mitsubishi in SJDM, Bulacan?","Mitsubishi SJ Legacy Motors is at Lot 9 Ebenezer Christian Academy, Sitio Gitna, Sto. Cristo, Quirino Highway, San Jose del Monte, Bulacan. Use the Google Maps link on this page for directions."),
 ("Is Mitsubishi SJ Legacy Motors an authorized Mitsubishi dealer?","Yes. Mitsubishi SJ Legacy Motors is an authorized Mitsubishi dealer."),
 ("Can I test drive a Mitsubishi in SJDM?","Yes. Book a schedule on the test drive page and bring a valid driver's license. Richard will confirm your slot."),
 ("Does the SJDM dealership have Zero DP promos?","Yes. This month's Zero DP and low-DP options are in the dated promo table on this page. They're all-in and subject to bank approval."),
 ("How do I contact a Mitsubishi sales executive in SJDM?","Call or text Richard Cuagdan on 0954 291 1201, or use the live chat on this website."),
 ("Can OFWs buy from the SJDM dealership?","Yes. OFWs can apply from abroad with an SPA or a co-borrower in the Philippines. See the OFW car loan guide.")])

L(slug="mitsubishi-casa-bulacan",kw="Mitsubishi casa Bulacan",img="xpglx_x37",alt="Mitsubishi Xpander GLX at a Mitsubishi casa in Bulacan",
 title="Mitsubishi Casa Bulacan: Buying at the SJDM Dealership",
 h1="Mitsubishi casa Bulacan: what a casa is and how to buy there",
 desc="Mitsubishi casa Bulacan guide: what \"casa\" means, buying at the SJDM dealership, test drives, PMS at an authorized casa, and Google Maps directions.",
 kick="Authorized Mitsubishi dealer · SJDM",
 lead="Searching \"Mitsubishi casa Bulacan\"? \"Casa\" is what most Filipinos call the brand's authorized dealership, ang mismong Mitsubishi dealer. In San Jose del Monte, that's Mitsubishi SJ Legacy Motors on Quirino Highway, an authorized Mitsubishi dealer. Here's what buying at a casa looks like, step by step.",
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
<p><b>Mitsubishi SJ Legacy Motors</b>, {ADDR.replace("Mitsubishi SJ Legacy Motors, ","")}.</p>
<p class="row"><a class="btn ghost dk" href="https://www.google.com/maps/dir/?api=1&amp;destination={MAPQ}" target="_blank" rel="noopener">Open in Google Maps</a></p>
<p>More on the SJDM dealership: <a href="/mitsubishi-sjdm-bulacan/">Mitsubishi SJDM Bulacan</a>.</p>
'''+CTAX("Message or call me before you go to the casa so I can have your unit ready."),
 faq=[("What does casa mean for cars in the Philippines?","Casa is the common term for a brand's authorized dealership, where you buy brand-new units and bring your car for service and warranty work."),
 ("Where is the Mitsubishi casa in San Jose del Monte?","Mitsubishi SJ Legacy Motors, Lot 9 Ebenezer Christian Academy, Sitio Gitna, Sto. Cristo, Quirino Highway, San Jose del Monte, Bulacan. Use the Google Maps link for directions."),
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
 ("Is there a Zero DP Mirage G4?","Zero DP depends on the month's promo and the variant. The current options are in the promo table; message Richard to confirm."),
 ("What salary do I need for a Mirage G4?","As a guide, keep the monthly at about 30–35% of your gross monthly income. Divide the monthly by 0.35 for a minimum income. The bank makes the final assessment."),
 ("What documents do I need for a Mirage G4 car loan?","Two valid IDs and proof of billing, plus income documents: COE and payslips or ITR if employed, business documents if self-employed, and contract and remittance proof if you're an OFW."),
 ("Can I pay the Mirage G4 in less than 5 years?","Yes, shorter terms are available. The monthly will be higher, but you pay less interest overall. Ask Richard for a computation.")])

L(slug="triton-downpayment-and-monthly",kw="Triton downpayment and monthly",img="tr_gx_u28",alt="Mitsubishi Triton GX pickup, with downpayment and monthly options",car="triton",
 title="Triton Downpayment and Monthly: Pickup Financing Guide",
 h1="Triton downpayment and monthly: how pickup financing works",
 desc="Triton downpayment and monthly guide: Zero DP vs low DP, documents for business owners, all-in inclusions, income guide and a dated Triton GX promo table.",
 kick="Mitsubishi Triton · Pickup",
 lead="Here's how Triton downpayment and monthly options work, whether the pickup is for the family, the farm or your negosyo. I cover Zero DP vs low DP, the documents business owners usually need, the all-in package, and the income that fits. Ang current figures ay nasa isang dated promo table.",
 figs=[("Zero DP or low DP","tr-how","Triton downpayment and monthly: Zero DP vs low DP compared"),("Documents","tr-docs","Business owner documents for a Triton car loan"),("Income guide","tr-income","Triton income guide: monthly at 30 to 35 percent of gross income"),("Which Triton","tr-photo","Mitsubishi Triton pickup")],
 table=["tritongxat"],tcap="Triton promos.",textra=f'<p class="muted">Triton GL, GLX, GLS, 4x4 and Athlete variants: <a href="{MSG}" rel="noopener">message Richard for the latest promo</a>.</p>',
 body=lambda T:f'''<h2>How it works</h2>
{HOW}
<h2>Zero DP or low DP</h2>
<p>For business buyers, Zero DP keeps cash in the business for stock, payroll or equipment, at the cost of a higher monthly. A down payment lowers the monthly so the pickup is lighter on monthly cash flow. Pick based on which is tighter for you: cash today or cash every month. See <a href="/guides/zero-dp-vs-low-dp/">Zero DP vs low DP</a>.</p>
{T}
<h2>What all-in covers</h2>
{ALLIN_EH}
<h2>Documents</h2>
{DOCS}
<h2>Income guide</h2>
{INCOME}
<p>For self-employed buyers, banks look at business records rather than payslips, so keep your ITR, financial statements and bank statements consistent.</p>
<h2>Which Triton</h2>
<p>The <a href="/cars/triton/">Triton</a> comes in 2WD and 4WD, manual and automatic, from the GL up to the Athlete. The GX 2WD A/T is a popular first pickup for its automatic gearbox. Read the <a href="/blog/triton-gx-2wd-at-first-pickup-guide/">Triton GX first-pickup guide</a>, <a href="/blog/triton-for-business-and-farm/">Triton for business and farm</a>, and <a href="/blog/l300-vs-triton-for-negosyo/">L300 vs Triton</a>.</p>
'''+CTAX("Check if a Triton fits your budget, then test drive it in SJDM.","triton"),
 faq=[("How much is the Triton downpayment and monthly?","The current all-in options on a 5-year term are in the dated promo table on this page. For other variants, message Richard for the latest promo."),
 ("Is there a Zero DP Triton?","Yes, on the variant shown in the promo table this month. Zero DP is subject to bank approval."),
 ("Can a business owner finance a Triton?","Yes. Banks typically ask for DTI or SEC registration, permits, ITR or financial statements and bank statements."),
 ("What income do I need for a Triton?","As a guide, keep the monthly at about 30–35% of gross monthly income. The table shows the income range for each option."),
 ("Is the Triton 4x4 on promo?","Message Richard for the latest promo on 4WD and other Triton variants.")])

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
 table=["mg4gls","l300","xglxmt","xglxat","xglsat","xcross","dglx","tritongxat","mglxmt","dgls","mgls","dgtm"],tcap="Units with a Zero DP option, lowest monthly first. Low-DP alternatives shown too.",
 textra=f'<p class="muted">Montero Sport Black Series is offered with a down payment this month (2WD: ₱88K DP, ₱45,117/mo; 4WD: ₱133K DP, ₱52,121/mo). Mirage G4 GLX and other variants: <a href="{MSG}" rel="noopener">message Richard for the latest promo</a>.</p>',
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

LAND_PATHS=[]
for a in LANDINGS:
    path=f"/{a['slug']}/"; LAND_PATHS.append((path,a))
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
            r=prow(i);ld.append({"@type":"Product","name":"Mitsubishi "+r["n"],"brand":{"@type":"Brand","name":"Mitsubishi"},"offers":{"@type":"Offer","price":r["srp"],"priceCurrency":"PHP","priceValidUntil":"2026-10-31","itemCondition":"https://schema.org/NewCondition","availability":"https://schema.org/InStock","seller":{"@id":D+"/#dealer"},"url":D+path}})
    page(path,a["title"],a["desc"],f'''<article class="art"><div class="w nar"><header><p class="kick">{e(a["kick"])}</p><h1>{e(a["h1"])}</h1><p class="muted">By <a href="/about/">Richard Cuagdan</a>, Car Sales Executive · Updated <time datetime="{PROMO_UPDATED}">{PROMO_UPDATED}</time></p></header>
{img(a["img"],a["alt"],eager=True,cls="aimg")}
<p class="lead" style="color:inherit">{e(a["lead"])}</p>
<p class="row"><a class="btn" href="/budgetcalculator/">Compute my monthly</a> <a class="btn ghost dk" href="/test-drive/{"?unit="+a["car"] if a.get("car") else ""}">Book a Test Drive</a> <a class="btn ghost dk" href="tel:{TEL}">Call {TELD}</a></p>
{body}
{LACTA}
{fq}
<aside class="box"><h2 class="h3">More guides</h2><ul class="links">{"".join(f'<li><a href="/{b["slug"]}/">{e(b["title"])}</a></li>' for b in LANDINGS if b is not a)}</ul></aside></div></article>''',ld=ld,ogtype="article",img=f"/assets/img/{a['img']}.webp",
    crumbs=[("/","Home"),("/promos-tips/","Promos & Tips"),(path,a["kw"])])
