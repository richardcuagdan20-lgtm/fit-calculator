# Draft blog posts (viral Oct 28 series). NOT published until the slug is added to PUBLISH.
# Facts checked against /workspace/content/viral_oct28/research.md and _src/data.py.
BY="Mitsubishi Sales Executive"
def CTA(lead,unit=""):
    q=f"?unit={unit}" if unit else ""
    return f'''<h2>Your next step</h2>
<p>{lead}</p>
<p class="row"><a class="btn" href="/budgetcalculator/">Check what fits my budget</a> <a class="btn ghost dk" href="/test-drive/{q}">Book a Test Drive</a></p>
<p class="muted">Questions muna? Message me anytime, walang pressure. Financing is subject to bank approval.</p>'''

def SRC(*links): return '<h2>Sources</h2><ul class="links">'+"".join(f'<li><a href="{u}" target="_blank" rel="noopener">{t}</a></li>' for t,u in links)+'</ul>'
# Publish switch: slugs listed here go live (section index, sitemap, JSON-LD) on the next build.


DRAFT_POSTS=[
dict(base="tips",car="xpander",slug="undas-road-trip-checklist-2026",date="2026-10-21",by=BY,img="xpglx_x37",alt="Mitsubishi Xpander 7-seater MPV ready for a family road trip",
title="Undas 2026 Road Trip Checklist for Families",
answer="Before your Undas 2026 drive, do a BLOWBAGETS check, load your RFID, and leave off-peak, since NLEX expects heavy traffic from October 28 to November 2. Pack water, medicines, a powerbank and your early warning device, and know what to do if you break down on the expressway.",
faq=[("When is the Undas 2026 traffic expected on NLEX?","Toll operators expect heavy traffic from October 28 to November 2, 2026. November 1 and 2 are special non-working days, so many families travel on the days before."),
("What does BLOWBAGETS mean?","It is a pre-trip check: Battery, Lights, Oil, Water, Brakes, Air, Gas, Engine, Tires and Self. It takes about 10 to 15 minutes."),
("What should I do if my car breaks down on NLEX?","Turn on your hazards, move to the shoulder, set up your early warning device, get passengers to a safer spot away from traffic, and call the expressway operator's official hotline."),
("Do I need to load my RFID before Undas?","Yes. Toll operators remind motorists to keep RFID accounts loaded before the exodus, so check your balance a day before and load enough for the round trip.")],
desc="Uuwi sa probinsya this Undas? Pre-trip checklist: BLOWBAGETS, RFID and NLEX tips, packing for kids and seniors, and what to do if you break down.",
body='''<p>Every Undas, a big part of Metro Manila and Bulacan heads north and south at the same time. Toll operators expect heavy traffic on NLEX from <b>October 28 to November 2</b>, and November 1 and 2 are special non-working days this year, so many families are stretching it into a long weekend. Kung kasama ka sa uuwi sa probinsya, a little preparation the night before saves you hours of stress on the road.</p>
<p>Here is the checklist I share with clients before any long drive. Treat it like a mission briefing: boring, step-by-step, and very effective.</p>

<h2>Step 1: BLOWBAGETS, the 10-point pre-trip check</h2>
<p>BLOWBAGETS is the checklist many Filipino drivers learned in driving school. It takes ten to fifteen minutes in your garahe and catches most of the problems that strand cars on the expressway.</p>
<ul class="ticks">
<li><b>Battery</b>: terminals clean and tight, no white crust. If your battery is old or slow to crank, have it tested before the trip, not after.</li>
<li><b>Lights</b>: headlights, brake lights, signal lights and hazards. Ask someone to stand behind the car while you test.</li>
<li><b>Oil</b>: check the engine oil level on the dipstick with the engine off and on level ground.</li>
<li><b>Water</b>: coolant reservoir between the marks, plus windshield washer fluid. Never open a hot radiator cap.</li>
<li><b>Brakes</b>: the pedal should feel firm. Listen for squealing or grinding.</li>
<li><b>Air</b>: tire pressure at the level printed on the driver's door jamb, including the spare.</li>
<li><b>Gas</b>: fill up before you hit the expressway so you are not forced to queue at a crowded stopover.</li>
<li><b>Engine</b>: look for leaks under the car and listen for unusual sounds.</li>
<li><b>Tires</b>: check tread depth and look for bulges or cracks on the sidewall.</li>
<li><b>Self</b>: the most important one. Sleep well, at hindi kayo dapat aalis nang puyat.</li>
</ul>
<p>If anything looks off, have it checked at your service center before the long weekend. Mas mura ang preventive check kaysa towing.</p>

<h2>Step 2: RFID and toll prep</h2>
<p>Toll operators have reminded motorists to keep their RFID accounts loaded before the Undas exodus. A low balance can mean being turned back at the toll lane, which slows down everyone behind you.</p>
<ul class="ticks">
<li>Check your RFID balance a day before and load enough for the round trip.</li>
<li>Make sure the sticker is not damaged and is reading properly. If it often fails, have it checked before you leave.</li>
<li>Keep a little cash or a backup payment option in the car for emergencies, but do not rely on it for the toll lanes.</li>
</ul>

<h2>Step 3: Leave off-peak, and plan around Candaba</h2>
<p>NLEX has advised motorists about lane restrictions on the Candaba Viaduct, one of the usual choke points for anyone going to Pampanga and further north. The simplest way to avoid the worst of it is timing.</p>
<ul class="ticks">
<li>Avoid leaving at the same time as everyone else, usually right after work on the first day of the break.</li>
<li>Very early morning departures are often lighter, but only if the driver had enough rest.</li>
<li>Check the toll operator's official advisories and traffic updates on the day itself, since conditions change.</li>
<li>Plan your stopovers in advance so you are not hunting for parking at a full rest area.</li>
</ul>

<h2>Step 4: Packing list for families and seniors</h2>
<p>A long drive with kids, lolo and lola is easier when the essentials are within reach, not buried under the bags.</p>
<ul class="ticks">
<li>Water, snacks and a small trash bag</li>
<li>Powerbank and car charger for phones (your navigation and emergency line)</li>
<li>Payong and a light jacket, since weather can change on the way</li>
<li>Maintenance medicines for seniors, plus a basic first-aid kit</li>
<li>Wet wipes, tissue and alcohol</li>
<li>Pillows or a neck rest for long stretches</li>
<li>Your driver's license, OR/CR and insurance details</li>
<li>Early warning device (EWD) and basic tools</li>
</ul>
<p>For seniors, plan more frequent stops to stretch and use the restroom. Seat them where getting in and out is easiest.</p>

<h2>What to do if tumirik ka sa expressway</h2>
<ol class="steps">
<li><h3>Get off the travel lane safely</h3><p>Turn on your hazard lights and steer to the shoulder as far from moving traffic as possible.</p></li>
<li><h3>Set up your early warning device</h3><p>Place the EWD well behind the car so approaching drivers have time to react.</p></li>
<li><h3>Get passengers to a safer spot</h3><p>On an expressway, staying inside a stopped car near fast traffic can be risky. If it is safe, move everyone behind the guardrail, away from the lanes.</p></li>
<li><h3>Call for help</h3><p>Save the expressway operator's official hotline in your phone before you leave (it is posted on their website and on signs along the road), plus your insurance's roadside assistance number if you have one.</p></li>
<li><h3>Do not attempt risky repairs</h3><p>Changing a tire on the traffic side of the car is dangerous. Wait for the patrol or tow if the position is unsafe.</p></li>
</ol>

<h2>Why a 7-seater makes probinsya trips easier</h2>
<p>Undas trips are rarely just the driver and one passenger. It is usually the whole family, plus bags, food for the visit and pasalubong. That is where a 7-seater earns its keep.</p>
<p>The <a href="/cars/xpander/">Mitsubishi Xpander</a> seats seven with a 1.5L gasoline engine, and its high ground clearance helps on provincial roads and during rainy-season floods. Families wanting more power for full loads on the expressway often look at the <a href="/cars/destinator/">Destinator</a>, a 7-seat SUV with a 1.5L turbo engine making 163 PS and 250 Nm. If you are comparing, my <a href="/blog/best-7-seater-for-filipino-families-2026/">7-seater guide for Filipino families</a> goes through the options.</p>
<p>Whatever you drive this Undas, ingat sa byahe. The goal is simple: ligtas na makauwi, at ligtas na makabalik.</p>
'''+SRC(("ABS-CBN News: Toll operators preparing for Undas exodus (Oct 21, 2026)","https://www.abs-cbn.com/news/business/2026/10/21/toll-operators-preparing-for-undas-exodus-1534"),("Motoring Today: NLEX Undas advisory","https://www.motoringtoday.ph/page.php?id=6119"),("GMA News: DOLE pay rules for Undas and Bonifacio Day 2026","https://www.gmanetwork.com/news/money/economy/1005753/dole-releases-pay-rules-for-undas-bonifacio-day-2026/story/"))+CTA("Planning to upgrade to a 7-seater before your next family trip? Check which unit fits your budget, then come and test drive it in San Jose del Monte.","xpander")),

dict(base="tips",car="mirage-g4",slug="first-time-car-buyer-checklist",date="2026-10-21",by=BY,img="mg4gls_u17",alt="Mitsubishi Mirage G4 GLS sedan, a common first car in the Philippines",
title="First-Time Car Buyer Checklist (Philippines)",
desc="Buying your first car in the Philippines? Check these first: true cost of ownership, loan documents, test drive points, and bank vs in-house financing.",
answer="Don't buy your first car until you know your full monthly cost of ownership (not just the amortization), have parking, have test driven the unit, understand bank vs in-house financing, and have your documents ready. If you can tick all of these, you're ready.",
faq=[("What documents do I need for a car loan in the Philippines?","Usually two valid IDs and proof of billing, plus income documents: certificate of employment and payslips or ITR if employed, business registration and bank statements if self-employed, and contract and remittance proof if you're an OFW. Each bank has its own list."),
("Is the monthly amortization the only cost of owning a car?","No. Budget for fuel, insurance renewal, preventive maintenance (PMS), parking, tolls and registration renewal on top of the monthly."),
("Bank financing or in-house financing?","Bank financing is the common route for new cars and is subject to bank approval. In-house or dealer-arranged options can differ in requirements and terms, so compare the total cost, not just the monthly."),
("Is the Mirage G4 good for a first car?","It's a common choice: a compact 1.2L gasoline sedan that's easy to park and among the most affordable units in the Mitsubishi lineup.")],
body='''<p>Your first car is a big milestone, at ang excitement minsan nauuna sa plano. Before you sign anything, go through this list. It takes one evening and can save you years of financial stress.</p>
<h2>1. Know the true cost of ownership</h2>
<p>The monthly amortization is only part of it. Add these to your budget:</p>
<ul class="ticks"><li><b>Fuel</b>: estimate your weekly kilometers, then multiply by current pump prices.</li><li><b>Insurance</b>: comprehensive insurance renews every year after the first.</li><li><b>PMS</b>: preventive maintenance at the intervals in your owner's manual.</li><li><b>Parking</b>: at home, at work, and wherever you go often.</li><li><b>Tolls</b>: if you use NLEX or the skyways regularly.</li><li><b>Registration</b>: brand-new dealer-registered cars now get a longer first registration, but renewals still come later. See my <a href="/tips/lto-rules-2026-car-owners/">LTO rules 2026 checklist</a>.</li></ul>
<p>If the monthly plus these costs still leaves room for savings and emergencies, that's a healthy plan.</p>
<h2>2. Make sure you have a garahe</h2>
<p>Check where the car will sleep at night. Many LGUs and subdivisions enforce rules against street parking, so settle this before release day.</p>
<h2>3. Test drive before you decide</h2>
<ul class="ticks"><li>Seat position and visibility: can you see the corners of the car?</li><li>Ease of parking and turning in tight streets</li><li>Transmission feel (manual vs automatic or CVT)</li><li>Rear seat space if you'll carry family or officemates</li><li>Cabin noise and AC performance on a hot day</li></ul>
<h2>4. Understand your financing</h2>
<p>Most new-car buyers use bank financing, which is always subject to bank approval. Ask about the term, what the package includes, and the total amount you'll pay over the life of the loan. My <a href="/guides/how-car-financing-works-philippines/">car financing guide</a> explains the basics, and <a href="/guides/zero-dp-vs-low-dp/">Zero DP vs low DP</a> covers the trade-off between paying upfront and a lower monthly.</p>
<h2>5. Read the inclusions</h2>
<p>Promo packages are often "all-in": registration, insurance, chattel mortgage and freebies. Ask for the list in writing. Here's <a href="/guides/what-all-in-includes/">what all-in usually covers</a>.</p>
<h2>6. Complete your documents</h2>
<p>Requirements depend on whether you're employed, self-employed or an OFW. Here is the <a href="/guides/car-loan-requirements/">full car loan requirements list</a>. Having everything ready speeds up approval.</p>
<h2>Why the Mirage G4 is a common first car</h2>
<p>The <a href="/cars/mirage-g4/">Mitsubishi Mirage G4</a> is a compact sedan with a 1.2L gasoline engine (78 PS, 100 Nm), offered in manual and CVT. It's easy to park around SJDM and Metro Manila and is the most affordable entry into the Mitsubishi lineup, with an official SRP starting at ₱793,000 (MMPC price list as of August 2026).</p>
'''+CTA("Ticked everything? Check which unit fits your income, then book a test drive at our SJDM showroom.","mirage-g4")),

dict(base="tips",car="l300",slug="fuel-saving-tips-diesel-vs-gasoline",date="2026-10-21",by=BY,img="l300_fb",alt="Mitsubishi L300 diesel commercial truck",
title="Fuel-Saving Tips: Diesel vs Gasoline (2026)",
desc="Diesel up, gasoline down? Why PH fuel prices change weekly, 7 driving habits that cut fuel use, and how to choose diesel or gasoline for how you drive.",
answer="Fuel prices in the Philippines are adjusted almost every week, so habits matter more than timing. Keep tires at the right pressure, accelerate and brake smoothly, cut extra weight, keep up with PMS, and avoid rush hour. Choose diesel for heavy loads and high mileage, gasoline for light city driving.",
faq=[("Why do fuel prices change every week in the Philippines?","Oil companies adjust pump prices weekly, generally following movements in world oil prices and supply. On October 20, 2026, gasoline was rolled back while diesel went up."),
("Is diesel or gasoline better?","It depends on use. Diesel engines suit heavy loads, hauling and high mileage, like an L300. Gasoline suits lighter, shorter city driving, like a Mirage G4."),
("Does tire pressure affect fuel consumption?","Yes. Under-inflated tires increase rolling resistance, so the engine works harder. Follow the pressure printed on your driver's door jamb."),
("Does using the aircon use more fuel?","AC adds load to the engine, so it uses some fuel. Keep it serviced and park in the shade so it doesn't have to work as hard.")],
body='''<p>On October 20, 2026, oil companies rolled back gasoline prices by at least ₱4.30 per liter, while diesel went up by ₱2.60 per liter. Prices remain above the levels seen before the Middle East conflict that began on February 28. In short: diesel ↑, gas ↓, and next week could be different again. The one thing you control is how much fuel you use.</p>
<h2>Why prices move every week</h2>
<p>Pump prices in the Philippines are adjusted weekly and generally follow world oil prices and supply conditions. That's why diesel and gasoline can move in opposite directions in the same week. Check the Department of Energy's weekly price adjustments before you plan big trips.</p>
<h2>7 habits that cut fuel use</h2>
<ol class="steps">
<li><h3>Check tire pressure</h3><p>Under-inflated tires waste fuel. Use the pressure on the door jamb, checked when tires are cold.</p></li>
<li><h3>Smooth acceleration and braking</h3><p>Iwas biglang arangkada at preno. Anticipate traffic and coast to stops.</p></li>
<li><h3>Remove extra weight</h3><p>Unload what you don't need. A trunk full of unused stuff is extra weight every trip.</p></li>
<li><h3>Keep up with PMS</h3><p>A clean air filter, fresh oil and a properly tuned engine help efficiency.</p></li>
<li><h3>Plan your route</h3><p>Combine errands and avoid rush hour. Idling in traffic burns fuel without moving you.</p></li>
<li><h3>Don't idle unnecessarily</h3><p>If you're parked and waiting a long time, turn off the engine when it's safe and allowed.</p></li>
<li><h3>Keep a steady speed on the expressway</h3><p>Steady cruising is more efficient than constant speeding up and slowing down.</p></li>
</ol>
<h2>Diesel vs gasoline: who should choose which</h2>
<ul class="ticks"><li><b>Choose diesel</b> if you carry heavy loads, haul cargo for a business or rack up high mileage. Diesel engines deliver strong pulling power for work.</li><li><b>Choose gasoline</b> if most of your driving is light, short city trips and you want a quieter, simpler daily car.</li></ul>
<h2>L300 vs Mirage G4: two different jobs</h2>
<p>The <a href="/cars/l300/">L300</a> runs a 2.2L turbo-intercooled diesel (4N14) with a 5-speed manual, built for deliveries and hauling. The <a href="/cars/mirage-g4/">Mirage G4</a> uses a 1.2L gasoline engine and is a light, compact sedan for daily commuting. The right choice is the one that matches your work and route.</p>
'''+SRC(("Rappler: Fuel price adjustments, October 20, 2026","https://www.rappler.com/business/fuel-prices-adjustments-october-20-2026/"),("ABS-CBN News: Gasoline prices fall, diesel prices climb on Oct 20","https://www.abs-cbn.com/news/business/2026/10/19/gasoline-prices-fall-diesel-prices-climb-on-oct-20-0952"),("Department of Energy: Retail pump price adjustments","https://doe.gov.ph/data-and-prices/liquid-fuels/retail-pump-prices/price-adjustments"))+CTA("Choosing between diesel and gasoline for your next vehicle? Check your budget, then test drive both types at our SJDM showroom.","l300")),

dict(base="tips",car="destinator",slug="lto-rules-2026-car-owners",date="2026-10-21",by=BY,img="de_x3n",alt="Mitsubishi Destinator 7-seater SUV",
title="LTO Rules 2026: Checklist for Car Owners",
desc="LTO rules in 2026: 5-year registration for brand-new cars, fake plate crackdown, 15 working days to settle fines, e-license, and the pedestrian memo.",
answer="In 2026, brand-new dealer-registered vehicles get a 5-year initial registration (from February 15), fake or improvised plates can get your car impounded (since September 1), apprehended drivers have 15 working days to settle fines instead of on-the-spot license confiscation, and the e-license in LTMS/eGovPH is valid.",
faq=[("Is LTO registration now 5 years for new cars?","Yes. Since February 15, 2026, brand-new cars and motorcycles registered through dealers get a five-year initial registration instead of three. After that, renewal is yearly, with a roadworthiness check required around the fourth year. Used vehicles don't qualify."),
("Can my car be impounded for improvised plates?","Yes. The LTO crackdown on fake or improvised plates, in effect since September 1, 2026, can lead to impoundment. Use the plates and documents issued for your vehicle."),
("Will the LTO confiscate my license on the spot?","Under the new enforcement rules, there's no on-the-spot license confiscation; apprehended drivers are given 15 working days to settle their fines."),
("Is the digital driver's license valid?","Yes. The e-license accessed through LTMS or the eGovPH app is recognized as valid."),
("Can the LTO revoke a license for endangering pedestrians?","An October 9, 2026 LTO memorandum says drivers who endanger pedestrians may lose their licenses.")],
body='''<p>Ang daming bagong LTO rules ngayong 2026. Here's a quick checklist so you're updated, whether you just got a brand-new car or you've been driving for years. Rules can still be updated, so always check the LTO's official announcements.</p>
<h2>1. 5-year initial registration for brand-new cars</h2>
<p>Starting <b>February 15, 2026</b>, brand-new cars and motorcycles registered through dealers get a <b>five-year</b> initial registration, up from three years. What's still required:</p>
<ul class="ticks"><li>Compulsory third-party liability (CTPL) insurance must stay valid.</li><li>A roadworthiness check is required around the fourth year.</li><li>After the five years, registration is renewed yearly.</li><li>Used vehicles don't qualify. Check the expiry printed on your Certificate of Registration (CR).</li></ul>
<h2>2. Fake and improvised plates: impound risk</h2>
<p>Since <b>September 1, 2026</b>, the LTO has been cracking down on fake and improvised plates, and violators risk having their vehicles impounded. If your plates aren't out yet, ask your dealer about the status and keep your official registration documents in the car. Don't make your own "commemorative" or printed plates.</p>
<h2>3. 15 working days to settle fines</h2>
<p>Under the LTO's new enforcement rules, there's no more on-the-spot confiscation of licenses. Apprehended drivers are given <b>15 working days</b> to settle their fines. Settle on time to avoid further penalties.</p>
<h2>4. Your e-license is valid</h2>
<p>The electronic driver's license you can access through the <b>LTMS</b> portal or the <b>eGovPH</b> app is recognized as valid. Make sure your account is set up and you can open it quickly when asked.</p>
<h2>5. Pedestrian safety: license revocation</h2>
<p>An <b>October 9, 2026</b> LTO memorandum states that drivers who endanger pedestrians may have their licenses revoked. Slow down near crossings and schools, and always yield at pedestrian lanes.</p>
<h2>Quick owner checklist</h2>
<ul class="ticks"><li>Check the registration expiry on your CR</li><li>Keep CTPL valid</li><li>Use only official plates</li><li>Set up your LTMS / eGovPH account</li><li>Settle any violation within 15 working days</li><li>Yield to pedestrians, always</li></ul>
<p>Buying a brand-new car? Ask your sales executive what registration and insurance your package includes. For example, the <a href="/cars/destinator/">Destinator</a> and other units come in all-in packages. Here's <a href="/guides/what-all-in-includes/">what all-in usually covers</a>.</p>
'''+SRC(("Inquirer: New vehicles' registration valid for 5 years","https://newsinfo.inquirer.net/2177851/new-vehicles-registration-valid-for-5-years"),("Philippine Information Agency: 5-year LTO vehicle registration","https://pia.gov.ph/news/new-5-year-lto-vehicle-registration-curbs-fixers-reduces-long-lines/"),("AutoCar PH: LTO issues new rules on traffic violation enforcement","https://autocar.com.ph/lto-issues-new-rules-on-traffic-violation-enforcement/"),("Philippine News Agency (LTO)","https://www.pna.gov.ph/index.php/articles/1266791"),("Philippine News Agency (LTO plates)","https://www.pna.gov.ph/index.php/articles/1282173"),("Interaksyon: Endangering pedestrians, drivers lose licenses (Oct 9, 2026)","https://interaksyon.philstar.com/politics-issues/2026/10/09/320118/endangering-pedestrians-drivers-lose-licenses-lto-new-memorandum/"))+CTA("Planning a brand-new car this year? Check your budget, then test drive at our SJDM showroom.","destinator")),

dict(base="tips",car="destinator",slug="el-nino-typhoon-car-care-tips",date="2026-10-21",by=BY,img="de_jh3",alt="Mitsubishi Destinator SUV with 214 mm ground clearance",
title="El Niño and Typhoon Car Care Tips (2026)",
desc="PAGASA says El Niño is very strong, but 1 to 2 typhoons a month are still possible. Car care for heat and floods, plus an after-flood checklist.",
answer="PAGASA expects a very strong El Niño through late 2026, so protect your battery, coolant, tires and AC from the heat. But 1 to 2 tropical cyclones are still expected each month from October to December, so stay flood-ready: don't drive through deep water, and don't restart an engine that was submerged.",
faq=[("Is there El Niño or La Niña in late 2026?","El Niño. PAGASA says a strong to very strong El Niño is present and is expected to last until the first half of 2027."),
("Can there still be typhoons during El Niño?","Yes. PAGASA expects 1 to 2 tropical cyclones each in October, November and December 2026, and says these may be strong."),
("How deep is too deep to drive through flood?","As a rule of thumb, don't push through water that reaches about half the height of your tires, and never cross moving water. If you're unsure of the depth, don't go."),
("What should I do if my car was submerged?","Don't try to start it. Have it towed to a service center for inspection, and contact your insurer.")],
body='''<p>Mainit ngayon, pero may bagyo pa rin? Yes. PAGASA says a strong to very strong El Niño is ongoing and may peak before the end of 2026, bringing below-normal rainfall and hotter-than-usual temperatures to many areas. But PAGASA also expects <b>1 to 2 tropical cyclones each month from October to December</b>, and they could reach typhoon strength. Your car needs to be ready for both.</p>
<h2>Heat care: what the init does to your car</h2>
<ul class="ticks">
<li><b>Battery</b>: heat speeds up battery wear. Have it tested at PMS, and replace it if it's weak.</li>
<li><b>Coolant</b>: keep it at the right level, with the correct type. Watch your temperature gauge in traffic.</li>
<li><b>Tires</b>: tire pressure rises when tires are hot. Check pressure in the morning when they're cold.</li>
<li><b>AC</b>: have it cleaned and checked. Park in the shade or use a sunshade to reduce heat build-up.</li>
<li><b>Paint and interior</b>: wash off dust and bird droppings promptly, and use a sunshade to protect the dashboard.</li>
</ul>
<h2>Flood rules when the bagyo comes</h2>
<ol class="steps">
<li><h3>Don't guess the depth</h3><p>If the water looks like it's around half your tire height or more, turn back.</p></li>
<li><h3>Never cross moving water</h3><p>Even shallow, fast-moving water can push a car.</p></li>
<li><h3>Go slow and steady</h3><p>If you must pass through shallow water, use low gear and avoid creating a wave.</p></li>
<li><h3>Don't restart a stalled car in water</h3><p>Restarting can let water into the engine and cause serious damage.</p></li>
<li><h3>Test your brakes after</h3><p>Lightly press the brakes a few times after leaving water to dry them.</p></li>
</ol>
<p>Higher ground clearance helps on flooded streets. The <a href="/cars/destinator/">Destinator</a> has 214 mm of ground clearance, but no car is a boat. Safety first pa rin.</p>
<h2>After-flood checklist</h2>
<ul class="ticks"><li>If water reached the floor or engine bay, don't start the car. Have it towed.</li><li>Take photos for your insurance claim.</li><li>Have the service center check the engine, transmission fluid, brakes and electricals.</li><li>Dry the interior to prevent mold and odor.</li></ul>
<h2>Bagyo-season emergency kit</h2>
<ul class="ticks"><li>Flashlight and extra batteries</li><li>Powerbank and charger</li><li>Drinking water and snacks</li><li>Raincoat and payong</li><li>First-aid kit</li><li>Early warning device and tow strap</li></ul>
<h2>Insurance: acts of nature</h2>
<p>Comprehensive insurance doesn't always cover flood or typhoon damage by default. Acts of nature (AON) coverage is often an add-on, so read your policy or ask your insurer exactly what is covered.</p>
'''+SRC(("PAGASA: Monthly agroclimatic review and outlook (El Niño advisory as of Oct 7, 2026)","https://www.pagasa.dost.gov.ph/agri-weather/monthly-agroclimatic-review-and-outlook"),("PAGASA: Seasonal climate outlook, July to December 2026","https://pubfiles.pagasa.dost.gov.ph/pagasaweb/files/climate/seasonalclimateoutlook/simplified_seasonal_jul-dec2026.pdf"),("Philippine News Agency: Few but strong tropical cyclones likely in last quarter of 2026","https://www.pna.gov.ph/articles/1284604"),("Cebu Daily News: 3 to 5 tropical cyclones expected Oct 2026 to Mar 2027","https://cebudailynews.inquirer.net/775047/3-to-5-tropical-cyclones-expected-from-october-2026-to-march-2027"))+CTA("Want a car with more clearance for the rainy days? Check your budget, then test drive the Destinator or Xpander in SJDM.","destinator")),

dict(base="blog",car="xpander",slug="car-loan-myths-philippines",date="2026-10-21",by=BY,img="xpgls_c31",alt="Mitsubishi Xpander GLS family MPV",
title="6 Car Loan Myths in the Philippines, Debunked",
desc="Kailangan ba malaki ang sahod? Bawal ba ang self-employed o OFW? 6 common car loan myths in the Philippines, what banks check, and how to prepare.",
answer="Most car loan myths in the Philippines are half-truths. Banks don't only look at salary size; they check your capacity to pay, your documents and your credit history. Self-employed buyers and OFWs can apply with the right documents, and cash isn't automatically cheaper once you compare promos and what your money could do elsewhere.",
faq=[("Can a self-employed person get a car loan in the Philippines?","Yes. Banks typically ask for business registration (DTI, SEC or mayor's permit), ITR or financial statements, and bank statements. Requirements vary by bank."),
("Can an OFW get a car loan while abroad?","Yes. Banks commonly ask for the employment or crew contract, payslips and proof of remittance, and may require a special power of attorney (SPA) or a co-borrower in the Philippines."),
("What do banks check for car loan approval?","Your capacity to pay (income versus obligations), complete and verifiable documents, and your credit history. Approval is always subject to bank evaluation."),
("Is it better to pay cash for a car?","Not always. Compare the cash price with financing promos and inclusions, and consider whether keeping your savings as an emergency fund or business capital is worth more to you.")],
body='''<p>"Hindi ka maaaprubahan, maliit sahod mo." "Bawal ang self-employed." "OFW ka, mahirap 'yan." I hear these sabi-sabi every week on the showroom floor. Some are outdated, some are half-true, and some keep good buyers from even trying. Let's go through them.</p>
<h2>Myth 1: You need a big salary to get approved</h2>
<p><b>Fact:</b> Banks look at your <b>capacity to pay</b>, meaning how your income compares with the monthly and your other obligations, not just the size of your salary. A modest earner with few debts and complete documents can be a stronger applicant than a high earner with many loans. The unit and terms you choose matter too, which is why I always start with the <a href="/budgetcalculator/">budget calculator</a>.</p>
<h2>Myth 2: Self-employed buyers can't get a car loan</h2>
<p><b>Fact:</b> Business owners apply all the time. You just prove income differently. Banks commonly ask for:</p>
<ul class="ticks"><li>DTI or SEC registration, or a mayor's/business permit</li><li>Latest ITR and financial statements</li><li>Business bank statements for the past several months</li><li>For some banks, trade references from suppliers or clients</li></ul>
<h2>Myth 3: OFWs abroad can't apply</h2>
<p><b>Fact:</b> Many banks accept OFW applicants. Common requirements include your passport, employment or crew contract, recent payslips and proof of remittance. If you're abroad, a special power of attorney (SPA) or a co-borrower in the Philippines may be required. More in my <a href="/blog/ofw-car-buying-guide/">OFW car buying guide</a>.</p>
<h2>Myth 4: Cash is always cheaper</h2>
<p><b>Fact:</b> Paying cash means no interest, but it's not automatically the better deal. Promos and inclusions can differ between cash and financing, and draining your savings leaves you without an emergency fund or business capital. Compare the total cost and what your cash could do elsewhere before deciding.</p>
<h2>Myth 5: One rejection means you can never get a car loan</h2>
<p><b>Fact:</b> A declined application usually has a reason: incomplete documents, high existing debt or a unit beyond your capacity. Fix the cause, choose a unit that fits, or add a co-borrower, then apply again.</p>
<h2>Myth 6: The monthly is the only thing you need to think about</h2>
<p><b>Fact:</b> Banks check if you can afford the monthly; you should check if you can afford the car. Add fuel, insurance renewal, PMS, parking and tolls. My <a href="/tips/first-time-car-buyer-checklist/">first-time car buyer checklist</a> covers the full list.</p>
<h2>What banks actually check</h2>
<ol class="steps"><li><h3>Capacity</h3><p>Income versus the monthly and your existing obligations.</p></li><li><h3>Documents</h3><p>Complete, consistent and verifiable IDs, income proof and proof of billing.</p></li><li><h3>Credit history</h3><p>How you've handled past loans and credit cards.</p></li><li><h3>Stability</h3><p>Length of employment or years in business.</p></li></ol>
<h2>How to prepare before applying</h2>
<ul class="ticks"><li>Gather your documents early. Here's the <a href="/guides/car-loan-requirements/">car loan requirements list</a>.</li><li>Settle or reduce small debts if you can.</li><li>Pick a unit that fits your budget, not just your dream.</li><li>Be honest and consistent in your application.</li><li>Ask your sales executive to pre-check your documents before submission.</li></ul>
<p>Whether you're eyeing the <a href="/cars/xpander/">Xpander</a> for the family or the <a href="/cars/destinator/">Destinator</a>, the process is the same: prepare, apply, and let the bank evaluate. Approval is always subject to bank evaluation.</p>
'''+SRC(("BPI: Auto loan requirements","https://www.bpi.com.ph/personal/loans/auto-loan/requirements"),("BDO: Auto loan","https://www.bdo.com.ph/personal/loans/auto-loan"),("Metrobank: Car loan requirements","https://mcola.metrobank.com.ph/car-loan/requirements"))+CTA("Curious what you could qualify for? Run your numbers first, then book a test drive in SJDM.","xpander")),

dict(base="blog",car="xpander",slug="ofw-car-buying-guide",date="2026-10-21",by=BY,img="xpglx_u33",alt="Mitsubishi Xpander GLX for an OFW family",
title="OFW Car Buying Guide: Apply From Abroad (2026)",
desc="Can OFWs get a car loan while abroad? Documents, SPA and co-borrower, release and registration while you're away, and timing for a Christmas homecoming.",
answer="Yes, OFWs can apply for a car loan while abroad. Banks commonly ask for a passport, employment or crew contract, recent payslips and proof of remittance, and may require a special power of attorney (SPA) or a co-borrower in the Philippines who can sign and receive the car for you.",
faq=[("Can I apply for a car loan while working abroad?","Yes. Many Philippine banks accept OFW applicants. You can usually start online and coordinate documents with your sales executive and family at home."),
("What documents does an OFW need for a car loan?","Typically a passport, employment or crew contract, recent payslips, and proof of remittance for the last few months. Some banks also require a consularized certificate of employment or an SPA."),
("Who can receive the car if I'm not in the Philippines?","Your attorney-in-fact named in an SPA, or your co-borrower, can sign documents and receive the unit, depending on the bank's and dealer's requirements."),
("How early should I start if I want the car by Christmas?","Start as early as you can. Bank approval, document authentication from abroad and unit availability all take time, so begin weeks ahead of your homecoming.")],
body='''<p>Para sa lahat ng OFW na nagsasakripisyo abroad: you don't have to wait until you're home to start your car plan. Many of my clients apply from abroad and their family receives the car here. Here's how it works.</p>

<h2>Can OFWs apply while abroad?</h2>
<p>Yes. Many Philippine banks accept applications from Filipinos working abroad. Since you can't be here to sign, banks usually ask for one of these:</p>
<ul class="ticks"><li><b>Special power of attorney (SPA)</b>: authorizes a trusted family member to sign and transact for you. SPAs signed abroad are usually notarized or authenticated through the Philippine embassy or consulate, depending on the bank's requirements.</li><li><b>Co-borrower</b>: a family member in the Philippines who applies with you and shares responsibility for the loan.</li></ul>
<h2>Required documents</h2>
<p>Exact lists vary by bank, but OFW applications commonly include:</p>
<ul class="ticks"><li>Passport and valid IDs</li><li>Employment contract (or crew contract for seafarers)</li><li>Latest payslips or a certificate of employment with income</li><li>Proof of remittance for the past several months</li><li>Proof of billing for your Philippine address</li><li>SPA and IDs of your attorney-in-fact, or co-borrower documents</li></ul>
<p>Some banks ask for a consularized certificate of employment, and seafarers may need crewing details. Full list here: <a href="/guides/car-loan-requirements/">car loan requirements</a>.</p>
<h2>Release and registration when you're not in the PH</h2>
<ol class="steps"><li><h3>Approval</h3><p>The bank evaluates your documents and approves the loan.</p></li><li><h3>Signing</h3><p>Your attorney-in-fact or co-borrower signs the loan and release documents here.</p></li><li><h3>Registration</h3><p>For brand-new cars, the dealer processes the LTO registration. Since February 15, 2026, brand-new dealer-registered vehicles get a five-year initial registration. See <a href="/tips/lto-rules-2026-car-owners/">LTO rules 2026</a>.</p></li><li><h3>Release</h3><p>Your family receives the car at the showroom, and I walk them through the unit.</p></li></ol>
<h2>Choosing a family car for when you're away</h2>
<p>When you're not around, you want your family in something safe, roomy and easy to maintain. Think about:</p>
<ul class="ticks"><li><b>Space</b>: kids, lolo and lola, and grocery runs. A 7-seater like the <a href="/cars/xpander/">Xpander</a> or <a href="/cars/destinator/">Destinator</a> gives room to grow.</li><li><b>Ground clearance</b>: helpful during the rainy season and on provincial roads.</li><li><b>Who will drive</b>: choose a transmission your family is comfortable with.</li><li><b>Service access</b>: a dealer near home makes PMS easy for your family.</li></ul>
<h2>Timeline tips for a Christmas homecoming</h2>
<ul class="ticks"><li>Start early. Authentication of documents from abroad and bank evaluation take time.</li><li>Send scanned documents first so I can pre-check them.</li><li>Decide your unit and color early; availability can vary.</li><li>Have your family do the test drive for you if you can't. <a href="/test-drive/">Book it here</a>.</li><li>Use 13th month or bonus savings wisely. See my <a href="/blog/13th-month-pay-car-budget-plan/">13th month car budget plan</a>.</li></ul>
<p>I coordinate with OFW clients on Messenger across time zones, so message me wherever you are. Approval is subject to bank evaluation.</p>
'''+SRC(("BPI: Auto loan requirements (OFW)","https://www.bpi.com.ph/personal/loans/auto-loan/requirements"),("BDO: Auto loan (employed abroad)","https://www.bdo.com.ph/personal/loans/auto-loan"),("Chinabank: AutoPlus requirements (employed abroad)","https://www.chinabank.ph/loans-autoplus-eligibilities-requirements"),("Inquirer: New vehicles' registration valid for 5 years","https://newsinfo.inquirer.net/2177851/new-vehicles-registration-valid-for-5-years"))+CTA("Check which unit fits your income, then have your family book a test drive at our SJDM showroom.","xpander")),

dict(base="blog",car="mirage-g4",slug="13th-month-pay-car-budget-plan",date="2026-10-21",by=BY,img="mg4glx_u17",alt="Mitsubishi Mirage G4 GLX sedan",
title="13th Month Pay 2026: A Smart Car Budget Plan",
desc="13th month pay is due by December 24. How it's computed, a simple split plan, building a car fund, and what to ask about Christmas car promos.",
answer="Your 13th month pay is one-twelfth of the basic salary you earned in the year, and employers must release it by December 24. Before it disappears in holiday sales, split it: emergency fund first, then Christmas, then a car fund and ownership costs like PMS and insurance.",
faq=[("How is 13th month pay computed in the Philippines?","It's the total basic salary you earned during the calendar year divided by 12. Allowances and overtime are generally not included in the basic salary."),
("When is the deadline for 13th month pay?","Employers must release it on or before December 24."),
("Can I use my 13th month pay for a car?","Yes, it can go toward a car fund or reservation, but keep an emergency fund first and budget for fuel, insurance and maintenance."),
("Should I buy a car in December?","December can be a good time to ask about year-end promos, but buy only if the monthly and ownership costs fit your budget for the full term.")],
body='''<p>Dumating na ang 13th month… and by December 15, naubos na sa sale? Hindi ka nag-iisa. A little plan turns your 13th month into something that lasts longer than a shopping cart.</p>
<h2>How 13th month pay is computed and when it's due</h2>
<p>Under Philippine law, rank-and-file employees are entitled to 13th month pay equal to <b>one-twelfth of the total basic salary earned within the calendar year</b>. Employers must release it <b>on or before December 24</b>. If you started mid-year, it's prorated based on what you actually earned.</p>
<h2>A simple split framework</h2>
<p>There's no single right formula, but here's a starting point many families use. Adjust it to your situation:</p>
<ul class="ticks"><li><b>Emergency fund first</b>: if you don't have a few months of expenses saved, prioritize this.</li><li><b>Debts</b>: pay down high-interest credit card balances.</li><li><b>Pasko</b>: set a fixed amount for gifts, Noche Buena and family, and stick to it.</li><li><b>Car fund</b>: if a car is your next goal, put a portion aside for reservation, initial costs or your first year of ownership.</li><li><b>Maintenance</b>: if you already own a car, set aside for PMS, tires, battery and insurance renewal.</li></ul>
<h2>Car fund vs impulse spending</h2>
<p>Online sales are designed to make you buy now. Before you check out, ask: "Will I still care about this in March?" A car fund works best in a separate account you don't touch, so the money is there when you're ready.</p>
<h2>Hidden ownership costs to budget for</h2>
<ul class="ticks"><li>Fuel (see my <a href="/tips/fuel-saving-tips-diesel-vs-gasoline/">fuel-saving tips</a>)</li><li>Comprehensive insurance renewal after the first year</li><li>PMS at the intervals in your owner's manual</li><li>Parking and tolls</li><li>Tires and battery replacement over time</li></ul>
<p>The goal is a monthly that still leaves room for savings, not one that sasakal sa'yo every payday.</p>
<h2>Christmas promos: what to ask your sales executive</h2>
<ul class="ticks"><li>What exactly is included in the all-in package? (<a href="/guides/what-all-in-includes/">here's the usual list</a>)</li><li>Which freebies come with the unit?</li><li>What is the total amount I'll pay over the term?</li><li>What documents do I need, and how long does approval take?</li><li>When is the promo valid until?</li></ul>
<h2>Which car fits a careful budget?</h2>
<p>The <a href="/cars/mirage-g4/">Mirage G4</a> is the most affordable entry into the Mitsubishi lineup, with an official SRP starting at ₱793,000 (MMPC price list as of August 2026). If your family needs seven seats, the <a href="/cars/xpander/">Xpander</a> starts at ₱1,099,000 SRP. Promo terms change monthly, so ask me for the latest.</p>
'''+SRC(("YahshuaHRIS: 13th month pay computation in the Philippines (2026)","https://yahshuahris.com/blog/13th-month-pay-computation-philippines-2026"))+CTA("See which unit fits your income before you spend your 13th month, then book a test drive in SJDM.","mirage-g4")),

dict(base="blog",car="l300",slug="l300-negosyo-guide",date="2026-10-21",by=BY,img="l300_fb",alt="Mitsubishi L300 commercial truck for small businesses",
title="Mitsubishi L300 Negosyo Guide for Small Business",
desc="Is the L300 right for your negosyo? Cab and chassis vs ready-to-work units, load planning, financing for self-employed, maintenance and ROI thinking.",
answer="The Mitsubishi L300 is a 2.2L turbo-diesel workhorse sold as a cab and chassis (for a custom body) or as a ready-to-work Dual AC unit. It suits deliveries, hauling, catering and retail. Pick the body for your cargo, never overload past the rated capacity, and compare monthly costs against what you now pay for deliveries.",
faq=[("What L300 variants are available in 2026?","At SJ Legacy Motors: the L300 Cab & Chassis 2.2D M/T (for custom bodies) and the 2026 L300 Dual AC. Ask for the latest body options."),
("What engine does the L300 have?","A 2.2L 16-valve DOHC turbo-intercooled diesel (4N14), Euro 4 compliant, paired with a 5-speed manual."),
("Can a self-employed person finance an L300?","Yes. Banks typically ask for business registration, ITR or financial statements and business bank statements. Approval is subject to bank evaluation."),
("How much can the L300 carry?","It depends on the variant and body. Always follow the rated capacity in the official specifications and on your registration; ask me for the spec sheet of the exact unit.")],
body='''<p>Pag lumalaki na ang orders, the delivery fees and the "sino maghahatid?" stress add up. For many Filipino small businesses, the next step is owning a truck. The L300 has long been a familiar sight on Philippine roads because it's built for exactly that job.</p>
<h2>L300 at a glance</h2>
<ul class="ticks"><li>Engine: 2.2L 16-valve DOHC (4N14) turbo-intercooled diesel, Euro 4</li><li>Transmission: 5-speed manual</li><li>Variants: <b>Cab &amp; Chassis 2.2D M/T</b> (official SRP ₱829,000, MMPC price list as of August 2026) and the <b>2026 L300 Dual AC</b></li></ul>
<h2>Cab and chassis vs ready-to-work body</h2>
<p>The <b>cab and chassis</b> gives you the truck without a rear body, so you can have one built for your business: a dropside for hardware and construction supplies, an aluminum van for goods that need protection, or a specialized body for food or catering. The <b>Dual AC</b> unit is ready to work from release day with air-conditioning front and rear. Ask me which bodies are available and how the build affects the timeline.</p>
<h2>Load planning in the real world</h2>
<ul class="ticks"><li><b>Know your typical load</b>: count your heaviest regular order, not your average.</li><li><b>Stay within the rated capacity</b>: overloading wears the suspension, brakes and tires faster and is a safety risk. Check the official specs for your exact variant and body.</li><li><b>Secure the cargo</b>: use straps, nets or racks so the load doesn't shift.</li><li><b>Plan routes</b>: know your delivery areas' truck bans and road restrictions.</li></ul>
<h2>Business financing and documents</h2>
<p>Business owners finance trucks all the time. Banks commonly ask for:</p>
<ul class="ticks"><li>DTI or SEC registration, and mayor's/business permit</li><li>Latest ITR and financial statements</li><li>Business bank statements for the past several months</li><li>Valid IDs and proof of billing</li></ul>
<p>More detail in my <a href="/guides/car-loan-requirements/">car loan requirements guide</a> and <a href="/blog/car-loan-myths-philippines/">car loan myths</a> post. Approval is subject to bank evaluation.</p>
<h2>Maintenance for heavy-use units</h2>
<ul class="ticks"><li>Follow the PMS schedule in the owner's manual. Heavy daily use may call for the severe-service intervals.</li><li>Check tires, brakes and suspension often if you carry heavy loads.</li><li>Use the correct diesel and keep the fuel filter serviced.</li><li>Keep a simple log of mileage and service so nothing is missed.</li></ul>
<p>To keep fuel costs down, see my <a href="/tips/fuel-saving-tips-diesel-vs-gasoline/">fuel-saving tips</a>.</p>
<h2>ROI thinking: delivery fees vs owning your truck</h2>
<p>Do this simple exercise before buying:</p>
<ol class="steps"><li><h3>Add up what you pay now</h3><p>Monthly delivery fees, lalamove or courier costs, and lost orders when no one could deliver.</p></li><li><h3>Estimate ownership costs</h3><p>Your monthly amortization plus fuel, insurance, PMS, a driver's pay (if any), tolls and parking.</p></li><li><h3>Count the upside</h3><p>More orders you can accept, faster deliveries, and new routes or services you could offer.</p></li><li><h3>Compare</h3><p>If owning costs about the same or less and lets you grow, the truck can pay for itself over time.</p></li></ol>
<p>Run your numbers on the <a href="/budgetcalculator/">budget calculator</a>, then come see the <a href="/cars/l300/">L300</a> in person.</p>
'''+CTA("Ready to grow your negosyo? Check the budget that fits, then book an L300 test drive in SJDM.","l300")),

dict(base="blog",car="destinator",slug="xpander-vs-destinator-family-car",date="2026-10-21",by=BY,img="de_x3n",alt="Mitsubishi Destinator GT 7-seater SUV, compared with the Xpander",
title="Xpander vs Destinator: Which Family Car Fits?",
desc="Xpander or Destinator? Compare seating, engine, fuel and price, see which fits city, probinsya and big families, and what to check on a test drive.",
answer="Both seat seven. The Xpander is the more affordable, family-proven MPV with a 1.5L engine (105 PS), while the Destinator is a 7-seat SUV with a 1.5L turbo (163 PS, 250 Nm) and 214 mm ground clearance. Choose the Xpander for value and city use, the Destinator for more power on full loads and rougher roads.",
faq=[("Is the Destinator bigger than the Xpander?","Both seat seven. The Destinator is an SUV with 214 mm ground clearance; compare cabin and cargo space in person on a test drive with your family."),
("Which is more powerful, Xpander or Destinator?","The Destinator. Its 1.5L turbo makes 163 PS and 250 Nm, versus the Xpander's 1.5L at 105 PS and 141 Nm."),
("Which is cheaper?","The Xpander, with an official SRP starting at ₱1,099,000. The Destinator starts at ₱1,389,000 (MMPC price list as of August 2026)."),
("What transmission do they use?","The Xpander comes in a 5-speed manual or 4-speed automatic; the Destinator uses a CVT.")],
body='''<p>Isang salita lang: Xpander is "maluwag," Destinator is "astig." But your family deserves more than one word. Here's a fair comparison to help you decide.</p>
<h2>Quick comparison</h2>
<table class="spec"><tr><th scope="row"></th><td><b>Xpander</b></td><td><b>Destinator</b></td></tr>
<tr><th scope="row">Type</th><td>7-seater MPV</td><td>7-seater SUV</td></tr>
<tr><th scope="row">Engine</th><td>1.5L MIVEC gasoline</td><td>1.5L turbo gasoline (4B40)</td></tr>
<tr><th scope="row">Power / torque</th><td>105 PS / 141 Nm</td><td>163 PS / 250 Nm</td></tr>
<tr><th scope="row">Transmission</th><td>5-speed MT or 4-speed AT</td><td>CVT</td></tr>
<tr><th scope="row">Ground clearance</th><td>High (ask for variant spec)</td><td>214 mm</td></tr>
<tr><th scope="row">Starting SRP</th><td>₱1,099,000</td><td>₱1,389,000</td></tr></table>
<p class="muted">SRPs from the official Mitsubishi Motors Philippines price list (as of August 2026), subject to change without notice.</p>
<h2>Size, seating and cargo</h2>
<p>Both seat seven, so the question is how you'll use the space. The <a href="/cars/xpander/">Xpander</a> is a practical MPV built around Filipino families, easy to get in and out of. The <a href="/cars/destinator/">Destinator</a> is an SUV with a more commanding stance and 214 mm of ground clearance. Reviewers have praised the Destinator's cabin space. The best test: bring your family and the stuff you usually carry, and try the third row and the cargo area of both.</p>
<h2>Engine, performance and fuel</h2>
<p>The Destinator's turbo engine (163 PS, 250 Nm) is a clear step up when the car is full and you're climbing or overtaking on the expressway. The Xpander's 1.5L is simpler and adequate for city driving and regular family trips. One practical note from reviews: the Destinator has a 45-liter fuel tank, so plan fuel stops on long drives. Actual fuel economy depends a lot on traffic and driving style; see my <a href="/tips/fuel-saving-tips-diesel-vs-gasoline/">fuel-saving tips</a>.</p>
<h2>Safety and features by variant</h2>
<p>Features differ by variant: the Xpander comes in GLX and GLS trims, and the Destinator in GLX, GLS and GT. Higher variants generally add more comfort and driver-assist features. Ask me for the official spec sheet of the exact variants you're comparing so you're looking at the real list, not assumptions.</p>
<h2>Which fits which family?</h2>
<ul class="ticks"><li><b>Mostly city, budget-conscious</b>: Xpander. Lower starting price, easy to drive and park.</li><li><b>Frequent probinsya trips with a full car</b>: Destinator. The turbo and torque make full-load highway driving easier.</li><li><b>Flood-prone areas or rough roads</b>: both have good clearance; the Destinator's 214 mm adds margin.</li><li><b>Big family, growing kids</b>: try both third rows in person before deciding.</li></ul>
<p>Still deciding among more models? See my <a href="/blog/best-7-seater-for-filipino-families-2026/">best 7-seater for Filipino families</a> and <a href="/guides/xpander-vs-xpander-cross-vs-destinator/">Xpander vs Xpander Cross vs Destinator</a> guides.</p>
<h2>Test drive both: what to compare</h2>
<ul class="ticks"><li>Third-row comfort for adults and kids</li><li>Cargo space with all seats up</li><li>Acceleration with passengers on board</li><li>Ride comfort over bumps</li><li>Visibility and ease of parking</li><li>AC reach to the back rows</li></ul>
'''+SRC(("Top Gear Philippines: Mitsubishi Destinator 2026 review","https://www.topgear.com.ph/drives/car-reviews/mitsubishi-destinator-2026-ph-review-a2584-20260212-lfrm"),("GoFlatOut PH: 2026 Mitsubishi Destinator GLS review","https://goflatoutph.com/2026/07/09/2026-mitsubishi-destinator-gls-review-the-turbocharged-sweet-spot/"))+CTA("Test drive the Xpander and Destinator back-to-back at our SJDM showroom, after checking which fits your budget.","destinator")),
]

# ---------- Bulk series (Oct 22, 2026). Prices: October 2026 dealer promos only, 5-year term, subject to bank approval.
TELL='<a href="tel:+639542911201">0954 291 1201</a>'
def CTA2(lead,unit=""):
    q=f"?unit={unit}" if unit else ""
    return f'''<h2>Your next step</h2>
<p>{lead}</p>
<p class="row"><a class="btn" href="/budgetcalculator/">Check what fits my budget</a> <a class="btn ghost dk" href="/test-drive/{q}">Book a Test Drive</a> <a class="btn ghost dk" href="tel:+639542911201">Call or text 0954 291 1201</a></p>
<p class="muted">Questions muna? Call or text me, Richard, on {TELL}, walang pressure. Showroom: Mitsubishi SJ Legacy Motors, Lot 9 Ebenezer Christian Academy, Sitio Gitna, Sto. Cristo, Quirino Highway, San Jose del Monte, Bulacan. Promo figures are for October 2026 on a 5-year term, all-in, subject to bank approval and change without notice.</p>'''
PN='<p class="muted">October 2026 dealer promos, 60 months, all-in. Subject to bank approval and change without notice. Message me for the latest promo.</p>'
def T(head,rows):
    return '<table class="spec"><tr>'+"".join(f'<th scope="col">{h}</th>' for h in head)+'</tr>'+"".join('<tr>'+f'<th scope="row">{r[0]}</th>'+"".join(f'<td>{c}</td>' for c in r[1:])+'</tr>' for r in rows)+'</table>'
BULK=[
dict(base="blog",car="xpander",slug="how-much-car-can-i-afford-philippines",date="2026-10-22",by=BY,img="xpglx_u33",alt="Mitsubishi Xpander GLX, a popular family car for a careful budget",
title="How Much Car Can I Afford? The 30–35% Rule",
desc="Use the 30–35% income rule to see which Mitsubishi fits your salary, with October 2026 Zero DP monthlies and the income each one needs.",
answer="A safe guide is to keep your car amortization at about 30 to 35 percent of your gross monthly income. Divide the monthly by 0.35 for the minimum income and by 0.30 for a comfortable one. For example, the Xpander GLX MT at ₱22,641 a month (Zero DP, October 2026 promo) fits a gross income of roughly ₱64,700 to ₱75,500.",
faq=[("What percentage of my income should go to a car loan?","As a guide, keep the monthly amortization at about 30 to 35 percent of your gross monthly income, so there's still room for fuel, insurance, savings and family needs. Banks make the final assessment."),
("Can I combine my income with my spouse's?","Many banks allow a co-borrower, often a spouse, so combined income can be considered. Requirements depend on the bank."),
("Does a bigger down payment lower the income I need?","Yes. A bigger down payment lowers the monthly, so the income needed goes down too. Compare the Zero DP and low DP options of the same unit."),
("Is the 30–35% rule the bank's official rule?","No. It's a planning guide I use with clients. Each bank has its own credit evaluation, and approval is always subject to bank approval.")],
body='''<p>"Kaya ko ba talaga?" is the most important question before buying a car, and the most skipped. The easy way to answer it is a simple rule I use with every client: <b>keep your monthly amortization at about 30 to 35 percent of your gross monthly income</b>.</p>
<p>That leaves the rest of your income for the things that don't stop when you buy a car: bills, food, tuition, savings, and the car's own running costs like fuel, PMS and insurance renewal.</p>

<h2>The rule in one line</h2>
<p>Work backwards from the monthly:</p>
<ul class="ticks">
<li><b>Minimum income</b> = monthly amortization ÷ 0.35</li>
<li><b>Comfortable income</b> = monthly amortization ÷ 0.30</li>
</ul>
<p>If your gross income is at or above the comfortable figure, you have breathing room. If it's between the two, it can still work, but budget carefully. If it's below the minimum, look at a bigger down payment, a co-borrower, or a different unit.</p>

<h2>October 2026 Zero DP monthlies and the income they need</h2>
<p>Here's the rule applied to this month's Zero DP promos on a 5-year term. Incomes are rounded to the nearest ₱100.</p>
'''+T(["Unit","Zero DP monthly","Gross income (30–35%)"],[
("L300 Dual AC","₱21,405","₱61,200 – ₱71,400"),
("Xpander GLX MT","₱22,641","₱64,700 – ₱75,500"),
("Xpander GLX AT","₱23,877","₱68,200 – ₱79,600"),
("Xpander GLS AT","₱25,937","₱74,100 – ₱86,500"),
("Xpander Cross","₱28,389","₱81,100 – ₱94,600"),
("Destinator GLX","₱28,615","₱81,800 – ₱95,400"),
("Triton GX AT","₱28,900","₱82,600 – ₱96,300"),
("Montero Sport GLX MT","₱30,284","₱86,500 – ₱100,900"),
("Destinator GLS","₱32,942","₱94,100 – ₱109,800"),
("Montero Sport GLS","₱39,699","₱113,400 – ₱132,300"),
("Destinator GT","₱39,740","₱113,500 – ₱132,500")])+PN+'''

<h2>How a down payment changes the picture</h2>
<p>Every unit also has a low DP option. Paying more upfront lowers the monthly, and so lowers the income you need. A few examples from this month's promos:</p>
'''+T(["Unit","Zero DP","With down payment"],[
("Xpander GLX MT","₱22,641/mo","₱148K DP: ₱19,811/mo"),
("Xpander GLS AT","₱25,937/mo","₱148K DP: ₱22,695/mo"),
("Destinator GLS","₱32,942/mo","₱123K DP: ₱30,883/mo"),
("Triton GX AT","₱28,900/mo","₱140K DP: ₱25,200/mo")])+'''
<p>For a deeper look at the trade-off, read my <a href="/guides/zero-dp-vs-low-dp/">Zero DP vs low DP guide</a>.</p>

<h2>Three ways to make a unit fit</h2>
<ol class="steps">
<li><h3>Add a co-borrower</h3><p>Many banks allow a spouse or immediate family member as co-borrower, so combined income is considered.</p></li>
<li><h3>Put down a bigger DP</h3><p>A low DP option lowers the monthly. Even part of your 13th month can help; see my <a href="/blog/13th-month-pay-car-budget-plan/">13th month car budget plan</a>.</p></li>
<li><h3>Choose the right variant</h3><p>The difference between variants can be a few thousand pesos a month. A manual GLX may fit where an automatic GLS doesn't.</p></li>
</ol>

<h2>Don't forget the costs after the monthly</h2>
<p>The 30–35% rule covers the amortization only. Set aside a separate monthly budget for fuel, parking, tolls, PMS and the comprehensive insurance renewal after the locked period. The all-in package covers a lot at the start: LTO registration, TPL insurance, 1-year comprehensive insurance with the rate locked for 3 years, chattel mortgage, free labor up to 5,000 km and a 3-year warranty. Here's <a href="/guides/what-all-in-includes/">what all-in covers</a>.</p>
<p>Want me to do the math for you? The <a href="/budgetcalculator/">Budget Fit Calculator</a> matches your income to the units that fit in under a minute.</p>
'''+CTA2("Tell the calculator your income and see which unit fits, then test drive it in San Jose del Monte.","xpander")),

dict(base="blog",car="triton",slug="triton-for-business-and-farm",date="2026-10-22",by=BY,img="tr_gx_u28",alt="Mitsubishi Triton GX pickup for business and farm use",
title="Mitsubishi Triton for Business and Farm Use",
desc="Is the Triton the right pickup for your negosyo, farm or resort? 2WD vs 4WD, cargo bed tips, the October 2026 Triton GX AT promo, and financing.",
answer="The Mitsubishi Triton is a 2.4L turbo-diesel pickup with a cargo bed, offered in 2WD and 4WD and in manual or automatic by variant. It suits contractors, farms, resorts and businesses that haul supplies on weekdays and carry the family on weekends. In October 2026, the Triton GX AT is ₱1,430,000 SRP, from ₱28,900 a month at Zero DP or ₱25,200 a month with ₱140K DP, plus ₱20K fuel.",
faq=[("Should I get a 2WD or 4WD Triton?","Choose 2WD if your routes are paved or well-maintained provincial roads. Choose 4WD if you regularly drive on mud, steep farm roads, river crossings or unpaved hills."),
("How much is the Triton GX AT promo in October 2026?","SRP ₱1,430,000. Zero DP at ₱28,900 a month or ₱140K DP at ₱25,200 a month on 60 months, all-in, with ₱20K fuel. Subject to bank approval."),
("Can a business finance a Triton?","Yes. Self-employed buyers and businesses commonly submit business registration, ITR or financial statements and bank statements. Approval is subject to bank evaluation."),
("Is a pickup comfortable for the family?","The Triton is a double-cab pickup with a rear seat, so it can do family duty on weekends. Bring your family to the test drive to check the rear seat.")],
body='''<p>Sa probinsya at sa negosyo, a pickup does two jobs. Monday to Saturday it carries sacks of feed, hollow blocks, tools or resort supplies. On Sunday it takes the family to church and lunch. That's the job the <a href="/cars/triton/">Mitsubishi Triton</a> was built for.</p>

<h2>Triton at a glance</h2>
<ul class="ticks">
<li><b>Engine</b>: 2.4L 4N16 intercooled turbo diesel</li>
<li><b>Transmission</b>: 6-speed manual or automatic, by variant</li>
<li><b>Drivetrain</b>: 2WD or 4WD, by variant</li>
<li><b>Body</b>: pickup with an open cargo bed</li>
</ul>
<p>The lineup runs from the work-focused GL variants up to the GLX, GLS and Athlete. Exact features differ per variant, so ask me for the official spec sheet of the ones you're comparing.</p>

<h2>Who the Triton is for</h2>
<ul class="ticks">
<li><b>Contractors and hardware owners</b>: tools, materials and crew in one trip.</li>
<li><b>Farm owners</b>: feed, fertilizer, harvest and farm roads that turn muddy after rain.</li>
<li><b>Resort and events businesses</b>: supplies, coolers and equipment.</li>
<li><b>Families in the province</b>: weekend family use with a cargo bed for balikbayan boxes and pasalubong.</li>
</ul>

<h2>2WD or 4WD?</h2>
<p>This is the biggest choice, and it depends on your roads, not your pride.</p>
<ul class="ticks">
<li><b>2WD</b> is enough for paved highways, city deliveries and well-kept provincial roads. It's usually the more affordable choice.</li>
<li><b>4WD</b> earns its keep on mud, steep unpaved farm roads, river crossings and hilly sites, especially during the rainy season.</li>
</ul>
<p>Ask yourself: how many days a year do I really need 4WD? If the answer is "every rainy season, every week," get 4WD.</p>

<h2>The October 2026 Triton GX AT promo</h2>
'''+T(["Triton GX 2.4D 2WD A/T","Monthly (60 months)"],[("Zero DP","₱28,900"),("₱140K DP","₱25,200")])+'''
<p>SRP ₱1,430,000, all-in, plus ₱20K fuel. Using the 30–35% income guide, the Zero DP monthly fits a gross monthly income of roughly ₱82,600 to ₱96,300. For other Triton variants, message me for the latest promo.</p>
'''+PN+'''

<h2>Cargo bed tips for working owners</h2>
<ol class="steps">
<li><h3>Stay within the rated payload</h3><p>Overloading wears the suspension, brakes and tires faster and is a safety risk. Check the official spec for your variant.</p></li>
<li><h3>Tie down every load</h3><p>Use straps or a cargo net so sacks and tools don't shift on bumps.</p></li>
<li><h3>Protect the bed</h3><p>A bed liner helps against scratches from tools and hollow blocks. Ask what accessories are available.</p></li>
<li><h3>Cover what needs cover</h3><p>Feed, cement and electronics need protection from rain. Keep a tarpaulin in the cab.</p></li>
</ol>

<h2>Financing for business owners</h2>
<p>Business owners finance pickups all the time. Banks commonly ask for DTI or SEC registration, a mayor's or business permit, your latest ITR or financial statements, and business bank statements. Full list in my <a href="/guides/car-loan-requirements/">car loan requirements guide</a>. If you're choosing between a pickup and a truck for deliveries, my <a href="/blog/l300-negosyo-guide/">L300 negosyo guide</a> covers the truck side.</p>
'''+CTA2("Check if the Triton fits your negosyo budget, then book a test drive, ideally with the load you usually carry in mind.","triton")),

dict(base="blog",car="montero-sport",slug="montero-sport-variants-explained",date="2026-10-22",by=BY,img="msbs_jh3",alt="Mitsubishi Montero Sport Black Series SUV",
title="Montero Sport Variants Explained: GLX, GLS, Black Series",
desc="Montero Sport GLX MT, GLS, Black Series 2WD or 4WD? What changes between variants and the October 2026 promo monthlies for each.",
answer="All Montero Sport variants share the 2.4L 4N15 turbo diesel (181 PS, 430 Nm) and seven seats. The GLX MT is the value pick with a 6-speed manual (₱1,568,000 SRP). The GLS AT (₱1,927,000) adds the 8-speed automatic. The Black Series AT comes in 2WD (₱2,190,000) and 4WD (₱2,530,000) for buyers who want the top trim and, on the 4WD, off-road capability.",
faq=[("What engine does the Montero Sport have?","A 2.4L (2,442 cc) 4N15 MIVEC intercooled turbo diesel with 181 PS and 430 Nm, Euro 4 compliant."),
("Which Montero Sport is manual?","The GLX 2.4D 2WD M/T, with a 6-speed manual. The GLS and Black Series use an 8-speed automatic."),
("Do I need the Black Series 4WD?","Only if you regularly drive on rough, muddy or steep roads, or want 4WD for out-of-town trips. For city and highway use, 2WD is usually enough."),
("What's the lowest monthly for a Montero Sport this month?","The GLX MT at ₱28,265 a month with ₱30K DP, or ₱30,284 at Zero DP, on 60 months all-in (October 2026 promo, subject to bank approval).")],
body='''<p>The <a href="/cars/montero-sport/">Montero Sport</a> is the full-size, ladder-frame diesel SUV in the Mitsubishi lineup. All variants share the same heart, so choosing one is really about three questions: manual or automatic, how much trim you want, and whether you need 4WD.</p>

<h2>What every Montero Sport shares</h2>
<ul class="ticks">
<li>2.4L (2,442 cc) 4N15 MIVEC intercooled turbo diesel, Euro 4</li>
<li>181 PS and 430 Nm</li>
<li>Seven seats on a ladder frame built for long drives and heavy loads</li>
</ul>

<h2>The four variants, side by side</h2>
'''+T(["Variant","SRP","Promo monthly (60 mos)"],[
("GLX 2.4D 2WD M/T","₱1,568,000","Zero DP ₱30,284 · ₱30K DP ₱28,265"),
("GLS 2.4D 2WD A/T","₱1,927,000","Zero DP ₱39,699 · ₱138K DP ₱37,218 · ₱20K fuel"),
("Black Series 2.4D 2WD A/T","₱2,190,000","₱88K DP ₱45,117 · ₱218K DP ₱42,297 · ₱20K fuel"),
("Black Series 2.4D 4WD A/T","₱2,530,000","₱133K DP ₱52,121 · ₱283K DP ₱48,864 · ₱20K fuel")])+PN+'''

<h2>GLX MT: the value pick</h2>
<p>The GLX uses a <b>6-speed manual</b> and is the most affordable way into a Montero Sport. It suits buyers who are comfortable with a clutch, drive long highway stretches, or want the diesel SUV body and torque at the lowest monthly. At ₱28,265 a month with just ₱30K down, it's the entry point.</p>

<h2>GLS AT: the everyday automatic</h2>
<p>The GLS steps up to the <b>8-speed automatic</b>, which makes daily traffic on Quirino Highway or EDSA much easier on your left leg. It's the sweet spot for most families who want a Montero Sport they'll drive every day.</p>

<h2>Black Series: 2WD or 4WD</h2>
<p>The Black Series is the top trim with its own styling, offered in <b>2WD</b> and <b>4WD</b>, both automatic. Choose the 2WD if you want the look and trim for city and highway use. Choose the 4WD if your weekends include mountain roads, beach access roads or farm properties, or if you live in an area where roads get rough in the rainy season.</p>
<p>Features differ by variant, so ask me for the official spec sheet before deciding. I'd rather you compare the real list than assumptions.</p>

<h2>Which income fits which variant?</h2>
<p>Using the 30–35% income guide on the lowest monthly of each variant:</p>
<ul class="ticks">
<li><b>GLX MT</b> (₱28,265): about ₱80,800 to ₱94,200 gross monthly income</li>
<li><b>GLS AT</b> (₱37,218): about ₱106,300 to ₱124,100</li>
<li><b>Black Series 2WD</b> (₱42,297): about ₱120,800 to ₱141,000</li>
<li><b>Black Series 4WD</b> (₱48,864): about ₱139,600 to ₱162,900</li>
</ul>
<p>More on this in <a href="/blog/how-much-car-can-i-afford-philippines/">How much car can I afford?</a></p>
'''+CTA2("Narrowed it down? Check which variant fits your budget, then test drive the Montero Sport in SJDM.","montero-sport")),
dict(base="blog",car="xpander",slug="xpander-variants-explained",date="2026-10-22",by=BY,img="xpgls_c31",alt="Mitsubishi Xpander GLS AT family MPV",
title="Xpander GLX MT vs GLX AT vs GLS vs Cross",
desc="Which Xpander should you get? GLX MT, GLX AT, GLS AT or Xpander Cross compared, with October 2026 promo monthlies, fuel freebies and who each fits.",
answer="All four seat seven and use the same 1.5L MIVEC gasoline engine (105 PS, 141 Nm). The GLX MT (₱1,099,000) is the lowest monthly at ₱22,641 Zero DP. The GLX AT (₱1,159,000) adds a 4-speed automatic. The GLS AT (₱1,259,000) is the higher trim, and the Xpander Cross (₱1,378,000) adds a rugged crossover look and a more premium cabin.",
faq=[("Which Xpander variant is cheapest?","The Xpander GLX MT, at ₱1,099,000 SRP. In October 2026 it's ₱22,641 a month at Zero DP or ₱19,811 with ₱148K DP, plus ₱30K fuel."),
("Is the Xpander Cross more powerful than the Xpander?","No. Both use the 1.5L MIVEC gasoline engine with 105 PS and 141 Nm and a 4-speed automatic on the AT units. The Cross differs in styling and cabin."),
("Manual or automatic Xpander?","Get the manual for the lowest monthly if you're comfortable with a clutch. Get the automatic if you sit in daily traffic or if several family members will drive."),
("Which Xpander gets the biggest fuel freebie?","In October 2026, the GLX AT, GLS AT and Xpander Cross each come with ₱60K fuel; the GLX MT comes with ₱30K.")],
body='''<p>The <a href="/cars/xpander/">Xpander</a> is the car I'm asked about most on the showroom floor. The question is usually not "Xpander o hindi?" but "Alin sa Xpander?" Here's how the four choices differ, with this month's promo numbers.</p>

<h2>Same engine, different packages</h2>
<p>Every Xpander and the <a href="/cars/xpander-cross/">Xpander Cross</a> share a 1.5L in-line 4 DOHC 16-valve MIVEC gasoline engine with 105 PS and 141 Nm, and seven seats. What changes is the transmission, the trim and the look.</p>

<h2>October 2026 promos at a glance</h2>
'''+T(["Variant","SRP","Zero DP","Low DP","Fuel"],[
("GLX 1.5G M/T","₱1,099,000","₱22,641","₱148K DP: ₱19,811","₱30K"),
("GLX 1.5G A/T","₱1,159,000","₱23,877","₱138K DP: ₱20,892","₱60K"),
("GLS 1.5G A/T","₱1,259,000","₱25,937","₱148K DP: ₱22,695","₱60K"),
("Xpander Cross A/T","₱1,378,000","₱28,389","₱148K DP: ₱24,840","₱60K")])+PN+'''

<h2>GLX MT: lowest monthly</h2>
<p>A 5-speed manual and the lowest price of the four. Great for buyers who already drive manual, want the most seats for the money, or use the car for a small business like school service or deliveries. Note the fuel freebie is ₱30K, versus ₱60K on the automatics.</p>

<h2>GLX AT: the practical automatic</h2>
<p>Only ₱1,236 more a month than the GLX MT at Zero DP, and it comes with the 4-speed automatic and ₱60K fuel. For most families who'll face SJDM to Metro Manila traffic, this is the value automatic.</p>

<h2>GLS AT: the higher trim</h2>
<p>The GLS is the upper Xpander trim, with more comfort and convenience features than the GLX. It suits buyers who want a nicer daily cabin without moving up to an SUV. Ask me for the spec sheet so you can see the exact GLX vs GLS differences.</p>

<h2>Xpander Cross: MPV practicality, SUV style</h2>
<p>The Cross keeps the Xpander's seven seats and engine, then adds a rugged crossover look and a more premium cabin, in a two-tone finish. Choose it if styling matters to you and the monthly fits. If you're torn between the Cross and an SUV, read <a href="/guides/xpander-vs-xpander-cross-vs-destinator/">Xpander vs Xpander Cross vs Destinator</a> and <a href="/blog/xpander-vs-destinator-family-car/">Xpander vs Destinator</a>.</p>

<h2>Quick picker</h2>
<ul class="ticks">
<li><b>Tightest budget, comfortable with manual</b>: GLX MT</li>
<li><b>Daily traffic, multiple drivers at home</b>: GLX AT</li>
<li><b>Wants a nicer cabin</b>: GLS AT</li>
<li><b>Wants the crossover look</b>: Xpander Cross</li>
</ul>
'''+CTA2("Check which Xpander fits your income, then test drive the manual and automatic back-to-back in SJDM.","xpander")),

dict(base="blog",car="destinator",slug="destinator-glx-vs-gls-vs-gt",date="2026-10-22",by=BY,img="de_d34",alt="Mitsubishi Destinator GLS 7-seater SUV",
title="Destinator GLX vs GLS vs GT: Which Variant?",
desc="Destinator GLX, GLS or GT? Same 1.5L turbo and CVT, different trims and monthlies. October 2026 promo figures and a simple way to choose.",
answer="Every Destinator has the 1.5L turbo (163 PS, 250 Nm), a CVT, seven seats and 214 mm ground clearance. The GLX (₱1,389,000) is the entry, from ₱26,827 a month with ₱93K DP. The GLS (₱1,599,000) is the mid trim with ₱20K fuel. The GT (₱1,929,000 mono, ₱1,939,000 two-tone) is the top trim with ₱40K fuel.",
faq=[("Do all Destinator variants have the turbo engine?","Yes. GLX, GLS and GT all use the 1.5L turbocharged 4B40 gasoline engine with 163 PS and 250 Nm, paired with a CVT."),
("How much is the Destinator GT two-tone?","₱1,939,000 SRP, versus ₱1,929,000 for the monotone. Both share the same October 2026 promo: Zero DP ₱39,740 a month or ₱88K DP ₱37,256, with ₱40K fuel."),
("Which Destinator has the lowest monthly?","The GLX: ₱28,615 a month at Zero DP or ₱26,827 with ₱93K DP (October 2026, 60 months, all-in)."),
("Is the GLS worth it over the GLX?","It depends on which features matter to you. Compare the official spec sheets, and note the GLS comes with ₱20K fuel this month while the GLX doesn't.")],
body='''<p>Once families decide on the <a href="/cars/destinator/">Destinator</a>, the next question is which variant. Good news: you don't lose the engine by choosing the entry trim. All three share the same turbo, so the choice is about features, look and monthly.</p>

<h2>What all three share</h2>
<ul class="ticks">
<li>1.5L turbocharged gasoline engine (4B40), Euro 4: 163 PS and 250 Nm</li>
<li>CVT automatic</li>
<li>Seven seats and 214 mm ground clearance</li>
</ul>

<h2>October 2026 promos</h2>
'''+T(["Variant","SRP","Zero DP","Low DP","Fuel"],[
("GLX","₱1,389,000","₱28,615","₱93K DP: ₱26,827","Ask"),
("GLS","₱1,599,000","₱32,942","₱123K DP: ₱30,883","₱20K"),
("GT (Monotone)","₱1,929,000","₱39,740","₱88K DP: ₱37,256","₱40K"),
("GT (Two-Tone)","₱1,939,000","₱39,740","₱88K DP: ₱37,256","₱40K")])+PN+'''

<h2>GLX: the turbo SUV at the lowest monthly</h2>
<p>The GLX gives you the full turbo performance and seven seats for the lowest monthly in the range. It's for families who want an SUV that pulls well with a full car and are happy with an entry-level feature set.</p>

<h2>GLS: the balanced middle</h2>
<p>The GLS adds more comfort and convenience over the GLX and comes with ₱20K fuel this month. For many families it's the sensible middle: more features, without the GT's monthly.</p>

<h2>GT: the top of the range</h2>
<p>The GT is the flagship trim, offered in monotone or two-tone, with the most features in the range and ₱40K fuel this month. Choose it if you want the most complete package and the monthly sits comfortably within your budget.</p>
<p>Exact features differ per variant. Ask me for the official spec sheets so we compare the real list side by side.</p>

<h2>How to choose in 3 steps</h2>
<ol class="steps">
<li><h3>Start with your income</h3><p>At 30–35% of gross income, the GLX Zero DP monthly fits roughly ₱81,800 to ₱95,400 a month, the GLS ₱94,100 to ₱109,800, and the GT ₱113,500 to ₱132,500.</p></li>
<li><h3>List your must-have features</h3><p>Write down the 3 features you really care about, then check which variant has them on the spec sheet.</p></li>
<li><h3>Test drive with the family</h3><p>Bring the people who'll ride in the third row. Here's my <a href="/blog/xpander-vs-destinator-family-car/">Xpander vs Destinator</a> comparison if you're still choosing models.</p></li>
</ol>
'''+CTA2("Pick your Destinator variant with real numbers, then test drive it in San Jose del Monte.","destinator")),
dict(base="tips",car="xpander",slug="pms-schedule-guide",date="2026-10-22",by=BY,img="xpglx_x37",alt="Mitsubishi Xpander ready for its preventive maintenance service",
title="PMS Schedule Guide for New Car Owners",
desc="What is PMS, when is it due, and what gets checked? A plain guide to preventive maintenance for new Mitsubishi owners, plus how to keep your warranty.",
answer="PMS (preventive maintenance service) is the scheduled check-up in your owner's manual and warranty booklet, set by kilometers or months, whichever comes first. Follow those intervals at an authorized service center, keep every receipt, and use the free labor on your all-in package for the services up to 5,000 km.",
faq=[("How often is PMS for a new car?","Follow the intervals in your owner's manual and warranty booklet. They're set by kilometers or months, whichever comes first, and heavy use may call for the severe-service schedule."),
("Is PMS free for new Mitsubishi cars?","The all-in package includes free labor up to 5,000 km. Parts, oil and fluids, and later services are paid. Ask the service center for a quote before each PMS."),
("Will skipping PMS void my warranty?","Missing scheduled maintenance can affect warranty claims. Follow the schedule in your warranty booklet and keep your service records."),
("How much does PMS cost?","It depends on the model, the kilometer interval and the parts needed. Ask the service center for a written estimate for your unit before booking.")],
body='''<p>Bagong kotse, bagong responsibilidad. The easiest way to keep a new car reliable, and your warranty in good standing, is to follow its PMS schedule. Here's what you need to know without the jargon.</p>

<h2>What PMS is (and isn't)</h2>
<p>PMS means <b>preventive maintenance service</b>: scheduled check-ups that replace fluids and filters and inspect wear items before they fail. It's not a repair visit. It's how you avoid repair visits.</p>

<h2>Where to find your schedule</h2>
<p>Your exact PMS intervals are in your <b>owner's manual and warranty booklet</b>. Each interval is set by kilometers or months, <b>whichever comes first</b>. So even if you barely drive, the car still needs its check-up when the months are up.</p>
<ul class="ticks">
<li>Check your odometer once a month and note the next due kilometer.</li>
<li>Put the due month in your phone calendar on release day.</li>
<li>If you drive in heavy traffic, on rough roads, or carry heavy loads every day, ask if the severe-service schedule applies to you.</li>
</ul>

<h2>What usually gets checked</h2>
<p>Each interval has its own list, but most PMS visits cover some of these:</p>
<ul class="ticks">
<li>Engine oil and oil filter</li>
<li>Air filter and cabin (aircon) filter</li>
<li>Brake pads, discs and brake fluid</li>
<li>Coolant, power steering and other fluids</li>
<li>Tires: pressure, tread, rotation</li>
<li>Battery, lights, wipers and belts</li>
<li>Underchassis and suspension</li>
</ul>

<h2>Free labor up to 5,000 km</h2>
<p>The all-in package includes <b>free labor up to 5,000 km</b>. That covers the labor on your early services; parts, oil and fluids are usually paid. Ask the service center what's covered before your visit so there are no surprises. Costs vary by model and interval, so always ask for a written estimate.</p>

<h2>PMS habits that protect your warranty</h2>
<ol class="steps">
<li><h3>Book ahead</h3><p>Service centers get busy before long weekends. Book a few days early.</p></li>
<li><h3>Stay on schedule</h3><p>Missing intervals can affect warranty claims. The all-in package comes with a 3-year warranty, so protect it.</p></li>
<li><h3>Keep every receipt</h3><p>Service records help with warranty claims and resale value later.</p></li>
<li><h3>Mention anything odd</h3><p>Noises, warning lights or vibrations: tell the service advisor so they check it during PMS.</p></li>
</ol>
<p>Just got your car? Read my <a href="/tips/first-1000-km-break-in-tips/">first 1,000 km tips</a> next. And for heat and flood season, see <a href="/tips/el-nino-typhoon-car-care-tips/">El Niño and typhoon car care</a>.</p>
'''+CTA2("Planning your first car? Check what fits your budget, then test drive in SJDM. I'll walk you through the PMS schedule on release day.","xpander")),

dict(base="tips",car="destinator",slug="first-1000-km-break-in-tips",date="2026-10-22",by=BY,img="de_w81",alt="Brand-new Mitsubishi Destinator on its first drives",
title="First 1,000 km: New Car Break-In Tips",
desc="Just got your new car? How to drive the first 1,000 km, what to check in week one, and the habits that set your car up for years of reliable use.",
answer="For the first 1,000 km, drive gently: vary your speed, avoid full-throttle starts and sustained high RPM, don't tow or overload, and avoid hard braking when you can. Check your owner's manual for the exact break-in guidance for your unit, and watch for leaks or warning lights in the first weeks.",
faq=[("Do modern cars still need a break-in period?","Many manufacturers still give break-in guidance for the first part of the car's life. Follow what your owner's manual says for your unit."),
("Can I drive on the expressway during the first 1,000 km?","Yes, but vary your speed rather than holding one constant speed for long periods, and avoid full-throttle acceleration."),
("Can I go on a long road trip with a brand-new car?","You can, if you follow the break-in guidance: moderate speeds that vary, regular stops and no overloading."),
("What should I check in the first week?","Tire pressure, fluid levels, any leaks under the car, warning lights, and that all the accessories and freebies on your release list are there.")],
body='''<p>Congrats sa bagong sasakyan! The first weeks are exciting, and it's tempting to test everything at once. But how you drive the first 1,000 km can set the tone for years. Here's a simple guide.</p>

<h2>Why the first 1,000 km matters</h2>
<p>During the early kilometers, engine, transmission, brakes and tires are still settling in. Gentle, varied driving helps parts wear in evenly. Your <b>owner's manual has the exact break-in guidance</b> for your unit, so read that section on release day.</p>

<h2>The do's</h2>
<ul class="ticks">
<li>Vary your speed and engine RPM, especially on long drives</li>
<li>Accelerate smoothly and gradually</li>
<li>Let the car warm up briefly and drive gently for the first few minutes</li>
<li>Brake gently when traffic allows, so new pads and discs bed in</li>
<li>Check tire pressure when cold</li>
</ul>

<h2>The don'ts</h2>
<ul class="ticks">
<li>No full-throttle starts or "testing the top speed"</li>
<li>Avoid holding one constant speed for very long periods</li>
<li>Don't tow or carry very heavy loads</li>
<li>Don't rev a cold engine</li>
<li>Avoid hard, sudden braking unless it's an emergency</li>
</ul>

<h2>Week-one owner checklist</h2>
<ol class="steps">
<li><h3>Read the manual</h3><p>Break-in section, PMS schedule, and what each warning light means.</p></li>
<li><h3>Look under the car</h3><p>After parking overnight, check the floor for any drips.</p></li>
<li><h3>Check the freebies</h3><p>Compare what's in the car against your release list: tint, mats, early warning device, tools.</p></li>
<li><h3>Save the numbers</h3><p>Service center, your insurer's claims hotline, and your sales executive.</p></li>
<li><h3>Mark your first PMS</h3><p>Put the first service in your calendar. See my <a href="/tips/pms-schedule-guide/">PMS schedule guide</a>.</p></li>
</ol>

<h2>After 1,000 km</h2>
<p>Once you're past the break-in period, keep up with PMS, check tire pressure monthly and drive the way you'd want to be driven. Your car and your passengers will thank you. If you're still choosing your new car, my <a href="/tips/first-time-car-buyer-checklist/">first-time car buyer checklist</a> is a good start.</p>
'''+CTA2("Still choosing your new car? Check what fits your budget, then book a test drive in San Jose del Monte.","destinator")),

dict(base="tips",car="xpander-cross",slug="car-insurance-explained-philippines",date="2026-10-22",by=BY,img="xc_x3n",alt="Mitsubishi Xpander Cross insured under an all-in package",
title="Car Insurance Explained: CTPL vs Comprehensive",
desc="CTPL, comprehensive, acts of nature and participation fees explained in plain English, plus what the all-in package covers and how to file a claim.",
answer="CTPL (compulsory third-party liability) is required for LTO registration and covers injury or death of third parties. Comprehensive insurance covers your own car against accidents, theft and more, plus extra third-party coverage. Acts of nature (flood, typhoon) is often an add-on. The all-in package includes TPL and 1-year comprehensive with the rate locked for 3 years.",
faq=[("Is comprehensive insurance required in the Philippines?","CTPL is required for registration. Comprehensive isn't legally required, but banks typically require it while the car is financed."),
("Does comprehensive insurance cover floods?","Not always. Flood and typhoon damage usually falls under acts of nature (AON), which is often an add-on. Check your policy."),
("What is a participation fee?","It's the amount you shoulder per claim before the insurer pays the rest, similar to a deductible. The amount is stated in your policy."),
("What does 'rate locked for 3 years' mean?","In the all-in package, the 1-year comprehensive insurance rate is locked for 3 years, so your renewal premiums for that period follow the locked rate. Ask me for the details of your unit's package.")],
body='''<p>"Insured naman 'yan, di ba?" Many owners only learn what their insurance covers on the day they need to claim. Let's fix that now, in plain English.</p>

<h2>CTPL: the one the law requires</h2>
<p><b>Compulsory Third-Party Liability (CTPL)</b> is required to register your vehicle with the LTO. It covers <b>death or bodily injury to third parties</b> caused by your vehicle. It does <b>not</b> cover damage to your own car or to other people's property.</p>

<h2>Comprehensive: protection for your own car</h2>
<p>Comprehensive insurance (often called "comprehensive" or "own damage and theft") typically covers:</p>
<ul class="ticks">
<li><b>Own damage</b>: repairs to your car after a collision or accident</li>
<li><b>Theft</b>: loss of the car, and in some policies, parts</li>
<li><b>Third-party property damage</b>: damage you cause to other cars or property</li>
<li><b>Excess bodily injury</b>: third-party injury coverage beyond CTPL</li>
<li><b>Auto personal accident</b>: for you and your passengers, depending on the policy</li>
</ul>
<p>Banks typically require comprehensive insurance while your car is financed.</p>

<h2>Acts of nature: read this before bagyo season</h2>
<p>Flood, typhoon and earthquake damage usually fall under <b>acts of nature (AON)</b>, which is often an add-on and not automatic. If you live in a flood-prone area, ask your insurer if your policy has AON. More on weather prep in my <a href="/tips/el-nino-typhoon-car-care-tips/">El Niño and typhoon car care tips</a>.</p>

<h2>What the all-in package includes</h2>
<ul class="ticks">
<li>TPL insurance</li>
<li>1-year comprehensive insurance, with the rate locked for 3 years</li>
<li>LTO registration, chattel mortgage, free labor up to 5,000 km and a 3-year warranty</li>
</ul>
<p>Ask me for the policy details of your exact unit. Here's the full <a href="/guides/what-all-in-includes/">all-in guide</a>.</p>

<h2>How to file a claim</h2>
<ol class="steps">
<li><h3>Stay safe and document</h3><p>Hazards on, early warning device out, then take photos of the scene, both cars and plate numbers.</p></li>
<li><h3>Get a police or incident report</h3><p>Most insurers ask for one, especially for third-party claims.</p></li>
<li><h3>Call your insurer right away</h3><p>Save their claims hotline in your phone on release day.</p></li>
<li><h3>Submit the documents</h3><p>Usually the claim form, OR/CR, driver's license, photos and report.</p></li>
<li><h3>Pay the participation fee</h3><p>The amount per claim is stated in your policy; the insurer covers the rest of the approved repair.</p></li>
</ol>
'''+CTA2("Want a unit with insurance already in the all-in package? Check your budget, then book a test drive in SJDM.","xpander-cross")),
]
BULK2=[
dict(base="tips",car="xpander",slug="child-car-seat-law-philippines",date="2026-10-22",by=BY,img="xpgls_w81",alt="Mitsubishi Xpander family MPV with room for child car seats",
title="Child Car Seat Law (RA 11229): Parent Guide",
desc="RA 11229 in plain English: who needs a car seat, the 150 cm rule, why kids 12 and below ride in the back, and how to choose and install a seat.",
answer="Under RA 11229, the Child Safety in Motor Vehicles Act, children 12 and below must ride in an appropriate, approved child restraint system unless they are at least 150 cm (59 inches) tall and can use the regular seat belt. Children 12 and below can't sit in the front seat unless they meet that height and are belted, and a child must never be left alone in a vehicle.",
faq=[("Who needs a car seat in the Philippines?","Children 12 years old and below who are shorter than 150 cm (59 inches). Once a child reaches 150 cm, they can use the regular seat belt."),
("Can my child sit in the front seat?","Not if they're 12 or below, unless they're at least 150 cm tall and properly secured with the regular seat belt."),
("What kind of car seat is allowed?","One appropriate to your child's age, height and weight, and compliant with the standards set by the DTI, including recognized UN regulations. Look for the approval markings on the seat."),
("Are there exceptions?","The law lists cases where a car seat would put the child in greater danger, such as medical emergencies or a child's medical or developmental condition, plus others in the implementing rules.")],
body='''<p>Sa Pilipinas, kandong is love, pero sa sasakyan, it's risky. In a sudden stop, even a careful parent can't hold a child in place. That's why the <b>Child Safety in Motor Vehicles Act (RA 11229)</b> exists. Here's what it means for your family car.</p>

<h2>The rule in one sentence</h2>
<p>Children <b>12 years old and below</b> must be secured in an appropriate child restraint system (car seat) whenever the engine is running or the car is on the road, <b>unless they are at least 150 cm (59 inches) tall</b> and properly secured with the regular seat belt.</p>

<h2>Back seat for 12 and below</h2>
<p>No child 12 and below may sit in the front seat unless they meet the 150 cm height requirement and are properly belted. The LTO also notes that car seats should be mounted in a rear seat.</p>
<ul class="ticks">
<li>Shorter than 150 cm: car seat, in the back</li>
<li>150 cm or taller: regular seat belt; front seat allowed if properly belted</li>
<li>Never leave a child alone in the car, even if they're buckled in</li>
</ul>

<h2>Choosing the right seat</h2>
<p>The law requires a seat that fits your child's <b>age, height and weight</b> and that complies with the DTI standard and recognized UN regulations. In practice, seats come in stages:</p>
<ol class="steps">
<li><h3>Rear-facing infant seat</h3><p>For babies. Rear-facing protects the head and neck best.</p></li>
<li><h3>Forward-facing seat with harness</h3><p>For toddlers who have outgrown the rear-facing limits of their seat.</p></li>
<li><h3>Booster seat</h3><p>For older kids, so the adult seat belt crosses the shoulder and hips correctly.</p></li>
<li><h3>Regular seat belt</h3><p>Once your child is at least 150 cm tall.</p></li>
</ol>
<p>Follow the height and weight limits printed on the seat itself, and keep the manual.</p>

<h2>Installation checklist</h2>
<ul class="ticks">
<li>Read both the car seat manual and your car's owner's manual</li>
<li>Use the car's ISOFIX/anchor points if your seat and car support them, or the seat belt routing in the seat manual</li>
<li>The seat shouldn't move more than a little side to side at the belt path</li>
<li>Harness straps snug, chest clip at armpit level</li>
<li>No thick jackets under the harness</li>
<li>Ask me to show you the anchor points on release day</li>
</ul>

<h2>Family cars with room for car seats</h2>
<p>If you'll carry two or more car seats plus lolo and lola, a 7-seater gives you flexibility. The <a href="/cars/xpander/">Xpander</a> and <a href="/cars/destinator/">Destinator</a> both seat seven. Bring your car seat to the test drive and try it in the second row. My <a href="/blog/xpander-vs-destinator-family-car/">Xpander vs Destinator</a> comparison helps you choose.</p>
'''+SRC(("Lawphil: Republic Act No. 11229","https://lawphil.net/statutes/repacts/ra2019/ra_11229_2019.html"),("Philippine News Agency: Child car seat enforcement to start with education, LTO","https://www.pna.gov.ph/articles/1129213"),("WHO Philippines: Child restraint law","https://www.who.int/philippines/news/detail/13-03-2019-child-restraint-law-will-save-children-s-lives-on-philippine-roads"))+CTA2("Bring your car seat and test it in our 7-seaters. Check your budget first, then book a test drive in SJDM.","xpander")),

dict(base="tips",car="mirage-g4",slug="new-driver-tips-philippines",date="2026-10-22",by=BY,img="mg4glx_a66",alt="Mitsubishi Mirage G4, an easy car for new drivers",
title="New Driver Tips: Your First Months Behind the Wheel",
desc="Bagong lisensya? Practical tips for new drivers in the Philippines: first drives, parking, expressways, rain, night driving and what to keep in the car.",
answer="Start with short, familiar routes at off-peak hours, keep a safe following distance, master parking before rush hour, and add expressway, night and rain driving one at a time. Always carry your license, OR/CR and early warning device, and never drive tired or after drinking.",
faq=[("Should a new driver get a manual or automatic?","An automatic or CVT is easier while you learn traffic, especially in stop-and-go roads. A manual can lower the monthly if you're confident with a clutch."),
("What should I always have in the car?","Your driver's license (or e-license), OR/CR, early warning device, a basic tool kit, a powerbank and your insurer's hotline."),
("When can a new driver use the expressway?","Once you're comfortable with lane changes, merging and steady speeds in normal traffic. Start with a short stretch at an off-peak time with an experienced driver along."),
("Is it okay to drive after one or two drinks?","Don't. The Anti-Drunk and Drugged Driving Act penalizes driving under the influence. Arrange a designated driver or a ride.")],
body='''<p>May lisensya ka na, congrats! The license says you can drive. Experience is what makes you confident. Here's a step-by-step plan for your first months, based on what I see from first-time owners every week.</p>

<h2>Step up gradually</h2>
<ol class="steps">
<li><h3>Weeks 1–2: familiar, quiet routes</h3><p>Your subdivision, the barangay roads, the grocery. Practice at off-peak hours with an experienced driver beside you.</p></li>
<li><h3>Weeks 3–4: busier roads</h3><p>Quirino Highway or your main road at mid-morning. Focus on lane discipline and signals.</p></li>
<li><h3>Month 2: expressway</h3><p>A short NLEX stretch at off-peak. Practice merging and keeping a steady speed.</p></li>
<li><h3>Month 3: night and rain</h3><p>Add one new condition at a time, never both on the same first try.</p></li>
</ol>

<h2>Habits that keep you safe</h2>
<ul class="ticks">
<li><b>Following distance</b>: keep at least a 3-second gap, more in rain</li>
<li><b>Mirrors every few seconds</b>, and check blind spots before changing lanes</li>
<li><b>Signal early</b>, not while you're already turning</li>
<li><b>Phone away</b>: set navigation before you move</li>
<li><b>Yield to pedestrians</b>: see the latest in my <a href="/tips/lto-rules-2026-car-owners/">LTO rules 2026</a> guide</li>
<li><b>No driving tired or after drinking</b>, ever</li>
</ul>

<h2>Parking without panic</h2>
<ul class="ticks">
<li>Practice in an empty parking lot first: forward, reverse and parallel</li>
<li>Go slow. Slow is smooth, smooth is fast</li>
<li>Use your mirrors and reverse camera, but turn your head too</li>
<li>Choose end spots at the mall while you're learning</li>
</ul>

<h2>Keep these in the car</h2>
<ul class="ticks">
<li>Driver's license or e-license, OR/CR</li>
<li>Early warning device and basic tools (usually part of new-car freebies)</li>
<li>Powerbank and charger</li>
<li>Your insurer's claims hotline and roadside assistance number</li>
<li>Payong, water and a small first-aid kit</li>
</ul>

<h2>Choosing a car as a new driver</h2>
<p>A compact, easy-to-park car with good visibility makes learning easier. The <a href="/cars/mirage-g4/">Mirage G4</a> is a common first car; message me for the latest promo. If your family needs more seats, the Xpander GLX AT gives you an automatic 7-seater from ₱23,877 a month at Zero DP (October 2026 promo, 60 months). Start with my <a href="/tips/first-time-car-buyer-checklist/">first-time car buyer checklist</a>.</p>
'''+CTA2("New driver and choosing your first car? Check what fits your budget, then book an unhurried test drive in SJDM.","mirage-g4")),

dict(base="tips",car="xpander",slug="sjdm-to-manila-commute-tips",date="2026-10-22",by=BY,img="xpglx_graphite",alt="Mitsubishi Xpander for the daily SJDM to Metro Manila commute",
title="SJDM to Manila Commute: Daily Driving Tips",
desc="Driving daily from San Jose del Monte to Metro Manila? Timing, route planning, number coding, RFID, fuel and comfort tips for the Bulacan commute.",
answer="For the daily SJDM to Metro Manila drive, leave before the peak, pick your main route (Quirino Highway toward Fairview and Commonwealth, or via NLEX) and keep a backup, check MMDA number coding for your plate, keep RFID loaded, and choose an automatic if you face stop-and-go traffic every day.",
faq=[("What's the best time to leave SJDM for Manila?","As early as you can before the morning peak. Traffic changes with school days, road works and weather, so check a live traffic app before leaving."),
("Does number coding apply if I'm from Bulacan?","MMDA's number coding applies to vehicles on covered Metro Manila roads, regardless of where the car is registered. Check MMDA's current scheme and exemptions."),
("Manual or automatic for the daily commute?","Automatic or CVT is much less tiring in stop-and-go traffic. If your budget prefers a manual, practice smooth clutch work and take breaks."),
("How do I cut fuel costs on a long commute?","Correct tire pressure, smooth driving, less idling, and keeping up with PMS. See my fuel-saving tips.")],
body='''<p>Taga-SJDM ka pero sa Maynila ang trabaho? You're one of many. The commute can be long, but a few habits make it more predictable, and a lot less stressful.</p>

<h2>Know your routes, and a backup</h2>
<p>Most SJDM drivers head down <b>Quirino Highway</b> toward Fairview and Commonwealth, or take <b>NLEX</b> depending on where in Metro Manila they work. Know both, because a single accident or road work can change everything.</p>
<ul class="ticks">
<li>Check a live traffic app before leaving and before major junctions</li>
<li>Save your main and backup routes in your navigation app</li>
<li>Watch for advisories on road works and rerouting from your LGU and the toll operator</li>
</ul>

<h2>Timing is everything</h2>
<ul class="ticks">
<li>Leaving even 15 to 30 minutes earlier can make a big difference before the peak</li>
<li>School days and paydays are usually heavier</li>
<li>Rainy days slow everyone down: leave earlier</li>
<li>If your work allows, shift your hours away from the peak</li>
</ul>

<h2>Number coding and RFID</h2>
<p>MMDA's number coding (UVVRP) applies on covered Metro Manila roads based on your plate's last digit, wherever your car is registered. Check the MMDA's current scheme, hours and exemptions, since they can change.</p>
<p>If you use NLEX or the skyways, keep your RFID loaded and the sticker in good condition. A failed read at the toll gate costs you time every single day.</p>

<h2>Make the car part of the solution</h2>
<ul class="ticks">
<li><b>Automatic or CVT</b>: much easier in daily stop-and-go</li>
<li><b>Fuel economy habits</b>: see my <a href="/tips/fuel-saving-tips-diesel-vs-gasoline/">fuel-saving tips</a></li>
<li><b>Carpooling</b>: a 7-seater can share costs with officemates or bring the kids to school on the way</li>
<li><b>Comfort</b>: good AC, a comfortable seat and phone charging make long drives easier</li>
</ul>
<p>For carpools and school runs, the Xpander GLX AT is a popular choice: an automatic 7-seater at ₱1,159,000 SRP, from ₱23,877 a month at Zero DP, with ₱60K fuel (October 2026 promo, 60 months).</p>

<h2>Stay fresh on long drives</h2>
<ul class="ticks">
<li>Sleep well. Puyat driving is dangerous driving</li>
<li>Keep water and a light snack in the car</li>
<li>Use podcasts or music, not your phone screen</li>
<li>Keep up with PMS so the car never adds to your stress. See my <a href="/tips/pms-schedule-guide/">PMS schedule guide</a></li>
</ul>
'''+SRC(("MMDA: Official website (number coding advisories)","https://mmda.gov.ph/"))+CTA2("Want an easier daily commute? Check what fits your budget, then test drive an automatic right here on Quirino Highway, SJDM.","xpander")),

dict(base="tips",car="destinator",slug="car-trade-in-tips",date="2026-10-22",by=BY,img="de_xd1",alt="Trading in an old car for a new Mitsubishi Destinator",
title="Car Trade-In Tips: Get a Fair Value for Your Old Car",
desc="Trading in your old car for a new one? How trade-in works, the documents you need, how to prepare the car, and how to compare offers fairly.",
answer="To get a fair trade-in value, prepare your documents (OR/CR, IDs and, if financed, the loan release), clean the car and fix small issues, bring service records, and know your car's market range before the appraisal. Compare the trade-in offer against selling it yourself, counting the time and hassle saved.",
faq=[("Can I trade in a car that still has a loan?","Often yes, but the remaining loan balance must be settled as part of the process. Ask your bank for the exact payoff amount first."),
("What documents do I need to trade in a car?","Usually the original OR/CR, valid IDs, and a deed of sale. If the car was financed, you'll need the release of chattel mortgage once the loan is paid."),
("Does a dealer trade-in pay less than selling privately?","Sometimes, but trade-in saves you time, safety risks and paperwork. Compare the net amount and the hassle before deciding."),
("Do service records really matter?","Yes. Complete PMS records show the car was maintained and help support the appraisal.")],
body='''<p>Panahon na para mag-upgrade? Your current car can help pay for the next one. Here's how to prepare so you get a fair value and a smooth process.</p>

<h2>How a trade-in works</h2>
<ol class="steps">
<li><h3>Appraisal</h3><p>Your car is inspected and given a value based on condition, mileage, model and market demand.</p></li>
<li><h3>Offer</h3><p>You receive an offer. Ask how it was computed.</p></li>
<li><h3>Paperwork</h3><p>Deed of sale, documents and, if there's a loan, settling the balance.</p></li>
<li><h3>Applied to your new car</h3><p>The agreed value can go toward your new car. Message me to check if a trade-in applies to your purchase and how it works with the current promo.</p></li>
</ol>

<h2>Prepare your documents</h2>
<ul class="ticks">
<li>Original OR/CR, with the registration up to date</li>
<li>Valid IDs of the registered owner</li>
<li>If financed: your bank's payoff amount, and later the release of chattel mortgage</li>
<li>Service and repair records</li>
<li>Spare key, owner's manual and accessories</li>
</ul>

<h2>Prepare the car</h2>
<ul class="ticks">
<li><b>Clean it inside and out</b>: first impressions affect appraisals</li>
<li><b>Fix the small things</b>: bulbs, wipers, minor warning lights</li>
<li><b>Don't over-invest</b>: big repairs rarely pay back in trade-in value</li>
<li><b>Be honest</b> about accidents or flood history. It always comes out in inspection</li>
</ul>

<h2>Know your car's value</h2>
<p>Before the appraisal, check listings of the same model, year, variant and mileage to get a realistic range. Remember that listing prices are asking prices, not selling prices.</p>

<h2>Trade-in vs selling it yourself</h2>
<ul class="ticks">
<li><b>Trade-in</b>: one transaction, less paperwork, no strangers test-driving your car</li>
<li><b>Selling privately</b>: possibly a higher price, but more time, haggling and risk</li>
<li>Compare the <b>net amount</b> and the time and hassle saved, not just the headline offer</li>
</ul>
<p>Thinking of upgrading to a 7-seat SUV? See <a href="/blog/destinator-glx-vs-gls-vs-gt/">Destinator GLX vs GLS vs GT</a>, and to keep your next car's value high, read my <a href="/tips/car-resale-value-tips/">resale value tips</a>.</p>
'''+CTA2("Planning to upgrade? Check what your next car's monthly could be, then book a test drive and message me about your trade-in.","destinator")),
dict(base="tips",car="montero-sport",slug="car-resale-value-tips",date="2026-10-22",by=BY,img="ms_white",alt="Well-kept Mitsubishi Montero Sport that holds its resale value",
title="Car Resale Value Tips: Protect Your Car's Worth",
desc="Want a better price when you sell or trade in later? 8 habits that protect resale value, from PMS records and color choice to flood and accident care.",
answer="Resale value is protected by habits: follow PMS at an authorized service center and keep the records, avoid floods and fix damage properly, keep the interior and paint clean, skip extreme modifications, and keep all documents, keys and accessories. Popular models, variants and colors also tend to sell more easily.",
faq=[("Does PMS at an authorized service center affect resale value?","Complete, documented service history gives buyers and appraisers confidence and supports a better price."),
("Do modifications increase resale value?","Usually not. Extreme modifications can narrow your buyers. Keep original parts if you modify, so you can restore the car."),
("Does car color affect resale value?","Common colors like white, silver and black are often easier to sell because more buyers want them, but demand varies by model."),
("Does flood damage affect resale value?","Yes, significantly. Avoid floods, and if the car is submerged, have it towed and inspected and keep the repair records.")],
body='''<p>The day you buy a car is also the day you start building its resale value. Hindi mo kailangang maging car expert. You just need a few consistent habits.</p>

<h2>8 habits that protect resale value</h2>
<ol class="steps">
<li><h3>Follow the PMS schedule</h3><p>At an authorized service center, on time. See my <a href="/tips/pms-schedule-guide/">PMS schedule guide</a>.</p></li>
<li><h3>Keep every service record</h3><p>A complete folder of receipts is one of the strongest selling points.</p></li>
<li><h3>Avoid floods</h3><p>Flood history hurts value badly. Follow my <a href="/tips/el-nino-typhoon-car-care-tips/">flood rules</a>.</p></li>
<li><h3>Repair damage properly</h3><p>Use proper body shops and insurance claims, and keep the paperwork.</p></li>
<li><h3>Protect paint and interior</h3><p>Regular washing, shade parking, seat covers and floor mats.</p></li>
<li><h3>Go easy on modifications</h3><p>Keep the original parts if you do modify.</p></li>
<li><h3>Keep mileage reasonable</h3><p>Not always possible, but well-documented mileage matters.</p></li>
<li><h3>Keep documents and extras complete</h3><p>OR/CR, spare key, manuals, tools and accessories.</p></li>
</ol>

<h2>Choices at purchase that help later</h2>
<ul class="ticks">
<li><b>Popular models and variants</b> tend to have more buyers</li>
<li><b>Common colors</b> like white, silver and black are often easier to sell</li>
<li><b>The right transmission</b>: automatics are in demand for city driving, manuals for work and budget buyers</li>
<li><b>Warranty and records</b>: the 3-year warranty in the all-in package plus your PMS records reassure the next buyer</li>
</ul>

<h2>What hurts resale value most</h2>
<ul class="ticks">
<li>Flood or major accident history</li>
<li>Missing service records</li>
<li>Smoke and pet odor inside the cabin</li>
<li>Extreme modifications</li>
<li>Incomplete documents or unsettled violations</li>
</ul>

<h2>When it's time to sell</h2>
<p>Clean it well, gather every record and accessory, and compare a trade-in with selling privately. My <a href="/tips/car-trade-in-tips/">car trade-in tips</a> walk you through the process.</p>
<p>Full-size SUVs like the <a href="/cars/montero-sport/">Montero Sport</a> are built for long service lives, and good care shows when you sell. See <a href="/blog/montero-sport-variants-explained/">Montero Sport variants explained</a>.</p>
'''+CTA2("Choosing a car you'll keep for years? Check your budget, then test drive in SJDM.","montero-sport")),

dict(base="tips",car="xpander-cross",slug="new-car-release-day-checklist",date="2026-10-22",by=BY,img="xc_green",alt="Mitsubishi Xpander Cross on release day",
title="New Car Release Day Checklist",
desc="Getting your new car soon? What to bring, how to inspect the unit, which documents to check, and what to ask before you drive home.",
answer="On release day, bring your valid IDs and any remaining payment or documents, inspect the car in good light (paint, glass, tires, interior, lights and features), check that the VIN and engine numbers match your documents, confirm the freebies and accessories, and ask for the owner's manual, warranty booklet and PMS schedule before driving home.",
faq=[("What should I bring on release day?","Valid IDs, any remaining payment or documents requested by your sales executive, and your driver's license if you'll drive home."),
("What do I check on the car itself?","Paint and body panels, glass, tires including the spare, lights, AC, infotainment, windows, locks, and that the mileage is low."),
("What documents should I receive?","Your insurance documents, registration documents or their status, the owner's manual and warranty booklet. Ask what to expect and when for plates and the CR."),
("Can I bring someone to help inspect?","Yes, it helps. Bring someone who can check while you listen to the walkaround.")],
body='''<p>Excited na sa release? Me too, it's my favorite part of the job. A calm, thorough check now saves you questions later. Here's the list I walk my clients through.</p>

<h2>Before you go</h2>
<ul class="ticks">
<li>Confirm the release schedule and the time with your sales executive</li>
<li>Bring valid IDs and any remaining payment or documents requested</li>
<li>Bring your driver's license if you'll drive home</li>
<li>Plan to arrive with daylight left, so you can inspect in good light</li>
<li>Bring a family member to help check</li>
</ul>

<h2>Exterior walkaround</h2>
<ul class="ticks">
<li>Paint and body panels: scratches, dents, uneven gaps</li>
<li>Glass and mirrors: chips or cracks</li>
<li>Tires: all four plus the spare, no damage</li>
<li>Lights: headlights, signals, brake lights, hazards</li>
</ul>

<h2>Interior and features</h2>
<ul class="ticks">
<li>Seats, upholstery and trim clean and undamaged</li>
<li>AC cold, front and rear where applicable</li>
<li>Windows, locks, mirrors and wipers working</li>
<li>Infotainment, phone pairing and reverse camera</li>
<li>Odometer shows low delivery mileage</li>
</ul>

<h2>Documents and inclusions</h2>
<ol class="steps">
<li><h3>Match the numbers</h3><p>The VIN and engine number on the car should match your documents.</p></li>
<li><h3>Insurance</h3><p>Check your TPL and comprehensive insurance details, and save the claims hotline.</p></li>
<li><h3>Registration</h3><p>Ask about the status of your LTO registration, CR and plates, and what to carry in the meantime. See <a href="/tips/lto-rules-2026-car-owners/">LTO rules 2026</a>.</p></li>
<li><h3>Freebies and accessories</h3><p>Check each item on your release list: tint, mats, early warning device, tools and others.</p></li>
<li><h3>Manuals and warranty</h3><p>Owner's manual, warranty booklet and PMS schedule.</p></li>
</ol>

<h2>Ask before you drive home</h2>
<ul class="ticks">
<li>When is my first PMS, and how do I book it?</li>
<li>What does the free labor up to 5,000 km cover?</li>
<li>Who do I call for warranty or roadside concerns?</li>
<li>How do I use the key features: lights, wipers, safety systems, phone pairing?</li>
</ul>
<p>Then drive gently. My <a href="/tips/first-1000-km-break-in-tips/">first 1,000 km tips</a> are your next read.</p>
'''+CTA2("Haven't picked your unit yet? Check what fits your budget, then book a test drive in San Jose del Monte.","xpander-cross")),

dict(base="tips",car="xpander",slug="christmas-holiday-driving-tips",date="2026-10-22",by=BY,img="xpgls_red",alt="Mitsubishi Xpander ready for Christmas holiday family trips",
title="Christmas Holiday Driving Tips for Families",
desc="Simbang Gabi, mall traffic, Noche Buena runs and probinsya trips: holiday driving tips for Filipino families, plus a no-drinking-and-driving reminder.",
answer="For Christmas driving, plan around mall and Simbang Gabi traffic, go early for errands, park in well-lit areas and never leave valuables in sight, do a BLOWBAGETS check before probinsya trips, and never drive after drinking at parties. Arrange a designated driver or a ride home.",
faq=[("When is holiday traffic usually worst?","Weekends and paydays in December, the days before Christmas Eve and New Year's Eve, and areas around malls and churches during Simbang Gabi."),
("How can I keep my car safe at crowded malls?","Park in well-lit, busy areas, lock the car, take valuables with you or keep them out of sight, and note where you parked."),
("Is it okay to drive after a few drinks at a Christmas party?","No. The Anti-Drunk and Drugged Driving Act (RA 10586) penalizes driving under the influence. Use a designated driver or book a ride."),
("What should I check before a long holiday trip?","Do a BLOWBAGETS check, load your RFID, plan stopovers, and pack water, medicines and an early warning device.")],
body='''<p>Pasko na naman! Between Simbang Gabi, Christmas parties, mall runs and uwian sa probinsya, December is the busiest driving month for many families. Here's how to enjoy it without the stress.</p>

<h2>Simbang Gabi and early-morning drives</h2>
<ul class="ticks">
<li>Leave earlier: church parking fills up fast</li>
<li>Watch for pedestrians, especially kids and seniors walking in the dark</li>
<li>Use headlights properly and keep your windshield clean</li>
<li>Don't drive puyat: switch drivers if you need to</li>
</ul>

<h2>Mall and errand runs</h2>
<ul class="ticks">
<li>Shop on weekday mornings if you can; weekends and paydays are heaviest</li>
<li>Make one list and combine errands into one trip</li>
<li>Park in well-lit, busy areas and note your parking slot</li>
<li>Keep bags in the trunk, never on the seat in plain sight</li>
<li>Be patient in parking lots. Fender benders spike in December</li>
</ul>

<h2>Christmas parties: plan your ride home</h2>
<p>If you'll drink, don't drive. The <b>Anti-Drunk and Drugged Driving Act (RA 10586)</b> penalizes driving under the influence, and no party is worth the risk.</p>
<ol class="steps">
<li><h3>Choose a designated driver</h3><p>Decide before you leave the house, not at the party.</p></li>
<li><h3>Or book a ride</h3><p>Leave the car parked safely and pick it up the next day.</p></li>
<li><h3>Host responsibly</h3><p>If you're the host, offer non-alcoholic drinks and help guests get home safely.</p></li>
</ol>

<h2>Probinsya trips for Pasko and Bagong Taon</h2>
<p>For long drives, use the same prep as Undas: BLOWBAGETS, RFID, off-peak departure and a packing list for kids and seniors. My <a href="/tips/undas-road-trip-checklist-2026/">road trip checklist</a> covers it step by step.</p>
<ul class="ticks">
<li>Check toll operator advisories for holiday traffic before leaving</li>
<li>Pack gifts so they don't block the rear view</li>
<li>Plan rest stops every couple of hours</li>
</ul>

<h2>Thinking of a new car for the holidays?</h2>
<p>If you're planning to use your 13th month toward a car, read my <a href="/blog/13th-month-pay-car-budget-plan/">13th month car budget plan</a> first. For a family 7-seater, the Xpander GLS AT is ₱1,259,000 SRP, from ₱25,937 a month at Zero DP or ₱22,695 with ₱148K DP, with ₱60K fuel (October 2026 promo, 60 months). For December promos, message me for the latest.</p>
'''+SRC(("Lawphil: Republic Act No. 10586, Anti-Drunk and Drugged Driving Act of 2013","https://lawphil.net/statutes/repacts/ra2013/ra_10586_2013.html"))+CTA2("Want a roomier car for the family's Christmas trips? Check your budget, then test drive in SJDM.","xpander")),

dict(base="blog",car="triton",slug="l300-vs-triton-for-negosyo",date="2026-10-22",by=BY,img="tr_glx",alt="Mitsubishi Triton pickup compared with the L300 truck for business",
title="L300 vs Triton: Which Workhorse for Your Negosyo?",
desc="Truck or pickup for your business? L300 Dual AC vs Triton GX AT compared: body, engine, use cases and October 2026 promo monthlies.",
answer="Choose the L300 if your business is mainly about moving cargo: it's a 2.2L turbo-diesel truck with a 5-speed manual and body options, and the Dual AC is ₱1,039,000 SRP, from ₱21,405 a month at Zero DP. Choose the Triton if you need a pickup that works on rough roads and doubles as a family vehicle: the Triton GX AT is ₱1,430,000 SRP, from ₱28,900 a month at Zero DP.",
faq=[("Which is cheaper, L300 or Triton?","In October 2026, the L300 Dual AC is ₱1,039,000 SRP (Zero DP ₱21,405 a month, or ₱123K DP at ₱18,789), while the Triton GX AT is ₱1,430,000 SRP (Zero DP ₱28,900, or ₱140K DP at ₱25,200)."),
("Which carries more cargo?","It depends on the variant and body. The L300 is designed around cargo with body options like dropside and aluminum van. Check the official spec of each exact unit."),
("Is the Triton automatic?","The Triton GX 2.4D 2WD is an automatic. The L300 uses a 5-speed manual."),
("Can I use the L300 for family trips?","The L300 is a work truck. If you need one vehicle for both work and family, the Triton double cab is usually the better fit.")],
body='''<p>"Sir, L300 o Triton para sa negosyo?" Both are Mitsubishi workhorses, but they do different jobs. The right one depends on what you carry, where you drive and who else rides with you.</p>

<h2>At a glance</h2>
'''+T(["","L300 Dual AC","Triton GX AT"],[
("Type","Commercial truck","Pickup"),
("Engine","2.2L 4N14 turbo-intercooled diesel","2.4L 4N16 intercooled turbo diesel"),
("Transmission","5-speed manual","Automatic"),
("Best at","Moving cargo every day","Work plus family, rough roads"),
("SRP","₱1,039,000","₱1,430,000")])+'''

<h2>October 2026 promos</h2>
'''+T(["Unit","Zero DP","Low DP","Fuel"],[
("L300 Dual AC","₱21,405/mo","₱123K DP: ₱18,789/mo","₱20K"),
("Triton GX AT","₱28,900/mo","₱140K DP: ₱25,200/mo","₱20K")])+PN+'''

<h2>Choose the L300 if…</h2>
<ul class="ticks">
<li>Your business is about volume: deliveries, sari-sari restocking, hardware, water refilling, catering</li>
<li>You want a body built for your cargo; the Cab &amp; Chassis variant lets you fit a dropside or aluminum van</li>
<li>A driver, not the owner, will do most of the daily driving</li>
<li>Lowest monthly is a priority</li>
</ul>
<p>More in my <a href="/blog/l300-negosyo-guide/">L300 negosyo guide</a>.</p>

<h2>Choose the Triton if…</h2>
<ul class="ticks">
<li>You need one vehicle for work on weekdays and family on weekends</li>
<li>Your routes include farm roads, sites or rough provincial roads (consider a 4WD variant)</li>
<li>You carry tools, materials and a crew rather than full truckloads</li>
<li>You want an automatic</li>
</ul>
<p>More in my <a href="/blog/triton-for-business-and-farm/">Triton for business and farm</a> guide.</p>

<h2>Run the numbers both ways</h2>
<ol class="steps">
<li><h3>List what you carry every week</h3><p>Volume, weight and how often. Your heaviest regular load decides a lot.</p></li>
<li><h3>Add up ownership costs</h3><p>Monthly, fuel, insurance, PMS, a driver's pay, tolls and parking.</p></li>
<li><h3>Check the income guide</h3><p>At 30–35% of gross income, the L300 Zero DP monthly fits about ₱61,200 to ₱71,400 a month, the Triton GX AT about ₱82,600 to ₱96,300. For business owners, banks look at business income and documents. See <a href="/guides/car-loan-requirements/">car loan requirements</a>.</p></li>
<li><h3>Test drive both</h3><p>Drive the routes you actually use, if possible.</p></li>
</ol>
'''+CTA2("Not sure yet? Check your budget, then test drive the L300 and Triton back-to-back in SJDM.","triton")),
]
BULK3=[
dict(base="tips",car="xpander-cross",slug="rainy-season-driving-tips",date="2026-10-22",by=BY,img="xc_orange",alt="Mitsubishi Xpander Cross ready for rainy-season roads",
title="Rainy Season Driving Tips: See, Slow, Space",
desc="How to drive safely in heavy rain: visibility, hydroplaning, braking distance, headlights, and a pre-rain car check for wipers, tires and lights.",
answer="In heavy rain, slow down, double your following distance, turn on your headlights (not hazards while moving), and avoid sudden steering or braking. If the car hydroplanes, ease off the gas and steer straight until the tires grip again. Before the rainy months, check wipers, tire tread and all lights.",
faq=[("Should I use hazard lights while driving in heavy rain?","Use your headlights while moving. Hazards are for when you're stopped or a hazard to others; using them while moving can confuse drivers about your signals."),
("What do I do if my car hydroplanes?","Don't brake hard or jerk the wheel. Ease off the accelerator, hold the steering straight, and let the tires regain grip."),
("How often should I replace wiper blades?","When they streak, skip or squeak. Many owners check them before the rainy season; heat can also harden the rubber."),
("How much following distance in rain?","At least double your dry-weather gap. A 3-second gap in dry weather becomes 6 seconds or more in heavy rain.")],
body='''<p>Biglang buhos ng ulan sa Quirino Highway o sa NLEX? Rain changes everything: you see less, you're seen less, and your tires grip less. Remember three words: <b>see, slow, space</b>.</p>

<h2>See and be seen</h2>
<ul class="ticks">
<li>Turn on your <b>headlights</b> when it rains, even in the daytime</li>
<li>Don't drive with hazards on while moving; your turn signals won't be visible</li>
<li>Use the AC and defogger to clear fogged glass quickly</li>
<li>Keep the windshield clean inside and out; a dirty inside glass glares at night</li>
</ul>

<h2>Slow down and stay smooth</h2>
<ul class="ticks">
<li>Lower your speed: wet roads need longer stopping distances</li>
<li>Avoid sudden braking, accelerating and steering</li>
<li>The first minutes of rain are often the slipperiest, as oil and dust lift off the road</li>
<li>Watch out for painted lane markings and steel plates, which get slippery</li>
</ul>

<h2>Give yourself space</h2>
<p>Double your following distance. If you keep 3 seconds behind the car ahead in dry weather, make it 6 or more in heavy rain. Stay out of the spray of trucks and buses where you can't see.</p>

<h2>If the car hydroplanes</h2>
<ol class="steps">
<li><h3>Don't panic or brake hard</h3><p>Sudden braking can make the skid worse.</p></li>
<li><h3>Ease off the gas</h3><p>Let the car slow down naturally.</p></li>
<li><h3>Steer straight</h3><p>Hold the wheel steady in the direction you want to go.</p></li>
<li><h3>Wait for grip</h3><p>Once you feel the tires bite again, continue slowly.</p></li>
</ol>

<h2>Pre-rain car check</h2>
<ul class="ticks">
<li>Wiper blades: no streaks or squeaks; washer fluid filled</li>
<li>Tire tread and pressure: worn tires hydroplane sooner. See my <a href="/tips/tire-care-tips-philippines/">tire care guide</a></li>
<li>All lights working, including brake lights</li>
<li>Brakes checked at PMS</li>
<li>Payong and a towel in the car</li>
</ul>
<p>When the rain turns into flooding, follow my <a href="/tips/el-nino-typhoon-car-care-tips/">flood rules and after-flood checklist</a>, and keep an <a href="/tips/car-emergency-kit-list/">emergency kit</a> in the trunk.</p>
'''+CTA2("Want more clearance for rainy days? Check your budget, then test drive the Xpander Cross or Destinator in SJDM.","xpander-cross")),

dict(base="tips",car="destinator",slug="tire-care-tips-philippines",date="2026-10-22",by=BY,img="de_u33",alt="Mitsubishi Destinator wheels and tires",
title="Tire Care Guide: Pressure, Tread and Rotation",
desc="Tires are the only part of your car touching the road. How to check pressure and tread, when to rotate, signs of damage, and when to replace.",
answer="Check tire pressure at least monthly when the tires are cold, using the pressure on the driver's door jamb. Check tread depth and look for cracks, bulges and uneven wear. Rotate tires as your owner's manual recommends, usually during PMS, and replace tires that are worn, damaged or aged.",
faq=[("Where do I find the right tire pressure?","On the sticker on the driver's door jamb and in your owner's manual. Don't use the maximum number printed on the tire sidewall."),
("When should I check tire pressure?","At least once a month and before long trips, when the tires are cold, such as in the morning before driving."),
("How do I know if my tires are worn out?","Most tires have tread wear indicators, small raised bars in the grooves. If the tread is level with them, it's time to replace."),
("Do tires expire even if they have tread?","Rubber ages over time, especially in heat. Check the manufacturing date on the sidewall and have older tires inspected.")],
body='''<p>Your tires are the only part of the car that touches the road, four palm-sized patches holding your family's safety. A few minutes a month keeps them doing their job.</p>

<h2>1. Pressure: check monthly, when cold</h2>
<ul class="ticks">
<li>Use the pressure on the <b>driver's door jamb sticker</b> or the owner's manual</li>
<li>Check when cold: morning, before driving far</li>
<li>Don't forget the spare</li>
<li>Under-inflation wastes fuel and wears the edges; over-inflation wears the center and reduces grip</li>
</ul>

<h2>2. Tread: grip in the rain</h2>
<p>Tread channels water away so the tire can grip. Worn tread is a big cause of hydroplaning. Look for the <b>tread wear indicators</b> in the grooves. When the tread is level with them, replace the tire.</p>

<h2>3. Look for damage</h2>
<ul class="ticks">
<li>Bulges or bubbles on the sidewall: replace, don't drive far</li>
<li>Cracks in the rubber, often from heat and age</li>
<li>Nails, screws or cuts</li>
<li>Uneven wear: may mean alignment or pressure problems</li>
</ul>

<h2>4. Rotate and align</h2>
<p>Rotating tires helps them wear evenly. Follow the interval in your owner's manual; it's commonly done during <a href="/tips/pms-schedule-guide/">PMS</a>. If the car pulls to one side or the steering wheel is off-center, have the alignment checked.</p>

<h2>5. When to replace</h2>
<ul class="ticks">
<li>Tread at the wear indicators</li>
<li>Sidewall bulges, deep cuts or cracks</li>
<li>Older tires, even with tread left: check the date code on the sidewall</li>
<li>Replace in pairs or sets as recommended, with the size listed for your car</li>
</ul>
<p>Good tires matter most in the wet. Read my <a href="/tips/rainy-season-driving-tips/">rainy season driving tips</a> next.</p>
'''+CTA2("Shopping for a new car with fresh tires and a 3-year warranty? Check your budget, then test drive in SJDM.","destinator")),

dict(base="tips",car="xpander",slug="car-aircon-not-cooling-tips",date="2026-10-22",by=BY,img="xpglx_x37",alt="Mitsubishi Xpander with a cool cabin for the family",
title="Car Aircon Care: Keep It Cold and Fresh",
desc="Weak or smelly car aircon? Why it happens, simple habits that keep it cold, when to replace the cabin filter, and warning signs to have checked.",
answer="Keep your car AC cold and fresh by replacing the cabin filter at PMS, parking in the shade, using recirculation once the cabin cools, running the fan a few minutes before switching off to dry the system, and having the AC checked if it's weak, noisy or smelly.",
faq=[("Why does my car aircon smell?","Moisture and dirt in the system and a clogged cabin filter can cause musty odors. Have the filter replaced and the system cleaned if needed."),
("Why is my AC not as cold as before?","A clogged filter, a dirty condenser, low refrigerant or a component issue. Have it checked at a service center."),
("Should I use recirculation mode?","Once the cabin has cooled, recirculation helps keep it cool and blocks outside fumes. Switch to fresh air occasionally to avoid stuffiness and fogging."),
("Does using the AC use more fuel?","It adds some engine load. Parking in shade and keeping the system clean help it work less.")],
body='''<p>Sa init ng Pilipinas, ang aircon ay hindi luho, kailangan. Here's how to keep yours cold and fresh, especially in the El Niño heat.</p>

<h2>Why AC gets weak or smelly</h2>
<ul class="ticks">
<li>A dirty or clogged <b>cabin filter</b> blocks airflow and traps odors</li>
<li>Moisture in the system can lead to a musty smell</li>
<li>A dusty condenser at the front of the car cools less efficiently</li>
<li>Low refrigerant or a worn part, which needs a technician</li>
</ul>

<h2>Daily habits that help</h2>
<ol class="steps">
<li><h3>Park in the shade</h3><p>Or use a sunshade. A cooler cabin means less work for the AC.</p></li>
<li><h3>Vent first</h3><p>Open the windows for a minute when the car is very hot, then close them and turn on the AC.</p></li>
<li><h3>Use recirculation smartly</h3><p>Once cool, recirculate; switch to fresh air now and then.</p></li>
<li><h3>Dry the system</h3><p>Before you arrive, turn off the AC compressor and let the fan run a few minutes to reduce moisture.</p></li>
</ol>

<h2>Maintenance</h2>
<ul class="ticks">
<li>Have the <b>cabin filter</b> checked and replaced at <a href="/tips/pms-schedule-guide/">PMS</a> as recommended</li>
<li>Ask for an AC cleaning if odor persists</li>
<li>Keep the cabin clean; food crumbs and wet mats add odor</li>
</ul>

<h2>Warning signs to have checked</h2>
<ul class="ticks">
<li>Air not cold, or only cold while moving</li>
<li>Unusual noise when the AC turns on</li>
<li>Water dripping inside the cabin</li>
<li>Persistent bad smell after a filter change</li>
</ul>
<p>Families who ride in the third row should check rear AC reach on a test drive. See my <a href="/blog/xpander-vs-destinator-family-car/">Xpander vs Destinator</a> comparison.</p>
'''+CTA2("Check the AC reach for every row on a test drive. See what fits your budget first, then book in SJDM.","xpander")),

dict(base="tips",car="mirage-g4",slug="dashcam-philippines-parking-guide",date="2026-10-22",by=BY,img="mg4gls_p19",alt="Mitsubishi Mirage G4 parked safely",
title="Dashcam and Parking Guide for Filipino Drivers",
desc="Why a dashcam helps, where to mount it, and smart parking habits for malls, streets and subdivisions, plus what to do after a parking-lot scrape.",
answer="A dashcam gives you a record if there's an accident or dispute. Mount it behind the rearview mirror so it doesn't block your view, use a reliable memory card and check it regularly. For parking, choose well-lit, busy spots, reverse in when it's safe, fold your mirrors, and never leave valuables in sight.",
faq=[("Where should I mount a dashcam?","Usually behind the rearview mirror, where it records the road without blocking your view. Keep wires tidy and away from airbags."),
("Does a dashcam need a special memory card?","Dashcams record continuously, so use a card rated for that and check or format it regularly as the dashcam manual advises."),
("Is it better to reverse into a parking slot?","Often yes, when it's safe and allowed. Driving out forward gives better visibility when leaving."),
("What do I do if my parked car gets scraped?","Take photos, check for a note, ask the guard or building management for CCTV, file a report if needed, and contact your insurer.")],
body='''<p>Dashcams used to be for enthusiasts. Today, many Filipino drivers see them as basic protection. Combine one with smart parking habits and you avoid a lot of stress.</p>

<h2>Why a dashcam helps</h2>
<ul class="ticks">
<li>A record of what happened in an accident or road dispute</li>
<li>Helpful for insurance claims and police reports</li>
<li>Footage of hit-and-run or scrapes, with parking mode on some models</li>
<li>Peace of mind for family members driving your car</li>
</ul>

<h2>Choosing and installing</h2>
<ol class="steps">
<li><h3>Clear video, day and night</h3><p>Choose a model with good low-light recording and readable plate numbers.</p></li>
<li><h3>Mount behind the mirror</h3><p>So it doesn't block your view.</p></li>
<li><h3>Tidy, safe wiring</h3><p>Keep cables away from airbags and pedals. Have it installed properly.</p></li>
<li><h3>Right memory card</h3><p>Use a card made for continuous recording and check it monthly.</p></li>
</ol>

<h2>Smart parking habits</h2>
<ul class="ticks">
<li>Choose well-lit, busy areas near guards or CCTV</li>
<li>Reverse in when it's safe, for an easier, safer exit</li>
<li>Fold your side mirrors in tight spaces</li>
<li>Park away from carts and door-swing zones when you can</li>
<li>Bags in the trunk, not on the seat; take valuables with you</li>
<li>Note your slot or take a photo of the pillar sign</li>
</ul>

<h2>Street and subdivision parking</h2>
<p>Many LGUs and subdivisions have rules against street parking. Settle where your car will sleep before you buy, as I mention in the <a href="/tips/first-time-car-buyer-checklist/">first-time buyer checklist</a>.</p>

<h2>After a parking-lot scrape</h2>
<ol class="steps">
<li><h3>Take photos</h3><p>The damage, the area and nearby cars.</p></li>
<li><h3>Ask for CCTV</h3><p>Talk to the guard or building management right away.</p></li>
<li><h3>Report and claim</h3><p>File a report if needed and call your insurer. See <a href="/tips/car-insurance-explained-philippines/">car insurance explained</a>.</p></li>
</ol>
<p>New cars come with a reverse camera among the freebies, which helps with tight parking.</p>
'''+CTA2("Looking for an easy-to-park car with a reverse camera freebie? Check your budget, then test drive in SJDM.","mirage-g4")),

dict(base="tips",car="montero-sport",slug="car-emergency-kit-list",date="2026-10-22",by=BY,img="ms_black",alt="Mitsubishi Montero Sport with an emergency kit in the trunk",
title="Car Emergency Kit Checklist (Philippines)",
desc="What to keep in your car for breakdowns, floods, long trips and medical needs: a complete emergency kit checklist for Filipino families.",
answer="Every car should carry an early warning device, basic tools, a spare tire with jack and wrench, a flashlight, a powerbank, jumper cables or a tow strap, a first-aid kit, water, and your documents and emergency numbers. Add a raincoat, payong and snacks for typhoon season and long trips.",
faq=[("Is an early warning device required?","It's part of the standard freebies with a new car and essential for breakdowns. Set it up well behind your stopped vehicle."),
("What should a car first-aid kit have?","Bandages, gauze, antiseptic, tape, scissors, gloves, and any personal maintenance medicines for family members."),
("How often should I check my emergency kit?","Every few months and before long trips. Replace expired medicines, water and batteries."),
("What phone numbers should I save?","Your insurer's claims and roadside assistance lines, the expressway operator's hotline, your service center and a family contact.")],
body='''<p>Hindi natin hinihiling, pero mangyayari. Breakdowns, flat tires, floods and sudden illness happen when you least expect them. A packed emergency kit turns a crisis into an inconvenience.</p>

<h2>Breakdown basics</h2>
<ul class="ticks">
<li>Early warning device (EWD)</li>
<li>Spare tire, jack and lug wrench, checked for pressure</li>
<li>Basic tools</li>
<li>Jumper cables and a tow strap</li>
<li>Flashlight or headlamp with extra batteries</li>
<li>Reflective vest</li>
</ul>

<h2>Power and communication</h2>
<ul class="ticks">
<li>Powerbank and car charger</li>
<li>Saved numbers: insurer, roadside assistance, expressway hotline, service center, family</li>
<li>Small amount of cash</li>
</ul>

<h2>First aid and personal needs</h2>
<ul class="ticks">
<li>First-aid kit: bandages, gauze, antiseptic, tape, scissors, gloves</li>
<li>Maintenance medicines for seniors in the family</li>
<li>Drinking water and non-perishable snacks</li>
<li>Wet wipes, tissue, alcohol</li>
</ul>

<h2>Bagyo and long-trip add-ons</h2>
<ul class="ticks">
<li>Raincoat and payong</li>
<li>Towel and a change of clothes</li>
<li>Plastic bags for wet items</li>
<li>Blanket for kids and seniors</li>
</ul>

<h2>Documents</h2>
<ul class="ticks">
<li>Driver's license or e-license</li>
<li>OR/CR</li>
<li>Insurance policy details</li>
</ul>

<h2>Keep it ready</h2>
<ol class="steps">
<li><h3>Pack it in one bag or box</h3><p>So it's easy to find and doesn't roll around.</p></li>
<li><h3>Check every few months</h3><p>Replace expired medicines, water and batteries.</p></li>
<li><h3>Check before long trips</h3><p>Pair it with BLOWBAGETS in my <a href="/tips/undas-road-trip-checklist-2026/">road trip checklist</a>.</p></li>
</ol>
<p>New Mitsubishi units come with an early warning device and basic tools among the freebies.</p>
'''+CTA2("Ready for a car built for long drives? Check your budget, then test drive in SJDM.","montero-sport")),

dict(base="tips",car="xpander",slug="car-wash-at-home-guide",date="2026-10-22",by=BY,img="xpgls_u28",alt="Clean, freshly washed Mitsubishi Xpander",
title="Car Wash and Detailing Guide at Home",
desc="How to wash your car without scratching the paint, clean the interior, protect it from sun and rain, and know when to get professional detailing.",
answer="Wash your car in the shade with car shampoo (not dish soap), use the two-bucket method and a microfiber mitt, rinse well and dry with a microfiber towel. Clean the interior regularly, protect paint from bird droppings and sap quickly, and consider professional detailing for deep cleaning or paint protection.",
faq=[("Can I wash my car with dish soap?","It's better to use car shampoo. Dish soap can strip protective wax and dry out rubber and trim."),
("How often should I wash my car?","Every week or two for most owners, and sooner after rain, mud or bird droppings."),
("Why wash in the shade?","Sun dries soap and water quickly, leaving spots and streaks."),
("Is professional detailing worth it?","For deep interior cleaning, paint correction or ceramic coating, a professional detailer has the tools and products. Ask what's included and how long it lasts.")],
body='''<p>A clean car isn't only about pogi points. Regular washing protects your paint, keeps the cabin healthy, and helps resale value. Here's how to do it right at home.</p>

<h2>What you need</h2>
<ul class="ticks">
<li>Two buckets: one with car shampoo, one with clean rinse water</li>
<li>Microfiber wash mitt and drying towels (a microfiber cloth comes with new-car freebies)</li>
<li>Separate brush or mitt for wheels</li>
<li>Glass cleaner and interior cleaner</li>
<li>Vacuum</li>
</ul>

<h2>Exterior wash, step by step</h2>
<ol class="steps">
<li><h3>Park in the shade</h3><p>Let the paint cool before washing.</p></li>
<li><h3>Rinse first</h3><p>Remove loose dirt and sand that could scratch.</p></li>
<li><h3>Wheels first</h3><p>Use a separate brush so brake dust doesn't touch the paint.</p></li>
<li><h3>Two-bucket wash, top to bottom</h3><p>Dip the mitt in shampoo, wash a panel, rinse the mitt in clean water, repeat.</p></li>
<li><h3>Rinse and dry</h3><p>Dry with a clean microfiber towel to avoid water spots.</p></li>
</ol>

<h2>Interior cleaning</h2>
<ul class="ticks">
<li>Remove mats, vacuum seats and floors</li>
<li>Wipe dashboard and touchpoints: steering wheel, shifter, handles</li>
<li>Clean glass inside to reduce night glare</li>
<li>Dry wet mats fully to avoid odor</li>
</ul>

<h2>Protect the paint</h2>
<ul class="ticks">
<li>Remove bird droppings and tree sap quickly; they can etch paint in the heat</li>
<li>Wax or sealant adds a layer of protection</li>
<li>Use a sunshade and park in the shade when possible</li>
<li>After a flood or muddy road, rinse the underside too</li>
</ul>

<h2>When to go professional</h2>
<p>For deep interior shampooing, swirl removal or ceramic coating, a professional detailer has the right tools. Ask exactly what's included and how long protection lasts. A well-kept car pays you back later; see my <a href="/tips/car-resale-value-tips/">resale value tips</a>.</p>
'''+CTA2("Ready for a brand-new car to keep shiny? Check your budget, then test drive in SJDM.","xpander")),

dict(base="tips",car="xpander",slug="road-trip-from-bulacan",date="2026-10-22",by=BY,img="xpglx_u33",alt="Mitsubishi Xpander packed for a family road trip from Bulacan",
title="Family Road Trips from Bulacan: Baguio, Zambales, Batangas",
desc="Planning a family road trip from SJDM or Bulacan? Typical expressway routes to Baguio, Zambales and Batangas, plus prep for mountain, beach and long drives.",
answer="From Bulacan, Baguio is usually reached via NLEX, SCTEX and TPLEX, then a mountain road up; Zambales via NLEX and SCTEX toward Subic; and Batangas via NLEX, Skyway, SLEX and STAR Tollway. Load your RFID for each operator, plan rest stops, and prepare the car for mountain climbs and beach sand.",
faq=[("What's the usual route from Bulacan to Baguio?","Many drivers take NLEX, then SCTEX and TPLEX, then a mountain road up to Baguio. Check traffic and road advisories before leaving."),
("How do I drive safely on mountain roads?","Use a lower gear going down instead of riding the brakes, don't overtake on blind curves, and keep to your lane."),
("What's the route to Batangas from Bulacan?","Commonly NLEX to the Skyway, then SLEX and STAR Tollway into Batangas. Routes depend on your exact destination."),
("Do I need different RFID for different expressways?","Different operators use different RFID systems, so check that you have and have loaded the ones your route needs.")],
body='''<p>Weekend na! Bulacan is a great starting point for road trips: north to the mountains, west to the beaches, or south to Batangas. Here's how to plan each, plus the prep that keeps the trip fun.</p>
<p class="muted">Routes below are typical; always check a live navigation app and toll operator advisories before leaving.</p>

<h2>Baguio: mountain drive</h2>
<ul class="ticks">
<li><b>Typical route</b>: NLEX, then SCTEX and TPLEX, then a mountain road up to Baguio</li>
<li><b>Going up</b>: steady throttle, don't tailgate on climbs</li>
<li><b>Going down</b>: use a lower gear (or the low range on an automatic) instead of riding the brakes</li>
<li>No overtaking on blind curves; watch for fog and rain</li>
<li>Bring jackets, it's cold up there</li>
</ul>

<h2>Zambales: beach drive</h2>
<ul class="ticks">
<li><b>Typical route</b>: NLEX, then SCTEX toward Subic, then the coastal road</li>
<li>Don't drive onto soft sand unless you know it's firm</li>
<li>Rinse the car, especially the underside, after salty air and sand</li>
<li>Pack shade, water and sunblock</li>
</ul>

<h2>Batangas: south trip</h2>
<ul class="ticks">
<li><b>Typical route</b>: NLEX to the Skyway, then SLEX and STAR Tollway</li>
<li>Crossing Metro Manila: time it outside peak hours</li>
<li>Check the RFID systems your route needs, and load them</li>
</ul>

<h2>Prep for any road trip</h2>
<ol class="steps">
<li><h3>BLOWBAGETS</h3><p>The 10-point check in my <a href="/tips/undas-road-trip-checklist-2026/">road trip checklist</a>.</p></li>
<li><h3>RFID loaded</h3><p>For every operator on your route.</p></li>
<li><h3>Rest every 2 hours</h3><p>Stretch, restroom, coffee. Switch drivers if you can.</p></li>
<li><h3>Emergency kit</h3><p>See my <a href="/tips/car-emergency-kit-list/">emergency kit checklist</a>.</p></li>
<li><h3>Kids and seniors</h3><p>Car seats for kids under 150 cm (<a href="/tips/child-car-seat-law-philippines/">RA 11229</a>), and easy-access seats for lolo and lola.</p></li>
</ol>

<h2>The right car for barkada and family trips</h2>
<p>Seven seats and cargo room make a big difference. The Xpander GLX AT (₱1,159,000 SRP) starts at ₱23,877 a month at Zero DP with ₱60K fuel. For more power on mountain climbs with a full car, the Destinator GLX's 1.5L turbo (163 PS, 250 Nm) starts at ₱28,615 a month at Zero DP. October 2026 promos, 60 months, all-in, subject to bank approval.</p>
'''+CTA2("Planning more family trips? Check which 7-seater fits your budget, then test drive in SJDM.","xpander")),
]
BULK4=[
dict(base="blog",car="xpander",slug="bank-vs-in-house-car-financing-philippines",date="2026-10-22",by=BY,img="xpglx_x37",alt="Mitsubishi Xpander financed through a bank car loan",
title="Bank vs In-House Car Financing: How to Compare",
desc="Bank financing or in-house financing? How they differ in requirements, approval and total cost, and the questions to ask before you sign.",
answer="Bank financing is the common route for brand-new cars and is subject to bank approval, with requirements and terms set by the bank. In-house or other non-bank financing may differ in requirements, speed and total cost. Compare the total amount you'll pay over the term, the inclusions, the requirements and the fees, not just the monthly.",
faq=[("Which is cheaper, bank or in-house financing?","It depends on the offer. Compare the total amount paid over the full term, including fees and inclusions, from each option."),
("Are this site's promos bank-financed?","Promo monthlies here are all-in packages subject to bank approval. Message me for details of the financing behind your chosen unit."),
("Is in-house financing easier to get approved?","Requirements can differ, but easier approval may come with different costs or terms. Read everything before signing."),
("What should I ask before signing any car loan?","Total amount payable, term, what's included, fees and charges, penalties for late payment, and early payoff rules.")],
body='''<p>"Bank o in-house?" Both are ways to finance a car, but they're not the same deal. Here's a fair way to compare, so you're choosing based on numbers, not pressure.</p>

<h2>How bank financing works</h2>
<ul class="ticks">
<li>A bank pays the dealer; you pay the bank monthly over the term</li>
<li>Approval depends on the bank's evaluation of your capacity, documents and credit history</li>
<li>The car is under a chattel mortgage until the loan is paid (included in the all-in package)</li>
<li>Banks typically require comprehensive insurance while financed</li>
</ul>
<p>More in my <a href="/guides/how-car-financing-works-philippines/">how car financing works</a> guide.</p>

<h2>What "in-house" usually means</h2>
<p>In-house or non-bank financing is offered by the seller or a financing company rather than a bank. Requirements, approval speed and total cost can differ from a bank loan. Every offer is different, so treat each one on its own terms.</p>

<h2>Compare these five things</h2>
<ol class="steps">
<li><h3>Total amount payable</h3><p>Monthly × number of months + down payment + fees. This is the real price.</p></li>
<li><h3>Inclusions</h3><p>Registration, insurance, chattel mortgage, warranty. See <a href="/guides/what-all-in-includes/">what all-in includes</a>.</p></li>
<li><h3>Requirements</h3><p>What documents and income proof each option needs.</p></li>
<li><h3>Fees and penalties</h3><p>Processing fees, late payment penalties, early payoff rules.</p></li>
<li><h3>Flexibility</h3><p>Term options and what happens if your situation changes.</p></li>
</ol>

<h2>A sample: what an all-in promo includes</h2>
<p>For example, the Xpander GLX AT this month is ₱23,877 a month at Zero DP for 60 months, all-in, with ₱60K fuel. The all-in package covers LTO registration, TPL insurance, 1-year comprehensive insurance with the rate locked for 3 years, chattel mortgage, free labor up to 5,000 km and a 3-year warranty. When comparing offers, check that the other one includes the same items, or add their cost. (October 2026 promo, subject to bank approval.)</p>

<h2>Red flags</h2>
<ul class="ticks">
<li>No written breakdown of the total cost</li>
<li>Pressure to sign the same day</li>
<li>Unclear who holds the car's documents</li>
<li>Fees that appear only at signing</li>
</ul>
<p>Not sure you'll be approved? Read <a href="/blog/car-loan-myths-philippines/">car loan myths</a> and prepare with the <a href="/guides/car-loan-requirements/">requirements list</a>.</p>
'''+CTA2("Want a clear, written all-in breakdown? Check your budget, then message me or book a test drive in SJDM.","xpander")),

dict(base="blog",car="montero-sport",slug="montero-sport-vs-destinator",date="2026-10-22",by=BY,img="ms_white",alt="Mitsubishi Montero Sport compared with the Destinator for families",
title="Montero Sport vs Destinator: Which SUV for Your Family?",
desc="Diesel ladder-frame Montero Sport or turbo-gas Destinator? Compare engines, use, variants and October 2026 promo monthlies for families.",
answer="Both seat seven. The Montero Sport is a ladder-frame SUV with a 2.4L turbo diesel (181 PS, 430 Nm), available in 4WD on the Black Series, built for long drives, heavy loads and rough roads. The Destinator has a 1.5L turbo gasoline engine (163 PS, 250 Nm), a CVT and 214 mm clearance, and a lower entry price. Destinator GLX starts at ₱1,389,000; Montero Sport GLX MT at ₱1,568,000.",
faq=[("Which is more powerful?","The Montero Sport has more torque: 430 Nm from its 2.4L diesel versus 250 Nm from the Destinator's 1.5L turbo. Power is 181 PS vs 163 PS."),
("Which one has 4WD?","The Montero Sport Black Series 4WD A/T. The Destinator is 2WD."),
("Which is cheaper per month?","The Destinator GLX from ₱26,827 a month with ₱93K DP, versus the Montero Sport GLX MT from ₱28,265 with ₱30K DP (October 2026, 60 months, all-in)."),
("Which is better for the city?","The Destinator's CVT and smaller turbo engine suit city traffic well. The Montero Sport GLS and Black Series have an 8-speed automatic for those who want the diesel.")],
body='''<p>Two 7-seat SUVs, two different personalities. The <a href="/cars/montero-sport/">Montero Sport</a> is the tough, long-distance diesel. The <a href="/cars/destinator/">Destinator</a> is the newer turbo-gas family SUV. Here's how to choose.</p>

<h2>Side by side</h2>
'''+T(["","Montero Sport","Destinator"],[
("Engine","2.4L 4N15 turbo diesel","1.5L 4B40 turbo gasoline"),
("Power / torque","181 PS / 430 Nm","163 PS / 250 Nm"),
("Transmission","6-speed MT or 8-speed AT","CVT"),
("Drivetrain","2WD; 4WD on Black Series 4WD","2WD"),
("Build","Ladder frame","SUV, 214 mm clearance"),
("Starting SRP","₱1,568,000","₱1,389,000")])+'''

<h2>Promo monthlies, October 2026</h2>
'''+T(["Variant","Zero DP","Low DP"],[
("Destinator GLX","₱28,615","₱93K DP: ₱26,827"),
("Destinator GLS","₱32,942","₱123K DP: ₱30,883"),
("Destinator GT","₱39,740","₱88K DP: ₱37,256"),
("Montero Sport GLX MT","₱30,284","₱30K DP: ₱28,265"),
("Montero Sport GLS AT","₱39,699","₱138K DP: ₱37,218"),
("Montero Black Series 2WD","—","₱88K DP: ₱45,117"),
("Montero Black Series 4WD","—","₱133K DP: ₱52,121")])+PN+'''

<h2>Choose the Montero Sport if…</h2>
<ul class="ticks">
<li>You drive long distances often, or tow and carry heavy loads</li>
<li>Your roads include rough or unpaved stretches; consider the Black Series 4WD</li>
<li>You want diesel torque for mountain drives with a full car</li>
</ul>
<p>Variant details in <a href="/blog/montero-sport-variants-explained/">Montero Sport variants explained</a>.</p>

<h2>Choose the Destinator if…</h2>
<ul class="ticks">
<li>Most driving is city and highway with occasional provincial trips</li>
<li>You want a lower entry price and monthly</li>
<li>You prefer an easy CVT for daily traffic</li>
</ul>
<p>Variant details in <a href="/blog/destinator-glx-vs-gls-vs-gt/">Destinator GLX vs GLS vs GT</a>.</p>

<h2>Test drive both with the family</h2>
<ul class="ticks">
<li>Third-row access and comfort</li>
<li>Cargo space with all seats up</li>
<li>Ride over bumps and steering feel</li>
<li>Ease of parking at your home and office</li>
</ul>
'''+CTA2("Drive the Montero Sport and Destinator back-to-back in SJDM after checking which fits your budget.","montero-sport")),

dict(base="blog",car="xpander-cross",slug="xpander-cross-2026-price-philippines",date="2026-10-22",by=BY,img="xc_x3n",alt="Mitsubishi Xpander Cross for provincial roads",
title="Xpander Cross for Provincial Roads and Probinsya Life",
desc="Is the Xpander Cross right for provincial roads and frequent uwian? What it shares with the Xpander, what it adds, and the October 2026 promo.",
answer="The Xpander Cross keeps the Xpander's seven seats and 1.5L MIVEC engine (105 PS, 141 Nm) with a 4-speed automatic, and adds a rugged crossover look and a more premium cabin. It suits families who split time between the city and the province. In October 2026: SRP ₱1,378,000, Zero DP ₱28,389 a month or ₱148K DP ₱24,840, with ₱60K fuel.",
faq=[("Is the Xpander Cross 4WD?","No. It's a 2WD crossover-styled MPV. For regular off-road use, look at a 4WD Triton or the Montero Sport Black Series 4WD."),
("Does the Xpander Cross have a bigger engine than the Xpander?","No. Both use the 1.5L MIVEC gasoline engine with 105 PS and 141 Nm."),
("How much is the Xpander Cross monthly?","₱28,389 at Zero DP or ₱24,840 with ₱148K DP, 60 months, all-in, with ₱60K fuel (October 2026, subject to bank approval)."),
("Is it good for rough provincial roads?","Like the Xpander, it has high ground clearance for rough patches and flooded streets. Drive carefully on unpaved roads and avoid deep water.")],
body='''<p>Weekdays sa Bulacan o Maynila, weekends sa probinsya? Many families live between two places. The <a href="/cars/xpander-cross/">Xpander Cross</a> is built for that life: an MPV's practicality with an SUV-style look.</p>

<h2>What it shares with the Xpander</h2>
<ul class="ticks">
<li>Seven seats for the whole family</li>
<li>1.5L MIVEC gasoline engine, 105 PS and 141 Nm</li>
<li>4-speed automatic</li>
<li>High ground clearance for rough patches and flooded streets</li>
</ul>

<h2>What the Cross adds</h2>
<ul class="ticks">
<li>A rugged crossover look with bolder bumpers and skid-plate styling</li>
<li>A more premium cabin</li>
<li>A two-tone finish</li>
</ul>
<p>Ask me for the official spec sheet to compare it with the Xpander GLS. My <a href="/blog/xpander-variants-explained/">Xpander variants explained</a> post has all four side by side.</p>

<h2>The October 2026 promo</h2>
'''+T(["Xpander Cross 1.5G 2WD A/T","Monthly (60 months)"],[("Zero DP","₱28,389"),("₱148K DP","₱24,840")])+'''
<p>SRP ₱1,378,000, all-in, with ₱60K fuel. At 30–35% of gross income, the Zero DP monthly fits roughly ₱81,100 to ₱94,600 a month.</p>
'''+PN+'''

<h2>Provincial road tips</h2>
<ol class="steps">
<li><h3>Slow down on unpaved stretches</h3><p>Potholes and loose gravel hide under puddles.</p></li>
<li><h3>Mind the clearance, not just the look</h3><p>It's still a 2WD MPV. Avoid deep water and very rough trails.</p></li>
<li><h3>Watch for animals and tricycles</h3><p>Especially at night on barangay roads.</p></li>
<li><h3>Rinse after muddy trips</h3><p>Including the underside.</p></li>
</ol>
<p>For more power on mountain climbs, compare with the Destinator in <a href="/guides/xpander-vs-xpander-cross-vs-destinator/">Xpander vs Xpander Cross vs Destinator</a>.</p>
'''+CTA2("Check if the Xpander Cross fits your budget, then test drive it on Quirino Highway in SJDM.","xpander-cross")),

dict(base="blog",car="triton",slug="triton-gx-2wd-at-first-pickup-guide",date="2026-10-22",by=BY,img="tr_gx_u28",alt="Mitsubishi Triton GX automatic pickup",
title="Triton GX AT: A Guide for First-Time Pickup Owners",
desc="Buying your first pickup? What's different from a sedan or MPV, how to drive and park a pickup, cargo bed basics, and the Triton GX AT October 2026 promo.",
answer="A pickup is longer, sits higher and rides firmer when empty than a sedan or MPV, so give yourself time to learn its size, turning and parking. The Triton GX 2.4D 2WD A/T is an automatic, which makes the switch easier. In October 2026: SRP ₱1,430,000, Zero DP ₱28,900 a month or ₱140K DP ₱25,200, with ₱20K fuel.",
faq=[("Is a pickup hard to drive?","Not with an automatic and some practice. The main adjustment is its length and turning circle in tight streets and parking."),
("Why does a pickup ride firmer when empty?","Its rear suspension is built to carry loads, so it can feel firmer with an empty bed."),
("Can a pickup be a family car?","The Triton is a double cab with a rear seat, so it can carry the family. Try the rear seat during the test drive."),
("Is the Triton GX automatic?","Yes, the Triton GX 2.4D 2WD A/T is an automatic with the 2.4L turbo diesel.")],
body='''<p>Unang pickup mo? Congrats, it's one of the most useful vehicles you can own. But it drives differently from a sedan or MPV. Here's what to expect with the <a href="/cars/triton/">Triton GX AT</a>.</p>

<h2>What's different about a pickup</h2>
<ul class="ticks">
<li><b>Longer body</b>: give more room when turning and parking</li>
<li><b>Higher seating</b>: better view ahead, but check blind spots and the area close to the bumpers</li>
<li><b>Firmer ride when empty</b>: the rear is built to carry loads</li>
<li><b>Diesel torque</b>: strong pulling power for loads and climbs</li>
</ul>

<h2>Why the GX AT suits first-timers</h2>
<ul class="ticks">
<li>Automatic: one less thing to learn in traffic</li>
<li>2.4L 4N16 intercooled turbo diesel</li>
<li>2WD, which suits paved and provincial roads</li>
<li>Double cab with rear seat for family use</li>
</ul>

<h2>The October 2026 promo</h2>
'''+T(["Triton GX 2.4D 2WD A/T","Monthly (60 months)"],[("Zero DP","₱28,900"),("₱140K DP","₱25,200")])+'''
<p>SRP ₱1,430,000, all-in, with ₱20K fuel. At 30–35% of gross income, the Zero DP monthly fits roughly ₱82,600 to ₱96,300 a month.</p>
'''+PN+'''

<h2>Driving and parking tips</h2>
<ol class="steps">
<li><h3>Practice in an open lot</h3><p>Learn the turning circle and where the corners are.</p></li>
<li><h3>Take wider turns</h3><p>Watch the rear wheels in tight corners.</p></li>
<li><h3>Use mirrors and the reverse camera</h3><p>A reverse camera is among the new-car freebies; still turn your head.</p></li>
<li><h3>Check height limits</h3><p>Some parking buildings have low clearance.</p></li>
</ol>

<h2>Cargo bed basics</h2>
<ul class="ticks">
<li>Stay within the rated payload for your variant</li>
<li>Tie down loads with straps or a net</li>
<li>Cover rain-sensitive cargo with a tarpaulin</li>
<li>Don't let passengers ride in the bed</li>
</ul>
<p>Using it for business? Read <a href="/blog/triton-for-business-and-farm/">Triton for business and farm</a> and <a href="/blog/l300-vs-triton-for-negosyo/">L300 vs Triton</a>.</p>
'''+CTA2("Try the Triton GX AT yourself. Check your budget, then book a test drive in SJDM.","triton")),

dict(base="blog",car="mirage-g4",slug="minimum-salary-for-car-loan-philippines",date="2026-10-22",by=BY,img="mg4glx_u17",alt="Mitsubishi Mirage G4 for young professionals",
title="Car Budget Plan for Young Professionals",
desc="First job, first car? A simple budget plan for young professionals: income guide, emergency fund first, ownership costs, and choosing the right unit.",
answer="Build an emergency fund first, then keep your car monthly at about 30 to 35 percent of gross income, and budget separately for fuel, parking, tolls, PMS and insurance renewal. Start with a unit that fits comfortably rather than the dream car, and consider a co-borrower or larger down payment if needed.",
faq=[("How much salary do I need to buy a car?","Use the 30–35% guide. For example, the Xpander GLX MT at ₱22,641 a month (Zero DP, October 2026) fits a gross income of roughly ₱64,700 to ₱75,500. Banks make the final assessment."),
("Should I save an emergency fund before buying a car?","Yes. A few months of expenses saved protects you if income stops, so the car never becomes a burden."),
("Is it better to buy a car or keep commuting?","Compare the full monthly cost of owning (amortization plus running costs) with your current commuting costs and the time you'd save."),
("Can I apply if I'm newly employed?","Banks usually look at length of employment. Ask me what your bank requires; a co-borrower can help.")],
body='''<p>Unang sahod, unang kotse? It's a big step, and done right, a car makes work and life easier. Done wrong, it eats your sahod every month. Here's a simple plan.</p>

<h2>Step 1: Emergency fund first</h2>
<p>Before buying, save a few months of expenses. Jobs change, emergencies happen, and the monthly doesn't wait.</p>

<h2>Step 2: Use the 30–35% guide</h2>
<p>Keep the amortization at about 30 to 35 percent of gross monthly income. Divide the monthly by 0.35 for the minimum income and by 0.30 for a comfortable one. Full table in <a href="/blog/how-much-car-can-i-afford-philippines/">How much car can I afford?</a></p>
'''+T(["Unit (Zero DP, Oct 2026)","Monthly","Gross income"],[
("Xpander GLX MT","₱22,641","₱64,700 – ₱75,500"),
("Xpander GLX AT","₱23,877","₱68,200 – ₱79,600"),
("Xpander GLS AT","₱25,937","₱74,100 – ₱86,500")])+PN+'''
<p>For a compact sedan like the <a href="/cars/mirage-g4/">Mirage G4</a>, message me for the latest promo.</p>

<h2>Step 3: Budget the costs after the monthly</h2>
<ul class="ticks">
<li>Fuel: estimate weekly kilometers × pump price</li>
<li>Parking at home, at work, and where you go often</li>
<li>Tolls if you use expressways</li>
<li>PMS, tires and battery over time</li>
<li>Comprehensive insurance renewal after the locked period</li>
</ul>

<h2>Step 4: Pick the right car, not the dream car</h2>
<ul class="ticks">
<li>Start with what fits comfortably; you can upgrade later with a trade-in (see <a href="/tips/car-trade-in-tips/">trade-in tips</a>)</li>
<li>Manual can lower the monthly if you're comfortable with it</li>
<li>Think about who rides with you: barkada, family, carpool</li>
</ul>

<h2>Step 5: Strengthen your application</h2>
<ol class="steps">
<li><h3>Complete documents</h3><p>COE with compensation, payslips, IDs, proof of billing. See the <a href="/guides/car-loan-requirements/">requirements</a>.</p></li>
<li><h3>Keep credit clean</h3><p>Pay credit cards on time.</p></li>
<li><h3>Consider a co-borrower</h3><p>A parent or spouse, if the bank allows.</p></li>
<li><h3>Bigger down payment</h3><p>Lowers the monthly; see <a href="/guides/zero-dp-vs-low-dp/">Zero DP vs low DP</a>.</p></li>
</ol>
'''+CTA2("See which unit fits your first-job salary, then book a test drive in SJDM.","mirage-g4")),

dict(base="blog",car="xpander",slug="best-car-for-senior-citizens-philippines",date="2026-10-22",by=BY,img="xpgls_c31",alt="Mitsubishi Xpander with easy entry for senior passengers",
title="Choosing a Car for Seniors and PWD Family Members",
desc="Buying a car for lolo, lola or a family member with a disability? What to check: seat height, door opening, step-in, wheelchair space and driving aids.",
answer="For senior or PWD family members, look for a seat height that's easy to slide into, wide door openings, a low step-in, grab handles, cargo space for a wheelchair or walker, and an automatic transmission for easier driving. Test it with the actual person and their mobility aid before deciding.",
faq=[("Which is easier for seniors to get into, a sedan or an MPV?","Many seniors find a seat at hip height easier, like an MPV, because they slide in rather than step down or climb up. Test with the person."),
("Will a folding wheelchair fit?","It depends on the wheelchair and the car. Bring it to the test drive and try loading it with the seats in your usual setup."),
("Is an automatic better for older drivers?","Often yes. It reduces effort in traffic and lets the driver focus on the road."),
("Are there special discounts for senior or PWD car buyers?","I don't want to promise one. Message me for the latest promo and I'll tell you exactly what applies.")],
body='''<p>Kapag may lolo, lola o family member with a disability, comfort and access matter as much as price. The best car is the one they can get in and out of with dignity. Here's what to check.</p>

<h2>Getting in and out</h2>
<ul class="ticks">
<li><b>Seat height</b>: around hip height lets them slide in rather than climb or drop down</li>
<li><b>Door opening</b>: wide openings make it easier with a cane or walker</li>
<li><b>Step-in height</b>: a lower floor helps people with knee or hip pain</li>
<li><b>Grab handles</b>: check where they are for the front and second rows</li>
</ul>

<h2>Space for mobility aids</h2>
<ul class="ticks">
<li>Bring the actual wheelchair, walker or cane to the test drive</li>
<li>Try loading it with the seats in your usual setup</li>
<li>A 7-seater gives flexibility to fold seats when needed</li>
</ul>

<h2>For senior drivers</h2>
<ul class="ticks">
<li>Automatic transmission for less effort in traffic</li>
<li>Good visibility and easy-to-read instruments</li>
<li>Reverse camera for parking (part of the new-car freebies)</li>
<li>Comfortable seat adjustment and steering position</li>
</ul>

<h2>Test-drive checklist</h2>
<ol class="steps">
<li><h3>Bring the person</h3><p>Let them try getting in and out of each row.</p></li>
<li><h3>Bring the aid</h3><p>Load and unload it yourself.</p></li>
<li><h3>Ride, don't just sit</h3><p>Check ride comfort over bumps.</p></li>
<li><h3>Check the seatbelt reach</h3><p>Easy to buckle without twisting.</p></li>
</ol>

<h2>Units worth trying</h2>
<p>The <a href="/cars/xpander/">Xpander</a> is a common choice for families with seniors. The GLS AT is ₱1,259,000 SRP, from ₱25,937 a month at Zero DP or ₱22,695 with ₱148K DP, with ₱60K fuel. The <a href="/cars/destinator/">Destinator</a> GLX starts at ₱28,615 a month at Zero DP. October 2026 promos, 60 months, all-in, subject to bank approval. For any senior or PWD-specific offer, message me for the latest promo.</p>
'''+CTA2("Bring lolo, lola or your family member to try the seats. Check your budget, then book a test drive in SJDM.","xpander")),
]
ADDRP='<p><b>Mitsubishi SJ Legacy Motors</b><br>Lot 9 Ebenezer Christian Academy, Sitio Gitna, Sto. Cristo, Quirino Highway, San Jose del Monte, Bulacan</p>'
TOT='<p class="muted">Total of payments = down payment + 60 monthly amortizations, from the October 2026 promo figures. The all-in package (LTO registration, TPL, 1-year comprehensive with rate locked for 3 years, chattel mortgage, free labor up to 5,000 km, 3-year warranty) is included. Subject to bank approval.</p>'
BULK5=[
dict(base="blog",car="xpander",slug="mitsubishi-dealer-bulacan",date="2026-10-22",by=BY,img="xc_x3n",alt="Mitsubishi Xpander Cross at Mitsubishi SJ Legacy Motors, a Mitsubishi dealer in Bulacan",
title="Mitsubishi Dealer Bulacan: SJ Legacy Motors, SJDM",
desc="",answer="",
faq=[("Where is the Mitsubishi dealer in San Jose del Monte, Bulacan?","Mitsubishi SJ Legacy Motors is at Lot 9 Ebenezer Christian Academy, Sitio Gitna, Sto. Cristo, Quirino Highway, San Jose del Monte, Bulacan."),
("Can I test drive a Mitsubishi in SJDM?","Yes. Book online on the test drive page and Richard will confirm your schedule. Bring your valid driver's license."),
("How do I contact a Mitsubishi sales executive in SJDM?","Call or text Richard Cuagdan on 0954 291 1201, or send a message on Messenger."),
("Is SJ Legacy Motors near Metro Manila?","It's on Quirino Highway in San Jose del Monte, close to Caloocan, Quezon City, Norzagaray and Santa Maria.")],
body='''<p>Looking for a Mitsubishi dealer in Bulacan? Mitsubishi SJ Legacy Motors is an authorized Mitsubishi dealership on Quirino Highway in San Jose del Monte, close to Caloocan, Quezon City, Norzagaray and Santa Maria. I'm Richard Cuagdan, one of its car sales executives.</p>

<h2>Where to find us</h2>
'''+ADDRP+'''
<p>Call or text me on '''+TELL+''' before you visit so I can have your preferred unit ready. <a href="/contact/">Map and directions</a>.</p>

<h2>What you can do at the showroom</h2>
<ul class="ticks">
<li>See and compare the current lineup: Mirage G4, Xpander, Xpander Cross, Xforce, Destinator, Montero Sport, Triton, L300 and more (<a href="/cars/">all models</a>)</li>
<li>Take a test drive (<a href="/test-drive/">book here</a>)</li>
<li>Get the month's promo: Zero DP and low DP all-in options</li>
<li>Have your loan documents pre-checked before bank submission</li>
<li>Release of your new car, with a walkthrough of the unit</li>
</ul>

<h2>Popular units this month</h2>
'''+T(["Unit","SRP","Zero DP monthly"],[("Xpander GLX AT","₱1,159,000","₱23,877"),("Xpander GLS AT","₱1,259,000","₱25,937"),("Destinator GLX","₱1,389,000","₱28,615"),("Triton GX AT","₱1,430,000","₱28,900"),("L300 Dual AC","₱1,039,000","₱21,405")])+PN+'''

<h2>Who I help</h2>
<ul class="ticks">
<li><b>Employed buyers</b>: matching a monthly to your salary. See <a href="/blog/how-much-car-can-i-afford-philippines/">how much car can I afford</a></li>
<li><b>Business owners</b>: trucks and pickups for negosyo. See <a href="/blog/l300-vs-triton-for-negosyo/">L300 vs Triton</a></li>
<li><b>OFWs and their families</b>: applying from abroad. See the <a href="/blog/ofw-car-buying-guide/">OFW car loan guide</a></li>
</ul>

<h2>Before your visit</h2>
<ol class="steps">
<li><h3>Check your budget</h3><p>The <a href="/budgetcalculator/">Budget Fit Calculator</a> shows which units fit your income.</p></li>
<li><h3>Book a test drive</h3><p>Pick a unit and schedule online.</p></li>
<li><h3>Bring your license and IDs</h3><p>Plus income documents if you want them pre-checked. See <a href="/guides/car-loan-requirements/">requirements</a>.</p></li>
</ol>
'''+CTA2("Visit Mitsubishi SJ Legacy Motors in SJDM. Check your budget, book a test drive, or call me first.","xpander")),

dict(base="blog",car="destinator",slug="mitsubishi-promo-metro-manila-buyers",date="2026-10-22",by=BY,img="de_x3n",alt="Mitsubishi Destinator for Metro Manila buyers checking promos",
title="Mitsubishi Promo for Metro Manila Buyers: Buying in SJDM",
desc="",answer="",
faq=[("Can Metro Manila residents buy from a dealer in Bulacan?","Yes. You can buy from any authorized dealer. Ask about registration, release and where you'll do PMS."),
("Where can I do PMS if I buy in SJDM but live in Manila?","Ask your sales executive about service options near you; authorized service centers follow the same warranty schedule."),
("What is the Mitsubishi promo this month?","October 2026 promos include Zero DP options such as the Xpander GLX AT at ₱23,877 a month and the Destinator GLX at ₱28,615 a month, 60 months, all-in."),
("Can I do the process online?","Much of it. Check your budget online, send documents for pre-check, and come in for the test drive and release.")],
body='''<p>Shopping for a Mitsubishi promo in Metro Manila? Many of my clients from Caloocan, Quezon City and Fairview come to San Jose del Monte, just up Quirino Highway. Here's how buying from SJ Legacy Motors works if you live in Metro Manila.</p>

<h2>October 2026 promo highlights</h2>
'''+T(["Unit","Zero DP","Low DP"],[("Xpander GLX MT","₱22,641","₱148K DP: ₱19,811"),("Xpander GLX AT","₱23,877","₱138K DP: ₱20,892"),("Xpander Cross","₱28,389","₱148K DP: ₱24,840"),("Destinator GLX","₱28,615","₱93K DP: ₱26,827"),("Montero Sport GLX MT","₱30,284","₱30K DP: ₱28,265")])+PN+'''
<p>Full list on the <a href="/promos/">promos page</a>.</p>

<h2>How the process works from Metro Manila</h2>
<ol class="steps">
<li><h3>Check your budget online</h3><p>Use the <a href="/budgetcalculator/">Budget Fit Calculator</a>.</p></li>
<li><h3>Send documents for pre-check</h3><p>By message, before you travel. See <a href="/guides/car-loan-requirements/">requirements</a>.</p></li>
<li><h3>One visit for the test drive</h3><p>Book a schedule so your unit is ready.</p></li>
<li><h3>Approval and release</h3><p>Once approved, we schedule your release in SJDM.</p></li>
</ol>

<h2>Questions to ask any dealer</h2>
<ul class="ticks">
<li>What's included in the all-in package? (<a href="/guides/what-all-in-includes/">here's the usual list</a>)</li>
<li>What's the total of payments over the term?</li>
<li>Which freebies come with my unit?</li>
<li>Where will I do PMS near home?</li>
</ul>

<h2>Driving up from Manila</h2>
<p>Quirino Highway runs from Fairview to SJDM. Check traffic before you leave; my <a href="/tips/sjdm-to-manila-commute-tips/">SJDM to Manila tips</a> help in reverse too. Showroom: Lot 9 Ebenezer Christian Academy, Sitio Gitna, Sto. Cristo, Quirino Highway, San Jose del Monte.</p>
'''+CTA2("From Metro Manila? Check your budget, then book one trip to SJDM for your test drive.","destinator")),

dict(base="blog",car="xpander",slug="xpander-monthly-amortization",date="2026-10-22",by=BY,img="xpglx_x37",alt="Mitsubishi Xpander GLX AT, with monthly amortization options",
title="Xpander Monthly Amortization 2026: All Variants",
desc="",answer="",
faq=[("How much is the Xpander monthly amortization?","In October 2026 on 60 months, all-in: GLX MT ₱22,641 (Zero DP), GLX AT ₱23,877, GLS AT ₱25,937, and Xpander Cross ₱28,389. Low DP options are lower."),
("What is the Xpander GLS monthly amortization?","₱25,937 at Zero DP or ₱22,695 with ₱148K DP, 60 months, all-in (October 2026)."),
("How much is the Xpander Cross monthly amortization?","₱28,389 at Zero DP or ₱24,840 with ₱148K DP, 60 months, all-in (October 2026)."),
("Is there a cheaper Xpander monthly?","The GLX MT with ₱148K DP at ₱19,811 a month is the lowest Xpander monthly this October.")],
body='''<p>Here's the Xpander monthly amortization for every variant in October 2026, on a 5-year (60-month) all-in term, plus the total you'll pay and the income each one needs.</p>

<h2>Monthly amortization by variant</h2>
'''+T(["Variant","SRP","Zero DP","Low DP","Fuel"],[("GLX 1.5G M/T","₱1,099,000","₱22,641","₱148K DP: ₱19,811","₱30K"),("GLX 1.5G A/T","₱1,159,000","₱23,877","₱138K DP: ₱20,892","₱60K"),("GLS 1.5G A/T","₱1,259,000","₱25,937","₱148K DP: ₱22,695","₱60K"),("Xpander Cross A/T","₱1,378,000","₱28,389","₱148K DP: ₱24,840","₱60K")])+PN+'''

<h2>Total of payments over 60 months</h2>
'''+T(["Variant","Zero DP total","Low DP total"],[("GLX M/T","₱1,358,460","₱1,336,660"),("GLX A/T","₱1,432,620","₱1,391,520"),("GLS A/T","₱1,556,220","₱1,509,700"),("Xpander Cross","₱1,703,340","₱1,638,400")])+TOT+'''

<h2>Income you'll need</h2>
<p>At 30–35% of gross monthly income for the Zero DP monthly:</p>
<ul class="ticks"><li>GLX M/T: ₱64,700 – ₱75,500</li><li>GLX A/T: ₱68,200 – ₱79,600</li><li>GLS A/T: ₱74,100 – ₱86,500</li><li>Xpander Cross: ₱81,100 – ₱94,600</li></ul>
<p>Full method in <a href="/blog/how-much-car-can-i-afford-philippines/">How much car can I afford?</a></p>

<h2>Zero DP or low DP?</h2>
<p>Paying the down payment lowers both the monthly and the total of payments. Zero DP keeps your cash for emergencies. See <a href="/guides/zero-dp-vs-low-dp/">Zero DP vs low DP</a> and the variant breakdown in <a href="/blog/xpander-variants-explained/">Xpander GLX vs GLS vs Cross</a>.</p>
'''+CTA2("Find the Xpander monthly that fits you, then test drive it in SJDM.","xpander")),

dict(base="blog",car="destinator",slug="destinator-price-philippines",date="2026-10-22",by=BY,img="de_jh3",alt="Mitsubishi Destinator GT, with 2026 price in the Philippines",
title="Destinator Price Philippines 2026: SRP and Monthly",
desc="",answer="",
faq=[("How much is the Mitsubishi Destinator in the Philippines?","SRP: GLX ₱1,389,000, GLS ₱1,599,000, GT ₱1,929,000 (monotone) or ₱1,939,000 (two-tone)."),
("What is the Destinator monthly?","From ₱28,615 at Zero DP (GLX) or ₱26,827 with ₱93K DP, 60 months, all-in (October 2026)."),
("Does the Destinator come with free fuel?","In October 2026, the GLS comes with ₱20K fuel and the GT with ₱40K fuel."),
("What engine does the Destinator have?","A 1.5L turbocharged gasoline engine (4B40) with 163 PS and 250 Nm, paired with a CVT.")],
body='''<p>Here's the Destinator price in the Philippines for 2026, with October promo monthlies and the total of payments for each variant. All variants share the 1.5L turbo (163 PS, 250 Nm), CVT, seven seats and 214 mm ground clearance.</p>

<h2>Destinator SRP and promo</h2>
'''+T(["Variant","SRP","Zero DP","Low DP","Fuel"],[("GLX","₱1,389,000","₱28,615","₱93K DP: ₱26,827","Ask"),("GLS","₱1,599,000","₱32,942","₱123K DP: ₱30,883","₱20K"),("GT (Monotone)","₱1,929,000","₱39,740","₱88K DP: ₱37,256","₱40K"),("GT (Two-Tone)","₱1,939,000","₱39,740","₱88K DP: ₱37,256","₱40K")])+PN+'''

<h2>Total of payments over 60 months</h2>
'''+T(["Variant","Zero DP total","Low DP total"],[("GLX","₱1,716,900","₱1,702,620"),("GLS","₱1,976,520","₱1,975,980"),("GT","₱2,384,400","₱2,323,360")])+TOT+'''

<h2>Income guide</h2>
<ul class="ticks"><li>GLX Zero DP: ₱81,800 – ₱95,400 gross monthly</li><li>GLS Zero DP: ₱94,100 – ₱109,800</li><li>GT Zero DP: ₱113,500 – ₱132,500</li></ul>

<h2>Which variant?</h2>
<p>See <a href="/blog/destinator-glx-vs-gls-vs-gt/">Destinator GLX vs GLS vs GT</a>, and compare with other 7-seaters in <a href="/blog/xpander-vs-destinator-family-car/">Xpander vs Destinator</a> and <a href="/blog/montero-sport-vs-destinator/">Montero Sport vs Destinator</a>.</p>
'''+CTA2("Check which Destinator fits your budget, then test drive it in SJDM.","destinator")),

dict(base="blog",car="montero-sport",slug="montero-sport-price-philippines-2026",date="2026-10-22",by=BY,img="msbs_x8w",alt="Mitsubishi Montero Sport Black Series 4WD, with 2026 price in the Philippines",
title="Montero Sport Price Philippines 2026: SRP and Monthly",
desc="",answer="",
faq=[("How much is the Montero Sport in the Philippines in 2026?","SRP: GLX 2WD M/T ₱1,568,000, GLS 2WD A/T ₱1,927,000, Black Series 2WD A/T ₱2,190,000, Black Series 4WD A/T ₱2,530,000."),
("What's the cheapest Montero Sport monthly?","The GLX M/T at ₱28,265 a month with ₱30K DP, or ₱30,284 at Zero DP (October 2026, 60 months, all-in)."),
("How much is the Montero Sport automatic?","The GLS 2WD A/T is ₱1,927,000 SRP, from ₱37,218 a month with ₱138K DP or ₱39,699 at Zero DP."),
("How much is the Montero Black Series 4WD monthly?","₱52,121 with ₱133K DP or ₱48,864 with ₱283K DP (October 2026).")],
body='''<p>Here's the Montero Sport price in the Philippines for 2026, with October promo monthlies and total of payments for all four variants. Every variant has the 2.4L 4N15 turbo diesel (181 PS, 430 Nm) and seven seats.</p>

<h2>Montero Sport SRP and promo</h2>
'''+T(["Variant","SRP","Option 1","Option 2"],[("GLX 2WD M/T","₱1,568,000","Zero DP: ₱30,284","₱30K DP: ₱28,265"),("GLS 2WD A/T","₱1,927,000","Zero DP: ₱39,699","₱138K DP: ₱37,218"),("Black Series 2WD A/T","₱2,190,000","₱88K DP: ₱45,117","₱218K DP: ₱42,297"),("Black Series 4WD A/T","₱2,530,000","₱133K DP: ₱52,121","₱283K DP: ₱48,864")])+PN+'''
<p>Fuel freebie: ₱20K on the GLS and both Black Series variants.</p>

<h2>Total of payments over 60 months</h2>
'''+T(["Variant","Option 1 total","Option 2 total"],[("GLX M/T","₱1,817,040","₱1,725,900"),("GLS A/T","₱2,381,940","₱2,371,080"),("Black Series 2WD","₱2,795,020","₱2,755,820"),("Black Series 4WD","₱3,260,260","₱3,214,840")])+TOT+'''

<h2>Manual or automatic, 2WD or 4WD</h2>
<ul class="ticks"><li><b>Manual</b>: GLX, 6-speed, lowest price</li><li><b>Automatic</b>: GLS and Black Series, 8-speed</li><li><b>4WD</b>: Black Series 4WD only</li></ul>
<p>Details in <a href="/blog/montero-sport-variants-explained/">Montero Sport GLX vs GLS vs Black Series</a> and <a href="/blog/montero-sport-vs-destinator/">Montero Sport vs Destinator</a>.</p>
'''+CTA2("Check which Montero Sport fits your budget, then test drive it in SJDM.","montero-sport")),

dict(base="blog",car="l300",slug="l300-price-philippines-2026",date="2026-10-22",by=BY,img="l300_fb",alt="Mitsubishi L300 Dual AC, with 2026 price in the Philippines",
title="L300 Price Philippines 2026: Down Payment and Monthly",
desc="",answer="",
faq=[("How much is the L300 in the Philippines in 2026?","The 2026 L300 Dual AC is ₱1,039,000 SRP. For the Cab & Chassis, message Richard for the latest promo."),
("What is the L300 down payment and monthly?","Zero DP at ₱21,405 a month, or ₱123K DP at ₱18,789 a month, 60 months, all-in, with ₱20K fuel (October 2026)."),
("What engine does the L300 have?","A 2.2L 16-valve DOHC turbo-intercooled diesel (4N14), Euro 4, with a 5-speed manual."),
("Can a business finance an L300?","Yes. Banks typically ask for business registration, ITR or financial statements and bank statements.")],
body='''<p>Here's the L300 price in the Philippines for 2026, with the down payment and monthly options this October, the total of payments, and the income guide. The L300 runs a 2.2L 4N14 turbo-intercooled diesel with a 5-speed manual.</p>

<h2>L300 Dual AC price and promo</h2>
'''+T(["2026 L300 Dual AC","Monthly (60 months)","Total of payments"],[("Zero DP","₱21,405","₱1,284,300"),("₱123K DP","₱18,789","₱1,250,340")])+'''
<p>SRP ₱1,039,000, all-in, with ₱20K fuel. For the Cab &amp; Chassis variant, message me for the latest promo.</p>'''+TOT+'''

<h2>Income guide</h2>
<p>At 30–35% of gross income, the Zero DP monthly fits about ₱61,200 to ₱71,400 a month; the ₱123K DP option about ₱53,700 to ₱62,600. For businesses, banks look at business income and documents. See <a href="/guides/car-loan-requirements/">car loan requirements</a>.</p>

<h2>Is it right for your business?</h2>
<p>Read my <a href="/blog/l300-negosyo-guide/">L300 negosyo guide</a> and <a href="/blog/l300-vs-triton-for-negosyo/">L300 vs Triton</a> comparison.</p>
'''+CTA2("Check if the L300 fits your negosyo budget, then test drive it in SJDM.","l300")),

dict(base="blog",car="xpander",slug="zero-down-payment-car-philippines",date="2026-10-22",by=BY,img="xpglx_u33",alt="Mitsubishi Xpander available on a zero down payment car promo",
title="Zero Down Payment Car Philippines: October 2026 List",
desc="",answer="",
faq=[("Which Mitsubishi has the lowest zero down payment monthly?","Among October 2026 promos, the L300 Dual AC at ₱21,405 and the Xpander GLX MT at ₱22,641 a month, 60 months, all-in."),
("Is zero down payment really zero?","Zero DP means no down payment on the promo; the all-in package covers registration, insurance and chattel mortgage. Ask for the written breakdown of what you'll pay at signing."),
("Is zero DP harder to get approved?","The monthly is higher, so the bank checks that it fits your income. Approval is always subject to bank evaluation."),
("Which units don't have a zero DP option?","In October 2026, the Montero Sport Black Series variants are offered with a down payment.")],
body='''<p>Looking for a zero down payment car in the Philippines? Here are all the Mitsubishi Zero DP promos for October 2026, ranked by monthly, with the income each needs at 30–35% of gross income.</p>

<h2>Zero DP list, lowest monthly first</h2>
'''+T(["Unit","SRP","Zero DP monthly","Gross income"],[("L300 Dual AC","₱1,039,000","₱21,405","₱61.2K–₱71.4K"),("Xpander GLX MT","₱1,099,000","₱22,641","₱64.7K–₱75.5K"),("Xpander GLX AT","₱1,159,000","₱23,877","₱68.2K–₱79.6K"),("Xpander GLS AT","₱1,259,000","₱25,937","₱74.1K–₱86.5K"),("Xpander Cross","₱1,378,000","₱28,389","₱81.1K–₱94.6K"),("Destinator GLX","₱1,389,000","₱28,615","₱81.8K–₱95.4K"),("Triton GX AT","₱1,430,000","₱28,900","₱82.6K–₱96.3K"),("Montero Sport GLX MT","₱1,568,000","₱30,284","₱86.5K–₱100.9K"),("Destinator GLS","₱1,599,000","₱32,942","₱94.1K–₱109.8K"),("Montero Sport GLS","₱1,927,000","₱39,699","₱113.4K–₱132.3K"),("Destinator GT","₱1,929,000","₱39,740","₱113.5K–₱132.5K")])+PN+'''

<h2>What "zero DP all-in" means</h2>
<p>No down payment, and the package covers LTO registration, TPL insurance, 1-year comprehensive insurance with the rate locked for 3 years, chattel mortgage, free labor up to 5,000 km and a 3-year warranty. Ask for the written breakdown of anything due at signing. More in <a href="/guides/what-all-in-includes/">what all-in includes</a>.</p>

<h2>Pros and cons</h2>
<ul class="ticks"><li><b>Pro</b>: keep your savings for emergencies or business</li><li><b>Pro</b>: drive sooner</li><li><b>Con</b>: higher monthly and total of payments than a low DP option</li><li><b>Con</b>: needs a bit more income to qualify</li></ul>
<p>Compare both in <a href="/guides/zero-dp-vs-low-dp/">Zero DP vs low DP</a> and <a href="/blog/xpander-monthly-amortization/">Xpander monthly amortization</a>.</p>
'''+CTA2("See which Zero DP unit fits your income, then test drive it in SJDM.","xpander")),

dict(base="tips",car="xpander",slug="car-loan-approval-tips",date="2026-10-22",by=BY,img="xpgls_c31",alt="Mitsubishi Xpander GLS released after car loan approval",
title="Car Loan Approval Tips: 10 Ways to Get Approved",
desc="",answer="",
faq=[("How long does car loan approval take in the Philippines?","It depends on the bank and how complete your documents are. Complete, consistent documents usually move faster."),
("Why do car loans get declined?","Common reasons are incomplete documents, income that doesn't fit the monthly, high existing debt, or credit history issues."),
("Does a co-borrower help car loan approval?","It can, because combined income may be considered. Ask which banks allow it."),
("Does car loan approval expire?","Approvals are usually valid for a limited period set by the bank. Ask how long yours is valid so you can schedule release.")],
body='''<p>These car loan approval tips come from what I see every week when applications go to the bank. None of them guarantee approval, since the bank decides, but they make your application stronger and faster.</p>

<h2>10 car loan approval tips</h2>
<ol class="steps">
<li><h3>Choose a unit that fits</h3><p>Keep the monthly at about 30–35% of gross income. Use the <a href="/budgetcalculator/">calculator</a>.</p></li>
<li><h3>Complete documents the first time</h3><p>See the <a href="/guides/car-loan-requirements/">requirements list</a> for employed, self-employed and OFW.</p></li>
<li><h3>Make everything consistent</h3><p>Same name spelling, address and income across all documents.</p></li>
<li><h3>Pay down small debts</h3><p>Lower obligations mean more capacity.</p></li>
<li><h3>Pay cards on time</h3><p>Credit history matters.</p></li>
<li><h3>Show stable income</h3><p>Self-employed: clean business bank statements and ITR.</p></li>
<li><h3>Add a co-borrower if needed</h3><p>Spouse or immediate family, if the bank allows.</p></li>
<li><h3>Consider a down payment</h3><p>A lower monthly is easier to approve. See <a href="/guides/zero-dp-vs-low-dp/">Zero DP vs low DP</a>.</p></li>
<li><h3>Be reachable</h3><p>Answer the bank's verification call and keep your phone on.</p></li>
<li><h3>Have your documents pre-checked</h3><p>I review them before they go to the bank.</p></li>
</ol>

<h2>Common reasons for decline</h2>
<ul class="ticks"><li>Incomplete or inconsistent documents</li><li>Monthly too high for income</li><li>High existing debt</li><li>Credit history issues</li><li>Unreachable during verification</li></ul>
<p>Declined before? It's not the end. Read <a href="/blog/car-loan-myths-philippines/">car loan myths</a>, and if you're starting out, the <a href="/blog/minimum-salary-for-car-loan-philippines/">minimum salary guide</a>.</p>
'''+CTA2("Want me to pre-check your documents? Check your budget, then call or text me.","xpander")),

dict(base="tips",car="xpander-cross",slug="car-reservation-fee-philippines",date="2026-10-22",by=BY,img="xc_green",alt="Reserving a Mitsubishi Xpander Cross unit",
title="Car Reservation Fee Philippines: What to Know",
desc="",answer="",
faq=[("What is a car reservation fee?","An amount paid to hold a unit or color for you while your loan is processed or payment is arranged."),
("Is a car reservation fee refundable?","It depends on the dealer's terms and the reason for cancellation. Ask for the refund terms in writing before paying."),
("How much is the reservation fee?","It varies. Message Richard for the current amount and terms for your unit."),
("Is the reservation fee deducted from the price?","Ask how it's applied to your purchase and get it on the receipt.")],
body='''<p>Asked to pay a car reservation fee in the Philippines? Here's what it is, when it makes sense, and what to get in writing before you pay.</p>

<h2>What a reservation fee does</h2>
<ul class="ticks"><li>Holds a specific unit, variant or color for you</li><li>Lets the dealer process your application with the unit set aside</li><li>Shows you're a serious buyer when stock is limited</li></ul>

<h2>Before you pay, ask these</h2>
<ol class="steps">
<li><h3>How much, and for which unit?</h3><p>Variant and color on the receipt.</p></li>
<li><h3>How is it applied?</h3><p>Is it deducted from your down payment or charges?</p></li>
<li><h3>Is it refundable?</h3><p>Under which conditions, for example if the bank declines.</p></li>
<li><h3>How long is the hold?</h3><p>What happens after that period.</p></li>
<li><h3>Official receipt</h3><p>Always get an official receipt from the dealership.</p></li>
</ol>

<h2>When to reserve</h2>
<ul class="ticks"><li>You've test driven and decided on the unit</li><li>The monthly fits your budget (see the <a href="/blog/zero-down-payment-car-philippines/">Zero DP list</a>)</li><li>Your documents are ready (see <a href="/tips/car-loan-approval-tips/">approval tips</a>)</li></ul>
<p>For the current reservation amount and terms for your unit, message me for the latest. After approval, prepare for <a href="/tips/new-car-release-day-checklist/">release day</a>.</p>
'''+CTA2("Ready to reserve? Check your budget, test drive, then call or text me for the current terms.","xpander-cross")),

dict(base="tips",car="destinator",slug="mitsubishi-test-drive-sjdm",date="2026-10-22",by=BY,img="de_w81",alt="Mitsubishi Destinator test drive in SJDM",
title="Mitsubishi Test Drive in SJDM: What to Expect",
desc="",answer="",
faq=[("How do I book a Mitsubishi test drive in SJDM?","Use the online test drive page: pick a unit, choose a date and time, and Richard will confirm."),
("What do I need to bring?","A valid driver's license. Bring your family if they'll ride often in the car."),
("Can I test drive the Destinator?","Yes. Choose the Destinator variant on the booking page, subject to unit availability."),
("Can I test drive two models on the same day?","Ask when booking so both units can be prepared.")],
body='''<p>Planning a Mitsubishi test drive in SJDM? Here's how to book, what to bring, and what to check, so you get the most out of your drive at SJ Legacy Motors on Quirino Highway.</p>

<h2>How to book</h2>
<ol class="steps"><li><h3>Pick a unit</h3><p>On the <a href="/test-drive/">test drive page</a>.</p></li><li><h3>Choose a date and time</h3><p>Then send your details.</p></li><li><h3>I'll confirm</h3><p>By message or call. You can also call or text '''+TELL+'''.</p></li></ol>

<h2>What to bring</h2>
<ul class="ticks"><li>Valid driver's license</li><li>The people who'll ride often, especially third-row passengers</li><li>A child car seat if you use one (see <a href="/tips/child-car-seat-law-philippines/">RA 11229</a>)</li><li>Your usual cargo, like a stroller or tools</li></ul>

<h2>What to check on the drive</h2>
<ul class="ticks"><li>Seat position, visibility and mirrors</li><li>Acceleration with passengers on board</li><li>Ride over bumps, braking and steering</li><li>AC reach to every row</li><li>Parking and turning</li><li>Phone pairing and reverse camera</li></ul>

<h2>Compare back-to-back</h2>
<p>Driving two models on the same day makes the choice easier: Xpander vs Destinator, Montero Sport vs Destinator, or L300 vs Triton. Read <a href="/blog/xpander-vs-destinator-family-car/">Xpander vs Destinator</a> before you come.</p>
'''+CTA2("Book your test drive at Mitsubishi SJ Legacy Motors, SJDM, after checking your budget.","destinator")),
]
MAPL='<p><a href="https://www.google.com/maps/dir/?api=1&amp;destination=Mitsubishi+SJ+Legacy+Motors+Quirino+Highway+San+Jose+del+Monte+Bulacan" target="_blank" rel="noopener">Get directions in Google Maps</a></p>'
def LOCAL(area,slug,img,alt,title,intro,route,near,car):
    return dict(base="blog",car=car,slug=slug,date="2026-10-22",by=BY,img=img,alt=alt,title=title,desc="",answer="",
faq=[(f"Is there a Mitsubishi dealer near {area}?",f"Mitsubishi SJ Legacy Motors is on Quirino Highway in San Jose del Monte, Bulacan, reachable from {area} by car. There are other Mitsubishi dealers in the region too; choose the one that serves you best."),
("Can I do part of the process online?","Yes. Check your budget with the calculator, send documents for pre-check, and book your test drive online before you travel."),
("Where will I do PMS if I buy in SJDM?","Ask about service options near your home. Authorized service centers follow the same warranty schedule."),
("How do I contact the sales executive?","Call or text Richard Cuagdan on 0954 291 1201.")],
body=f'''<p>{intro}</p>

<h2>Getting to the showroom</h2>
'''+ADDRP+f'''<p>{route}</p>'''+MAPL+'''<p>Traffic changes by hour and day, so check a live map before leaving, and call or text me on '''+TELL+''' so your unit is ready when you arrive.</p>

<h2>Why some buyers from '''+area+''' choose SJDM</h2>
<ul class="ticks">
<li><b>One point of contact</b>: I handle your inquiry, test drive, bank application follow-up and release</li>
<li><b>Online-first process</b>: budget check, document pre-check and test drive booking before you travel</li>
<li><b>Same all-in promos</b>: October 2026 Zero DP and low DP options on 60 months</li>
<li><b>Help for OFW families</b>: coordination across time zones (see the <a href="/blog/ofw-car-buying-guide/">OFW car loan guide</a>)</li>
</ul>
<p>There are other Mitsubishi dealers in the area too. Compare service, the written all-in breakdown and convenience, then choose what works for you.</p>

<h2>Popular units for '''+area+''' drivers</h2>
'''+T(["Unit","SRP","Zero DP monthly"],[("Xpander GLX AT","₱1,159,000","₱23,877"),("Xpander Cross","₱1,378,000","₱28,389"),("Destinator GLX","₱1,389,000","₱28,615"),("Triton GX AT","₱1,430,000","₱28,900"),("L300 Dual AC","₱1,039,000","₱21,405")])+PN+f'''
<p>{near}</p>

<h2>Plan your visit in 3 steps</h2>
<ol class="steps">
<li><h3>Check your budget</h3><p>Use the <a href="/budgetcalculator/">Budget Fit Calculator</a>.</p></li>
<li><h3>Book a test drive</h3><p>On the <a href="/test-drive/">test drive page</a>; see <a href="/tips/mitsubishi-test-drive-sjdm/">what to expect</a>.</p></li>
<li><h3>Bring your documents</h3><p>For pre-check. See <a href="/tips/car-loan-approval-tips/">car loan approval tips</a>.</p></li>
</ol>
'''+CTA2(f"From {area}? Check your budget, book a test drive, or call me before you drive up to SJDM.",car))
BULK6=[
LOCAL("Caloocan and Novaliches","mitsubishi-near-caloocan-novaliches","xpglx_x37","Mitsubishi Xpander for families in Caloocan and Novaliches","Mitsubishi Near Caloocan and Novaliches: SJDM Showroom",
"Looking for a Mitsubishi near Caloocan or Novaliches? Mitsubishi SJ Legacy Motors in San Jose del Monte, Bulacan, is a short drive north along Quirino Highway for many North Caloocan and Novaliches residents. Here's how to get there and how to make the trip worth it.",
"From Novaliches, Quirino Highway runs north into San Jose del Monte. From North Caloocan, head to Quirino Highway and continue north to Sto. Cristo.",
"Driving daily into Metro Manila from the north? Read my <a href=\"/tips/sjdm-to-manila-commute-tips/\">SJDM to Manila commute tips</a>.","xpander"),
LOCAL("Fairview and Quezon City","mitsubishi-near-fairview-quezon-city","de_x3n","Mitsubishi Destinator for Fairview and Quezon City families","Mitsubishi Near Fairview, Quezon City: SJDM Showroom",
"Looking for a Mitsubishi near Fairview or elsewhere in Quezon City? Quirino Highway runs from Fairview to San Jose del Monte, where Mitsubishi SJ Legacy Motors is located. Here's the route and how to plan a visit.",
"From Fairview, take Quirino Highway north toward San Jose del Monte and continue to Sto. Cristo. From other parts of Quezon City, navigation apps usually route you to Quirino Highway.",
"Comparing family SUVs? See <a href=\"/blog/montero-sport-vs-destinator/\">Montero Sport vs Destinator</a> and <a href=\"/blog/destinator-price-philippines/\">Destinator price Philippines</a>.","destinator"),
LOCAL("Bulacan towns","mitsubishi-near-bulacan-towns","tr_gx_u28","Mitsubishi Triton for Bulacan business owners","Mitsubishi Near Marilao, Meycauayan, Sta. Maria and Malolos",
"Looking for a Mitsubishi near Marilao, Meycauayan, Sta. Maria, Norzagaray or Malolos? Mitsubishi SJ Legacy Motors is on Quirino Highway in San Jose del Monte, Bulacan. Here's how to plan a visit from other Bulacan towns, and the units Bulacan negosyo owners and families ask about most.",
"Routes depend on your town and barangay, so use the directions link below. Set your destination to Mitsubishi SJ Legacy Motors, Quirino Highway, Sto. Cristo, San Jose del Monte.",
"Running a negosyo in Bulacan? See <a href=\"/blog/l300-vs-triton-for-negosyo/\">L300 vs Triton</a> and the <a href=\"/blog/l300-price-philippines-2026/\">L300 price 2026</a>.","triton"),
]
BULK6+=[
dict(base="tips",car="xpander",slug="paano-mag-car-loan",date="2026-10-22",by=BY,img="xpglx_u33",alt="Mitsubishi Xpander, a common first car loan unit",
title="Paano Mag Car Loan: Step-by-Step Guide (2026)",desc="",answer="",
faq=[("Paano mag apply ng car loan sa bangko?","Pumili ng unit na pasok sa budget, ihanda ang requirements, at ang dealer o sales executive ang magsa-submit sa bangko. Ang bangko ang mag-a-approve."),
("Gaano katagal ang car loan approval?","Depende sa bangko at sa kumpletong documents. Mas mabilis kapag kumpleto at consistent ang papeles."),
("Kailangan ba ng down payment?","Hindi palagi. May Zero DP all-in promos, halimbawa ang Xpander GLX AT sa ₱23,877 kada buwan (October 2026, 60 months)."),
("Pwede ba mag car loan kahit self-employed?","Oo. Karaniwang hinihingi ang DTI o SEC registration, business permit, ITR o financial statements at bank statements.")],
body='''<p>Paano mag car loan? Mas simple kaysa sa iniisip mo. Here's the step-by-step process I walk my clients through, mula pagpili ng unit hanggang release.</p>

<h2>Step 1: Alamin ang budget mo</h2>
<p>Keep the monthly at about 30–35% of your gross monthly income. Halimbawa, ang Xpander GLX MT na ₱22,641 kada buwan (Zero DP) ay pasok sa gross income na around ₱64,700 hanggang ₱75,500. Try the <a href="/budgetcalculator/">Budget Fit Calculator</a>.</p>

<h2>Step 2: Pumili ng unit at mag test drive</h2>
<p>Subukan muna bago magdesisyon. <a href="/test-drive/">Mag-book ng test drive</a> at isama ang pamilya.</p>

<h2>Step 3: Ihanda ang requirements</h2>
<ul class="ticks">
<li>Dalawang valid ID at proof of billing</li>
<li><b>Employed</b>: COE with compensation, payslips o ITR</li>
<li><b>Self-employed</b>: DTI/SEC, business permit, ITR o financial statements, bank statements</li>
<li><b>OFW</b>: contract, payslips, remittance proof, SPA o co-borrower</li>
</ul>
<p>Buong listahan: <a href="/guides/car-loan-requirements/">car loan requirements</a>.</p>

<h2>Step 4: Submission at bank approval</h2>
<ol class="steps">
<li><h3>Pre-check</h3><p>Ire-review ko muna ang documents mo.</p></li>
<li><h3>Submit sa bangko</h3><p>Ang bangko ang mag-e-evaluate: capacity to pay, documents, credit history.</p></li>
<li><h3>Verification</h3><p>Sagutin ang tawag ng bangko.</p></li>
<li><h3>Approval</h3><p>Kapag approved, ise-schedule ang release.</p></li>
</ol>

<h2>Step 5: Release</h2>
<p>Sa release day, i-check ang unit, documents at freebies. Gamitin ang <a href="/tips/new-car-release-day-checklist/">release day checklist</a>. Kasama na sa all-in ang LTO registration, TPL insurance, 1-year comprehensive insurance (rate locked for 3 years), chattel mortgage, free labor up to 5,000 km at 3-year warranty.</p>
<p>Para mas mataas ang chance ng approval, basahin ang <a href="/tips/car-loan-approval-tips/">car loan approval tips</a>.</p>
'''+CTA2("Handa ka na? I-check ang budget mo, mag-book ng test drive, o tawagan ako.","xpander")),

dict(base="tips",car="mirage-g4",slug="paano-bumili-ng-bagong-sasakyan",date="2026-10-22",by=BY,img="mg4gls_u17",alt="Bagong Mitsubishi Mirage G4 sedan",
title="Paano Bumili ng Bagong Sasakyan: Cash o Financing",desc="",answer="",
faq=[("Ano ang mas mainam, cash o car loan?","Depende. Walang interest ang cash pero mauubos ang ipon mo. Ikumpara ang total na babayaran at kung ano ang magagawa ng pera mo sa iba."),
("Ano ang kailangan kapag cash ang bayad?","Valid IDs at ang bayad sa paraang tinatanggap ng dealer. Kumuha palagi ng official receipt."),
("Kasama na ba ang registration sa bagong sasakyan?","Sa all-in promo packages, kasama ang LTO registration, TPL insurance at iba pa. Itanong ang listahan nang nakasulat."),
("Gaano katagal bago makuha ang sasakyan?","Depende sa availability ng unit at, kung financing, sa bank approval.")],
body='''<p>Paano bumili ng bagong sasakyan sa Pilipinas? Dalawa ang daan: cash o financing. Here's how each works, step by step, para alam mo ang aasahan.</p>

<h2>Cash vs financing</h2>
'''+T(["","Cash","Financing"],[("Bayad","Buong halaga","Down payment (o Zero DP) + monthly"),("Interest","Wala","Kasama sa monthly"),("Approval","Hindi kailangan","Subject to bank approval"),("Ipon","Mababawasan nang malaki","Mananatili para sa emergency")])+'''

<h2>Kung cash</h2>
<ol class="steps">
<li><h3>Pumili ng unit at variant</h3><p>Mag test drive muna.</p></li>
<li><h3>Itanong ang cash price at inclusions</h3><p>Maaaring iba ang promo sa cash at financing.</p></li>
<li><h3>Magbayad at kumuha ng official receipt</h3><p>Sa paraang tinatanggap ng dealer.</p></li>
<li><h3>Release</h3><p>Gamitin ang <a href="/tips/new-car-release-day-checklist/">release checklist</a>.</p></li>
</ol>

<h2>Kung financing</h2>
<p>Sundan ang <a href="/tips/paano-mag-car-loan/">paano mag car loan</a> guide. Halimbawa ng October 2026 promo: Xpander GLS AT, Zero DP sa ₱25,937 kada buwan o ₱148K DP sa ₱22,695, 60 months, all-in, may ₱60K fuel.</p>

<h2>Huwag kalimutan ang ownership costs</h2>
<ul class="ticks"><li>Gas, parking at toll</li><li>PMS (tingnan ang <a href="/tips/pms-schedule-guide/">PMS schedule guide</a>)</li><li>Insurance renewal</li><li>Gulong at baterya sa paglipas ng panahon</li></ul>
<p>Para sa Mirage G4 at iba pang units na wala sa listahan, message me for the latest promo.</p>
'''+CTA2("Cash man o financing, i-check muna ang budget at mag test drive sa SJDM.","mirage-g4")),

dict(base="tips",car="destinator",slug="co-borrower-car-loan-philippines",date="2026-10-22",by=BY,img="de_d34",alt="Family co-borrowers buying a Mitsubishi Destinator",
title="Co-Borrower Car Loan Philippines: How It Works",desc="",answer="",
faq=[("Who can be a co-borrower for a car loan?","Banks commonly accept a spouse or immediate family member. Each bank sets its own rules."),
("What does a co-borrower sign up for?","A co-borrower shares responsibility for the loan, so they should understand the monthly and the term before signing."),
("Does a co-borrower need documents?","Yes. Typically IDs and income documents, similar to the main borrower."),
("Can an OFW use a co-borrower in the Philippines?","Yes. A co-borrower or an attorney-in-fact under an SPA is common for OFW applications.")],
body='''<p>A co-borrower car loan in the Philippines lets two people apply together, so the bank can consider combined income. It's common for couples, families and OFWs. Here's how it works and what to think about first.</p>

<h2>When a co-borrower helps</h2>
<ul class="ticks"><li>Your income alone is a bit short for the monthly</li><li>You're an OFW and need someone in the Philippines to sign</li><li>A couple wants to share the loan</li><li>You're newly employed and want a stronger application</li></ul>

<h2>Who can be a co-borrower</h2>
<p>Banks commonly accept a spouse or immediate family member. Rules vary by bank, so ask before you prepare documents.</p>

<h2>What the co-borrower needs</h2>
<ul class="ticks"><li>Valid IDs</li><li>Income documents (COE and payslips, or business documents)</li><li>Proof of billing</li></ul>
<p>Full lists in <a href="/guides/car-loan-requirements/">car loan requirements</a>.</p>

<h2>Think it through first</h2>
<ol class="steps">
<li><h3>Shared responsibility</h3><p>The co-borrower shares the loan. Both should agree on the monthly and the term.</p></li>
<li><h3>Agree who pays</h3><p>Put it in writing between you.</p></li>
<li><h3>Check the budget together</h3><p>Use the 30–35% guide on combined gross income. Example: the Destinator GLX Zero DP at ₱28,615 a month fits about ₱81,800 to ₱95,400 combined (October 2026).</p></li>
</ol>

<h2>Co-borrower vs SPA for OFWs</h2>
<p>An SPA lets someone sign on your behalf; a co-borrower shares the loan. See the <a href="/blog/ofw-car-buying-guide/">OFW car loan guide</a> and <a href="/tips/car-loan-approval-tips/">car loan approval tips</a>.</p>
'''+CTA2("Applying with a co-borrower? Check your combined budget, then book a test drive in SJDM.","destinator")),

dict(base="tips",car="xpander",slug="manual-vs-automatic-car-philippines",date="2026-10-22",by=BY,img="xpglx_graphite",alt="Mitsubishi Xpander available in manual and automatic",
title="Manual vs Automatic Car Philippines: Which to Buy?",desc="",answer="",
faq=[("Is a manual car cheaper in the Philippines?","Often the manual variant has a lower SRP and monthly. Example: Xpander GLX MT ₱1,099,000 vs GLX AT ₱1,159,000."),
("Is automatic better for traffic?","For daily stop-and-go traffic, most drivers find an automatic or CVT far less tiring."),
("Can I drive an automatic with a manual license?","Check your license restrictions with the LTO; restriction codes and categories define what you may drive."),
("Which is better for business?","Many work vehicles like the L300 are manual. For delivery drivers used to manual, it's a practical choice.")],
body='''<p>Manual vs automatic car in the Philippines: the right answer depends on your traffic, budget and who'll drive. Here's a clear comparison using real Xpander promo numbers.</p>

<h2>The price difference, in real numbers</h2>
'''+T(["Xpander GLX","Manual (M/T)","Automatic (A/T)"],[("SRP","₱1,099,000","₱1,159,000"),("Zero DP monthly","₱22,641","₱23,877"),("Low DP monthly","₱148K DP: ₱19,811","₱138K DP: ₱20,892"),("Fuel freebie","₱30K","₱60K")])+PN+'''
<p>At Zero DP, the automatic is ₱1,236 more a month, and this month it comes with ₱30K more fuel.</p>

<h2>Choose manual if…</h2>
<ul class="ticks"><li>Your budget is tight and every peso of the monthly counts</li><li>You already drive manual comfortably</li><li>It's a work vehicle and your drivers prefer manual</li></ul>

<h2>Choose automatic if…</h2>
<ul class="ticks"><li>You face daily traffic, like the <a href="/tips/sjdm-to-manila-commute-tips/">SJDM to Manila commute</a></li><li>Several family members will drive</li><li>You're a <a href="/tips/new-driver-tips-philippines/">new driver</a></li><li>Senior drivers in the family (see <a href="/blog/best-car-for-senior-citizens-philippines/">best car for senior citizens</a>)</li></ul>

<h2>Test both</h2>
<p>Drive the GLX MT and GLX AT back-to-back. More in <a href="/blog/xpander-variants-explained/">Xpander GLX vs GLS vs Cross</a>.</p>
'''+CTA2("Test drive manual and automatic back-to-back in SJDM after checking your budget.","xpander")),

dict(base="tips",car="xpander",slug="best-car-color-philippines",date="2026-10-22",by=BY,img="xpgls_red",alt="Mitsubishi Xpander in red, one of several color choices",
title="Best Car Color Philippines: Heat, Care and Resale",desc="",answer="",
faq=[("What is the best car color for the Philippine heat?","Lighter colors like white and silver generally absorb less heat than dark colors in direct sun."),
("Which car colors hide dirt best?","Silver and gray tend to show dust and water spots less than black."),
("Does car color affect resale value?","Common colors like white, silver and black are often easier to sell because more buyers want them."),
("Are all colors available for every variant?","No. Colors vary by model and variant. Ask Richard for the current color options and availability.")],
body='''<p>What's the best car color in the Philippines? There's no single answer, but heat, dust, maintenance and resale all point in useful directions. Here's how to choose with your head, not just your heart.</p>

<h2>Heat</h2>
<p>In direct sun, lighter colors like white and silver generally absorb less heat than black or very dark colors. Your AC still does the heavy lifting, but parking in the sun is a little kinder to light colors. See <a href="/tips/car-aircon-not-cooling-tips/">car aircon care</a>.</p>

<h2>Dust, rain and scratches</h2>
<ul class="ticks"><li><b>Silver and gray</b>: hide dust and water spots well</li><li><b>White</b>: shows mud but hides fine swirl marks</li><li><b>Black and dark colors</b>: look sharp clean, but show dust, swirls and water spots</li><li><b>Bold colors like red</b>: stand out; keep them waxed</li></ul>
<p>Whatever you choose, wash properly. See <a href="/tips/car-wash-at-home-guide/">car wash at home</a>.</p>

<h2>Resale</h2>
<p>Common colors such as white, silver and black are often easier to sell later because more buyers look for them. Unique colors can take longer to find the right buyer. More in <a href="/tips/car-resale-value-tips/">car resale value tips</a>.</p>

<h2>Practical checklist</h2>
<ol class="steps">
<li><h3>See it in daylight</h3><p>Showroom lights change how colors look.</p></li>
<li><h3>Check availability</h3><p>Colors vary by variant and stock.</p></li>
<li><h3>Two-tone options</h3><p>Some variants, like the Xpander Cross and Destinator GT, come in two-tone.</p></li>
<li><h3>Think 5 years ahead</h3><p>You'll see this color every day.</p></li>
</ol>
'''+CTA2("Want to see the colors in person? Check your budget, then visit or book a test drive in SJDM.","xpander")),

dict(base="tips",car="xforce",slug="car-accessories-worth-getting",date="2026-10-22",by=BY,img="xf_gls",alt="Mitsubishi Xforce with useful car accessories",
title="Car Accessories Philippines: What's Worth Getting",desc="",answer="",
faq=[("What accessories come free with a new Mitsubishi?","Typical freebies include full tint, floor mats, seat cover (fabric seats), reverse camera, early warning device, basic tools, umbrella, microfiber cloth and keychain. Freebies vary by variant."),
("Is a dashcam worth it?","Many drivers find it worth it for accident and insurance records. See the dashcam guide."),
("Do accessories affect my warranty?","Some modifications can affect warranty coverage. Ask before installing anything that touches the electrical system or engine."),
("Which accessories should I skip?","Extreme modifications that reduce safety or resale value, and anything that blocks visibility or airbags.")],
body='''<p>Car accessories in the Philippines range from essential to useless. Here's what's worth getting for a new car, what already comes free, and what to skip.</p>

<h2>Already included: new-car freebies</h2>
<ul class="ticks"><li>Full tint</li><li>Floor mats</li><li>Seat cover (fabric seats)</li><li>Reverse camera</li><li>Early warning device and basic tools</li><li>Umbrella, microfiber cloth and keychain</li></ul>
<p class="muted">Freebies vary by variant; ask for the list for your unit.</p>

<h2>Worth getting</h2>
<ul class="ticks">
<li><b>Dashcam</b>: records for accidents and claims. See the <a href="/tips/dashcam-philippines-parking-guide/">dashcam guide</a></li>
<li><b>Sunshade</b>: cooler cabin, protected dashboard</li>
<li><b>Tire pressure gauge</b>: for monthly checks (<a href="/tips/tire-care-tips-philippines/">tire care</a>)</li>
<li><b>Emergency kit additions</b>: jumper cables, flashlight, first aid (<a href="/tips/car-emergency-kit-list/">kit list</a>)</li>
<li><b>Child car seat</b>: required for kids under 150 cm (<a href="/tips/child-car-seat-law-philippines/">RA 11229</a>)</li>
<li><b>Trunk organizer or cargo mat</b>: keeps groceries and tools in place</li>
</ul>

<h2>Think twice</h2>
<ul class="ticks"><li>Electrical add-ons that might affect warranty: ask first</li><li>Anything that blocks airbags, mirrors or your view</li><li>Extreme modifications that hurt resale</li><li>Cheap seat covers that interfere with side airbags</li></ul>

<h2>Before installing</h2>
<ol class="steps"><li><h3>Ask about warranty</h3><p>Especially for electrical work.</p></li><li><h3>Use proper installers</h3><p>Tidy wiring, no cut harnesses.</p></li><li><h3>Keep original parts</h3><p>Helps resale.</p></li></ol>
<p>For the Xforce and other units not in this month's promo list, message me for the latest promo.</p>
'''+CTA2("Ask me which freebies come with your unit. Check your budget, then test drive in SJDM.","xforce")),

dict(base="tips",car="mirage-g4",slug="brand-new-vs-second-hand-car-philippines",date="2026-10-22",by=BY,img="mg4glx_a66",alt="Brand-new Mitsubishi Mirage G4 compared with buying second hand",
title="Brand New vs Second Hand Car Philippines",desc="",answer="",
faq=[("Is a second-hand car cheaper?","Usually the price is lower, but add repairs, unknown history and shorter or no warranty when you compare."),
("What do I get with a brand-new car?","A full warranty (3 years in the all-in package), known history, and an all-in package with registration and insurance."),
("What should I check on a second-hand car?","Documents (OR/CR, deed of sale), flood or accident history, service records, and a mechanic's inspection."),
("Can I finance a brand-new car with zero down?","Yes, through Zero DP all-in promos, subject to bank approval. Example: Xpander GLX MT at ₱22,641 a month (October 2026).")],
body='''<p>Brand new vs second hand car in the Philippines: the second-hand price looks cheaper, but the full picture includes warranty, history, repairs and financing. Here's a fair comparison.</p>

<h2>Side by side</h2>
'''+T(["","Brand new","Second hand"],[("History","Known: you're the first owner","Unknown unless documented"),("Warranty","3-year warranty in the all-in package","Usually short or none"),("Registration and insurance","Included in all-in package","Your cost"),("Flood or accident risk","None at release","Needs inspection"),("Down payment","Zero DP promos available","Depends on the seller")])+'''

<h2>When brand new makes sense</h2>
<ul class="ticks"><li>You want predictable costs and a warranty</li><li>You'll keep the car many years</li><li>Zero DP lets you keep your savings: see the <a href="/blog/zero-down-payment-car-philippines/">Zero DP list</a></li></ul>

<h2>When second hand can make sense</h2>
<ul class="ticks"><li>You're paying cash on a tight budget</li><li>You can have it inspected by a trusted mechanic</li><li>Documents are complete and history is clear</li></ul>

<h2>Second-hand checklist</h2>
<ol class="steps"><li><h3>Documents</h3><p>OR/CR, deed of sale, IDs; no unsettled loan.</p></li><li><h3>Flood and accident signs</h3><p>Rust, odor, water marks, uneven panels.</p></li><li><h3>Service records</h3><p>Proof of regular PMS.</p></li><li><h3>Mechanic inspection</h3><p>Before paying anything.</p></li></ol>

<h2>Compare the monthly</h2>
<p>An Xpander GLX MT brand new is ₱22,641 a month at Zero DP (October 2026, 60 months, all-in). Run your numbers in <a href="/blog/how-much-car-can-i-afford-philippines/">how much car can I afford</a> and read <a href="/tips/car-resale-value-tips/">resale value tips</a>.</p>
'''+CTA2("Compare a brand-new monthly with your options. Check your budget, then test drive in SJDM.","mirage-g4")),
]
DRAFT_POSTS=BULK6+BULK5+BULK4+BULK3+BULK2+BULK+DRAFT_POSTS
from zerodp import ZPOST as _Z
DRAFT_POSTS.insert(0,_Z)
from seo import apply as _seo
DRAFT_POSTS=_seo(DRAFT_POSTS)
PUBLISH=[a["slug"] for a in DRAFT_POSTS]  # all published Oct 21, 2026
