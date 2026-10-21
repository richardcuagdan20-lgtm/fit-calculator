import re
# SEO layer (keyword research Oct 22, 2026: Google PH autocomplete + related searches).
# slug -> (primary keyword, [secondary keywords], title override or None, meta description 150-160 chars)
SEO={
# --- original 10
"undas-road-trip-checklist-2026":("undas road trip checklist",["NLEX Undas traffic 2026","BLOWBAGETS","road trip checklist Philippines","what to bring on a road trip"],"Undas Road Trip Checklist 2026 for Families",
 "Undas road trip checklist for 2026: BLOWBAGETS pre-trip check, RFID and NLEX traffic dates, packing for kids and seniors, and what to do if you break down."),
"first-time-car-buyer-checklist":("first time car buyer checklist",["buying first car Philippines","car loan documents","bank vs in-house financing","cost of owning a car"],"First-Time Car Buyer Checklist Philippines (2026)",
 "First time car buyer checklist for the Philippines: true cost of ownership, garahe, test drive points, financing basics and the documents to prepare first."),
"fuel-saving-tips-diesel-vs-gasoline":("fuel saving tips",["diesel vs gasoline Philippines","fuel price rollback","how to save gas","fuel efficient driving"],None,
 "Fuel saving tips for Filipino drivers: why pump prices change weekly, 7 habits that cut fuel use, and how to choose diesel vs gasoline for the way you drive."),
"lto-rules-2026-car-owners":("LTO rules 2026",["LTO 5 year registration","LTO fake plates","LTO 15 days settle fine","LTMS e-license"],None,
 "LTO rules 2026 for car owners: 5-year registration for brand-new cars, fake plate crackdown, 15 working days to settle fines, the e-license and pedestrian memo."),
"el-nino-typhoon-car-care-tips":("car care tips",["El Niño 2026 Philippines","typhoon car tips","flood driving tips","after flood car checklist"],"El Niño and Typhoon Car Care Tips (2026)",
 "Car care tips for El Niño heat and typhoon season: battery, coolant, tires and AC, flood driving rules, an after-flood checklist and a bagyo emergency kit list."),
"car-loan-myths-philippines":("car loan Philippines",["car loan requirements","self-employed car loan","OFW car loan","car loan approval"],"Car Loan Philippines: 6 Myths, Debunked",
 "Car loan Philippines myths debunked: do you need a big salary, can self-employed buyers and OFWs apply, is cash cheaper, and what banks really check first."),
"ofw-car-buying-guide":("OFW car loan",["car loan for OFW Philippines","SPA car loan","co-borrower car loan","buy a car while abroad"],"OFW Car Loan Guide: Apply From Abroad (2026)",
 "OFW car loan guide: how to apply from abroad, required documents, SPA vs co-borrower, release and LTO registration while you're away, and Christmas timing."),
"13th-month-pay-car-budget-plan":("13th month pay",["13th month pay computation","13th month pay deadline","car fund","Christmas car promo"],None,
 "13th month pay 2026: how it's computed, the December 24 deadline, a simple split plan, building a car fund, and what to ask about Christmas car promos in SJDM."),
"l300-negosyo-guide":("Mitsubishi L300",["L300 Dual AC","L300 cab and chassis","L300 for business","L300 price Philippines"],None,
 "Mitsubishi L300 negosyo guide: cab and chassis vs Dual AC, load planning, business financing for self-employed owners, maintenance and simple ROI thinking."),
"xpander-vs-destinator-family-car":("Xpander vs Destinator",["Destinator vs Xpander","best 7 seater Philippines","Destinator price Philippines","Xpander price"],None,
 "Xpander vs Destinator compared for Filipino families: seating, engine and power, fuel, starting prices, which fits city or probinsya, and test drive tips."),
# --- round 1-2
"how-much-car-can-i-afford-philippines":("how much car can I afford",["car loan salary requirement","how much car can I afford based on salary","Xpander monthly","car amortization"],"How Much Car Can I Afford Based on Salary? (30–35% Rule)",
 "How much car can I afford? Use the 30–35% salary rule with October 2026 Zero DP monthlies for Xpander, Destinator, Triton and Montero and the income each needs."),
"triton-for-business-and-farm":("Triton for business",["Triton GX price","Triton 2WD vs 4WD","pickup for farm","Triton monthly"],"Mitsubishi Triton for Business and Farm Use (2026)",
 "Mitsubishi Triton for business and farm use: 2WD vs 4WD, cargo bed tips, financing for business owners, and the October 2026 Triton GX AT promo and monthly."),
"montero-sport-variants-explained":("Montero Sport GLX vs GLS",["Montero Sport Black Series","Montero Sport 2026 price","Montero Sport monthly","Montero 4WD"],"Montero Sport GLX vs GLS vs Black Series (2026)",
 "Montero Sport GLX vs GLS vs Black Series 2WD and 4WD: what changes between variants, who each fits, and October 2026 promo prices and monthlies for each one."),
"xpander-variants-explained":("Xpander GLX vs GLS",["Xpander GLX vs GLS vs Cross","Xpander monthly","Xpander 2026 price Philippines","Xpander manual vs automatic"],"Xpander GLX vs GLS vs Cross (2026): Price and Monthly",
 "Xpander GLX vs GLS vs Cross for 2026: manual or automatic, trims, October 2026 promo prices, Zero DP and low DP monthlies, fuel freebies and who each one fits."),
"destinator-glx-vs-gls-vs-gt":("Destinator GLX vs GLS vs GT",["Destinator GLX vs GLS","Destinator price Philippines","Destinator monthly","Destinator GT two tone"],"Destinator GLX vs GLS vs GT: Price and Monthly",
 "Destinator GLX vs GLS vs GT compared: same 1.5L turbo and CVT, different trims. October 2026 promo prices, Zero DP and low DP monthlies, and how to choose one."),
"pms-schedule-guide":("PMS schedule Mitsubishi",["PMS schedule for Xpander","preventive maintenance service","free labor 5000 km","car warranty Philippines"],"PMS Schedule Mitsubishi Guide for New Car Owners",
 "PMS schedule Mitsubishi guide: what preventive maintenance is, km or months rule, what gets checked, free labor up to 5,000 km, and warranty-saving habits."),
"first-1000-km-break-in-tips":("car break in period",["break in period km","new car tips","first 1000 km","new car checklist"],"Car Break-In Period: First 1,000 km Tips",
 "Car break-in period tips for your first 1,000 km: the do's and don'ts, highway driving, what to check in week one, and habits that keep a new car reliable."),
"car-insurance-explained-philippines":("car insurance Philippines",["CTPL vs comprehensive","acts of nature insurance","participation fee","car insurance claim"],"Car Insurance Philippines: CTPL vs Comprehensive",
 "Car insurance Philippines explained: CTPL vs comprehensive, acts of nature, participation fees, what the all-in package covers, and how to file a claim."),
"child-car-seat-law-philippines":("child car seat law Philippines",["RA 11229","car seat age Philippines","150 cm rule","child front seat law"],"Child Car Seat Law Philippines (RA 11229): Parent Guide",
 "Child car seat law Philippines (RA 11229) in plain English: who needs a car seat, the 150 cm rule, why kids 12 and below ride in back, and seat installation."),
"new-driver-tips-philippines":("new driver tips Philippines",["first time driver tips","driving tips for beginners","parking tips","what to keep in the car"],"New Driver Tips Philippines: Your First Months Driving",
 "New driver tips Philippines: a 3-month plan from quiet roads to NLEX, safe habits, parking without panic, what to keep in the car, and choosing your first car."),
"sjdm-to-manila-commute-tips":("SJDM to Manila",["San Jose del Monte to Manila","Quirino Highway traffic","MMDA number coding","Bulacan commute"],"SJDM to Manila Commute: Daily Driving Tips",
 "SJDM to Manila daily drive: Quirino Highway and NLEX routes, timing, MMDA number coding, RFID, and fuel and comfort tips for the San Jose del Monte commute."),
"car-trade-in-tips":("trade in car Philippines",["trade in car with loan balance","car trade in value","trade in financed car","sell car Philippines"],"Trade In Car Philippines: Tips for a Fair Value",
 "Trade in car Philippines tips: how trade-in works, documents (even with a loan balance), preparing the car, knowing its value, and trade-in vs selling yourself."),
"car-resale-value-tips":("car resale value Philippines",["best resale value car","how to keep car value","car depreciation","sell car tips"],"Car Resale Value Philippines: 8 Habits That Protect It",
 "Car resale value Philippines tips: 8 habits that protect your car's worth, choices at purchase that help, what hurts value most, and how to prepare to sell."),
"new-car-release-day-checklist":("new car release checklist",["new car inspection checklist","checklist for new car","car release day","new car documents"],"New Car Release Checklist: What to Check on Release Day",
 "New car release checklist: what to bring, how to inspect the unit outside and inside, which documents and freebies to check, and what to ask before you drive."),
"christmas-holiday-driving-tips":("Christmas driving safety tips",["holiday driving tips","Simbang Gabi traffic","drunk driving law Philippines","Christmas road trip"],"Christmas Driving Safety Tips for Families",
 "Christmas driving safety tips for Filipino families: Simbang Gabi, mall parking, party nights and RA 10586, and probinsya trips for Pasko and Bagong Taon."),
"l300-vs-triton-for-negosyo":("L300 vs Triton",["truck or pickup for business","L300 Dual AC price","Triton GX price","vehicle for negosyo"],None,
 "L300 vs Triton for your negosyo: truck or pickup, engines and use cases, and October 2026 promo prices and monthlies for the L300 Dual AC and Triton GX AT."),
# --- round 3
"rainy-season-driving-tips":("rainy season driving tips",["tips for driving in the rain","driving in the rain at night","hydroplaning","wiper blades"],None,
 "Rainy season driving tips for Filipino drivers: see and be seen, slow down, keep your distance, what to do if you hydroplane, and a pre-rain car checklist."),
"tire-care-tips-philippines":("tire care tips",["tire pressure","tire pressure for Mirage G4","when to replace tires","tire rotation"],"Tire Care Tips: Tire Pressure, Tread and Rotation",
 "Tire care tips for Filipino drivers: how to check tire pressure and tread, signs of damage, when to rotate and align, and when it's time to replace your tires."),
"car-aircon-not-cooling-tips":("car aircon not cooling",["car aircon cleaning","car aircon smell","cabin filter","car AC tips"],"Car Aircon Not Cooling? Care Tips to Keep It Cold",
 "Car aircon not cooling or smelly? The common causes, simple daily habits that keep it cold, cabin filter and cleaning tips, and warning signs to have checked."),
"dashcam-philippines-parking-guide":("dashcam Philippines",["best dashcam Philippines","dashcam installation","parking tips","parking mode dashcam"],"Dashcam Philippines Guide: Install, Use and Park Smart",
 "Dashcam Philippines guide: why it helps, how to choose and install one, smart parking habits for malls and streets, and what to do after a parking-lot scrape."),
"car-emergency-kit-list":("car emergency kit list",["car emergency kit checklist","early warning device","car first aid kit","typhoon emergency kit"],"Car Emergency Kit List and Checklist (Philippines)",
 "Car emergency kit list for Filipino families: breakdown tools, power and phone numbers, first aid, typhoon and long-trip add-ons, documents and how to keep it."),
"car-wash-at-home-guide":("car wash at home",["how to wash a car","car detailing","two bucket method","car interior cleaning"],"Car Wash at Home: Step-by-Step Detailing Guide",
 "Car wash at home, the right way: what you need, a step-by-step two-bucket wash, interior cleaning, protecting paint from sun and rain, and when to go pro."),
"road-trip-from-bulacan":("road trip from Bulacan",["Bulacan to Baguio","Bulacan to Zambales","Bulacan to Batangas","weekend road trip"],"Road Trip from Bulacan: Baguio, Zambales, Batangas",
 "Road trip from Bulacan or SJDM: typical routes to Baguio, Zambales and Batangas, mountain and beach driving tips, RFID, and prep for kids and seniors."),
"bank-vs-in-house-car-financing-philippines":("bank vs in-house financing",["in house vs bank financing car Philippines","bank auto loan","car loan comparison","all-in car promo"],"Bank vs In-House Financing for Cars in the Philippines",
 "Bank vs in-house financing for cars in the Philippines: how each works, 5 things to compare, what an all-in promo includes, and red flags before you sign."),
"montero-sport-vs-destinator":("Montero Sport vs Destinator",["Destinator vs Montero","diesel vs gas SUV","7 seater SUV Philippines","Montero Sport price"],"Montero Sport vs Destinator: Which Family SUV?",
 "Montero Sport vs Destinator for families: diesel ladder-frame vs turbo-gas SUV, power and torque, 4WD, and October 2026 promo prices and monthlies compared."),
"xpander-cross-2026-price-philippines":("Xpander Cross 2026 price Philippines",["Xpander Cross price","Xpander Cross monthly","Xpander Cross vs Xpander","Xpander Cross provincial roads"],"Xpander Cross 2026 Price Philippines and Probinsya Guide",
 "Xpander Cross 2026 price Philippines: ₱1,378,000 SRP, October promo monthlies, what it shares with the Xpander, what it adds, and tips for provincial roads."),
"triton-gx-2wd-at-first-pickup-guide":("Triton GX 2.4D 2WD A/T",["Triton GX price","Triton GX 2026","first pickup tips","Triton monthly"],"Triton GX 2.4D 2WD A/T: First-Time Pickup Guide",
 "Triton GX 2.4D 2WD A/T guide for first-time pickup owners: what's different, driving and parking tips, cargo bed basics, and the October 2026 promo monthly."),
"minimum-salary-for-car-loan-philippines":("minimum salary for car loan",["car loan for fresh graduate","car budget young professional","car loan requirements","how much car can I afford"],"Minimum Salary for Car Loan: Young Professional Budget Plan",
 "Minimum salary for car loan in the Philippines: a 5-step budget plan for young professionals, the 30–35% guide with Xpander monthlies, and how to qualify."),
"best-car-for-senior-citizens-philippines":("best car for senior citizens",["car for PWD Philippines","easy entry car","wheelchair space car","automatic car for seniors"],"Best Car for Senior Citizens and PWD Family Members (PH)",
 "Best car for senior citizens in the Philippines and PWD family members: seat height, door opening, step-in, wheelchair space, and a test-drive checklist to use."),
}
LEAD={
"undas-road-trip-checklist-2026":"Here's my Undas road trip checklist for 2026.",
"first-time-car-buyer-checklist":"This first time car buyer checklist covers the essentials.",
"fuel-saving-tips-diesel-vs-gasoline":"These fuel saving tips work whatever you drive.",
"lto-rules-2026-car-owners":"The LTO rules 2026 car owners need to know, in brief.",
"el-nino-typhoon-car-care-tips":"Car care tips for both heat and storms.",
"car-loan-myths-philippines":"Getting a car loan in the Philippines is easier to plan once the myths are cleared.",
"ofw-car-buying-guide":"An OFW car loan is possible from abroad.",
"xpander-vs-destinator-family-car":"Xpander vs Destinator, in short.",
"how-much-car-can-i-afford-philippines":"How much car can I afford? Here's the simple rule.",
"triton-for-business-and-farm":"The Triton for business and farm use, in short.",
"montero-sport-variants-explained":"Montero Sport GLX vs GLS vs Black Series, in short.",
"xpander-variants-explained":"Xpander GLX vs GLS vs Cross, in short.",
"destinator-glx-vs-gls-vs-gt":"Destinator GLX vs GLS vs GT, in short.",
"pms-schedule-guide":"Your PMS schedule (Mitsubishi or any brand-new car) is simple to follow.",
"first-1000-km-break-in-tips":"The car break in period is your first 1,000 km.",
"car-insurance-explained-philippines":"Car insurance in the Philippines comes in two main types.",
"child-car-seat-law-philippines":"The child car seat law in the Philippines is RA 11229.",
"new-driver-tips-philippines":"My new driver tips for the Philippines, in short.",
"sjdm-to-manila-commute-tips":"Driving SJDM to Manila every day? In short:",
"car-trade-in-tips":"To trade in a car in the Philippines and get a fair value:",
"car-resale-value-tips":"Car resale value in the Philippines comes down to habits.",
"new-car-release-day-checklist":"My new car release checklist, in short.",
"christmas-holiday-driving-tips":"Christmas driving safety tips, in short.",
"l300-vs-triton-for-negosyo":"L300 vs Triton for business, in short.",
"rainy-season-driving-tips":"Rainy season driving tips, in short.",
"tire-care-tips-philippines":"Tire care tips, in short.",
"car-aircon-not-cooling-tips":"Car aircon not cooling as it used to?",
"dashcam-philippines-parking-guide":"Thinking of a dashcam? In the Philippines, many drivers now see it as basic protection.",
"car-emergency-kit-list":"Here's the car emergency kit list I recommend.",
"car-wash-at-home-guide":"For a proper car wash at home:",
"road-trip-from-bulacan":"Planning a road trip from Bulacan?",
"bank-vs-in-house-car-financing-philippines":"Bank vs in-house financing, in short.",
"montero-sport-vs-destinator":"Montero Sport vs Destinator, in short.",
"xpander-cross-2026-price-philippines":"The Xpander Cross 2026 price in the Philippines is ₱1,378,000 SRP.",
"minimum-salary-for-car-loan-philippines":"There's no single minimum salary for car loan approval; banks decide, but you can plan.",
"best-car-for-senior-citizens-philippines":"The best car for senior citizens is the one they can get in and out of easily.",
}
def apply(posts):
    for a in posts:
        s=SEO.get(a["slug"])
        if not s: continue
        a["kw"]=(s[0],s[1])
        if s[2]: a["title"]=s[2]
        a["desc"]=s[3]
        if a["slug"] in LEAD: a["answer"]=LEAD[a["slug"]]+" "+a["answer"]
    by={x["slug"]:x for x in posts}
    for a in posts:
        have=set(re.findall(r'href="/(?:blog|tips|guides)/([^/"]+)/"',a["body"]))
        pool=[x for x in posts if x is not a and x["slug"] not in have]
        pool.sort(key=lambda x:(x["car"]!=a["car"],x["base"]!=a["base"]))
        rel=pool[:3]
        blk='<h2>Related reading</h2><ul class="links">'+"".join(f'<li><a href="/{x["base"]}/{x["slug"]}/">{x["title"]}</a></li>' for x in rel)+'</ul>\n'
        i=a["body"].rfind("<h2>Your next step</h2>")
        a["body"]=a["body"][:i]+blk+a["body"][i:] if i>=0 else a["body"]+blk
    return posts
