import json, os, html, sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from data import *
from content import GUIDES, POSTS
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES=[]
GA='''<!-- Google tag (gtag.js) GA4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-T89CH2TJS6"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-T89CH2TJS6');</script>'''
DEALER={"@type":"AutoDealer","@id":D+"/#dealer","name":"Mitsubishi SJ Legacy Motors","brand":{"@type":"Brand","name":"Mitsubishi"},
 "address":{"@type":"PostalAddress","addressLocality":"San Jose del Monte","addressRegion":"Bulacan","addressCountry":"PH"},
 "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"08:00","closes":"17:00"}],
 "url":D+"/"}
PERSON={"@type":"Person","@id":D+"/#richard","name":"Richard Cuagdan","jobTitle":"Car Sales Executive","image":D+"/assets/img/richard-600.webp","worksFor":{"@id":D+"/#dealer"},"url":D+"/about/","sameAs":[MSG]}
NAV=[("/","Home"),("/cars/","Cars"),("/promos/","Promos"),("/guides/","Guides"),("/blog/","Blog"),("/about/","About"),("/contact/","Contact")]
def e(s): return html.escape(s,quote=True)
def page(path,title,desc,body,ld=None,ogtype="website",img="/assets/img/xpglx_x37.webp",noindex=False,crumbs=None):
    url=D+path
    graph=[DEALER,PERSON]+(ld or [])
    if crumbs:
        graph.append({"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":D+p} for i,(p,n) in enumerate(crumbs)]})
    nav="".join(f'<a href="{p}"{" aria-current=\"page\"" if (p==path or (p!="/" and path.startswith(p))) else ""}>{n}</a>' for p,n in NAV)
    bc=""
    if crumbs:
        bc='<nav class="bc" aria-label="Breadcrumb"><div class="w">'+" <span>/</span> ".join(f'<a href="{p}">{e(n)}</a>' for p,n in crumbs[:-1])+f' <span>/</span> <span aria-current="page">{e(crumbs[-1][1])}</span></div></nav>'
    h=f'''<!doctype html>
<html lang="en-PH">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{GA}
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{'<meta name="robots" content="noindex">' if noindex else ''}
<link rel="canonical" href="{url}">
<meta property="og:type" content="{ogtype}">
<meta property="og:site_name" content="Richard Cuagdan · Mitsubishi SJ Legacy Motors">
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
<a class="brand" href="/"><svg viewBox="0 0 24 24" width="26" height="26" aria-hidden="true"><path fill="#E60012" d="M12 2l3.2 5.5L12 13 8.8 7.5zM5.6 13l3.2-5.5L12 13l-3.2 5.5H2.4zM18.4 13l-3.2-5.5L12 13l3.2 5.5h6.4z"/></svg><span><b>Richard Cuagdan</b><small>Mitsubishi SJ Legacy Motors</small></span></a>
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
<div><p class="fb">Richard Cuagdan</p><p>Car Sales Executive, Mitsubishi SJ Legacy Motors<br>San Jose del Monte, Bulacan, Philippines</p><p>Showroom hours: Monday to Saturday, 8:00 AM to 5:00 PM</p></div>
<div><p class="fb">Explore</p><p><a href="/cars/">Cars</a> · <a href="/promos/">Promos</a> · <a href="/guides/">Guides</a> · <a href="/blog/">Blog</a></p><p><a href="/apply/">Apply</a> · <a href="/about/">About</a> · <a href="/contact/">Contact</a> · <a href="/privacy/">Privacy</a></p></div>
</div>
<p class="disc">Richard Cuagdan is a sales executive of Mitsubishi SJ Legacy Motors, an authorized Mitsubishi dealership. This is his personal sales website and is not the official website of Mitsubishi Motors Philippines Corporation. Prices, monthly amortizations and freebies are dealer promos, subject to bank approval and change without notice. Mitsubishi names and logos belong to their respective owners.</p>
<p class="cp">© 2026 Richard Cuagdan</p>
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
    srp=v.get("srpl") or f(v["srp"])
    opts="".join(f'<li><span>{e(l)}</span><b>{f(mo)}<small>/mo</small></b></li>' for l,mo in v["opts"])
    fuel=f'<p class="fuel">Free fuel: <b>{f(v["fuel"])}</b></p>' if v["fuel"] else ""
    return f'''<article class="card vc">{img(v["img"],f"Mitsubishi {v['n']}")}
<div class="pad"><h3>{e(v["n"])}</h3><p class="srp">SRP <b>{e(srp)}</b></p>
<ul class="opts">{opts}</ul>{fuel}<p class="muted">60 months, all-in.</p></div></article>'''

def offers_ld(m):
    out=[]
    for v in m["variants"]:
        out.append({"@type":"Product","name":"Mitsubishi "+v["n"],"brand":{"@type":"Brand","name":"Mitsubishi"},"image":D+"/assets/img/"+v["img"]+".webp","category":m["cat"],
          "offers":{"@type":"Offer","price":v["srp"],"priceCurrency":"PHP","priceValidUntil":"2026-10-31","availability":"https://schema.org/InStock","itemCondition":"https://schema.org/NewCondition","seller":{"@id":D+"/#dealer"},"url":D+f"/cars/{m['slug']}/"}})
    return out

ALLIN_HTML="<ul class='ticks'>"+"".join(f"<li>{x}</li>" for x in ALLIN)+"</ul>"
FREE_HTML="<ul class='ticks'>"+"".join(f"<li>{x}</li>" for x in FREEBIES)+"</ul>"

# ---------- HOME
feat="".join(f'''<a class="card mc" href="/cars/{m['slug']}/">{img(m['img'],f"Mitsubishi {m['name']}")}<div class="pad"><p class="kick">{e(m['cat'])}</p><h3>{m['name']}</h3><p class="low">as low as <b>{f(lowest(m))}</b>/mo</p></div></a>''' for m in MODELS)
page("/","Mitsubishi Promos in SJDM, Bulacan | Richard Cuagdan, Mitsubishi SJ Legacy Motors",
 "October 2026 Mitsubishi promos in San Jose del Monte, Bulacan: Xpander, Destinator, Montero Sport, Triton, L300 and Mirage G4 with Zero DP and low-DP all-in monthly options.",
f'''<section class="hero"><div class="w hgrid"><div>
<p class="kick">Mitsubishi SJ Legacy Motors · San Jose del Monte, Bulacan</p>
<h1>Your next Mitsubishi, explained clearly and financed sensibly.</h1>
<p class="lead">I'm Richard Cuagdan, a Car Sales Executive at Mitsubishi SJ Legacy Motors. I help employed buyers, business owners and OFWs find a car and a monthly payment that fit their real budget.</p>
<p class="row"><a class="btn" href="/budgetcalculator/">Compute my monthly</a> <a class="btn ghost" href="/promos/">See October promos</a></p>
</div>{img("xc_x3n","Mitsubishi Xpander Cross in Quartz White Pearl",eager=True,cls="himg")}</div></section>
<section class="sec"><div class="w">
<h2>October 2026 featured promos</h2>
<p class="sub">Lowest all-in monthly per model on 60-month terms. Tap a model for every variant, down payment option and freebie.</p>
<div class="grid g3">{feat}</div>
<p class="note">{NOTE}</p>
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
<section class="sec"><div class="w split">
<div><div class="se"><img src="/assets/img/richard-300.webp" alt="Richard Cuagdan, Car Sales Executive at Mitsubishi SJ Legacy Motors SJDM" width="300" height="300" loading="lazy" decoding="async"><div><p class="kick">Your sales executive</p><p class="sen">Richard Cuagdan</p><p class="muted">Car Sales Executive, Mitsubishi SJ Legacy Motors</p></div></div><h2>Visit the showroom</h2><p><b>Mitsubishi SJ Legacy Motors</b><br>San Jose del Monte, Bulacan</p><p>Monday to Saturday, 8:00 AM to 5:00 PM</p><p>Message me before you visit so I can have your preferred unit ready for viewing or a test drive.</p><p class="row"><a class="btn" href="{MSG}" rel="noopener">Message on Messenger</a> <a class="btn ghost" href="/contact/">Contact details</a></p></div>
<div><h2>New to car financing?</h2><ul class="links"><li><a href="/guides/how-car-financing-works-philippines/">How car financing works in the Philippines</a></li><li><a href="/guides/car-loan-requirements/">Documents you need for a car loan</a></li><li><a href="/guides/zero-dp-vs-low-dp/">Zero DP vs low DP</a></li><li><a href="/guides/ofw-car-buying-guide/">OFW car-buying guide</a></li></ul></div>
</div></section>''', ld=[{"@type":"WebSite","@id":D+"/#site","name":"Mitsubishi Promos SJDM by Richard Cuagdan","url":D+"/"}])

# ---------- CARS index
cards="".join(f'''<a class="card mc" href="/cars/{m['slug']}/">{img(m['img'],f"Mitsubishi {m['name']}")}<div class="pad"><p class="kick">{e(m['cat'])}</p><h3>{m['name']}</h3><p class="muted">{len(m['variants'])} promo variant{'s' if len(m['variants'])>1 else ''}</p><p class="low">as low as <b>{f(lowest(m))}</b>/mo</p></div></a>''' for m in MODELS)
others="".join(f'<li class="card pad"><h3>{n}</h3><p class="muted">{c}</p><p><a href="{MSG}" rel="noopener">Ask for the latest promo →</a></p></li>' for n,c in OTHER)
page("/cars/","Mitsubishi Models & Prices October 2026 | SJ Legacy Motors SJDM",
 "Current Mitsubishi lineup at SJ Legacy Motors, San Jose del Monte: SRP, Zero DP and low-DP monthly options for Xpander, Destinator, Montero Sport, Triton, L300 and Mirage G4.",
f'''<section class="ph"><div class="w"><h1>Current Mitsubishi models</h1><p class="lead">Pick a model to compare variants, down payment options and fuel freebies. All monthly figures are all-in on 60 months.</p></div></section>
<section class="sec"><div class="w"><div class="grid g3">{cards}</div><p class="note">{NOTE}</p></div></section>
<section class="sec alt"><div class="w"><h2>Also in the lineup</h2><p class="sub">These are current Mitsubishi Philippines models. Promo figures change often, so message me for this month's offer.</p><ul class="grid g3 plain">{others}</ul></div></section>''',
 crumbs=[("/","Home"),("/cars/","Cars")])

# ---------- model pages
for m in MODELS:
    vs="".join(vcard(v,m) for v in m["variants"])
    sp="".join(f"<tr><th scope='row'>{e(a)}</th><td>{e(b)}</td></tr>" for a,b in m["specs"])
    rel=" · ".join(f'<a href="/cars/{x["slug"]}/">{x["name"]}</a>' for x in MODELS if x is not m)
    page(f"/cars/{m['slug']}/",f"Mitsubishi {m['name']} Promo October 2026, SRP & Monthly | SJDM Bulacan",
     f"Mitsubishi {m['name']} October 2026 promo at SJ Legacy Motors SJDM: SRP from {f(min(v['srp'] for v in m['variants']))}, all-in monthly as low as {f(lowest(m))} on 60 months.",
    f'''<section class="ph"><div class="w hgrid"><div><p class="kick">{e(m['cat'])}</p><h1>Mitsubishi {m['name']}</h1><p class="lead">{e(m['blurb'])}</p><p>A good fit for {e(m['who'])}.</p><p class="row"><a class="btn" href="/budgetcalculator/">Compute my monthly</a></p></div>{img(m['img'],f"Mitsubishi {m['name']}",eager=True,cls="himg")}</div></section>
<section class="sec"><div class="w"><h2>{m['name']} variants and October 2026 promos</h2><p class="sub">All-in monthly amortization on 60 months.</p><div class="grid g3">{vs}</div><p class="note">{NOTE}</p></div></section>
<section class="sec alt"><div class="w split"><div><h2>Key specs</h2><table class="spec">{sp}</table><p class="muted">Specs summarized from Mitsubishi Motors Philippines. Ask me for the full spec sheet of a specific variant.</p></div>
<div><h2>All-in includes</h2>{ALLIN_HTML}<h2>Freebies</h2>{FREE_HTML}<p class="muted">Fuel freebie amount depends on the variant, as shown above.</p></div></div></section>
<section class="sec"><div class="w"><h2>Compare other models</h2><p>{rel}</p></div></section>''',
    ld=offers_ld(m), ogtype="product", img=f"/assets/img/{m['img']}.webp",
    crumbs=[("/","Home"),("/cars/","Cars"),(f"/cars/{m['slug']}/",m['name'])])

# ---------- promos
rows=""
for m in MODELS:
    for v in m["variants"]:
        rows+=f'<tr><th scope="row"><a href="/cars/{m["slug"]}/">{e(v["n"])}</a></th><td>{e(v.get("srpl") or f(v["srp"]))}</td><td>{"<br>".join(f"{e(l)}: <b>{f(mo)}</b>" for l,mo in v["opts"])}</td><td>{f(v["fuel"]) if v["fuel"] else "None"}</td></tr>'
page("/promos/","Mitsubishi Promos October 2026 Bulacan: Zero DP & Low DP | Richard Cuagdan",
 "Every October 2026 Mitsubishi promo at SJ Legacy Motors SJDM in one table: SRP, Zero DP and low-DP all-in monthly on 60 months, plus fuel freebies.",
f'''<section class="ph"><div class="w"><h1>October 2026 Mitsubishi promos</h1><p class="lead">All current figures in one place. Monthly amounts are all-in on 60 months.</p></div></section>
<section class="sec"><div class="w"><div class="tw"><table class="pt"><caption class="vh">October 2026 promo figures</caption><thead><tr><th scope="col">Variant</th><th scope="col">SRP</th><th scope="col">Down payment and monthly</th><th scope="col">Free fuel</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="note">{NOTE}</p>
<p class="muted">Xforce, Outlander PHEV and Versa Van are also available. <a href="{MSG}" rel="noopener">Ask for the latest promo</a>.</p></div></section>
<section class="sec alt"><div class="w split"><div><h2>All-in includes</h2>{ALLIN_HTML}</div><div><h2>Freebies</h2>{FREE_HTML}</div></div></section>''',
 crumbs=[("/","Home"),("/promos/","Promos")])

# ---------- guides / blog
def articles(base,items,label,title,desc,intro):
    lst="".join(f'<li class="card pad"><h2 class="h3"><a href="/{base}/{a["slug"]}/">{e(a["title"])}</a></h2><p>{e(a["desc"])}</p>{f"<p class=muted>{a['date']}</p>" if base=="blog" else ""}</li>' for a in items)
    page(f"/{base}/",title,desc,f'<section class="ph"><div class="w"><h1>{label}</h1><p class="lead">{intro}</p></div></section><section class="sec"><div class="w"><ul class="grid g2 plain">{lst}</ul></div></section>',crumbs=[("/","Home"),(f"/{base}/",label)])
    for a in items:
        ld=[{"@type":"Article","headline":a["title"],"description":a["desc"],"datePublished":a["date"],"dateModified":a["date"],"author":{"@id":D+"/#richard"},"publisher":{"@id":D+"/#dealer"},"mainEntityOfPage":D+f"/{base}/{a['slug']}/","image":D+f"/assets/img/{a['img']}.webp"}]
        others="".join(f'<li><a href="/{base}/{b["slug"]}/">{e(b["title"])}</a></li>' for b in items if b is not a)
        page(f"/{base}/{a['slug']}/",a["title"]+" | Richard Cuagdan",a["desc"],
        f'''<article class="art"><div class="w nar"><header><p class="kick">{label}</p><h1>{e(a["title"])}</h1><p class="muted">By <a href="/about/">Richard Cuagdan</a>, Car Sales Executive · <time datetime="{a["date"]}">{a["date"]}</time></p></header>
{img(a["img"],a["alt"],eager=True,cls="aimg")}
{a["body"]}
<aside class="box"><h2 class="h3">More {label.lower()}</h2><ul class="links">{others}</ul></aside></div></article>''',ld=ld,ogtype="article",img=f"/assets/img/{a['img']}.webp",
        crumbs=[("/","Home"),(f"/{base}/",label),(f"/{base}/{a['slug']}/",a["title"])])
articles("guides",GUIDES,"Guides","Car Buying & Financing Guides (Philippines) | Richard Cuagdan",
 "Plain-language guides to buying a car in the Philippines: how financing works, loan documents, Zero DP vs low DP, OFW buying and all-in packages.",
 "Practical, plain-language guides to help you plan your purchase before you visit the showroom.")
articles("blog",POSTS,"Blog","Blog: Mitsubishi News, Promos & Tips | Richard Cuagdan SJDM",
 "Notes from the showroom floor at Mitsubishi SJ Legacy Motors, San Jose del Monte: monthly promo roundups, model comparisons and buying tips.",
 "Promo roundups, model comparisons and buying tips from the showroom floor.")

# ---------- about
page("/about/","About Richard Cuagdan, Car Sales Executive | Mitsubishi SJ Legacy Motors",
 "Richard Cuagdan is a Car Sales Executive at Mitsubishi SJ Legacy Motors in San Jose del Monte, Bulacan, helping employed buyers, business owners and OFW families.",
f'''<section class="ph"><div class="w"><h1>About Richard Cuagdan</h1><p class="lead">Car Sales Executive, Mitsubishi SJ Legacy Motors, San Jose del Monte, Bulacan</p></div></section>
<section class="sec"><div class="w nar">
<img class="pphoto" src="/assets/img/richard-600.webp" srcset="/assets/img/richard-300.webp 300w, /assets/img/richard-600.webp 600w" sizes="(min-width:640px) 300px, 240px" alt="Richard Cuagdan, Car Sales Executive at Mitsubishi SJ Legacy Motors SJDM" width="600" height="600" fetchpriority="high" decoding="async">
<p>I'm Richard Cuagdan, a Car Sales Executive at Mitsubishi SJ Legacy Motors, an authorized Mitsubishi dealership in San Jose del Monte, Bulacan.</p>
<!-- PLACEHOLDER: years of experience goes here (e.g. "I've been helping car buyers for X years.") -->
<p>Most of the people I work with fall into three groups: employed buyers looking for a monthly that fits their salary, business owners who need a dependable vehicle for work, and OFWs and their families who are buying from abroad or for loved ones at home. Each situation has different paperwork and different priorities, and I take time to understand yours before recommending a unit.</p>
<h2>How I work</h2>
<ul class="ticks"><li>I explain the SRP, down payment and monthly together so you can decide with complete numbers.</li><li>I tell you which documents your bank application needs and help you complete them.</li><li>I stay your single point of contact from inquiry to release.</li><li>I'm reachable on Messenger, including for clients in other time zones.</li></ul>
<h2>Good to know</h2>
<p>This is my personal sales website. It is not the official website of Mitsubishi Motors Philippines Corporation. Promo figures here are dealership offers and are always subject to bank approval.</p>
<p class="row"><a class="btn" href="{MSG}" rel="noopener">Message me</a> <a class="btn ghost" href="/contact/">Contact and showroom</a></p>
<!-- PLACEHOLDER: contact number goes here once available -->
</div></section>''', ld=[{"@type":"ProfilePage","mainEntity":{"@id":D+"/#richard"}}], crumbs=[("/","Home"),("/about/","About")])

# ---------- apply
page("/apply/","Apply for Mitsubishi Car Financing in SJDM | Steps & Requirements",
 "How to apply for Mitsubishi financing with Richard Cuagdan at SJ Legacy Motors: start with the budget calculator, then submit documents for bank approval.",
f'''<section class="ph"><div class="w"><h1>Apply for financing</h1><p class="lead">The fastest way to start is the budget calculator. It matches a unit to your income and sends your details to me so I can follow up.</p><p class="row"><a class="btn" href="/budgetcalculator/">Start with the calculator</a></p></div></section>
<section class="sec"><div class="w nar">
<h2>The steps</h2>
<ol class="steps"><li><h3>Check your fit</h3><p>Use the <a href="/budgetcalculator/">calculator</a> to see which models fit your monthly budget and choose a down payment option.</p></li>
<li><h3>Talk with me</h3><p>I'll message or call you to confirm the unit, color and terms, and answer your questions.</p></li>
<li><h3>Submit documents</h3><p>Send the requirements for your situation. I'll check them before they go to the bank.</p></li>
<li><h3>Bank approval</h3><p>The bank evaluates your application. Approval time varies by bank and by how complete the documents are.</p></li>
<li><h3>Pay the down payment and release</h3><p>Once approved, settle the down payment (if any), sign the documents and drive home your Mitsubishi.</p></li></ol>
<h2>Typical documents</h2>
<p>Banks set the final list, but most ask for the following:</p>
<ul class="ticks"><li>Two valid government IDs with matching signatures</li><li>Proof of billing for your current address</li><li>Employed: certificate of employment with compensation and recent payslips or ITR</li><li>Business owner: DTI or SEC registration, business permit, bank statements and ITR or financial statements</li><li>OFW: employment contract, recent payslips or remittance records, and details of your co-borrower or attorney-in-fact in the Philippines</li></ul>
<p>See the full <a href="/guides/car-loan-requirements/">car loan requirements guide</a>.</p>
<p class="note">{NOTE}</p>
</div></section>''', crumbs=[("/","Home"),("/apply/","Apply")])

# ---------- contact
page("/contact/","Contact Richard Cuagdan | Mitsubishi SJ Legacy Motors, San Jose del Monte",
 "Message Richard Cuagdan on Messenger or visit Mitsubishi SJ Legacy Motors in San Jose del Monte, Bulacan, Monday to Saturday, 8 AM to 5 PM.",
f'''<section class="ph"><div class="w"><h1>Contact</h1><p class="lead">The quickest way to reach me is Messenger.</p><div class="se"><img src="/assets/img/richard-300.webp" alt="Richard Cuagdan, Car Sales Executive at Mitsubishi SJ Legacy Motors SJDM" width="300" height="300" loading="lazy" decoding="async"><div><p class="kick">Your sales executive</p><p class="sen">Richard Cuagdan</p><p class="sem">Car Sales Executive, Mitsubishi SJ Legacy Motors</p></div></div></div></section>
<section class="sec"><div class="w grid g3">
<div class="card pad"><h2 class="h3">Messenger</h2><p>Send a message any time. I'll reply as soon as I can.</p><p><a class="btn" href="{MSG}" rel="noopener">Open Messenger</a></p></div>
<div class="card pad"><h2 class="h3">Showroom</h2><address>Mitsubishi SJ Legacy Motors<br>San Jose del Monte, Bulacan<br>Philippines</address><p>Monday to Saturday<br>8:00 AM to 5:00 PM</p></div>
<div class="card pad"><h2 class="h3">Compute first</h2><p>See your all-in monthly options before you visit.</p><p><a class="btn ghost" href="/budgetcalculator/">Compute my monthly</a></p></div>
<!-- PLACEHOLDER: phone / mobile number goes here once available -->
</div></section>''', ld=[{"@type":"ContactPage","about":{"@id":D+"/#dealer"}}], crumbs=[("/","Home"),("/contact/","Contact")])

# ---------- 404
page("/__404/","Page not found | Richard Cuagdan","The page you were looking for could not be found.",
 '<section class="ph"><div class="w"><h1>Page not found</h1><p class="lead">That page doesn\'t exist or has moved.</p><p class="row"><a class="btn" href="/">Go to Home</a> <a class="btn ghost" href="/cars/">Browse cars</a></p></div></section>',noindex=True)
s=open(R+"/__404/index.html").read().replace('<link rel="canonical" href="https://mitsubishipromos.online/__404/">\n','').replace('<meta property="og:url" content="https://mitsubishipromos.online/__404/">\n','')
open(R+"/404.html","w").write(s); os.remove(R+"/__404/index.html"); os.rmdir(R+"/__404")

# ---------- root redirect injection
s=open(R+"/index.html").read()
rd="<script>(function(){var q=location.search;if(/(seg=|unit=|utm_|adset=|fbclid)/i.test(q)){location.replace('/budgetcalculator/'+q+location.hash);}})();</script>\n"
s=s.replace('<meta charset="utf-8">\n','<meta charset="utf-8">\n'+rd,1); open(R+"/index.html","w").write(s)

# ---------- sitemap/robots
PAGES.append("/privacy/")
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>{D}{p}</loc><lastmod>2026-10-21</lastmod></url>\n" for p in PAGES)+"</urlset>\n"
open(R+"/sitemap.xml","w").write(sm)
open(R+"/robots.txt","w").write(f"User-agent: *\nAllow: /\n\nSitemap: {D}/sitemap.xml\n")
print(len(PAGES),"pages")
