"""Branded 1200x630 link-preview (og:image) generator: real unit photo + dark gradient + short white heading."""
import os,re,hashlib
from PIL import Image,ImageDraw,ImageFont,ImageFilter
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT="/usr/share/fonts/truetype/sand-box/google/Inter/Inter-VariableFont_opsz,wght.ttf"
W,H=1200,630
OVR={"/":"Mitsubishi Cars & Promos in SJDM","/loan-assessment/":"AI Car Loan Assessment","/apply/":"Official Application Form",
 "/promos/":"October 2026 Promos","/cars/":"2026 Mitsubishi Models & Prices","/__404/":"Mitsubishi Motors","/about/":"About Richard Dennis Cuagdan","/guides/zero-dp-vs-low-dp/":"Down Payment Options Compared",
 "/budgetcalculator/":"Budget Fit Calculator","/privacy/":"Privacy Policy","/mitsubishi-zero-down-payment-promo/":"Mitsubishi Low DP Promos"}
def _f(sz,wt="Bold"):
    f=ImageFont.truetype(FONT,sz)
    try:f.set_variation_by_name(wt)
    except Exception:pass
    return f
def clean(t):
    t=re.sub(r'(?i)\bzero[\s-]*(dp|down\s*payment)\b\s*(vs\.?|or)\s*','',t)   # never show Zero DP on an image
    t=re.sub(r'(?i)\bzero[\s-]*(dp|down\s*payment)\b','Low DP',t)
    t=re.sub(r'(?i)\b(low dp)\s+vs\.?\s+low dp\b','Down Payment Options',t)
    t=t.strip(" -|:")
    return t[:1].upper()+t[1:]
def heading(path,title,crumbs,suffixes):
    if path in OVR:return OVR[path]
    if crumbs and len(crumbs)>=2:h=crumbs[-1][1]
    else:
        h=title
        for s in suffixes:
            if h.endswith(s):h=h[:-len(s)]
        h=h.split(" | ")[0]
    return clean(h)
def wrap(d,t,f,mw):
    lines,cur=[],""
    for w in t.split():
        x=(cur+" "+w).strip()
        if d.textlength(x,font=f)<=mw:cur=x
        else:
            if cur:lines.append(cur)
            cur=w
    if cur:lines.append(cur)
    return lines
def make(path,head,img):
    src=os.path.join(R,img.lstrip("/"))
    if not os.path.exists(src):src=os.path.join(R,"assets/img/xpglx_x37.webp")
    key=hashlib.md5((head+"|"+img+"|v3").encode()).hexdigest()[:8]
    slug=re.sub(r'[^a-z0-9]+','-',path.strip("/").lower()).strip("-") or "home"
    rel=f"/assets/og/{slug}-{key}.jpg";out=os.path.join(R,rel.lstrip("/"))
    if os.path.exists(out):return rel
    os.makedirs(os.path.dirname(out),exist_ok=True)
    im=Image.open(src).convert("RGB");sc=max(W/im.width,H/im.height);im=im.resize((round(im.width*sc),round(im.height*sc)),Image.LANCZOS)
    l=(im.width-W)//2;t=(im.height-H)//2;im=im.crop((l,t,l+W,t+H))
    g=Image.new("L",(W,H))
    gd=ImageDraw.Draw(g)
    for x in range(W):gd.line([(x,0),(x,H)],fill=int(140*max(0,1-x/W*1.15)**0.8*0.6)+110)
    for y in range(H):  # extra bottom darkening
        pass
    dark=Image.new("RGB",(W,H),(8,8,10));im=Image.composite(dark,im,g)
    d=ImageDraw.Draw(im)
    d.rectangle([60,70,72,190],fill=(230,0,18))
    for sz in (84,74,64,56,48):
        f=_f(sz);ls=wrap(d,head,f,720)
        if len(ls)<=3:break
    y=70
    for s in ls[:3]:
        d.text((96,y),s,font=f,fill="white");y+=int(sz*1.18)
    d.text((96,H-92),"Mitsubishi Motors by Richard",font=_f(30,"SemiBold"),fill=(235,235,235))
    d.text((96,H-54),"San Juan Motors · San Jose del Monte, Bulacan",font=_f(22,"Regular"),fill=(190,190,190))
    im.save(out,"JPEG",quality=84,optimize=True,progressive=True)
    return rel

def inject(path,img,title,desc,D="https://mitsubishipromos.online"):
    """Add og/twitter tags to a hand-written static page (idempotent: strips old og:image/twitter tags first)."""
    import html as H
    f=os.path.join(R,path.strip("/"),"index.html");s=open(f).read()
    s=re.sub(r'<meta (property="og:(image|title|description|type|image:[a-z]+)"|name="twitter:[a-z]+")[^>]*>\n?','',s)
    rel=make(path,OVR.get(path,title),img);e=lambda x:H.escape(x,quote=True)
    tags=(f'<meta property="og:type" content="website">\n<meta property="og:title" content="{e(title)}">\n<meta property="og:description" content="{e(desc)}">\n'
      f'<meta property="og:image" content="{D}{rel}">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n<meta property="og:image:type" content="image/jpeg">\n'
      f'<meta name="twitter:card" content="summary_large_image">\n<meta name="twitter:image" content="{D}{rel}">\n')
    s=re.sub(r'</title>\n+','</title>\n',s)
    s=s.replace('</title>\n','</title>\n'+tags,1);open(f,'w').write(s)
