import json, os, html, sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from data import *
from content import GUIDES, POSTS
GUIDES=[g for g in GUIDES if g["slug"]!="ofw-car-buying-guide"]  # merged into /blog/ofw-car-buying-guide/
from drafts import DRAFT_POSTS, PUBLISH
# Posts in drafts.py go live only when their slug is in PUBLISH.
LIVE=[a for a in DRAFT_POSTS if a["slug"] in PUBLISH]
TIPS=[a for a in LIVE if a["base"]=="tips"]
POSTS=[a for a in LIVE if a["base"]=="blog"]+POSTS
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES=[]
GA='''<!-- Google tag (gtag.js) GA4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-T89CH2TJS6"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-T89CH2TJS6');</script>'''
TEL="+639542911201"; TELD="0954 291 1201"
ADDR="Mitsubishi SJ Legacy Motors, Lot 9 Ebenezer Christian Academy, Sitio Gitna, Sto. Cristo, Quirino Highway, San Jose del Monte, Bulacan"
ADDR_HTML="Mitsubishi SJ Legacy Motors<br>Lot 9 Ebenezer Christian Academy, Sitio Gitna<br>Sto. Cristo, Quirino Highway<br>San Jose del Monte, Bulacan, Philippines"
import urllib.parse as _up
MAPQ=_up.quote_plus(ADDR)
DEALER={"@type":"AutoDealer","@id":D+"/#dealer","name":"Mitsubishi SJ Legacy Motors","alternateName":"Mitsubishi SJ Legacy Motors San Jose del Monte","sameAs":[FB],"brand":{"@type":"Brand","name":"Mitsubishi"},
 "telephone":TEL,"hasMap":"https://www.google.com/maps/search/?api=1&query="+MAPQ,
 "address":{"@type":"PostalAddress","streetAddress":"Lot 9 Ebenezer Christian Academy, Sitio Gitna, Sto. Cristo, Quirino Highway","addressLocality":"San Jose del Monte","addressRegion":"Bulacan","addressCountry":"PH"},
 "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"08:00","closes":"17:00"}],
 "url":D+"/"}
PERSON={"@type":"Person","@id":D+"/#richard","name":"Richard Dennis Cuagdan","alternateName":"Richard Cuagdan","jobTitle":"Car Sales Executive","telephone":TEL,"image":D+"/assets/img/richard-600.webp","worksFor":{"@id":D+"/#dealer"},"url":D+"/about/","sameAs":[FB,MSG]}
PX='''<!-- Meta Pixel -->
<script>try{!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');fbq('init','1820790069172672');fbq('track','PageView');}catch(_){}</script>'''
CL='''<!-- Microsoft Clarity -->
<script>try{(function(c,l,a,r,i,t,y){c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);})(window,document,"clarity","script","z0ztjrla58");}catch(_){}</script>
'''
SUF0=" | Mitsubishi Motors - SJ Legacy Motors"
NAV=[("/","Home"),("/cars/","Cars"),("/promos-tips/","Promos & Tips"),("/apply/","Apply Now"),("/test-drive/","Book a Test Drive"),("/about/","About"),("/contact/","Contact")]
GROUP=[("/promos/","Promos"),("/guides/","Guides"),("/blog/","Blog")]
from figs import FIGS
ILLS=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"ill_sizes.json")))
def e(s): return html.escape(s,quote=True)
def page(path,title,desc,body,ld=None,ogtype="website",img="/assets/img/xpglx_x37.webp",noindex=False,crumbs=None):
    url=D+path
    if title.endswith(SUF0):
        base_=title[:-len(SUF0)]
        title=next(base_+x for x in [" | Mitsubishi Motors by Richard Dennis Cuagdan"," | Mitsubishi Motors by Richard Cuagdan"," | Mitsubishi by Richard Cuagdan",""] if len(base_+x)<=65)
    graph=[DEALER,PERSON]+(ld or [])
    if crumbs:
        graph.append({"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":D+p} for i,(p,n) in enumerate(crumbs)]})
    cur=lambda p:(p==path or (p!="/" and path.startswith(p)))
    def item(p,n):
        act=cur(p) or (p=="/promos-tips/" and any(cur(q) for q,_ in GROUP))
        return f'<a href="{p}"{" aria-current=\"page\"" if act else ""}>{e(n)}</a>'
    nav="".join(item(p,n) for p,n in NAV)
    bc=""
    if crumbs:
        bc='<nav class="bc" aria-label="Breadcrumb"><div class="w">'+" <span>/</span> ".join(f'<a href="{p}">{e(n)}</a>' for p,n in crumbs[:-1])+f' <span>/</span> <span aria-current="page">{e(crumbs[-1][1])}</span></div></nav>'
    h=f'''<!doctype html>
<html lang="en-PH">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{GA}
{PX}
{CL}<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{'<meta name="robots" content="noindex">' if noindex else ''}
<link rel="canonical" href="{url}">
<meta property="og:type" content="{ogtype}">
<meta property="og:site_name" content="Mitsubishi Motors by Richard Dennis Cuagdan">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{D}{img}">
<meta property="og:locale" content="en_PH">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0b0b0c">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/site.css">
<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@graph":graph},ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="hd"><div class="w hdi">
<a class="brand" href="/"><svg viewBox="0 0 24 24" width="26" height="26" aria-hidden="true"><path fill="#E60012" d="M12 2l3.2 5.5L12 13 8.8 7.5zM5.6 13l3.2-5.5L12 13l-3.2 5.5H2.4zM18.4 13l-3.2-5.5L12 13l3.2 5.5h6.4z"/></svg><span class="bt"><b>Mitsubishi Motors</b><small>By Richard Dennis Cuagdan</small></span></a>
<button class="mt" aria-expanded="false" aria-controls="nav" onclick="var n=document.getElementById('nav');var o=n.classList.toggle('open');this.setAttribute('aria-expanded',o)">Menu</button>
<nav id="nav" class="nav" aria-label="Main">{nav}<a class="btn sm" href="/budgetcalculator/">Compute my monthly</a></nav>

</div></header>
{bc}
<main id="main">
{body}
<section class="cta"><div class="w">
<h2>Find a monthly that fits your budget</h2>
<p>Answer a few quick questions and see which Mitsubishi matches your income, with all-in Zero DP and low-DP options.</p>
<p class="row"><a class="btn" href="/budgetcalculator/">Compute my monthly</a> <a class="btn ghost" href="{MSG}" rel="noopener">Message Richard</a></p>
</div></section>
</main>
<footer class="ft"><div class="w">
<div class="fg">
<div><p class="fb">Richard Dennis Cuagdan</p><p>Car Sales Executive, Mitsubishi SJ Legacy Motors</p><address style="font-style:normal">{ADDR_HTML}</address><p>Mobile: <a href="tel:{TEL}">{TELD}</a></p><p>Showroom hours: Monday to Saturday, 8:00 AM to 5:00 PM</p><p><a class="btn sm" href="/apply/">Apply Now</a></p></div>
<div><p class="fb">Explore</p><p><a href="/cars/">Cars</a> · <a href="/promos/">Promos</a> · <a href="/guides/">Guides</a> · <a href="/blog/">Blog</a></p><p><a href="/apply/">Apply</a> · <a href="/test-drive/">Book a Test Drive</a> · <a href="/about/">About</a> · <a href="/contact/">Contact</a> · <a href="/privacy/">Privacy</a></p></div>
</div>
<p class="fsoc"><a class="fbl" href="{FB}" target="_blank" rel="noopener" aria-label="Mitsubishi Motors by Richard Dennis Cuagdan on Facebook"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path fill="currentColor" d="M24 12a12 12 0 1 0-13.9 11.9v-8.4H7.1V12h3V9.4c0-3 1.8-4.7 4.5-4.7 1.3 0 2.7.2 2.7.2v3h-1.5c-1.5 0-2 .9-2 1.9V12h3.4l-.5 3.5h-2.9v8.4A12 12 0 0 0 24 12z"/></svg><span>Facebook</span></a></p>
<p class="disc">Richard Dennis Cuagdan is a sales executive of Mitsubishi SJ Legacy Motors, an authorized Mitsubishi dealership. This is his personal sales website and is not the official website of Mitsubishi Motors Philippines Corporation. Prices, monthly amortizations and freebies are dealer promos, subject to bank approval and change without notice. Mitsubishi names and logos belong to their respective owners.</p>
<p class="cp">© 2026 Richard Dennis Cuagdan · Mitsubishi SJ Legacy Motors, San Jose del Monte, Bulacan</p>
</div></footer>
<a class="fab" href="{MSG}" rel="noopener" aria-label="Chat with Richard on Messenger"><svg viewBox="0 0 24 24" width="26" height="26" aria-hidden="true"><path fill="#fff" d="M12 2C6.4 2 2 6.1 2 11.6c0 2.9 1.2 5.4 3.2 7.1V22l3-1.7c1.2.3 2.4.5 3.8.5 5.6 0 10-4.1 10-9.6S17.6 2 12 2zm1 12.9l-2.5-2.7-5 2.7 5.5-5.8 2.6 2.7 4.9-2.7z"/></svg><span>Messenger</span></a>
</body>
</html>
'''
    d=R+path; os.makedirs(d,exist_ok=True)
    open(d+"index.html","w").write(h)
    if not noindex: PAGES.append(path)

def img(k,alt,eager=False,cls=""):
    return f'<img src="/assets/img/{k}.webp" alt="{e(alt)}" width="640" height="427" {"fetchpriority=\"high\"" if eager else "loading=\"lazy\""} decoding="async"{f" class=\"{cls}\"" if cls else ""}>'

def vcard(v,m):
    promo=f'<a class="btn sm ghost dk" href="/promos/#{m["slug"]}">See promo</a>' if v["promo"] else f'<a class="btn sm ghost dk" href="{MSG}" rel="noopener">Ask for the latest promo</a>'
    return f'''<article class="card vc">{img(v["img"],f"Mitsubishi {v['n']}")}
<div class="pad"><h3>{e(v["n"])}</h3><p class="srp">SRP <b>{srp_txt(v)}</b></p><p class="muted">All-in packages with freebies, ask for details.</p><p class="row">{promo} <a class="btn sm" href="/apply/?unit={v['id']}">Apply for this unit</a> <a class="btn sm ghost dk" href="/test-drive/?unit={v['id']}">Book a Test Drive</a></p></div></article>'''

def offers_ld(m):
    out=[]
    for v in m["variants"]:
        p={"@type":"Product","name":"Mitsubishi "+v["n"],"brand":{"@type":"Brand","name":"Mitsubishi"},"image":D+"/assets/img/"+v["img"]+".webp","category":m["cat"]}
        if v["srp"]:
            p["offers"]={"@type":"Offer","price":v["srp"],"priceCurrency":"PHP","priceValidUntil":"2026-10-31","availability":"https://schema.org/InStock","itemCondition":"https://schema.org/NewCondition","seller":{"@id":D+"/#dealer"},"url":D+f"/cars/{m['slug']}/"}
        out.append(p)
    return out

ALLIN_HTML="<ul class='ticks'>"+"".join(f"<li>{x}</li>" for x in ALLIN)+"</ul>"
FREE_HTML="<ul class='ticks'>"+"".join(f"<li>{x}</li>" for x in FREEBIES)+"</ul>"
def from_txt(m):
    s=srp_from(m); return f'SRP from <b>{f(s)}</b>' if s else 'Ask for price'
UNIT_OPTS="".join(f'<optgroup label="{e(m["name"])}">'+"".join(f'<option value="{e(v["n"])}" data-id="{v["id"]}" data-model="{m["slug"]}">{e(v["n"])}</option>' for v in m["variants"])+'</optgroup>' for m in MODELS)
LACTA='<aside class="lacta"><h2>Pasok ka ba sa car loan?</h2><p>Alamin sa loob ng 3 minuto gamit ang libreng AI Car Loan Application Assessment. Walang documents na kailangan.</p><a class="btn" href="/loan-assessment/">Simulan ang AI Car Loan Application Assessment</a></aside>'
CONSENT='<label class="chk"><input type="checkbox" id="consent" required> <span>I agree to the collection and processing of my personal information under the Data Privacy Act of 2012 (RA 10173), as described in the <a href="/privacy/">Privacy Policy</a>, so Richard Cuagdan can contact me about this inquiry.</span></label><p class="er" id="e_consent" hidden>Please tick the consent box.</p>'

# ---------- HOME
feat="".join(f'''<a class="card mc" href="/cars/{m['slug']}/">{img(m['img'],f"Mitsubishi {m['name']}")}<div class="pad"><p class="kick">{e(m['cat'])}</p><h3>{m['name']}</h3><p class="low">{from_txt(m)}</p></div></a>''' for m in MODELS)
page("/","Mitsubishi Cars & Promos in SJDM, Bulacan | Mitsubishi Motors - SJ Legacy Motors",
 "Mitsubishi cars in San Jose del Monte, Bulacan: official SRPs for Xpander, Xforce, Destinator, Montero Sport, Triton, L300 and more, with all-in Zero DP and low-DP options.",
f'''<section class="hero"><div class="w hgrid"><div>
<p class="kick">Mitsubishi SJ Legacy Motors · San Jose del Monte, Bulacan</p>
<h1>Your next Mitsubishi, explained clearly and financed sensibly.</h1>
<p class="lead">I'm Richard Cuagdan, a Car Sales Executive at Mitsubishi SJ Legacy Motors. I help employed buyers, business owners and OFWs find a car and a monthly payment that fit their real budget.</p>
<p class="row"><a class="btn" href="/apply/">Apply for Financing</a> <a class="btn ghost" href="/budgetcalculator/">Compute my monthly</a> <a class="btn ghost" href="/promos/">See October promos</a></p>
<p class="tdl"><a href="/test-drive/">Book a test drive →</a></p>
</div>{img("xc_x3n","Mitsubishi Xpander Cross in Quartz White Pearl",eager=True,cls="himg")}</div></section>
<div class="w">{LACTA}</div>
<section class="sec"><div class="w">
<h2>The 2026 Mitsubishi lineup</h2>
<p class="sub">Starting SRP per model from the official price list. Tap a model for every variant, or <a href="/promos/">unlock this month's promo figures</a>.</p>
<div class="grid g3">{feat}</div>
<p class="note">{SRPNOTE}</p>
<p><a class="more" href="/cars/">View all current models →</a></p>
</div></section>
<section class="sec alt"><div class="w">
<h2>Why buy from Richard</h2>
<div class="grid g3">
<div class="feat"><h3>Straight answers on the monthly</h3><p>You see the SRP, the down payment and the monthly side by side before you commit to anything, so there are no surprises on release day.</p></div>
<div class="feat"><h3>Help with your bank application</h3><p>I walk you through the requirements for your situation, whether you're employed, running a business or working abroad, and follow up with the bank for you.</p></div>
<div class="feat"><h3>OFW families welcome</h3><p>Applying from abroad or buying for a family member at home is common. I coordinate with you online and with your family here in the Philippines.</p></div>
<div class="feat"><h3>Personal, hands-on service</h3><p>One point of contact from your first question through test drive, approval and release. Message me any time and I'll get back to you.</p></div>
<div class="feat"><h3>All-in packages</h3><p>Promos include LTO registration, insurance, chattel mortgage and more. <a href="/guides/what-all-in-includes/">Here's what "all-in" covers</a>.</p></div>
<div class="feat"><h3>Local to SJDM</h3><p>The showroom is in San Jose del Monte, Bulacan, close to Caloocan, Quezon City, Norzagaray and Santa Maria.</p></div>
</div></div></section>
<section class="sec alt"><div class="w"><h2>Popular guides for SJDM buyers</h2><div class="grid g3">
<a class="card pad mc" href="/mitsubishi-sjdm-bulacan/"><h3>Mitsubishi SJDM Bulacan</h3><p class="muted">Promos, test drive and directions</p></a>
<a class="card pad mc" href="/mitsubishi-casa-bulacan/"><h3>Mitsubishi casa Bulacan</h3><p class="muted">Buying at the authorized dealer</p></a>
<a class="card pad mc" href="/mitsubishi-zero-down-payment-promo/"><h3>Zero down payment promo</h3><p class="muted">How Zero DP works</p></a>
<a class="card pad mc" href="/mirage-g4-downpayment-and-monthly/"><h3>Mirage G4 downpayment and monthly</h3><p class="muted">First-car financing guide</p></a>
<a class="card pad mc" href="/triton-downpayment-and-monthly/"><h3>Triton downpayment and monthly</h3><p class="muted">Pickup financing guide</p></a>
<a class="card pad mc" href="/l300-monthly-installment/"><h3>L300 monthly installment</h3><p class="muted">For negosyo buyers</p></a>
</div></div></section>
<section class="sec"><div class="w split">
<div><div class="se"><img src="/assets/img/richard-300.webp" alt="Richard Cuagdan, Car Sales Executive at Mitsubishi SJ Legacy Motors SJDM" width="300" height="300" loading="lazy" decoding="async"><div><p class="kick">Your sales executive</p><p class="sen">Richard Cuagdan</p><p class="muted">Car Sales Executive, Mitsubishi SJ Legacy Motors</p></div></div><h2>Visit the showroom</h2><p><b>Mitsubishi SJ Legacy Motors</b><br>San Jose del Monte, Bulacan</p><p>Monday to Saturday, 8:00 AM to 5:00 PM</p><p>Message me before you visit so I can have your preferred unit ready for viewing or a test drive.</p><p class="row"><a class="btn" href="{MSG}" rel="noopener">Message on Messenger</a> <a class="btn ghost" href="/contact/">Contact details</a></p></div>
<div><h2>New to car financing?</h2><ul class="links"><li><a href="/guides/how-car-financing-works-philippines/">How car financing works in the Philippines</a></li><li><a href="/guides/car-loan-requirements/">Documents you need for a car loan</a></li><li><a href="/guides/zero-dp-vs-low-dp/">Zero DP vs low DP</a></li><li><a href="/blog/ofw-car-buying-guide/">OFW car-buying guide</a></li><li><a href="/mitsubishi-zero-down-payment-promo/">Mitsubishi zero down payment promo</a></li></ul></div>
</div></section>''', ld=[{"@type":"WebSite","@id":D+"/#site","name":"Mitsubishi Motors by Richard Dennis Cuagdan","url":D+"/"}])

# ---------- CARS index
cards="".join(f'''<a class="card mc" href="/cars/{m['slug']}/">{img(m['img'],f"Mitsubishi {m['name']}")}<div class="pad"><p class="kick">{e(m['cat'])}</p><h3>{m['name']}</h3><p class="muted">{len(m['variants'])} variant{'s' if len(m['variants'])>1 else ''}</p><p class="low">{from_txt(m)}</p></div></a>''' for m in MODELS)
page("/cars/","2026 Models & Prices | Mitsubishi Motors - SJ Legacy Motors",
 "Every current Mitsubishi model at SJ Legacy Motors, San Jose del Monte: Mirage G4, Xpander, Xpander Cross, Xforce, Destinator, Outlander PHEV, Montero Sport, Triton, L300 and Versa Van with official SRPs.",
f'''<section class="ph"><div class="w"><h1>2026 Mitsubishi models</h1><p class="lead">Browse every current model and variant with its official SRP. Promo packages are all-in and come with freebies.</p></div></section>
<section class="sec"><div class="w"><div class="grid g3">{cards}</div><p class="note">{SRPNOTE}</p><p class="row"><a class="btn" href="/promos/">Unlock October promos</a></p></div></section>''',
 crumbs=[("/","Home"),("/cars/","Cars")])

# ---------- model pages
EVM={k:f'<section class="sec"><div class="w"><h2>Financing guide</h2><p><a class="more" href="/{u}/">{t} →</a></p><p class="muted">How DP, term and monthly work, documents, income guide and this month\'s promo table. Also see the <a href="/mitsubishi-zero-down-payment-promo/">Mitsubishi zero down payment promo</a> guide.</p></div></section>' for k,u,t in [("mirage-g4","mirage-g4-downpayment-and-monthly","Mirage G4 downpayment and monthly"),("triton","triton-downpayment-and-monthly","Triton downpayment and monthly"),("l300","l300-monthly-installment","L300 monthly installment")]}
for m in MODELS:
    vs="".join(vcard(v,m) for v in m["variants"])
    sp="".join(f"<tr><th scope='row'>{e(a)}</th><td>{e(b)}</td></tr>" for a,b in m["specs"])
    rel=" · ".join(f'<a href="/cars/{x["slug"]}/">{x["name"]}</a>' for x in MODELS if x is not m)
    s0=srp_from(m)
    haspromo=any(v["promo"] for v in m["variants"])
    page(f"/cars/{m['slug']}/",f"{m['name']} 2026 Price | Mitsubishi Motors - SJ Legacy Motors",
     f"Mitsubishi {m['name']} at SJ Legacy Motors, San Jose del Monte: {len(m['variants'])} variant{'s' if len(m['variants'])>1 else ''}"+(f", official SRP from {f(s0)}" if s0 else "")+", all-in packages with freebies.",
    f'''<section class="ph"><div class="w hgrid"><div><p class="kick">{e(m['cat'])}</p><h1>Mitsubishi {m['name']}</h1><p class="lead">{e(m['blurb'])}</p><p>A good fit for {e(m['who'])}.</p><p class="row"><a class="btn" href="/apply/?unit={m['slug']}">Apply for this unit</a> <a class="btn ghost" href="/test-drive/?unit={m['slug']}">Book a Test Drive</a> <a class="btn ghost" href="/budgetcalculator/">Compute my monthly</a> {f'<a class="btn ghost" href="/promos/#{m["slug"]}">See promo</a>' if haspromo else f'<a class="btn ghost" href="{MSG}" rel="noopener">Ask for the latest promo</a>'}</p></div>{img(m['img'],f"Mitsubishi {m['name']}",eager=True,cls="himg")}</div></section>
<section class="sec"><div class="w"><h2>{m['name']} variants and prices</h2><p class="sub">Official SRP per variant. Promo down payment and monthly options are shared on the <a href="/promos/">promos page</a>.</p><div class="grid g3">{vs}</div><p class="note">{SRPNOTE}</p></div></section>
<section class="sec alt"><div class="w split"><div><h2>Key specs</h2><table class="spec">{sp}</table><p class="muted">Specs summarized from Mitsubishi Motors Philippines. Ask me for the full spec sheet of a specific variant.</p></div>
<div><h2>All-in includes</h2>{ALLIN_HTML}<h2>Freebies</h2>{FREE_HTML}<p class="muted">Freebies vary by variant; ask for details.</p></div></div></section>
{EVM.get(m['slug'],'')}<section class="sec"><div class="w"><h2>Compare other models</h2><p>{rel}</p></div></section>''',
    ld=offers_ld(m), ogtype="product", img=f"/assets/img/{m['img']}.webp",
    crumbs=[("/","Home"),("/cars/","Cars"),(f"/cars/{m['slug']}/",m['name'])])

# ---------- promos (gated, noindex; figures live only in JS data)
PD=[{"slug":m["slug"],"name":m["name"],"v":[{"n":v["n"],"srp":(v["promo"]["srp"] or v["srp"]),"opts":v["promo"]["opts"],"fuel":v["promo"]["fuel"]} for v in m["variants"] if v["promo"]]} for m in MODELS]
PD=[x for x in PD if x["v"]]
page("/promos/","October 2026 Promos | Mitsubishi Motors - SJ Legacy Motors",
 "Unlock this month's Mitsubishi promo figures at SJ Legacy Motors, San Jose del Monte: Zero DP and low-DP all-in options with freebies.",
f'''<section class="ph"><div class="w"><h1>October 2026 Mitsubishi promos</h1><p class="lead">See every down payment and monthly option this month, all-in on 60 months. Leave your name and mobile once to unlock them.</p></div></section>
<section class="sec"><div class="w">
<div id="gate" class="card pad formc nar">
<h2 class="h3">Unlock the promo figures</h2>
<form id="gf" novalidate>
<div class="fld"><label for="name">Full name</label><input id="name" autocomplete="name" required><p class="er" id="e_name" hidden>Please enter your name.</p></div>
<div class="fld"><label for="mobile">Mobile number</label><input id="mobile" type="tel" inputmode="tel" autocomplete="tel" placeholder="09XX XXX XXXX" required><p class="er" id="e_mobile" hidden>Enter a valid mobile number (09XXXXXXXXX or +country code).</p></div>
<div class="fld"><label for="unit">Unit of interest</label><select id="unit" required><option value="">Select a unit</option>{UNIT_OPTS}<option value="Not sure yet">Not sure yet</option></select><p class="er" id="e_unit" hidden>Please choose a unit.</p></div>
{CONSENT}
<button class="btn" type="submit" id="gb">Show the promos</button>
</form></div>
<div id="pv" hidden></div>
<noscript><p>Please enable JavaScript to view promo figures, or <a href="{MSG}">message Richard</a>.</p></noscript>
</div></section>
<section class="sec alt"><div class="w split"><div><h2>All-in includes</h2>{ALLIN_HTML}</div><div><h2>Freebies</h2>{FREE_HTML}</div></div></section>
<script src="/assets/lead.js" defer></script>
<script type="application/json" id="pd">{json.dumps(PD,ensure_ascii=False)}</script>
<script>
document.addEventListener('DOMContentLoaded',function(){{
var KEY='mp_promo_unlocked',MSG='{MSG}',NOTE={json.dumps(NOTE)};
function peso(n){{return '₱'+Number(n).toLocaleString('en-PH')}}
function esc(t){{return String(t).replace(/[&<>"]/g,function(c){{return {{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[c]}})}}
function show(){{var d=JSON.parse(document.getElementById('pd').textContent),h='';
 d.forEach(function(m){{h+='<section class="pm" id="'+m.slug+'"><h2>'+esc(m.name)+'</h2><div class="grid g3">';
  m.v.forEach(function(v){{h+='<article class="card pad"><h3>'+esc(v.n)+'</h3><p class="srp">SRP <b>'+peso(v.srp)+'</b></p><ul class="opts">'+v.opts.map(function(o){{return '<li><span>'+esc(o[0])+'</span><b>'+peso(o[1])+'<small>/mo</small></b></li>'}}).join('')+'</ul>'+(v.fuel?'<p class="fuel">Free fuel: <b>'+peso(v.fuel)+'</b></p>':'')+'<p class="muted">60 months, all-in.</p></article>'}});
  h+='</div></section>'}});
 h+='<p class="note">'+esc(NOTE)+'</p><p class="muted">Xforce, Outlander PHEV, Versa Van and other variants not listed: <a href="'+MSG+'" rel="noopener">ask for the latest promo</a>.</p><p class="row"><a class="btn" href="/apply/">Apply Now</a> <a class="btn ghost dk" href="'+MSG+'" rel="noopener">Message Richard on Messenger</a></p>';
 var pv=document.getElementById('pv');pv.innerHTML=h;pv.hidden=false;document.getElementById('gate').hidden=true;
 if(location.hash){{var t=document.getElementById(location.hash.slice(1));if(t)t.scrollIntoView()}}}}
var un=false;try{{un=localStorage.getItem(KEY)==='1'}}catch(_){{}}
if(un){{show();return}}
document.getElementById('gf').addEventListener('submit',function(ev){{ev.preventDefault();
 var n=document.getElementById('name').value.trim(),mo=document.getElementById('mobile').value.trim(),u=document.getElementById('unit').value,c=document.getElementById('consent').checked;
 var bad=[Lead.err('name',n.length<2),Lead.err('mobile',!Lead.okMobile(mo)),Lead.err('unit',!u),Lead.err('consent',!c)];
 if(bad.some(Boolean)){{var x=document.querySelector('.er:not([hidden])');if(x)x.scrollIntoView({{block:'center'}});return}}
 var b=document.getElementById('gb');b.disabled=true;b.textContent='Unlocking...';
 var L=Lead.base('promo_gate');L.name=n;L.mobile=mo.replace(/[\\s()-]/g,'');L.chosenUnit=u;L.seg='';
 Lead.send(L).then(function(){{try{{localStorage.setItem(KEY,'1')}}catch(_){{}}Lead.track(u);show();window.scrollTo(0,document.getElementById('pv').offsetTop-80)}});
}});
}});
</script>''', noindex=True, crumbs=[("/","Home"),("/promos/","Promos")])

# ---------- promos & tips hub
EVGL=[("/mitsubishi-zero-down-payment-promo/","Mitsubishi zero down payment promo"),("/mitsubishi-sjdm-bulacan/","Mitsubishi SJDM Bulacan"),("/mitsubishi-casa-bulacan/","Mitsubishi casa Bulacan"),("/mirage-g4-downpayment-and-monthly/","Mirage G4 downpayment and monthly"),("/triton-downpayment-and-monthly/","Triton downpayment and monthly"),("/l300-monthly-installment/","L300 monthly installment")]
EVG="".join(f'<a class="card pad mc" href="{p}"><p class="kick">Guide</p><h3>{n}</h3></a>' for p,n in EVGL)
LATEST="".join(f'<a class="card pad mc" href="/{a["base"]}/{a["slug"]}/"><p class="kick">{"Blog" if a["base"]=="blog" else "Tips"}</p><h3>{e(a["title"])}</h3><p class="muted">{e(a["desc"])}</p></a>' for a in sorted(LIVE,key=lambda a:a["date"],reverse=True))
HUB=[("/promos/","Promos","Unlock this month's promos and freebies","msbs_jh3","Mitsubishi Montero Sport Black Series"),
     ("/guides/","Guides","Financing, requirements and buying tips","xpgls_c31","Mitsubishi Xpander GLS"),
     ("/blog/","Blog","News, model comparisons and updates","de_x3n","Mitsubishi Destinator GT")]+([("/tips/","Tips","Checklists for road trips, PMS, insurance, LTO and car care","xpglx_x37","Mitsubishi Xpander GLX")] if TIPS else [])
page("/promos-tips/","Promos & Tips | Mitsubishi Motors - SJ Legacy Motors",
 "Start here for Mitsubishi promos at SJ Legacy Motors SJDM, plain-language car financing guides, and blog updates and model comparisons.",
f'''<section class="ph"><div class="w"><p class="kick">Promos &amp; Tips</p><h1>What would you like to check?</h1><p class="lead">Pick one to get started.</p></div></section>
<section class="sec"><div class="w"><div class="grid g3 hub">{"".join(f'<a class="card hubc" href="{p}">{img(k,a)}<div class="pad"><h2>{t}</h2><p>{d}</p><span class="more">Open {t} →</span></div></a>' for p,t,d,k,a in HUB)}</div></div></section>
<section class="sec"><div class="w"><h2>Buying guides</h2><p class="sub">Evergreen guides with this month's promo table.</p><div class="grid g3">{EVG}</div></div></section>
<section class="sec alt"><div class="w"><h2>Latest articles</h2><p class="sub">New blog posts and tips, newest first.</p><div class="grid g2">{LATEST}</div></div></section>''',
 crumbs=[("/","Home"),("/promos-tips/","Promos & Tips")])

# ---------- evergreen cross-links into existing articles
XL={"l300-price-philippines-2026":("l300-monthly-installment","L300 monthly installment guide"),"l300-negosyo-guide":("l300-monthly-installment","L300 monthly installment guide"),
 "l300-vs-triton-for-negosyo":("triton-downpayment-and-monthly","Triton downpayment and monthly guide"),"triton-for-business-and-farm":("triton-downpayment-and-monthly","Triton downpayment and monthly guide"),
 "triton-gx-2wd-at-first-pickup-guide":("triton-downpayment-and-monthly","Triton downpayment and monthly guide"),"zero-down-payment-car-philippines":("mitsubishi-zero-down-payment-promo","how the Mitsubishi zero down payment promo works"),
 "xpander-monthly-amortization":("mitsubishi-zero-down-payment-promo","Mitsubishi zero down payment promo guide"),"mitsubishi-dealer-bulacan":("mitsubishi-sjdm-bulacan","Mitsubishi SJDM Bulacan page"),
 "mitsubishi-test-drive-sjdm":("mitsubishi-sjdm-bulacan","Mitsubishi SJDM Bulacan page"),"mitsubishi-near-bulacan-towns":("mitsubishi-casa-bulacan","Mitsubishi casa Bulacan guide"),
 "pms-schedule-guide":("mitsubishi-casa-bulacan","Mitsubishi casa Bulacan guide"),"first-time-car-buyer-checklist":("mirage-g4-downpayment-and-monthly","Mirage G4 downpayment and monthly guide"),
 "minimum-salary-for-car-loan-philippines":("mirage-g4-downpayment-and-monthly","Mirage G4 downpayment and monthly guide")}
for _a in POSTS+TIPS:
    if _a["slug"] in XL:
        _u,_t=XL[_a["slug"]];_p=f'<p>See also: the <a href="/{_u}/">{_t}</a>.</p>\n';_i=_a["body"].rfind("<h2>Your next step</h2>")
        _a["body"]=_a["body"][:_i]+_p+_a["body"][_i:] if _i>=0 else _a["body"]+_p
# ---------- guides / blog
def xl(base):
    o={"guides":[("/blog/","Blog","Promo roundups, model comparisons and showroom tips."),("/promos/","Promos","Unlock this month's down payment and monthly options.")],
       "tips":[("/blog/","Blog","Longer guides on financing, OFW buying and model comparisons."),("/guides/","Guides","Plain-language guides to financing, documents and OFW buying.")],
       "blog":[("/guides/","Guides","Plain-language guides to financing, documents and OFW buying."),("/promos/","Promos","Unlock this month's down payment and monthly options.")]}[base]
    return '<section class="sec alt"><div class="w"><h2>More in Promos &amp; Tips</h2><div class="grid g2">'+"".join(f'<a class="card pad mc" href="{p}"><h3>{n} →</h3><p class="muted">{d}</p></a>' for p,n,d in o)+'</div></div></section>'
def articles(base,items,label,title,desc,intro):
    lst="".join(f'<li class="card pad"><h2 class="h3"><a href="/{base}/{a["slug"]}/">{e(a["title"])}</a></h2><p>{e(a["desc"])}</p>{f"<p class=muted>{a['date']}</p>" if base=="blog" else ""}</li>' for a in items)
    page(f"/{base}/",title,desc,f'<section class="ph"><div class="w"><h1>{label}</h1><p class="lead">{intro}</p></div></section><section class="sec"><div class="w"><ul class="grid g2 plain">{lst}</ul></div></section>'+xl(base),crumbs=[("/","Home"),(f"/{base}/",label)])
    for a in items:
        ld=[{"@type":"Article","headline":a["title"],"description":a["desc"],"datePublished":a["date"],"dateModified":a["date"],"author":{"@id":D+"/#richard"},"publisher":{"@id":D+"/#dealer"},"mainEntityOfPage":D+f"/{base}/{a['slug']}/","image":D+f"/assets/img/{a['img']}.webp"}]
        if a.get("by"):
            ld[0]["author"]={"@type":"Person","@id":D+"/#richard","name":"Richard Cuagdan","jobTitle":a["by"],"url":D+"/about/"}
        body=a["body"]
        for key,k,alt in FIGS.get(a["slug"],[]) if base!="guides" else []:
            w,h=ILLS[k];tag=f'<figure class="fig"><img src="/assets/img/ill/{k}.webp" alt="{e(alt)}" width="{w}" height="{h}" loading="lazy" decoding="async"></figure>\n'
            i=body.find("<h2>"+key);assert i>=0,(a["slug"],key);body=body[:i]+tag+body[i:]
        top=f'<div class="box ans"><p><b>Quick answer:</b> {e(a["answer"])}</p></div>' if a.get("answer") else ""
        fq=""
        if a.get("faq"):
            ld.append({"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":x}} for q,x in a["faq"]]})
            fq='<h2>Frequently asked questions</h2>'+"".join(f'<h3>{e(q)}</h3><p>{e(x)}</p>' for q,x in a["faq"])
        others="".join(f'<li><a href="/{base}/{b["slug"]}/">{e(b["title"])}</a></li>' for b in items if b is not a)
        page(f"/{base}/{a['slug']}/",(a["title"]+" | Mitsubishi Motors - SJ Legacy Motors" if len(a["title"])<=27 else a["title"]),a["desc"],
        f'''<article class="art"><div class="w nar"><header><p class="kick">{label}</p><h1>{e(a["title"])}</h1><p class="muted">By <a href="/about/">Richard Cuagdan</a>, {a.get("by","Car Sales Executive")} · <time datetime="{a["date"]}">{a["date"]}</time></p></header>
{img(a["img"],a["alt"],eager=True,cls="aimg")}
{top}
{body}
{LACTA}
{fq}
<aside class="box"><h2 class="h3">More {label.lower()}</h2><ul class="links">{others}</ul></aside></div></article>''',ld=ld,ogtype="article",img=f"/assets/img/{a['img']}.webp",
        crumbs=[("/","Home"),(f"/{base}/",label),(f"/{base}/{a['slug']}/",a["title"])])
articles("guides",GUIDES,"Guides","Car Buying Guides | Mitsubishi Motors - SJ Legacy Motors",
 "Plain-language guides to buying a car in the Philippines: how financing works, loan documents, Zero DP vs low DP, OFW buying and all-in packages.",
 "Practical, plain-language guides to help you plan your purchase before you visit the showroom.")
if TIPS: articles("tips",TIPS,"Tips","Car Tips & Checklists | Mitsubishi by Richard Cuagdan",
 "Quick, save-worthy checklists for Filipino drivers: road trips, fuel saving, LTO rules, weather car care and first-car buying.",
 "Short, practical checklists you can save before your next drive or car purchase.")
articles("blog",POSTS,"Blog","Blog | Mitsubishi Motors - SJ Legacy Motors",
 "Notes from the showroom floor at Mitsubishi SJ Legacy Motors, San Jose del Monte: monthly promo roundups, model comparisons and buying tips.",
 "Promo roundups, model comparisons and buying tips from the showroom floor.")

# ---------- about
page("/about/","About Richard Dennis Cuagdan | Mitsubishi Motors",
 "Richard Dennis Cuagdan is a Car Sales Executive at Mitsubishi SJ Legacy Motors in San Jose del Monte, Bulacan, helping employed buyers, business owners and OFW families.",
f'''<section class="ph"><div class="w"><h1>About Richard Dennis Cuagdan</h1><p class="lead">Car Sales Executive, Mitsubishi SJ Legacy Motors, San Jose del Monte, Bulacan</p></div></section>
<section class="sec"><div class="w nar">
<img class="pphoto" src="/assets/img/richard-600.webp" srcset="/assets/img/richard-300.webp 300w, /assets/img/richard-600.webp 600w" sizes="(min-width:640px) 300px, 240px" alt="Richard Cuagdan, Car Sales Executive at Mitsubishi SJ Legacy Motors SJDM" width="600" height="600" fetchpriority="high" decoding="async">
<p>I'm Richard Dennis Cuagdan, a Car Sales Executive at Mitsubishi SJ Legacy Motors, an authorized Mitsubishi dealership in San Jose del Monte, Bulacan.</p>
<!-- PLACEHOLDER: years of experience goes here (e.g. "I've been helping car buyers for X years.") -->
<p>Most of the people I work with fall into three groups: employed buyers looking for a monthly that fits their salary, business owners who need a dependable vehicle for work, and OFWs and their families who are buying from abroad or for loved ones at home. Each situation has different paperwork and different priorities, and I take time to understand yours before recommending a unit.</p>
<h2>How I work</h2>
<ul class="ticks"><li>I explain the SRP, down payment and monthly together so you can decide with complete numbers.</li><li>I tell you which documents your bank application needs and help you complete them.</li><li>I stay your single point of contact from inquiry to release.</li><li>I'm reachable on Messenger, including for clients in other time zones.</li></ul>
<h2>Good to know</h2>
<p>This is my personal sales website. It is not the official website of Mitsubishi Motors Philippines Corporation. Promo figures here are dealership offers and are always subject to bank approval.</p>
<p class="row"><a class="btn" href="{MSG}" rel="noopener">Message me</a> <a class="btn ghost dk" href="{FB}" target="_blank" rel="noopener">Follow us on Facebook</a> <a class="btn ghost dk" href="/contact/">Contact and showroom</a></p>
<p>Call or text me: <a href="tel:{TEL}">{TELD}</a>. Showroom: {ADDR}.</p>
</div></section>''', ld=[{"@type":"ProfilePage","mainEntity":{"@id":D+"/#richard"}}], crumbs=[("/","Home"),("/about/","About")])

# ---------- apply
page("/apply/","Apply for a Mitsubishi | Mitsubishi Motors - SJ Legacy Motors",
 "Apply online for a Mitsubishi at SJ Legacy Motors, San Jose del Monte: send your details, choose cash or financing, and Richard Cuagdan will get back to you.",
f'''<section class="ph"><div class="w"><h1>Apply for your Mitsubishi</h1><p class="lead">Send your details below and I'll get back to you with the right unit, the latest promo and the documents you need. Prefer to check your budget first? Use the <a href="/budgetcalculator/" style="color:#fff">budget calculator</a>.</p></div></section>
<section class="sec"><div class="w split">
<div>
<div id="af-wrap" class="card pad formc">
<h2 class="h3">Application form</h2>
<form id="af" novalidate>
<div class="fld"><label for="name">Full name *</label><input id="name" autocomplete="name" required><p class="er" id="e_name" hidden>Please enter your name.</p></div>
<div class="fld"><label for="mobile">Mobile number *</label><input id="mobile" type="tel" inputmode="tel" autocomplete="tel" placeholder="09XX XXX XXXX" required><p class="er" id="e_mobile" hidden>Enter a valid mobile number (09XXXXXXXXX or +country code).</p></div>
<div class="fld"><label for="email">Email (optional)</label><input id="email" type="email" autocomplete="email"><p class="er" id="e_email" hidden>Please check your email address.</p></div>
<div class="fld"><label for="loc">City / location *</label><input id="loc" autocomplete="address-level2" placeholder="e.g. San Jose del Monte, Bulacan" required><p class="er" id="e_loc" hidden>Please enter your city or location.</p></div>
<div class="fld"><label for="unit">Unit of interest *</label><select id="unit" required><option value="">Select a unit</option>{UNIT_OPTS}<option value="Not sure yet">Not sure yet</option></select><p class="er" id="e_unit" hidden>Please choose a unit.</p></div>
<div class="fld"><label for="pay">Preferred payment *</label><select id="pay" required><option value="">Select</option><option>Financing</option><option>Cash</option></select><p class="er" id="e_pay" hidden>Please choose a payment option.</p></div>
<div class="fld"><label for="emp">Employment type *</label><select id="emp" required><option value="">Select</option><option value="Employed">Employed</option><option value="Business owner">Business owner</option><option value="OFW">OFW</option><option value="OFW family">OFW family</option></select><p class="er" id="e_emp" hidden>Please choose your employment type.</p></div>
<div class="fld"><label for="inc">Gross monthly income *</label><select id="inc" required><option value="">Select a range</option><option data-min="0">Below ₱30,000</option><option data-min="30000">₱30,000 to ₱49,999</option><option data-min="50000">₱50,000 to ₱79,999</option><option data-min="80000">₱80,000 to ₱119,999</option><option data-min="120000">₱120,000 to ₱199,999</option><option data-min="200000">₱200,000 and above</option></select><p class="er" id="e_inc" hidden>Please choose an income range.</p></div>
<div class="fld"><label for="tl">When do you plan to buy? *</label><select id="tl" required><option value="">Select</option><option>This month</option><option>Within 1 to 3 months</option><option>Within 3 to 6 months</option><option>Just checking options</option></select><p class="er" id="e_tl" hidden>Please choose a timeline.</p></div>
<div class="fld"><label for="msg">Message (optional)</label><textarea id="msg" rows="4" maxlength="1000"></textarea></div>
{CONSENT}
<button class="btn" type="submit" id="ab">Send my application</button>
</form></div>
<div id="thanks" class="card pad formc" hidden><h2 class="h3">Thank you!</h2><p>Your details were sent. I'll get in touch with you soon. Reference: <b id="ref"></b></p><p>For a faster reply, message me on Messenger with your reference number.</p><p><a class="btn" href="{MSG}" rel="noopener">Message Richard on Messenger</a></p></div>
</div>
<div>
<h2>What happens next</h2>
<ol class="steps"><li><h3>I review your details</h3><p>I check which unit and payment option fit what you shared.</p></li>
<li><h3>We talk</h3><p>I'll message or call you to confirm the unit, color and terms and share this month's promo.</p></li>
<li><h3>Submit documents</h3><p>For financing, send the requirements for your situation. I'll check them before they go to the bank.</p></li>
<li><h3>Approval and release</h3><p>Once the bank approves (or once payment is settled for cash), we schedule your release.</p></li></ol>
<h2>Typical documents for financing</h2>
<ul class="ticks"><li>Two valid government IDs with matching signatures</li><li>Proof of billing</li><li>Employed: certificate of employment with compensation, payslips or ITR</li><li>Business owner: DTI or SEC registration, business permit, bank statements, ITR or financial statements</li><li>OFW: employment contract, payslips or remittance records, and co-borrower or attorney-in-fact details</li></ul>
<p>Full list: <a href="/guides/car-loan-requirements/">car loan requirements guide</a>.</p>
<p class="muted">Financing is subject to bank approval.</p>
</div></div></section>
<script src="/assets/lead.js" defer></script>
<script>
document.addEventListener('DOMContentLoaded',function(){{
var $=function(i){{return document.getElementById(i)}};
var q=new URLSearchParams(location.search).get('unit');if(q){{var k=q.replace(/[^a-z0-9-]/gi,''),o=document.querySelector('#unit option[data-id="'+k+'"]')||document.querySelector('#unit option[data-model="'+k+'"]');if(o)o.selected=true}}
$('af').addEventListener('submit',function(ev){{ev.preventDefault();
 var v=function(i){{return $(i).value.trim()}};
 var em=v('email');
 var bad=[Lead.err('name',v('name').length<2),Lead.err('mobile',!Lead.okMobile(v('mobile'))),Lead.err('email',!!em&&!/^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(em)),Lead.err('loc',!v('loc')),Lead.err('unit',!v('unit')),Lead.err('pay',!v('pay')),Lead.err('emp',!v('emp')),Lead.err('inc',!v('inc')),Lead.err('tl',!v('tl')),Lead.err('consent',!$('consent').checked)];
 if(bad.some(Boolean)){{var x=document.querySelector('.er:not([hidden])');if(x)x.scrollIntoView({{block:'center'}});return}}
 var b=$('ab');b.disabled=true;b.textContent='Sending...';
 var emp=v('emp'),inc=$('inc').selectedOptions[0];
 var L=Lead.base('apply_form');
 L.name=v('name');L.mobile=v('mobile').replace(/[\\s()-]/g,'');L.location=v('loc');L.chosenUnit=v('unit');L.dpPreference=v('pay');L.employment=emp;
 L.seg=emp==='OFW'?'ofw_abroad':(emp==='OFW family'?'ofw_family':'local');L.income=Number(inc.dataset.min)||0;L.timeline=v('tl');
 L.usage=['Income range: '+inc.textContent,em?'Email: '+em:'',v('msg')?'Message: '+v('msg'):''].filter(Boolean).join(' | ');
 Lead.send(L).then(function(){{Lead.track(L.chosenUnit);$('ref').textContent=L.leadId;$('af-wrap').hidden=true;$('thanks').hidden=false;$('thanks').scrollIntoView({{block:'center'}})}});
}});
}});
</script>''', crumbs=[("/","Home"),("/apply/","Apply")])

# ---------- test drive
TDU=[{"id":v["id"],"m":m["slug"],"model":m["name"],"n":v["n"],"srp":srp_txt(v),"img":v["img"]} for m in MODELS for v in m["variants"]]
rows_td="".join(f'''<div class="tdrow"><h3>{e(m["name"])}</h3><div class="tdtrack" role="radiogroup" aria-label="{e(m["name"])} variants">'''+"".join(f'''<button type="button" class="tdc" role="radio" aria-checked="false" data-id="{v["id"]}">{img(v["img"],"Mitsubishi "+v["n"])}<span class="tdn">{e(v["n"])}</span><span class="tds">SRP {srp_txt(v)}</span></button>''' for v in m["variants"])+'</div></div>' for m in MODELS)
TIMES=[("08:00","8:00 AM"),("09:00","9:00 AM"),("10:00","10:00 AM"),("11:00","11:00 AM"),("13:00","1:00 PM"),("14:00","2:00 PM"),("15:00","3:00 PM"),("16:00","4:00 PM")]
page("/test-drive/","Book a Test Drive | Mitsubishi Motors - SJ Legacy Motors",
 "Book a Mitsubishi test drive at SJ Legacy Motors, San Jose del Monte, Bulacan. Pick your unit, choose a date and time from Monday to Saturday, and Richard will confirm.",
f'''<section class="ph"><div class="w"><h1>Book a test drive</h1><p class="lead">Choose a unit, pick a schedule, and I'll have it ready for you at Mitsubishi SJ Legacy Motors, San Jose del Monte.</p></div></section>
<section class="sec"><div class="w">
<ol class="tdsteps" aria-label="Progress"><li id="st1" class="on">1. Choose a unit</li><li id="st2">2. Your schedule</li><li id="st3">3. Confirmed</li></ol>
<div id="s1"><h2>Which Mitsubishi would you like to drive?</h2><p class="sub">Swipe each row to see every variant. SRP shown; ask me for this month's promo.</p>{rows_td}
<div id="go1" class="tdgo" hidden><button class="btn" type="button" id="next1">Test drive this unit</button></div></div>
<div id="s2" hidden>
<div class="tdsel card"><img id="selimg" src="" alt="" width="640" height="427"><div class="pad"><p class="kick">Your unit</p><h2 class="h3" id="selname"></h2><p class="muted" id="selsrp"></p><div id="chips" class="chips" role="radiogroup" aria-label="Choose a variant" hidden></div><p><a href="#" id="chg">Change unit</a></p></div></div>
<div class="card pad formc"><h2 class="h3">Your schedule and details</h2>
<form id="tf" novalidate>
<div class="fld"><label for="name">Full name *</label><input id="name" autocomplete="name" required><p class="er" id="e_name" hidden>Please enter your name.</p></div>
<div class="fld"><label for="mobile">Mobile number *</label><input id="mobile" type="tel" inputmode="tel" autocomplete="tel" placeholder="09XX XXX XXXX" required><p class="er" id="e_mobile" hidden>Enter a valid PH mobile number (09XXXXXXXXX or +639XXXXXXXXX).</p></div>
<div class="fld"><label for="email">Email (optional)</label><input id="email" type="email" autocomplete="email"><p class="er" id="e_email" hidden>Please check your email address.</p></div>
<div class="fld"><label for="date">Preferred date *</label><input id="date" type="date" required><p class="muted" style="margin:6px 0 0">Monday to Saturday only, from tomorrow up to 60 days ahead.</p><p class="er" id="e_date" hidden>Please choose a Monday to Saturday date within the next 60 days (no Sundays).</p></div>
<div class="fld"><label for="time">Preferred time *</label><select id="time" required><option value="">Select a time</option>{"".join(f'<option value="{a}">{b}</option>' for a,b in TIMES)}</select><p class="er" id="e_time" hidden>Please choose a time slot.</p></div>
<div class="fld"><p class="fl">Location</p><p><b>Mitsubishi SJ Legacy Motors</b><br>San Jose del Monte, Bulacan<br><span class="muted">Showroom hours: Monday to Saturday, 8:00 AM to 5:00 PM</span></p></div>
<div class="fld"><label for="notes">Notes (optional)</label><textarea id="notes" rows="3" maxlength="1000" placeholder="e.g. preferred color, number of passengers joining"></textarea></div>
<label class="chk"><input type="checkbox" id="lic" required> <span>I have a valid driver's license and will bring it to the test drive.</span></label><p class="er" id="e_lic" hidden>A valid driver's license is required for the test drive.</p>
{CONSENT}
<button class="btn" type="submit" id="tb">Book my test drive</button>
</form></div></div>
<div id="s3" hidden><div class="card tdsel"><img id="cimg" src="" alt="" width="640" height="427"><div class="pad">
<p class="kick">Test drive request received</p><h2 id="cname"></h2>
<p><b id="cwhen"></b><br>Mitsubishi SJ Legacy Motors, San Jose del Monte, Bulacan</p>
<p>Richard will message you to confirm your schedule. Please bring your valid driver's license.</p>
<p>Reference: <b id="cref"></b></p>
<p class="row"><a class="btn" id="gcal" href="#" target="_blank" rel="noopener">Add to Google Calendar</a> <a class="btn ghost dk" href="{MSG}" rel="noopener">Message Richard on Messenger</a></p></div></div></div>
</div></section>
<script src="/assets/lead.js" defer></script>
<script type="application/json" id="tdu">{json.dumps(TDU,ensure_ascii=False)}</script>
<script>
document.addEventListener('DOMContentLoaded',function(){{
var $=function(i){{return document.getElementById(i)}},U=JSON.parse($('tdu').textContent),sel=null;
var TL={json.dumps(dict(TIMES))};
function step(n){{[1,2,3].forEach(function(i){{$('s'+i).hidden=i!==n;$('st'+i).className=i<=n?'on':''}});window.scrollTo(0,0)}}
function pick(id,scroll){{sel=U.filter(function(u){{return u.id===id}})[0];if(!sel)return;
 document.querySelectorAll('.tdc').forEach(function(c){{var on=c.dataset.id===id;c.classList.toggle('sel',on);c.setAttribute('aria-checked',on)}});
 var c=document.querySelector('.tdc[data-id="'+id+'"]'),t=c.parentElement,g=$('go1');t.parentElement.appendChild(g);g.hidden=false;$('next1').textContent='Test drive this unit: '+sel.n;
 if(scroll){{t.scrollTo({{left:Math.max(0,c.offsetLeft-(t.clientWidth-c.offsetWidth)/2),behavior:'smooth'}});setTimeout(function(){{g.scrollIntoView({{block:'nearest',behavior:'smooth'}})}},250)}}}}
function toStep2(){{$('selimg').src='/assets/img/'+sel.img+'.webp';$('selimg').alt='Mitsubishi '+sel.n;$('selname').textContent=sel.n;$('selsrp').textContent='SRP '+sel.srp;step(2)}}
document.querySelectorAll('.tdc').forEach(function(c){{c.addEventListener('click',function(){{pick(c.dataset.id,true)}})}});
$('next1').addEventListener('click',function(){{if(sel)toStep2()}});
$('chg').addEventListener('click',function(e){{e.preventDefault();$('chips').hidden=true;step(1);var c=document.querySelector('.tdc.sel');if(c)c.scrollIntoView({{block:'center'}})}});
function ymd(d){{return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0')}}
var t0=new Date();t0.setHours(0,0,0,0);var mn=new Date(t0);mn.setDate(mn.getDate()+1);var mx=new Date(t0);mx.setDate(mx.getDate()+60);
if(mn.getDay()===0)mn.setDate(mn.getDate()+1);
$('date').min=ymd(mn);$('date').max=ymd(mx);
function badDate(v){{if(!v)return true;var p=v.split('-'),d=new Date(+p[0],p[1]-1,+p[2]);return d.getDay()===0||d<mn||d>mx}}
$('date').addEventListener('change',function(){{Lead.err('date',badDate(this.value))}});
var q=new URLSearchParams(location.search).get('unit');
if(q){{var k=q.replace(/[^a-z0-9-]/gi,''),ex=U.filter(function(u){{return u.id===k}})[0],ms=U.filter(function(u){{return u.m===k}});
 if(ex){{pick(ex.id,false);toStep2()}}
 else if(ms.length){{pick(ms[0].id,false);toStep2();if(ms.length>1){{var ch=$('chips');
  ch.innerHTML=ms.map(function(u){{return '<button type="button" class="chip" role="radio" data-id="'+u.id+'">'+u.n.replace(u.model+' ','')+'</button>'}}).join('');ch.hidden=false;
  var mark=function(){{ch.querySelectorAll('.chip').forEach(function(c){{var on=c.dataset.id===sel.id;c.classList.toggle('on',on);c.setAttribute('aria-checked',on)}})}};mark();
  ch.querySelectorAll('.chip').forEach(function(c){{c.addEventListener('click',function(){{pick(c.dataset.id,false);toStep2();mark()}})}})}}}}}}
$('tf').addEventListener('submit',function(ev){{ev.preventDefault();
 var v=function(i){{return $(i).value.trim()}},em=v('email'),mob=v('mobile').replace(/[\\s()-]/g,'');
 var bad=[Lead.err('name',v('name').length<2),Lead.err('mobile',!/^(09\\d{{9}}|\\+639\\d{{9}})$/.test(mob)),Lead.err('email',!!em&&!/^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(em)),Lead.err('date',badDate(v('date'))),Lead.err('time',!v('time')),Lead.err('lic',!$('lic').checked),Lead.err('consent',!$('consent').checked)];
 if(bad.some(Boolean)){{var x=document.querySelector('#s2 .er:not([hidden])');if(x)x.scrollIntoView({{block:'center'}});return}}
 var b=$('tb');b.disabled=true;b.textContent='Booking...';
 var dt=v('date'),tm=v('time'),tl=TL[tm];
 var L=Lead.base('test_drive');L.name=v('name');L.mobile=mob;L.chosenUnit=sel.n;L.unitParam=sel.id;L.location='Mitsubishi SJ Legacy Motors, San Jose del Monte, Bulacan';
 L.timeline='TD '+dt+' '+tl;L.usage=['Driver\\'s license: yes',em?'Email: '+em:'',v('notes')?'Notes: '+v('notes'):''].filter(Boolean).join(' | ');
 Lead.send(L).then(function(){{
  if(!Lead.skipped()){{try{{if(typeof window.fbq==='function')window.fbq('track','Schedule',{{content_name:sel.n}})}}catch(_){{}}
  try{{if(typeof window.gtag==='function')window.gtag('event','book_test_drive',{{unit:sel.n,date:dt}})}}catch(_){{}}}}
  var s=dt.replace(/-/g,'')+'T'+tm.replace(':','')+'00',h=String(+tm.slice(0,2)+1).padStart(2,'0'),en=dt.replace(/-/g,'')+'T'+h+tm.slice(3)+'00';
  var g='https://calendar.google.com/calendar/render?action=TEMPLATE&text='+encodeURIComponent('Mitsubishi test drive: '+sel.n)+'&dates='+s+'/'+en+'&ctz=Asia/Manila&location='+encodeURIComponent('Mitsubishi SJ Legacy Motors, San Jose del Monte, Bulacan')+'&details='+encodeURIComponent('Test drive with Richard Cuagdan. Bring your valid driver\\'s license. Ref: '+L.leadId+'. Messenger: https://m.me/504759566043148');
  $('gcal').href=g;$('cimg').src='/assets/img/'+sel.img+'.webp';$('cimg').alt='Mitsubishi '+sel.n;$('cname').textContent=sel.n;
  var p=dt.split('-');$('cwhen').textContent=new Date(+p[0],p[1]-1,+p[2]).toLocaleDateString('en-PH',{{weekday:'long',year:'numeric',month:'long',day:'numeric'}})+', '+tl;
  $('cref').textContent=L.leadId;step(3)}});
}});
}});
</script>''', crumbs=[("/","Home"),("/test-drive/","Book a Test Drive")])

# ---------- contact
page("/contact/","Contact | Mitsubishi Motors - SJ Legacy Motors",
 "Message Richard Cuagdan on Messenger or visit Mitsubishi SJ Legacy Motors in San Jose del Monte, Bulacan, Monday to Saturday, 8 AM to 5 PM.",
f'''<section class="ph"><div class="w"><h1>Contact</h1><p class="lead">The quickest way to reach me is Messenger.</p><div class="se"><img src="/assets/img/richard-300.webp" alt="Richard Cuagdan, Car Sales Executive at Mitsubishi SJ Legacy Motors SJDM" width="300" height="300" loading="lazy" decoding="async"><div><p class="kick">Your sales executive</p><p class="sen">Richard Cuagdan</p><p class="sem">Car Sales Executive, Mitsubishi SJ Legacy Motors</p></div></div></div></section>
<section class="sec"><div class="w grid g3">
<div class="card pad"><h2 class="h3">Messenger</h2><p>Send a message any time. I'll reply as soon as I can.</p><p><a class="btn" href="{MSG}" rel="noopener">Open Messenger</a></p></div>
<div class="card pad"><h2 class="h3">Facebook</h2><p>Follow the page for new arrivals, promos and updates.</p><p><a class="btn ghost dk" href="{FB}" target="_blank" rel="noopener">Follow us on Facebook</a></p></div>
<div class="card pad"><h2 class="h3">Call or text</h2><p>Mobile: <a href="tel:{TEL}">{TELD}</a></p><p><a class="btn" href="tel:{TEL}">Call {TELD}</a></p></div>
<div class="card pad"><h2 class="h3">Showroom</h2><address>{ADDR_HTML}</address><p><a href="https://www.google.com/maps/dir/?api=1&amp;destination={MAPQ}" target="_blank" rel="noopener">Get directions</a></p><p>Monday to Saturday<br>8:00 AM to 5:00 PM</p></div>
<div class="card pad"><h2 class="h3">Apply online</h2><p>Send your details and preferred unit, and I'll get back to you with the latest promo.</p><p><a class="btn" href="/apply/">Apply Now</a></p></div>
<div class="card pad"><h2 class="h3">Compute first</h2><p>See your all-in monthly options before you visit.</p><p><a class="btn ghost" href="/budgetcalculator/">Compute my monthly</a></p></div>
</div></section>
<section class="sec"><div class="w"><h2>Find the showroom</h2><p>{ADDR}</p><iframe title="Map to Mitsubishi SJ Legacy Motors, San Jose del Monte" src="https://www.google.com/maps?q={MAPQ}&amp;output=embed" width="100%" height="380" style="border:0;border-radius:12px" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe><p><a class="btn" href="https://www.google.com/maps/dir/?api=1&amp;destination={MAPQ}" target="_blank" rel="noopener">Get directions</a></p></div></section>''', ld=[{"@type":"ContactPage","about":{"@id":D+"/#dealer"}}], crumbs=[("/","Home"),("/contact/","Contact")])

exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"landing.py")).read())
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"loanapp.py")).read())
# ---------- OFW guide merge: redirect old URL
os.makedirs(R+"/guides/ofw-car-buying-guide",exist_ok=True)
open(R+"/guides/ofw-car-buying-guide/index.html","w").write('<!doctype html><html lang="en-PH"><head><meta charset="utf-8"><title>Moved: OFW Car Loan Guide</title><link rel="canonical" href="'+D+'/blog/ofw-car-buying-guide/"><meta name="robots" content="noindex,follow"><meta http-equiv="refresh" content="0; url=/blog/ofw-car-buying-guide/"></head><body><p>This guide has moved to <a href="/blog/ofw-car-buying-guide/">the OFW car loan guide</a>.</p></body></html>\n')
# ---------- /preview-loan/ retired: redirect stub to the live assessment
os.makedirs(R+"/preview-loan",exist_ok=True)
open(R+"/preview-loan/index.html","w").write('<!doctype html><html lang="en-PH"><head><meta charset="utf-8"><title>Moved: AI Car Loan Application Assessment</title><link rel="canonical" href="'+D+'/loan-assessment/"><meta name="robots" content="noindex,follow"><meta http-equiv="refresh" content="0; url=/loan-assessment/"><script>location.replace("/loan-assessment/"+location.search)</script></head><body><p>Moved to <a href="/loan-assessment/">the AI Car Loan Application Assessment</a>.</p></body></html>\n')
# ---------- 404
page("/__404/","Page not found | Mitsubishi Motors - SJ Legacy Motors","The page you were looking for could not be found.",
 '<section class="ph"><div class="w"><h1>Page not found</h1><p class="lead">That page doesn\'t exist or has moved.</p><p class="row"><a class="btn" href="/">Go to Home</a> <a class="btn ghost" href="/cars/">Browse cars</a></p></div></section>',noindex=True)
s=open(R+"/__404/index.html").read().replace('<link rel="canonical" href="https://mitsubishipromos.online/__404/">\n','').replace('<meta property="og:url" content="https://mitsubishipromos.online/__404/">\n','')
open(R+"/404.html","w").write(s); os.remove(R+"/__404/index.html"); os.rmdir(R+"/__404")

# ---------- root redirect injection
s=open(R+"/index.html").read()
rd="<script>(function(){try{var q=location.search;if(!q)return;var p=new URLSearchParams(q);var sg=(p.get('seg')||'').toLowerCase();if(/^(local|ofw_abroad|ofw_family)$/.test(sg)||p.has('adset')||/^ad\\d+$/i.test(p.get('utm_content')||'')){location.replace('/budgetcalculator/'+q+location.hash);}}catch(_){}})();</script>\n"
s=s.replace('<meta charset="utf-8">\n','<meta charset="utf-8">\n'+rd,1); open(R+"/index.html","w").write(s)

# ---------- sitemap/robots
PAGES.append("/privacy/")
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>{D}{p}</loc><lastmod>2026-10-21</lastmod></url>\n" for p in PAGES)+"</urlset>\n"
open(R+"/sitemap.xml","w").write(sm)
AI_BOTS=["GPTBot","OAI-SearchBot","ChatGPT-User","PerplexityBot","ClaudeBot","Google-Extended","Bingbot"]
open(R+"/robots.txt","w").write(f"User-agent: *\nAllow: /\n\n"+"".join(f"User-agent: {b}\nAllow: /\n\n" for b in AI_BOTS)+f"Sitemap: {D}/sitemap.xml\n")
def _ll(items,base): return "".join(f"- [{a['title']}]({D}/{base}/{a['slug']}/): {a['desc']}\n" for a in items)
open(R+"/llms.txt","w").write(f"""# Mitsubishi Motors by Richard Cuagdan

> Personal sales website of Richard Cuagdan, Mitsubishi Sales Executive at Mitsubishi SJ Legacy Motors, San Jose del Monte (SJDM), Bulacan, Philippines. Not the official Mitsubishi Motors Philippines website. Prices shown are official SRPs; promos are subject to bank approval.

## Key pages
- [Home]({D}/): Mitsubishi lineup and SRPs
- [Cars]({D}/cars/): every current model and variant with SRP
- [Budget calculator]({D}/budgetcalculator/): match a unit to your income
- [Book a test drive]({D}/test-drive/): Monday to Saturday, 8 AM to 5 PM
- [Apply]({D}/apply/): financing or cash application
- [About]({D}/about/) and [Contact]({D}/contact/)

## Buying guides (evergreen, with dated monthly promo table)
"""+"".join(f"- [{a['title']}]({D}/{a['slug']}/): {a['desc']}\n" for a in LANDINGS)+f"""
## Contact
- Sales executive: Richard Dennis Cuagdan, Car Sales Executive
- Mobile (call or text): {TELD} ({TEL})
- Showroom: {ADDR}
- Hours: Monday to Saturday, 8:00 AM to 5:00 PM
- Directions: https://www.google.com/maps/dir/?api=1&destination={MAPQ}

## Models
"""+"".join(f"- [{m['name']}]({D}/cars/{m['slug']}/): {m['blurb']}\n" for m in MODELS)+"\n## Tips\n"+_ll(TIPS,"tips")+"\n## Blog\n"+_ll(POSTS,"blog")+"\n## Guides\n"+_ll(GUIDES,"guides"))
print(len(PAGES),"pages")
