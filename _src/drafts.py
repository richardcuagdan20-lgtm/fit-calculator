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
PUBLISH=["undas-road-trip-checklist-2026"]

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
]
