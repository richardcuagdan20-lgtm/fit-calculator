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
ADDR="Mitsubishi San Juan Motors, serving San Jose del Monte (SJDM), Bulacan and Quezon City"
AREAS=[{"@type":"City","name":"San Jose del Monte","containedInPlace":{"@type":"AdministrativeArea","name":"Bulacan"}},{"@type":"City","name":"Quezon City"}]
import urllib.parse as _up
DEALER={"@type":"AutoDealer","@id":D+"/#dealer","name":"Mitsubishi San Juan Motors","alternateName":"Mitsubishi San Juan Motors San Jose del Monte","sameAs":[FB],"brand":{"@type":"Brand","name":"Mitsubishi"},
 "telephone":TEL,"areaServed":AREAS,
 "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"08:00","closes":"17:00"}],
 "url":D+"/"}
PERSON={"@type":"Person","@id":D+"/#richard","name":"Richard Dennis Cuagdan","alternateName":"Richard Cuagdan","jobTitle":"Car Sales Executive","telephone":TEL,"image":[D+"/assets/img/richard-600.webp",D+"/assets/img/richard/xpander-1x1.jpg"],"worksFor":{"@id":D+"/#dealer"},"areaServed":AREAS,"url":D+"/about/","sameAs":[FB,MSG]}
PX='''<!-- Meta Pixel -->
<script>try{!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');fbq('init','1820790069172672');fbq('track','PageView');}catch(_){}</script>'''
CL='''<!-- Microsoft Clarity -->
<script>try{(function(c,l,a,r,i,t,y){c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);})(window,document,"clarity","script","z0ztjrla58");}catch(_){}</script>
'''
SUF0=" | Mitsubishi Motors - San Juan Motors"
V4="V4:true" in open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"assets","lead.js")).read()  # status page flag lives in assets/lead.js
NAV=[("/","Home"),("/cars/","Cars"),("/tips/","Guides & Tips"),("/apply/","Apply Now"),("/test-drive/","Book a Test Drive"),("/about/","About"),("/contact/","Contact")]+([("/status/","Track Application")] if V4 else [])
# Guides & Tips (2026-10-29): ONE combined article index at /tips/; /blog/, /guides/, /promos-tips/ are redirect stubs to it.
GT="/tips/"; GT_EN="Guides & Tips"; GT_TL="Guides at Tips"
GT_PFX=("/tips/","/blog/","/guides/")
GT_LAND=set()  # landing-guide paths, filled by landing.py
from figs import FIGS
ILLS=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"ill_sizes.json")))
def e(s): return html.escape(s,quote=True)
def page(path,title,desc,body,ld=None,ogtype="website",img="/assets/img/xpglx_x37.webp",noindex=False,crumbs=None,og=None):
    url=D+path
    import og as _og
    ogimg=og or _og.make(path,_og.heading(path,title,crumbs,[SUF0," | Mitsubishi Motors"]),img)
    if title.endswith(SUF0):
        base_=title[:-len(SUF0)]
        title=next(base_+x for x in [" | Mitsubishi Motors by Richard Dennis Cuagdan"," | Mitsubishi Motors by Richard Cuagdan"," | Mitsubishi by Richard Cuagdan",""] if len(base_+x)<=65)
    graph=[DEALER,PERSON]+(ld or [])
    if crumbs:
        graph.append({"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":D+p} for i,(p,n) in enumerate(crumbs)]})
    cur=lambda p:(p==path or (p!="/" and path.startswith(p)))
    def item(p,n):
        act=cur(p) or (p==GT and (path.startswith(GT_PFX) or path in GT_LAND))
        lbl=f'<span class="nv-en">{e(GT_EN)}</span><span class="nv-tl" lang="fil">{e(GT_TL)}</span>' if p==GT else e(n)
        return f'<a href="{p}"{" aria-current=\"page\"" if act else ""}>{lbl}</a>'
    def dd(lbl,items,key):
        on=any(cur(p) for p,_ in items)
        return (f'<details class="dd"{" data-on" if on else ""}><summary>{e(lbl)}</summary><div class="ddp">'
                +"".join(item(p,n) for p,n in items)+'</div></details>')
    nav=(item("/","Home")
        +dd("Cars",[("/cars/","All models and prices"),("/promos/","Promos"),("/test-drive/","Book a test drive")],"cars")
        +item(GT,GT_EN)
        +dd("Apply",[("/apply/","Apply now"),("/status/","Track your application"),("/loan-assessment/","Loan Application Assessment"),("/budgetcalculator/","Compute my monthly")],"apply")
        +item("/about/","About")+item("/contact/","Contact"))
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
<meta property="og:image" content="{D}{ogimg}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:type" content="image/jpeg">
<meta name="twitter:image" content="{D}{ogimg}">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta property="og:locale" content="en_PH">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0b0b0c">
<link rel="icon" href="/favicon.ico?v=2" sizes="48x48">
<link rel="icon" href="/assets/favicon.svg?v=2" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png?v=2">
<link rel="manifest" href="/site.webmanifest?v=2">
<link rel="stylesheet" href="/assets/site.css">
<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@graph":graph},ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="hd"><div class="w hdi">
<a class="brand" href="/"><svg viewBox="0 -15.465 224.9 224.9" width="26" height="26" aria-hidden="true"><path fill="#e60012" d="m112.45 0 38.42 65.13-38.42 65.12L74.03 65.6Zm0 130.25h74.96l37.49 63.72h-74.97zm0 0H37.48L0 193.97h74.97z"/></svg><span class="bt"><b>Mitsubishi Motors</b><small>By Richard Dennis Cuagdan</small></span></a>
<a class="pbtn" href="/promos/">Promos</a><button class="mt" aria-expanded="false" aria-controls="nav" onclick="var n=document.getElementById('nav');var o=n.classList.toggle('open');this.setAttribute('aria-expanded',o)">Menu</button>
<nav id="nav" class="nav" aria-label="Main">{nav}<a class="btn sm" href="{MSG}" rel="noopener" data-msgr="header">Message Richard<span class="xl"> on Messenger</span></a></nav>

</div></header>
{bc}
<main id="main">
{body}
<section class="cta"><div class="w">
<h2>Estimate your monthly in a minute</h2>
<p>Choose a car, a down payment and a term to see an estimated monthly, compared with the official promo for that unit.</p>
<p class="row"><a class="btn" href="/budgetcalculator/">Compute my monthly</a> <a class="btn ghost" href="{MSG}" rel="noopener" data-msgr="cta-band">Message Richard on Messenger</a></p>
</div></section>
</main>
<footer class="ft"><div class="w">
<div class="fg">
<div><p class="fb">Richard Dennis Cuagdan</p><p>Car Sales Executive, Mitsubishi San Juan Motors</p><p>Serving San Jose del Monte (SJDM), Bulacan and Quezon City. Message or call for showroom visits and directions.</p><p>Mobile: <a href="tel:{TEL}">{TELD}</a></p><p>Showroom hours: Monday to Saturday, 8:00 AM to 5:00 PM</p><p><a class="btn sm" href="/apply/">Apply Now</a></p></div>
<div><p class="fb">Explore</p><p><a href="/cars/">Cars</a> · <a href="/promos/">Promos</a> · <a href="/tips/">Guides &amp; Tips</a></p><p><a href="/apply/">Apply</a> · <a href="/test-drive/">Book a Test Drive</a> · <a href="/about/">About</a> · <a href="/contact/">Contact</a> · <a href="/privacy/">Privacy</a>{' · <a href="/status/">Track your application</a>' if V4 else ''}</p></div>
</div>
<p class="fsoc"><a class="fbl" href="{FB}" target="_blank" rel="noopener" aria-label="Mitsubishi Motors by Richard Dennis Cuagdan on Facebook"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path fill="currentColor" d="M24 12a12 12 0 1 0-13.9 11.9v-8.4H7.1V12h3V9.4c0-3 1.8-4.7 4.5-4.7 1.3 0 2.7.2 2.7.2v3h-1.5c-1.5 0-2 .9-2 1.9V12h3.4l-.5 3.5h-2.9v8.4A12 12 0 0 0 24 12z"/></svg><span>Facebook</span></a> <a class="fbl" href="{MSG}" target="_blank" rel="noopener" aria-label="Message Mitsubishi Motors by Richard on Messenger"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path fill="currentColor" d="M12 2C6.4 2 2 6.1 2 11.7c0 2.9 1.2 5.5 3.2 7.2v3.5l3-1.7c1.2.3 2.4.5 3.8.5 5.6 0 10-4.1 10-9.6S17.6 2 12 2zm1 12.9-2.5-2.7-5 2.7 5.5-5.8 2.6 2.7 4.9-2.7-5.5 5.8z"/></svg><span>Messenger</span></a></p>
<p class="disc">Richard Dennis Cuagdan is a sales executive of Mitsubishi San Juan Motors, an authorized Mitsubishi dealership. This is his personal sales website and is not the official website of Mitsubishi Motors Philippines Corporation. Prices, monthly amortizations and freebies are dealer promos, subject to bank approval and change without notice. Mitsubishi names and logos belong to their respective owners.</p>
<p class="cp">© 2026 Richard Dennis Cuagdan · Mitsubishi San Juan Motors, San Jose del Monte, Bulacan · <a class="adm" href="https://script.google.com/macros/s/AKfycbxkJ1e4Z-Sy0vspk2V7mQwYa1X1lBOgWnR8uk61zXJMykX0zx1zVsM4cDLL86rK9CNK/exec" rel="nofollow noopener" target="_blank" style="opacity:.55;font-size:.9em;color:inherit">Admin</a></p>
</div></footer>

</body>
</html>
'''
    d=R+path; os.makedirs(d,exist_ok=True)
    open(d+"index.html","w").write(h)
    if not noindex: PAGES.append(path)

def img(k,alt,eager=False,cls=""):
    return f'<img src="/assets/img/{k}.webp" alt="{e(alt)}" width="640" height="427" {"fetchpriority=\"high\"" if eager else "loading=\"lazy\""} decoding="async"{f" class=\"{cls}\"" if cls else ""}>'

# ---------- Richard photos (assets/img/richard/, made by /workspace/loanapp/photos/make_photos.py)
RXCAR={"xpander":"Xpander","xforce":"Xforce","mirage":"Mirage G4","destinator":"Destinator"}
RXMODEL={"xpander":"xpander","xforce":"xforce","mirage-g4":"mirage","destinator":"destinator"}
def rx_alt(c): return f"Richard Cuagdan, Mitsubishi Car Sales Executive, beside the Mitsubishi {RXCAR[c]}"
def rx_og(c): return f"/assets/img/richard/og-{c}.jpg"
def rx_card(c,cap="",eager=False,ratio="16x9",cls="rx"):
    """clean photo of Richard; optional single short caption line only where nothing nearby introduces him"""
    b=f"/assets/img/richard/{c}-{ratio}";sm,w,h,bw={"16x9":("800",800,450,1600),"1x1":("640",640,640,1200),"4x5":("480",480,600,960)}[ratio]
    sz="(min-width:900px) 420px, min(calc(100vw - 40px), 420px)" if ratio=="4x5" else "(min-width:800px) 720px, calc(100vw - 40px)"
    ld='loading="eager" fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<figure class="{cls}"><picture><source type="image/webp" srcset="{b}-{sm}.webp {sm}w, {b}.webp {bw}w" sizes="{sz}">'
            f'<img src="{b}-{sm}.jpg" alt="{e(rx_alt(c))}" width="{w}" height="{h}" {ld} decoding="async"></picture>'
            +(f'<figcaption class="rxc">{cap}</figcaption>' if cap else '')+'</figure>')
# ---------- HERO MODULE: one CTA only ("View Promos" -> /promos/). Messenger/compute/apply live in header + in-page sections.
HERO_CTA={"en":"View Promos","tl":"Tingnan ang Promos"}
def hero_cta(href="/promos/",lang="en",src="hero"):
    return f'<p class="row hcta"><a class="btn" href="{href}" data-herocta="{e(src)}">{HERO_CTA.get(lang,HERO_CTA["en"])}</a></p>'
def hero(title,sub,media="",kick="",cta_href="/promos/",lang="en",src="hero",cls="hero",extra=""):
    """reusable hero: kicker, h1, lead, exactly ONE CTA, optional media (e.g. rx_card 4:5 / img himg)"""
    k=f'<p class="kick">{kick}</p>' if kick else ""
    return f'<section class="{cls}"><div class="w hgrid"><div>{k}<h1>{title}</h1><p class="lead">{sub}</p>{extra}{hero_cta(cta_href,lang,src)}</div>{media}</div></section>'
def rx_pick(slug):
    s=slug.lower();hits=[(s.find(k),c) for k,c in (("xforce","xforce"),("destinator","destinator"),("mirage","mirage"),("xpander","xpander")) if k in s and not (k=="xpander" and "xpander-cross" in s and s.count("xpander")==1)]
    return min(hits)[1] if hits else None
def rx_bio(c=None,tl=False):
    c=c or "xpander";b=f"/assets/img/richard/{c}-1x1-240"
    w=("Isinulat ni","Tungkol kay Richard","I-message si Richard sa Messenger") if tl else ("Written by","About Richard","Message Richard on Messenger")
    return (f'<aside class="abio"><picture><source type="image/webp" srcset="{b}.webp"><img src="{b}.jpg" alt="{e(rx_alt(c))}" width="240" height="240" loading="lazy" decoding="async"></picture>'
            f'<div><p class="abn">{w[0]} Richard Cuagdan, Mitsubishi Car Sales Executive</p><p class="abd">Mitsubishi San Juan Motors · San Jose del Monte, Bulacan</p>'
            f'<p class="abl"><a href="/about/">{w[1]}</a> · <a href="{MSG}" rel="noopener">{w[2]}</a></p></div></aside>')

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
import re as _re0
def _dpv(l):
    m=_re0.search(r"([\d.]+)K",l); return int(float(m.group(1))*1000) if m else 0
CALCD=[{"slug":m["slug"],"name":m["name"],"v":[{"id":v["id"],"n":v["n"],"srp":v["srp"] or (v["promo"] or {}).get("srp"),"fuel":(v["promo"] or {}).get("fuel"),"p":[{"dp":_dpv(l),"mo":mo} for l,mo in (v["promo"] or {}).get("opts",[])]} for v in m["variants"] if (v["srp"] or (v["promo"] or {}).get("srp"))]} for m in MODELS]
def CALC(src): return f'<div data-rpcalc data-src="{src}"></div><script type="application/json" id="calc-data">{json.dumps(CALCD,ensure_ascii=False)}</script><script src="/assets/calc.js" defer></script>'
LACTA='<aside class="lacta"><h2>Will you qualify for a car loan?</h2><p>Find out in 3 minutes with the free AI Car Loan Application Assessment. No documents needed. Your result is a Pre-qualified estimate; financing is subject to bank approval.</p><a class="btn" href="/loan-assessment/">Start the AI Car Loan Application Assessment</a></aside>'
LACTA_TL='<aside class="lacta"><h2>Pasok ka ba sa car loan?</h2><p>Alamin sa loob ng 3 minuto gamit ang libreng AI Car Loan Application Assessment. Walang documents na kailangan.</p><a class="btn" href="/loan-assessment/?lang=tl">Simulan ang AI Car Loan Application Assessment</a></aside>'
CONSENT='<label class="chk"><input type="checkbox" id="consent" required> <span>I agree to the collection and processing of my personal information under the Data Privacy Act of 2012 (RA 10173), as described in the <a href="/privacy/">Privacy Policy</a>, so Richard Cuagdan can contact me about this inquiry.</span></label><p class="er" id="e_consent" hidden>Please tick the consent box.</p>'

# ---------- HOME
feat="".join(f'''<a class="card mc" href="/cars/{m['slug']}/">{img(m['img'],f"Mitsubishi {m['name']}")}<div class="pad"><p class="kick">{e(m['cat'])}</p><h3>{m['name']}</h3><p class="low">{from_txt(m)}</p></div></a>''' for m in MODELS)
page("/","Mitsubishi Cars & Promos in SJDM, Bulacan | Mitsubishi Motors - San Juan Motors",
 "Mitsubishi cars in San Jose del Monte, Bulacan: official SRPs for Xpander, Xforce, Destinator, Montero Sport, Triton, L300 and more, with all-in down payment and monthly options.",
hero("Your next Mitsubishi, explained clearly and financed sensibly.","Official SRPs, this month's all-in down payment and monthly promos, and help with your bank application for employed buyers, business owners and OFWs.",rx_card("xpander",eager=True,ratio="4x5",cls="rx himg"),kick="Mitsubishi San Juan Motors · San Jose del Monte, Bulacan",src="home")+f'''
<div class="w">{LACTA}</div>
<section class="sec"><div class="w">
<h2>The 2026 Mitsubishi lineup</h2>
<p class="sub">Starting SRP per model from the official price list. Tap a model for every variant, or <a href="/promos/">see this month's promo figures</a>, including Zero DP Promo on select units (subject to bank approval). Every unit has two promo options on the <a href="/promos/">promos page</a>.</p>
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
<a class="card pad mc" href="/mirage-g4-downpayment-and-monthly/"><h3>Mirage G4 downpayment and monthly</h3><p class="muted">First-car financing guide</p></a>
<a class="card pad mc" href="/triton-downpayment-and-monthly/"><h3>Triton downpayment and monthly</h3><p class="muted">Pickup financing guide</p></a>
<a class="card pad mc" href="/l300-monthly-installment/"><h3>L300 monthly installment</h3><p class="muted">For negosyo buyers</p></a>
</div></div></section>
<section class="sec"><div class="w split">
<div><h2>Visit the showroom</h2><p><b>Mitsubishi San Juan Motors</b><br>San Jose del Monte, Bulacan</p><p>Monday to Saturday, 8:00 AM to 5:00 PM</p><p>Message me before you visit so I can have your preferred unit ready for viewing or a test drive.</p><p class="row"><a class="btn" href="{MSG}" rel="noopener" data-msgr="home-visit">Message Richard on Messenger</a> <a class="btn ghost" href="/contact/">Contact details</a></p></div>
<div><h2>New to car financing?</h2><ul class="links"><li><a href="/guides/how-car-financing-works-philippines/">How car financing works in the Philippines</a></li><li><a href="/guides/car-loan-requirements/">Documents you need for a car loan</a></li><li><a href="/guides/zero-dp-vs-low-dp/">Choosing your down payment</a></li><li><a href="/blog/ofw-car-buying-guide/">OFW car-buying guide</a></li></ul></div>
</div></section>''', ld=[{"@type":"WebSite","@id":D+"/#site","name":"Mitsubishi Motors by Richard Dennis Cuagdan","url":D+"/"}])

# ---------- CARS index
cards="".join(f'''<a class="card mc" href="/cars/{m['slug']}/">{img(m['img'],f"Mitsubishi {m['name']}")}<div class="pad"><p class="kick">{e(m['cat'])}</p><h3>{m['name']}</h3><p class="muted">{len(m['variants'])} variant{'s' if len(m['variants'])>1 else ''}</p><p class="low">{from_txt(m)}</p></div></a>''' for m in MODELS)
page("/cars/","2026 Models & Prices | Mitsubishi Motors - San Juan Motors",
 "Every current Mitsubishi model at San Juan Motors, San Jose del Monte: Mirage G4, Xpander, Xpander Cross, Xforce, Destinator, Outlander PHEV, Montero Sport, Triton, L300 and Versa Van with official SRPs.",
f'''<section class="ph"><div class="w"><h1>2026 Mitsubishi models</h1><p class="lead">Browse every current model and variant with its official SRP. Promo packages are all-in and come with freebies.</p></div></section>
<section class="sec"><div class="w"><div class="grid g3">{cards}</div><p class="note">{SRPNOTE}</p><p class="row"><a class="btn" href="/promos/">See October promos</a></p></div></section>''',
 crumbs=[("/","Home"),("/cars/","Cars")])

# ---------- model pages
EVM={k:f'<section class="sec"><div class="w"><h2>Financing guide</h2><p><a class="more" href="/{u}/">{t} →</a></p><p class="muted">How DP, term and monthly work, documents, income guide and this month\'s promo table. Also see the <a href="/mitsubishi-zero-down-payment-promo/">Mitsubishi zero down payment promo</a> guide.</p></div></section>' for k,u,t in [("mirage-g4","mirage-g4-downpayment-and-monthly","Mirage G4 downpayment and monthly"),("triton","triton-downpayment-and-monthly","Triton downpayment and monthly"),("l300","l300-monthly-installment","L300 monthly installment")]}
for m in MODELS:
    vs="".join(vcard(v,m) for v in m["variants"])
    sp="".join(f"<tr><th scope='row'>{e(a)}</th><td>{e(b)}</td></tr>" for a,b in m["specs"])
    rel=" · ".join(f'<a href="/cars/{x["slug"]}/">{x["name"]}</a>' for x in MODELS if x is not m)
    s0=srp_from(m)
    haspromo=any(v["promo"] for v in m["variants"])
    page(f"/cars/{m['slug']}/",f"{m['name']} 2026 Price | Mitsubishi Motors - San Juan Motors",
     f"Mitsubishi {m['name']} at San Juan Motors, San Jose del Monte: {len(m['variants'])} variant{'s' if len(m['variants'])>1 else ''}"+(f", official SRP from {f(s0)}" if s0 else "")+", all-in packages with freebies.",
    f'''<section class="ph"><div class="w hgrid"><div><p class="kick">{e(m['cat'])}</p><h1>Mitsubishi {m['name']}</h1><p class="lead">{e(m['blurb'])}</p><p>A good fit for {e(m['who'])}.</p>{hero_cta(f"/promos/#{m['slug']}" if haspromo else "/promos/",src="model-"+m['slug'])}</div>{img(m['img'],f"Mitsubishi {m['name']}",eager=True,cls="himg")}</div></section>
<section class="sec"><div class="w"><h2>{m['name']} variants and prices</h2><p class="sub">Official SRP per variant. Promo down payment and monthly options are shared on the <a href="/promos/">promos page</a>.</p><div class="grid g3">{vs}</div><p class="note">{SRPNOTE}</p></div></section>
{(f'<section class="sec rxs"><div class="w">'+rx_card(RXMODEL[m["slug"]],cap=f"Richard Cuagdan, your sales executive, with the Mitsubishi {e(RXCAR[RXMODEL[m['slug']]])}")+'</div></section>') if m["slug"] in RXMODEL else ""}<section class="sec alt"><div class="w split"><div><h2>Key specs</h2><table class="spec">{sp}</table><p class="muted">Specs summarized from Mitsubishi Motors Philippines. Ask me for the full spec sheet of a specific variant.</p></div>
<div><h2>All-in includes</h2>{ALLIN_HTML}<h2>Freebies</h2>{FREE_HTML}<p class="muted">Freebies vary by variant; ask for details.</p></div></div></section>
{EVM.get(m['slug'],'')}<section class="sec"><div class="w"><h2>Compare other models</h2><p>{rel}</p></div></section>''',
    ld=offers_ld(m), ogtype="product", img=f"/assets/img/{m['img']}.webp", og=rx_og(RXMODEL[m["slug"]]) if m["slug"] in RXMODEL else None,
    crumbs=[("/","Home"),("/cars/","Cars"),(f"/cars/{m['slug']}/",m['name'])])

# ---------- promos (gated, noindex; figures live only in JS data)
PD=[{"slug":m["slug"],"name":m["name"],"v":[{"n":v["n"],"srp":(v["promo"]["srp"] or v["srp"]),"opts":v["promo"]["opts"],"fuel":v["promo"]["fuel"]} for v in m["variants"] if v["promo"]]} for m in MODELS]
PD=[x for x in PD if x["v"]]
def _promo_cards(m):
    out=""
    for v in m["variants"]:
        if not v["promo"]: continue
        srp=v["promo"]["srp"] or v["srp"];opts=[(l,mo) for l,mo in v["promo"]["opts"] if _dpv(l)>0]
        if not opts: continue
        rows="".join(f'<li><span>{e(l)}</span><b>{f(mo)}<small>/mo</small></b></li>' for l,mo in sorted(opts,key=lambda x:_dpv(x[0])))
        fuel=f'<p class="fuel">Plus <b>{v["promo"]["fuel"]:,} fuel points</b></p>' if v["promo"]["fuel"] else ""
        out+=f'<article class="card pad pcard"><h3>{e(v["n"])}</h3><p class="srp">SRP <b>{f(srp)}</b></p><ul class="opts">{rows}</ul>{fuel}<p class="muted">60 months, all-in.</p><p class="row"><a class="btn sm" href="/loan-assessment/?unit={v["id"]}">See if you&rsquo;re Pre-Qualified in 2 minutes →</a> <a class="btn sm ghost dk" href="/budgetcalculator/?unit={v["id"]}">Compare with my own DP</a></p></article>'
    return out
PROMO_SECS="".join(f'<section class="pm" id="{m["slug"]}"><h2>{e(m["name"])}</h2><div class="grid g3">{_promo_cards(m)}</div></section>' for m in MODELS if _promo_cards(m))
import promosab as _pab
_PAB_UNITS=_pab.build(page,e,f,R,hero_cta,ALLIN_HTML,FREE_HTML,NOTE,MSG)
_pab.inject_cars(R)  # DRAFT: promos module on car pages
# /lowest-down-payment/ retired 2026-10-29: folded into /promos/ (Option A unlock); stub keeps old links/ads alive
import os as _os
_os.makedirs(R+"/lowest-down-payment",exist_ok=True)
open(R+"/lowest-down-payment/index.html","w").write('<!doctype html><html lang="en-PH"><head><meta charset="utf-8"><title>Promos | Mitsubishi Motors - San Juan Motors</title><meta name="robots" content="noindex"><link rel="canonical" href="https://mitsubishipromos.online/promos/"><meta http-equiv="refresh" content="0; url=/promos/"><script>location.replace("/promos/"+location.search+location.hash)</script></head><body><p><a href="/promos/">Go to Promos</a></p></body></html>')
# ---------- /promos-tips/ hub retired (2026-10-29): redirect stub to the combined Guides & Tips index, written at the end of the build
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
GT_ALL=[]  # (url,title,desc,date) of every article for the combined /tips/ index
def articles(base,items,label,title=None,desc=None,intro=None):
    # per-type index pages retired: /tips/ is the single combined index; /blog/ and /guides/ become redirect stubs
    label=GT_EN
    for a in items:
        GT_ALL.append((f"/{base}/{a['slug']}/",a["title"],a["desc"],a["date"]))
    for a in items:
        ld=[{"@type":"Article","headline":a["title"],"description":a["desc"],"datePublished":a["date"],"dateModified":a["date"],"author":{"@id":D+"/#richard"},"publisher":{"@id":D+"/#dealer"},"mainEntityOfPage":D+f"/{base}/{a['slug']}/","image":D+f"/assets/img/{a['img']}.webp"}]
        if a.get("lang"): ld[0]["inLanguage"]={"tl":"fil-PH","en":"en-PH"}[a["lang"]]
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
        page(f"/{base}/{a['slug']}/",(a["title"]+" | Mitsubishi Motors - San Juan Motors" if len(a["title"])<=27 else a["title"]),a["desc"],
        f'''<article class="art"><div class="w nar"><header><p class="kick">{e(label)}</p><h1>{e(a["title"])}</h1><p class="muted">By <a href="/about/">Richard Cuagdan</a>, {a.get("by","Car Sales Executive")} · <time datetime="{a["date"]}">{a["date"]}</time></p></header>
{img(a["img"],a["alt"],eager=True,cls="aimg")}
{top}
{body}
{rx_bio(rx_pick(a["slug"]),a.get("lang")=="tl")}
{LACTA}
{fq}
<aside class="box"><h2 class="h3">More guides &amp; tips</h2><ul class="links">{others}</ul><p><a class="more" href="{GT}">See all guides &amp; tips →</a></p></aside></div></article>''',ld=ld,ogtype="article",img=f"/assets/img/{a['img']}.webp",
        crumbs=[("/","Home"),(GT,GT_EN),(f"/{base}/{a['slug']}/",a["title"])])
articles("guides",GUIDES,"Guides","Car Buying Guides | Mitsubishi Motors - San Juan Motors",
 "Plain-language guides to buying a car in the Philippines: how financing works, loan documents, Zero DP vs low DP, OFW buying and all-in packages.",
 "Practical, plain-language guides to help you plan your purchase before you visit the showroom.")
if TIPS: articles("tips",TIPS,"Tips","Car Tips & Checklists | Mitsubishi by Richard Cuagdan",
 "Quick, save-worthy checklists for Filipino drivers: road trips, fuel saving, LTO rules, weather car care and first-car buying.",
 "Short, practical checklists you can save before your next drive or car purchase.")
articles("blog",POSTS,"Blog","Blog | Mitsubishi Motors - San Juan Motors",
 "Notes from the showroom floor at Mitsubishi San Juan Motors, San Jose del Monte: monthly promo roundups, model comparisons and buying tips.",
 "Promo roundups, model comparisons and buying tips from the showroom floor.")

# ---------- about
page("/about/","About Richard Dennis Cuagdan | Mitsubishi Motors",
 "Richard Dennis Cuagdan is a Car Sales Executive at Mitsubishi San Juan Motors in San Jose del Monte, Bulacan, helping employed buyers, business owners and OFW families.",
f'''<section class="ph"><div class="w"><h1>About Richard Dennis Cuagdan</h1><p class="lead">Car Sales Executive, Mitsubishi San Juan Motors, San Jose del Monte, Bulacan</p></div></section>
<section class="sec"><div class="w nar">
{rx_card("destinator",eager=True)}
<p>I'm Richard Dennis Cuagdan, a Car Sales Executive at Mitsubishi San Juan Motors, an authorized Mitsubishi dealership in San Jose del Monte, Bulacan.</p>
<!-- PLACEHOLDER: years of experience goes here (e.g. "I've been helping car buyers for X years.") -->
<p>Most of the people I work with fall into three groups: employed buyers looking for a monthly that fits their salary, business owners who need a dependable vehicle for work, and OFWs and their families who are buying from abroad or for loved ones at home. Each situation has different paperwork and different priorities, and I take time to understand yours before recommending a unit.</p>
<h2>How I work</h2>
<ul class="ticks"><li>I explain the SRP, down payment and monthly together so you can decide with complete numbers.</li><li>I tell you which documents your bank application needs and help you complete them.</li><li>I stay your single point of contact from inquiry to release.</li><li>I'm reachable on Messenger, including for clients in other time zones.</li></ul>
<h2>Good to know</h2>
<p>This is my personal sales website. It is not the official website of Mitsubishi Motors Philippines Corporation. Promo figures here are dealership offers and are always subject to bank approval.</p>
<p class="row"><a class="btn" href="{MSG}" rel="noopener">Message me</a> <a class="btn ghost dk" href="{FB}" target="_blank" rel="noopener">Follow us on Facebook</a> <a class="btn ghost dk" href="/contact/">Contact and showroom</a></p>
<p>Call or text me: <a href="tel:{TEL}">{TELD}</a>. Message me for showroom visits and directions.</p>
</div></section>''', ld=[{"@type":"ProfilePage","mainEntity":{"@id":D+"/#richard"}}], crumbs=[("/","Home"),("/about/","About")], og=rx_og("mirage"))

# ---------- apply: Official Application Form, see _src/applyform.py (exec'd after loanapp.py)

# ---------- test drive
TDU=[{"id":v["id"],"m":m["slug"],"model":m["name"],"n":v["n"],"srp":srp_txt(v),"img":v["img"]} for m in MODELS for v in m["variants"]]
rows_td="".join(f'''<div class="tdrow"><h3>{e(m["name"])}</h3><div class="tdtrack" role="radiogroup" aria-label="{e(m["name"])} variants">'''+"".join(f'''<button type="button" class="tdc" role="radio" aria-checked="false" data-id="{v["id"]}">{img(v["img"],"Mitsubishi "+v["n"])}<span class="tdn">{e(v["n"])}</span><span class="tds">SRP {srp_txt(v)}</span></button>''' for v in m["variants"])+'</div></div>' for m in MODELS)
TIMES=[("08:00","8:00 AM"),("09:00","9:00 AM"),("10:00","10:00 AM"),("11:00","11:00 AM"),("13:00","1:00 PM"),("14:00","2:00 PM"),("15:00","3:00 PM"),("16:00","4:00 PM")]
page("/test-drive/","Book a Test Drive | Mitsubishi Motors - San Juan Motors",
 "Book a Mitsubishi test drive at San Juan Motors, San Jose del Monte, Bulacan. Pick your unit, choose a date and time from Monday to Saturday, and Richard will confirm.",
f'''<section class="ph"><div class="w"><h1>Book a test drive</h1><p class="lead">Choose a unit, pick a schedule, and I'll have it ready for you at Mitsubishi San Juan Motors, San Jose del Monte.</p></div></section>
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
<div class="fld"><p class="fl">Location</p><p><b>Mitsubishi San Juan Motors</b><br>San Jose del Monte, Bulacan<br><span class="muted">Showroom hours: Monday to Saturday, 8:00 AM to 5:00 PM</span></p></div>
<div class="fld"><label for="notes">Notes (optional)</label><textarea id="notes" rows="3" maxlength="1000" placeholder="e.g. preferred color, number of passengers joining"></textarea></div>
<label class="chk"><input type="checkbox" id="lic" required> <span>I have a valid driver's license and will bring it to the test drive.</span></label><p class="er" id="e_lic" hidden>A valid driver's license is required for the test drive.</p>
{CONSENT}
<button class="btn" type="submit" id="tb">Book my test drive</button>
</form></div></div>
<div id="s3" hidden><div class="card tdsel"><img id="cimg" src="" alt="" width="640" height="427"><div class="pad">
<p class="kick">Test drive request received</p><h2 id="cname"></h2>
<p><b id="cwhen"></b><br>Mitsubishi San Juan Motors, San Jose del Monte, Bulacan</p>
<p>Richard will message you to confirm your schedule. Please bring your valid driver's license.</p>
<p>Reference: <b id="cref"></b></p>
<p class="row"><a class="btn" id="gcal" href="#" target="_blank" rel="noopener">Add to Google Calendar</a> <a class="btn ghost dk" href="{MSG}" rel="noopener" data-msgr="testdrive-confirmed">Message Richard on Messenger</a></p></div></div></div>
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
 var L=Lead.base('test_drive');L.name=v('name');L.mobile=mob;L.chosenUnit=sel.n;L.unitParam=sel.id;L.location='Mitsubishi San Juan Motors, San Jose del Monte, Bulacan';
 L.timeline='TD '+dt+' '+tl;L.usage=['Driver\\'s license: yes',em?'Email: '+em:'',v('notes')?'Notes: '+v('notes'):''].filter(Boolean).join(' | ');
 Lead.send(L).then(function(){{
  if(!Lead.skipped()){{try{{if(typeof window.fbq==='function')window.fbq('track','Schedule',{{content_name:sel.n}})}}catch(_){{}}
  try{{if(typeof window.gtag==='function')window.gtag('event','book_test_drive',{{unit:sel.n,date:dt}})}}catch(_){{}}}}
  var s=dt.replace(/-/g,'')+'T'+tm.replace(':','')+'00',h=String(+tm.slice(0,2)+1).padStart(2,'0'),en=dt.replace(/-/g,'')+'T'+h+tm.slice(3)+'00';
  var g='https://calendar.google.com/calendar/render?action=TEMPLATE&text='+encodeURIComponent('Mitsubishi test drive: '+sel.n)+'&dates='+s+'/'+en+'&ctz=Asia/Manila&location='+encodeURIComponent('Mitsubishi San Juan Motors, San Jose del Monte, Bulacan')+'&details='+encodeURIComponent('Test drive with Richard Cuagdan. Bring your valid driver\\'s license. Ref: '+L.leadId+'. Messenger: https://m.me/504759566043148');
  $('gcal').href=g;$('cimg').src='/assets/img/'+sel.img+'.webp';$('cimg').alt='Mitsubishi '+sel.n;$('cname').textContent=sel.n;
  var p=dt.split('-');$('cwhen').textContent=new Date(+p[0],p[1]-1,+p[2]).toLocaleDateString('en-PH',{{weekday:'long',year:'numeric',month:'long',day:'numeric'}})+', '+tl;
  $('cref').textContent=L.leadId;step(3)}});
}});
}});
</script>''', crumbs=[("/","Home"),("/test-drive/","Book a Test Drive")])

# ---------- contact
page("/contact/","Contact | Mitsubishi Motors - San Juan Motors",
 "Message Richard Cuagdan on Messenger or arrange a showroom visit with Mitsubishi San Juan Motors in San Jose del Monte, Bulacan, Monday to Saturday, 8 AM to 5 PM.",
f'''<section class="ph"><div class="w"><h1>Contact</h1><p class="lead">The quickest way to reach me is Messenger. I reply personally.</p>{rx_card("xforce",eager=True)}</div></section>
<section class="sec"><div class="w grid g3">
<div class="card pad"><h2 class="h3">Messenger</h2><p>Send me a message any time about units, promos, your application or a showroom visit. I'll reply as soon as I can.</p><p><a class="btn" href="{MSG}" rel="noopener" data-msgr="contact-card">Message Richard on Messenger</a></p></div>
<div class="card pad"><h2 class="h3">Facebook</h2><p>Follow the page for new arrivals, promos and updates.</p><p><a class="btn ghost dk" href="{FB}" target="_blank" rel="noopener">Follow us on Facebook</a></p></div>
<div class="card pad"><h2 class="h3">Call or text</h2><p>Mobile: <a href="tel:{TEL}">{TELD}</a></p><p><a class="btn" href="tel:{TEL}">Call {TELD}</a></p></div>
<div class="card pad"><h2 class="h3">Showroom visits</h2><p>Serving San Jose del Monte (SJDM), Bulacan and Quezon City.</p><p><a href="{MSG}" rel="noopener">Message me for the showroom location and directions</a></p><p>Monday to Saturday<br>8:00 AM to 5:00 PM</p></div>
<div class="card pad"><h2 class="h3">Apply online</h2><p>Send your details and preferred unit, and I'll get back to you with the latest promo.</p><p><a class="btn" href="/apply/">Apply Now</a></p></div>
<div class="card pad"><h2 class="h3">Compute first</h2><p>See your all-in monthly options before you visit.</p><p><a class="btn ghost" href="/budgetcalculator/">Compute my monthly</a></p></div>
</div></section>
<section class="sec"><div class="w"><h2>Visiting the showroom</h2><p>I serve buyers in San Jose del Monte (SJDM), Bulacan and Quezon City. Message or call me before you come so I can send directions and have your preferred unit ready for viewing or a test drive.</p><p class="row"><a class="btn" href="{MSG}" rel="noopener">Message Richard on Messenger</a> <a class="btn ghost dk" href="tel:{TEL}">Call {TELD}</a></p></div></section>''', ld=[{"@type":"ContactPage","about":{"@id":D+"/#dealer"}}], crumbs=[("/","Home"),("/contact/","Contact")], og=rx_og("xforce"))

# ---------- calculator (replaces the old budget-fit page; old copy kept in git history and /workspace/loanapp/budgetcalculator-old-20261029.html)
page("/budgetcalculator/","Monthly Estimate Calculator | Mitsubishi Motors - San Juan Motors",
 "Estimate your Mitsubishi monthly: choose a car, a down payment and a term, then compare it with the official promo. Estimate only, subject to bank evaluation.",
f'''<section class="ph"><div class="w"><h1>Estimate your monthly</h1><p class="lead">Choose a car, a down payment and how many years. You will see an estimated monthly and, when there is one, the official promo for the same unit.</p></div></section>
<section class="sec"><div class="w">{CALC("budgetcalculator")}</div></section>
<script src="/assets/lead.js" defer></script>''', crumbs=[("/","Home"),("/budgetcalculator/","Monthly estimate")])
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"landing.py")).read())
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"loanapp.py")).read())
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"applyform.py")).read())
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"statuspage.py")).read())
# ---------- GUIDES & TIPS: one combined index of every article (blog, guides, tips, evergreen landing guides), newest first. No promos page here.
for _p,_a in LAND_PATHS: GT_ALL.append((_p,_a["title"],_a["desc"],PROMO_UPDATED))
import datetime as _dt
def _gtd(d): return _dt.date.fromisoformat(d).strftime("%B %-d, %Y")
_GTL=sorted(GT_ALL,key=lambda x:(x[3],x[1]),reverse=True)
_gtl="".join(f'<li class="card pad"><h2 class="h3"><a href="{u}">{e(t)}</a></h2><p>{e(d)}</p><p class="muted"><time datetime="{dt}">{_gtd(dt)}</time></p></li>' for u,t,d,dt in _GTL)
page(GT,"Guides & Tips | Mitsubishi Motors - San Juan Motors",
 "Every car-buying guide, financing explainer, model comparison and driving tip from Richard Cuagdan of Mitsubishi San Juan Motors SJDM, newest first.",
 f'''<section class="ph"><div class="w"><h1>Guides &amp; Tips</h1><p class="lead">Every guide, blog post and tip in one place, newest first: financing, loan requirements, model comparisons, car care and driving checklists.</p></div></section>
<section class="sec"><div class="w"><ul class="grid g2 plain gtl">{_gtl}</ul></div></section>''',
 ld=[{"@type":"CollectionPage","name":"Guides & Tips","url":D+GT,"hasPart":[{"@type":"Article","headline":t,"url":D+u,"datePublished":dt} for u,t,d,dt in _GTL]}],
 crumbs=[("/","Home"),(GT,GT_EN)])
# old indexes -> redirect stubs (GitHub Pages has no server redirects): meta refresh + canonical + JS replace
for _old,_nm in (("/blog/","Blog"),("/guides/","Guides"),("/promos-tips/","Promos & Tips")):
    os.makedirs(R+_old,exist_ok=True)
    open(R+_old+"index.html","w").write(f'<!doctype html><html lang="en-PH"><head><meta charset="utf-8"><title>Moved: Guides &amp; Tips</title><link rel="canonical" href="{D}{GT}"><meta name="robots" content="noindex,follow"><meta http-equiv="refresh" content="0; url={GT}"><script>location.replace("{GT}"+location.search+location.hash)</script></head><body><p>{e(_nm)} has moved to <a href="{GT}">Guides &amp; Tips</a>.</p></body></html>\n')
# ---------- OFW guide merge: redirect old URL
os.makedirs(R+"/guides/ofw-car-buying-guide",exist_ok=True)
open(R+"/guides/ofw-car-buying-guide/index.html","w").write('<!doctype html><html lang="en-PH"><head><meta charset="utf-8"><title>Moved: OFW Car Loan Guide</title><link rel="canonical" href="'+D+'/blog/ofw-car-buying-guide/"><meta name="robots" content="noindex,follow"><meta http-equiv="refresh" content="0; url=/blog/ofw-car-buying-guide/"></head><body><p>This guide has moved to <a href="/blog/ofw-car-buying-guide/">the OFW car loan guide</a>.</p></body></html>\n')
# ---------- /preview-loan/ retired: redirect stub to the live assessment
os.makedirs(R+"/preview-loan",exist_ok=True)
open(R+"/preview-loan/index.html","w").write('<!doctype html><html lang="en-PH"><head><meta charset="utf-8"><title>Moved: AI Car Loan Application Assessment</title><link rel="canonical" href="'+D+'/loan-assessment/"><meta name="robots" content="noindex,follow"><meta http-equiv="refresh" content="0; url=/loan-assessment/"><script>location.replace("/loan-assessment/"+location.search)</script></head><body><p>Moved to <a href="/loan-assessment/">the AI Car Loan Application Assessment</a>.</p></body></html>\n')
# ---------- 404
page("/__404/","Page not found | Mitsubishi Motors - San Juan Motors","The page you were looking for could not be found.",
 '<section class="ph"><div class="w"><h1>Page not found</h1><p class="lead">That page doesn\'t exist or has moved.</p><p class="row"><a class="btn" href="/">Go to Home</a> <a class="btn ghost" href="/cars/">Browse cars</a></p></div></section>',noindex=True)
s=open(R+"/__404/index.html").read().replace('<link rel="canonical" href="https://mitsubishipromos.online/__404/">\n','').replace('<meta property="og:url" content="https://mitsubishipromos.online/__404/">\n','')
open(R+"/404.html","w").write(s); os.remove(R+"/__404/index.html"); os.rmdir(R+"/__404")

# ---------- root redirect injection
s=open(R+"/index.html").read()
rd="<script>(function(){try{var q=location.search;if(!q)return;var p=new URLSearchParams(q);var sg=(p.get('seg')||'').toLowerCase();if(/^(local|ofw_abroad|ofw_family)$/.test(sg)||p.has('adset')||/^ad\\d+$/i.test(p.get('utm_content')||'')){location.replace('/budgetcalculator/'+q+location.hash);}}catch(_){}})();</script>\n"
s=s.replace('<meta charset="utf-8">\n','<meta charset="utf-8">\n'+rd,1); open(R+"/index.html","w").write(s)

# ---------- Car loan guide (TL + EN): cache-busting, html lang, hreflang, EN assessment box, old-slug redirect
from loanguide import SLUGS as _ZS, PDFS as _ZP, OLD_SLUG as _ZO, SWITCH as _ZSW
import re as _re
_HL={"tl":"fil-PH","en":"en-PH"}
_ALT="".join(f'<link rel="alternate" hreflang="{_HL[l]}" href="{D}/blog/{_ZS[l]}/">\n' for l in ("tl","en"))+f'<link rel="alternate" hreflang="x-default" href="{D}/blog/{_ZS["en"]}/">\n'
for _l in ("tl","en"):
    _zp=R+f"/blog/{_ZS[_l]}/index.html"; _s=open(_zp).read()
    _s=_s.replace('src="/assets/lead.js"',f'src="/assets/lead.js?v={_vh("/assets/lead.js")}"').replace('href="/assets/site.css"',f'href="/assets/site.css?v={_vh("/assets/site.css")}"')
    if os.path.exists(R+_ZP[_l]): _s=_s.replace(f'href="{_ZP[_l]}"',f'href="{_ZP[_l]}?v={_vh(_ZP[_l])}"')
    _s=_s.replace('<article class="art"><div class="w nar"><header>','<article class="art"><div class="w nar">'+_ZSW[_l]+'<header>',1)
    _s=_s.replace('<html lang="en-PH">',f'<html lang="{_HL[_l]}">',1).replace('</head>',_ALT+'</head>',1)
    _s=_s.replace(f'<meta property="og:locale" content="en_PH">',f'<meta property="og:locale" content="{"fil_PH" if _l=="tl" else "en_PH"}">',1)
    # no zero-downpayment promotion on these pages (dealer restriction)
    _s=_s.replace('with all-in Zero DP and low-DP options.','with all-in down payment and monthly options.')
    _s=_re.sub(r'<li><a href="/(?:blog|tips|guides)/[^"]*zero[^"]*/">[^<]*</a></li>','',_s)
    _s=_re.sub(r'<li><a href="/mitsubishi-zero-down-payment-promo/">[^<]*</a></li>','',_s)
    if _l=="tl": _s=_s.replace(LACTA,LACTA_TL)
    _s=_s.replace('href="/loan-assessment/"',f'href="/loan-assessment/?lang={_l}"')
    open(_zp,'w').write(_s)
os.makedirs(R+f'/blog/{_ZO}',exist_ok=True)
open(R+f'/blog/{_ZO}/index.html','w').write(f'<!doctype html><html lang="en-PH"><head><meta charset="utf-8"><title>Moved: Paano Ma-approve sa Car Loan</title><link rel="canonical" href="{D}/blog/{_ZS["tl"]}/"><meta name="robots" content="noindex,follow"><meta http-equiv="refresh" content="0; url=/blog/{_ZS["tl"]}/"><script>location.replace("/blog/{_ZS["tl"]}/"+location.search+location.hash)</script></head><body><p>This guide has moved to <a href="/blog/{_ZS["tl"]}/">Paano Ma-approve sa Car Loan</a>.</p></body></html>\n')
# ---------- English-default: EN twin primary in listings; Taglish-only tips get html lang + EN pointer
import glob as _gl
_TLG=_ZS["tl"]
for _f in _gl.glob(R+"/**/index.html",recursive=True):
    if f"/blog/{_TLG}/" in _f or f"/blog/{_ZO}/" in _f or "/tips/paano-" in _f: continue
    _s=open(_f).read();_o=_s
    _s=_re.sub(r'<li class="card pad"><h2 class="h3"><a href="/blog/'+_TLG+r'/">.*?</li>','',_s,flags=_re.S)
    _s=_re.sub(r'<li><a href="/blog/'+_TLG+r'/">[^<]*</a></li>','',_s)
    _s=_s.replace(f'href="/blog/{_TLG}/"',f'href="/blog/{_ZS["en"]}/"')
    if _s!=_o: open(_f,"w").write(_s)
TL_ONLY={"tips/paano-mag-car-loan":("/blog/how-to-get-car-loan-approved-philippines/","Read the English car loan guide →"),
         "tips/paano-bumili-ng-bagong-sasakyan":("/tips/first-time-car-buyer-checklist/","Read the English first-time car buyer checklist →")}
for _k,(_u,_t) in TL_ONLY.items():
    _f=R+"/"+_k+"/index.html";_s=open(_f).read()
    _s=_s.replace('<html lang="en-PH">','<html lang="fil-PH">',1).replace('<meta property="og:locale" content="en_PH">','<meta property="og:locale" content="fil_PH">',1)
    _s=_s.replace('<article class="art"><div class="w nar"><header>',f'<article class="art"><div class="w nar"><p class="zlang"><a href="{_u}" hreflang="en-PH" lang="en">{_t}</a></p><header>',1)
    _s=_s.replace(LACTA,LACTA_TL)
    _s=_s.replace('<p class="abn">Written by ','<p class="abn">Isinulat ni ').replace('<a href="/about/">About Richard</a> · <a href="'+MSG+'" rel="noopener">Message Richard on Messenger</a>','<a href="/about/">Tungkol kay Richard</a> · <a href="'+MSG+'" rel="noopener">I-message si Richard sa Messenger</a>')
    open(_f,"w").write(_s)
# ---------- sitemap/robots
PAGES.append("/privacy/")
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>{D}{p}</loc><lastmod>2026-10-21</lastmod></url>\n" for p in PAGES)+"</urlset>\n"
open(R+"/sitemap.xml","w").write(sm)
AI_BOTS=["GPTBot","OAI-SearchBot","ChatGPT-User","PerplexityBot","ClaudeBot","Google-Extended","Bingbot"]
open(R+"/robots.txt","w").write(f"User-agent: *\nAllow: /\n\n"+"".join(f"User-agent: {b}\nAllow: /\n\n" for b in AI_BOTS)+f"Sitemap: {D}/sitemap.xml\n")
def _ll(items,base): return "".join(f"- [{a['title']}]({D}/{base}/{a['slug']}/): {a['desc']}\n" for a in items)
open(R+"/llms.txt","w").write(f"""# Mitsubishi Motors by Richard Cuagdan

> Personal sales website of Richard Cuagdan, Mitsubishi Sales Executive at Mitsubishi San Juan Motors, San Jose del Monte (SJDM), Bulacan, Philippines. Not the official Mitsubishi Motors Philippines website. Prices shown are official SRPs; promos are subject to bank approval.

## Key pages
- [Home]({D}/): Mitsubishi lineup and SRPs
- [Cars]({D}/cars/): every current model and variant with SRP
- [Budget calculator]({D}/budgetcalculator/): match a unit to your income
- [Book a test drive]({D}/test-drive/): Monday to Saturday, 8 AM to 5 PM
- [Apply]({D}/apply/): financing or cash application
- [Promos]({D}/promos/): this month's all-in promos, two options per unit (Option A lowest down payment, unlocked with a short form; Option B 30% down payment with a lower monthly), subject to bank approval
- [Guides & Tips]({D}/tips/): every guide, blog post and tip in one list, newest first
- [About]({D}/about/) and [Contact]({D}/contact/)

## Buying guides (evergreen, with dated monthly promo table)
"""+"".join(f"- [{a['title']}]({D}/{a['slug']}/): {a['desc']}\n" for a in LANDINGS)+f"""
## Contact
- Sales executive: Richard Dennis Cuagdan, Car Sales Executive
- Mobile (call or text): {TELD} ({TEL})
- Dealer: Mitsubishi San Juan Motors (authorized Mitsubishi dealer)
- Areas served: San Jose del Monte (SJDM), Bulacan and Quezon City; message or call for showroom visits and directions
- Hours: Monday to Saturday, 8:00 AM to 5:00 PM
- Messenger: {MSG}

## Models
"""+"".join(f"- [{m['name']}]({D}/cars/{m['slug']}/): {m['blurb']}\n" for m in MODELS)+"\n## Guides & Tips (all articles, newest first; index: "+D+GT+")\n"+"".join(f"- [{t}]({D}{u}): {d}\n" for u,t,d,dt in _GTL if u not in GT_LAND))
import og as _og
_og.inject("/budgetcalculator/","/assets/img/xpglx_x37.webp","Budget Fit Calculator | Mitsubishi Motors by Richard","Find the Mitsubishi that fits your monthly budget: Mirage G4, Xpander, L300, Triton, Destinator, Montero Sport all-in financing.")
_og.inject("/privacy/","/assets/img/xpglx_x37.webp","Privacy Policy | Mitsubishi Motors by Richard Dennis Cuagdan","How Richard Dennis Cuagdan (Mitsubishi San Juan Motors) collects and protects your personal information under the Data Privacy Act.")
# official three-diamond mark in standalone pages' header + responsive table wrappers site-wide
_OLDMK='<svg viewBox="0 0 24 24" width="26" height="26" aria-hidden="true"><path fill="#E60012" d="M12 2l3.2 5.5L12 13 8.8 7.5zM5.6 13l3.2-5.5L12 13l-3.2 5.5H2.4zM18.4 13l-3.2-5.5L12 13l3.2 5.5h6.4z"/></svg>';_NEWMK='<svg viewBox="0 -15.465 224.9 224.9" width="26" height="26" aria-hidden="true"><path fill="#e60012" d="m112.45 0 38.42 65.13-38.42 65.12L74.03 65.6Zm0 130.25h74.96l37.49 63.72h-74.97zm0 0H37.48L0 193.97h74.97z"/></svg>'
for _f in _gl.glob(R+'/**/*.html',recursive=True):
    if '/_src/' in _f: continue
    _s=open(_f).read();_o=_s.replace(_OLDMK,_NEWMK)
    _o=_o.replace('href="/assets/site.css"','href="/assets/site.css?v='+_vh('/assets/site.css')+'"')
    _o=_re.sub(r'(?<!<div class="tw">)(<table\b.*?</table>)',r'<div class="tw">\1</div>',_o,flags=_re.S)
    if _o!=_s: open(_f,'w').write(_o)
# favicon set for the standalone pages (not built by page())
_ICONS='<link rel="icon" href="/favicon.ico?v=2" sizes="48x48"><link rel="icon" href="/assets/favicon.svg?v=2" type="image/svg+xml"><link rel="apple-touch-icon" href="/apple-touch-icon.png?v=2"><link rel="manifest" href="/site.webmanifest?v=2">'
for _p in ("/privacy/",):
    _fp=R+_p+"index.html";_s=open(_fp).read()
    if "favicon.ico?v=2" not in _s: open(_fp,"w").write(_s.replace("</head>",_ICONS+"</head>",1))

# --- Own site chat: every in-content Messenger CTA becomes an own-chat opener ([data-chat]); the footer .fbl link stays Messenger.
# Without JS / before the own chat boots, the link still falls back to Messenger. ---
import re as _re, glob as _gl
_LBL={'Message Richard':'Chat with Richard','Message me':'Chat with me','message me on Messenger':'chat with me here','mag-message sa akin sa Messenger':'mag-chat sa akin dito'}
def _chatify(m):
    a,txt=m.group(1),m.group(2)
    if 'class="fbl"' in a or 'data-chat' in a: return m.group(0)
    a=a.replace('<a ','<a data-chat ',1);a=_re.sub(r'href="https://m\.me/[^"]*"','href="#chat"',a)
    return a+_LBL.get(txt,txt)
for _f in (_gl.glob(R+'/**/*.html',recursive=True) if SITECHAT else []):  # shelved: only when SITECHAT is on
    if '/_src/' in _f: continue
    _s=open(_f).read()
    _n=_re.sub(r'(<a [^>]*href="https://m\.me/[^"]*"[^>]*>)([^<]*)',_chatify,_s)
    if _n!=_s: open(_f,'w').write(_n)

# --- inject the site chat flag + loader into every page (skip redirect stubs) ---
_SCV=_vh("/assets/chat.js"); _SCL=_vh("/assets/sitechat.js")
_SCTAG=f'<script>window.SITECHAT_ON={"true" if SITECHAT else "false"};window.SITECHAT_V="{_SCV}"</script><script src="/assets/sitechat.js?v={_SCL}" defer></script>'
for _f in _gl.glob(R+'/**/*.html',recursive=True):
    if '/_src/' in _f: continue
    _s=open(_f).read()
    if 'http-equiv="refresh"' in _s or '</body>' not in _s: continue
    _n=_re.sub(r'<script>window\.SITECHAT_ON=.*?</script><script src="/assets/sitechat\.js[^"]*" defer></script>','',_s)
    _n=_re.sub(r'<script src="/assets/track\.js[^"]*" defer></script>','',_n)
    _n=_n.replace('src="/assets/calc.js"','src="/assets/calc.js?v='+_vh('/assets/calc.js')+'"')
    _n=_n.replace('</body>',_SCTAG+'<script src="/assets/track.js?v='+_vh('/assets/track.js')+'" defer></script></body>',1)
    if _n!=_s: open(_f,'w').write(_n)
print(len(PAGES),"pages")
# --- header dropdowns: close others when one opens; close on outside click (desktop)
_DDJS='<script>document.addEventListener("click",function(e){document.querySelectorAll("details.dd[open]").forEach(function(d){if(!d.contains(e.target))d.removeAttribute("open")})});document.querySelectorAll("details.dd").forEach(function(d){d.addEventListener("toggle",function(){if(d.open)document.querySelectorAll("details.dd[open]").forEach(function(o){if(o!==d)o.removeAttribute("open")})})})</script>'
for _f in _gl.glob(R+'/**/*.html',recursive=True):
    if '/_src/' in _f: continue
    _s=open(_f).read()
    if 'class="dd"' in _s and _DDJS not in _s: open(_f,'w').write(_s.replace('</body>',_DDJS+'</body>',1))

# --- FLOATING MESSENGER (2026-10-29): remove all in-content/header Messenger CTAs; keep footer .fbl link;
# add ONE floating Messenger button per page (tracked by track.js -> ref=web_floating_<page> + Pixel Contact). ---
_FM_SVG='<svg viewBox="0 0 36 36" aria-hidden="true" focusable="false"><path fill="#fff" d="M18 2.5C9.3 2.5 2.5 8.9 2.5 17.1c0 4.3 1.8 8 4.6 10.6.2.2.4.6.4.9l.1 2.6c0 .8.9 1.4 1.7 1l2.9-1.3c.2-.1.5-.1.8-.1 1.6.4 3.2.7 5 .7 8.7 0 15.5-6.4 15.5-14.6S26.7 2.5 18 2.5zm9.3 11.6-4.6 7.2c-.7 1.2-2.3 1.4-3.3.7l-3.6-2.7a.9.9 0 0 0-1.1 0l-4.9 3.7c-.7.5-1.5-.3-1.1-1l4.6-7.2c.7-1.2 2.3-1.4 3.3-.7l3.6 2.7c.3.3.8.3 1.1 0l4.9-3.7c.7-.5 1.5.3 1.1 1z"/></svg>'
_FM_TAG0='<a class="fmsg" id="fmsg" href="'+MSG+'" target="_blank" rel="noopener" data-msgr="floating" aria-label="Chat with Richard on Messenger" title="Chat with Richard on Messenger">'+_FM_SVG+'</a>'
_FM_JS='<script>(function(){var f=document.getElementById("fmsg");if(!f)return;var q="button[type=submit],input[type=submit],form button.btn,.af-big,.la-fina,.st-err,#st-r .btn";function c(){var r=f.getBoundingClientRect(),h=0;document.querySelectorAll(q).forEach(function(e){if(h||!e.offsetParent)return;var b=e.getBoundingClientRect();if(!(b.right<r.left-8||b.left>r.right+8||b.bottom<r.top-8||b.top>r.bottom+8))h=1});f.classList.toggle("fmsg-off",!!h)}var t;function s(){if(!t)t=requestAnimationFrame(function(){t=0;c()})}addEventListener("scroll",s,{passive:true});addEventListener("resize",s);document.addEventListener("click",function(){setTimeout(c,50)});setTimeout(c,0);addEventListener("load",c);try{new ResizeObserver(s).observe(document.body)}catch(_){}setInterval(c,1000)})()</script>'
_FM_TAG=_FM_TAG0+_FM_JS
_FM_CSS='<link rel="stylesheet" href="/assets/fmsg.css?v='+_vh('/assets/fmsg.css')+'">'
_FM_A=_re.compile(r'(\s*·\s*)?(\s?)<a ([^>]*href="https://m\.me/[^"]*"[^>]*)>(.*?)</a>',_re.S)
def _fm_strip(s,status):
    def f(m):
        attrs,txt=m.group(3),m.group(4)
        if 'class="fbl"' in attrs or 'class="fmsg"' in attrs or 'data-inquire=' in attrs: return m.group(0)  # Richard 2026-10-30: "Inquire this promo" -> Messenger stays
        plain=_re.sub(r'<[^>]+>','',txt).strip()
        if _re.search(r'class="[^"]*\bbtn\b',attrs) or plain.lower() in ('message richard on messenger','i-message si richard sa messenger'):
            return ''  # button / standalone CTA -> removed (floating button replaces it)
        if status: return m.group(0)  # /status/: plain text follow-up links stay
        return (m.group(1) or '')+m.group(2)+txt  # inline sentence link -> plain text
    s=_FM_A.sub(f,s)
    s=_re.sub(r'<p class="row">\s*</p>|<p>\s*</p>','',s)
    return s
for _f in _gl.glob(R+'/**/*.html',recursive=True):
    if '/_src/' in _f: continue
    _s=open(_f).read()
    if 'http-equiv="refresh"' in _s or '</body>' not in _s: continue
    _n=_re.sub(r'<a class="fmsg".*?</a>(<script>\(function\(\)\{var f=document\.getElementById\("fmsg"\).*?</script>)?','',_s,flags=_re.S); _n=_re.sub(r'<link rel="stylesheet" href="/assets/fmsg\.css[^"]*">','',_n)
    _n=_fm_strip(_n,'/status/' in _f.replace(R,''))
    if _f.replace(R,'').startswith('/loan-assessment/'):  # Richard 2026-10-29: no Messenger/Facebook link anywhere on the assessment
        _n=_re.sub(r'<p class="fsoc">.*?</p>','',_n,count=1,flags=_re.S)
        _n=_re.sub(r',?\s*"sameAs": \[[^\]]*\]','',_n)  # no FB/m.me URLs in this page's JSON-LD either
    else:
        _n=_n.replace('</head>',_FM_CSS+'</head>',1).replace('</body>',_FM_TAG+'</body>',1)
    if _n!=_s: open(_f,'w').write(_n)
