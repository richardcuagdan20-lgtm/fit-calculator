# Generates article illustrations (brand: charcoal/white + Mitsubishi red). Run: python3 _src/illus.py
import os,json,sys
from PIL import Image,ImageDraw,ImageFont
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)));OUT=R+"/assets/img/ill/"
FP='/usr/share/fonts/truetype/sand-box/google/Inter/Inter-VariableFont_opsz,wght.ttf'
INK=(31,32,35);RED=(230,0,18);MU=(113,113,122);BG=(255,255,255);SOFT=(244,244,245);LINE=(228,228,231)
def F(s,w='Bold'):
    f=ImageFont.truetype(FP,s);f.set_variation_by_name(w);return f
W=1080;P=64
MAN={}
def wrap(d,t,f,mw):
    out=[];
    for para in t.split("\n"):
        cur=""
        for wd in para.split():
            tr=(cur+" "+wd).strip()
            if d.textlength(tr,font=f)<=mw: cur=tr
            else: out.append(cur);cur=wd
        out.append(cur)
    return out
def save(img,name):
    p=OUT+name+".webp";q=88
    while True:
        img.convert("RGB").save(p,"WEBP",quality=q,method=6)
        if os.path.getsize(p)<145000 or q<50: break
        q-=6
    MAN[name]=img.size;print(name,img.size,os.path.getsize(p)//1024,"KB")
def head(d,kick,title,dark=False):
    y=P
    d.rectangle([P,y,P+56,y+8],fill=RED);y+=30
    d.text((P,y),kick.upper(),font=F(26,'SemiBold'),fill=(161,161,170) if dark else MU);y+=48
    for ln in wrap(d,title,F(54),W-2*P):
        d.text((P,y),ln,font=F(54),fill=BG if dark else INK);y+=66
    return y+24
def foot(d,h,dark=False):
    d.text((P,h-P+8),"mitsubishipromos.online",font=F(22,'Medium'),fill=(161,161,170) if dark else MU)
def measure(fn):
    tmp=Image.new("RGB",(W,4000));return fn(ImageDraw.Draw(tmp),True)
def canvas(fn,name,dark=False):
    h=measure(lambda d,m:fn(d,m))
    img=Image.new("RGB",(W,h),INK if dark else BG);d=ImageDraw.Draw(img)
    if not dark: d.rounded_rectangle([2,2,W-3,h-3],radius=28,outline=LINE,width=3)
    fn(d,False);foot(d,h,dark);save(img,name)
def badge(d,x,y,t,r=34,fill=RED,fg=BG):
    d.ellipse([x,y,x+2*r,y+2*r],fill=fill)
    f=F(int(r*0.95)) if len(t)<3 else F(int(r*0.62))
    if t=="✓":
        d.line([(x+r*0.55,y+r*1.02),(x+r*0.9,y+r*1.38),(x+r*1.5,y+r*0.68)],fill=fg,width=max(5,r//6),joint="curve");return
    d.text((x+r,y+r),t,font=f,fill=fg,anchor="mm")
# ---------- layouts ----------
def tiles(name,kick,title,items,cols=2,dark=False):
    # items: (badge,label,sub)
    def fn(d,m):
        y=head(d,kick,title,dark);gap=24;tw=(W-2*P-gap*(cols-1))//cols
        rows=[items[i:i+cols] for i in range(0,len(items),cols)]
        for row in rows:
            hs=[]
            for b,l,s in row:
                lh=len(wrap(d,l,F(36),tw-56))*46+(len(wrap(d,s,F(28,'Regular'),tw-56))*38+8 if s else 0)
                hs.append(28+76+20+lh+28)
            rh=max(hs)
            for i,(b,l,s) in enumerate(row):
                x=P+i*(tw+gap)
                if not m:
                    d.rounded_rectangle([x,y,x+tw,y+rh],radius=22,fill=(46,47,51) if dark else SOFT)
                    badge(d,x+28,y+28,b,38)
                    yy=y+28+76+20
                    for ln in wrap(d,l,F(36),tw-56): d.text((x+28,yy),ln,font=F(36),fill=BG if dark else INK);yy+=46
                    if s:
                        yy+=8
                        for ln in wrap(d,s,F(28,'Regular'),tw-56): d.text((x+28,yy),ln,font=F(28,'Regular'),fill=(161,161,170) if dark else MU);yy+=38
            y+=rh+gap
        return y+P+10
    canvas(fn,name,dark)
def steps(name,kick,title,items):
    def fn(d,m):
        y=head(d,kick,title);r=36;tx=P+2*r+32;mw=W-tx-P
        for i,(l,s) in enumerate(items):
            ls=wrap(d,l,F(38),mw);ss=wrap(d,s,F(29,'Regular'),mw) if s else []
            h=max(2*r,len(ls)*48+len(ss)*40+(8 if ss else 0))
            if not m:
                if i<len(items)-1: d.line([(P+r,y+2*r),(P+r,y+h+40)],fill=LINE,width=6)
                badge(d,P,y,str(i+1),r)
                yy=y+6
                for ln in ls: d.text((tx,yy),ln,font=F(38),fill=INK);yy+=48
                yy+=8
                for ln in ss: d.text((tx,yy),ln,font=F(29,'Regular'),fill=MU);yy+=40
            y+=h+40
        return y+P
    canvas(fn,name)
def compare(name,kick,title,cols,rows,imgs=None):
    # cols: (A,B); rows: (label, a, b)
    def fn(d,m):
        y=head(d,kick,title);cw=(W-2*P-24)//2
        if imgs:
            ih=300
            for i,p in enumerate(imgs):
                x=P+i*(cw+24)
                if not m:
                    d.rounded_rectangle([x,y,x+cw,y+ih],radius=22,fill=SOFT)
                    im=Image.open(p).convert("RGBA");bb=im.getbbox();im=im.crop(bb);im.thumbnail((cw-40,ih-40),Image.LANCZOS)
                    d._image.paste(im,(x+(cw-im.width)//2,y+(ih-im.height)//2),im)
            y+=ih+20
        for i,c in enumerate(cols):
            x=P+i*(cw+24)
            if not m: d.rounded_rectangle([x,y,x+cw,y+76],radius=18,fill=RED if i else INK);d.text((x+cw//2,y+38),c,font=F(36),fill=BG,anchor="mm")
        y+=100
        for lab,a,b in rows:
            d.text((P,y),lab.upper(),font=F(24,'SemiBold'),fill=MU) if not m else None;y+=38
            la=wrap(d,a,F(34),cw-20);lb=wrap(d,b,F(34),cw-20);n=max(len(la),len(lb))
            if not m:
                for j,ln in enumerate(la): d.text((P,y+j*44),ln,font=F(34),fill=INK)
                for j,ln in enumerate(lb): d.text((P+cw+24,y+j*44),ln,font=F(34),fill=INK)
            y+=n*44+18
            if not m: d.line([(P,y),(W-P,y)],fill=LINE,width=2)
            y+=22
        return y+P
    canvas(fn,name)
def stats(name,kick,title,items,dark=True):
    # items: (big, label)
    def fn(d,m):
        y=head(d,kick,title,dark)
        for big,l in items:
            bf=F(88,'ExtraBold');ls=wrap(d,l,F(32,'Medium'),W-2*P-40)
            h=40+100+len(ls)*42+36
            if not m:
                d.rounded_rectangle([P,y,W-P,y+h],radius=22,fill=(46,47,51))
                d.rectangle([P,y+24,P+10,y+h-24],fill=RED)
                d.text((P+40,y+30),big,font=bf,fill=BG)
                yy=y+40+100
                for ln in ls: d.text((P+40,yy),ln,font=F(32,'Medium'),fill=(212,212,216));yy+=42
            y+=h+24
        return y+P
    canvas(fn,name,True)
def bars(name,kick,title,groups,cols,imgs):
    # groups: (label, unit, a, b)
    def fn(d,m):
        y=head(d,kick,title);cw=(W-2*P-24)//2;ih=260
        for i,p in enumerate(imgs):
            x=P+i*(cw+24)
            if not m:
                d.rounded_rectangle([x,y,x+cw,y+ih],radius=22,fill=SOFT)
                im=Image.open(p).convert("RGBA");im=im.crop(im.getbbox());im.thumbnail((cw-40,ih-50),Image.LANCZOS)
                d._image.paste(im,(x+(cw-im.width)//2,y+(ih-im.height)//2-10),im)
                d.text((x+cw//2,y+ih-24),cols[i],font=F(30),fill=INK if not i else RED,anchor="mm")
        y+=ih+40
        for lab,u,a,b in groups:
            if not m: d.text((P,y),lab.upper(),font=F(26,'SemiBold'),fill=MU)
            y+=44;mx=max(a,b);bw=W-2*P-230
            for j,(v,c,n) in enumerate([(a,INK,cols[0]),(b,RED,cols[1])]):
                if not m:
                    d.text((P,y+6),n,font=F(28,'SemiBold'),fill=INK)
                    L=int(bw*v/mx);d.rounded_rectangle([P+230,y,P+230+L,y+46],radius=12,fill=c)
                    d.text((P+230+L-16,y+23),f"{v} {u}",font=F(28),fill=BG,anchor="rm")
                y+=62
            y+=24
        return y+P
    canvas(fn,name)
def table(name,kick,title,header,rows,widths=None,note=""):
    # header: column titles; rows: list of cell tuples; first column bold
    n=len(header);tw=W-2*P;ws=widths or [1/n]*n;cw=[int(tw*x) for x in ws]
    def fn(d,m):
        y=head(d,kick,title);fs=F(28);fb=F(28,'SemiBold');pad=18
        x=P
        hl=[wrap(d,h,F(26,'SemiBold'),cw[i]-2*pad) for i,h in enumerate(header)];hh=max(len(l) for l in hl)*34+2*pad
        if not m:
            d.rounded_rectangle([P,y,W-P,y+hh],radius=16,fill=INK)
            for i,ls in enumerate(hl):
                for j,ln in enumerate(ls): d.text((x+pad,y+pad+j*34),ln.upper(),font=F(26,'SemiBold'),fill=BG)
                x+=cw[i]
        y+=hh+6
        for r_,row in enumerate(rows):
            cl=[wrap(d,c,fb if i==0 else fs,cw[i]-2*pad) for i,c in enumerate(row)];rh=max(len(l) for l in cl)*38+2*pad
            if not m:
                if r_%2==0: d.rounded_rectangle([P,y,W-P,y+rh],radius=14,fill=SOFT)
                x=P
                for i,ls in enumerate(cl):
                    for j,ln in enumerate(ls): d.text((x+pad,y+pad+j*38),ln,font=fb if i==0 else fs,fill=INK if i==0 else (RED if i==n-1 and n>2 else INK))
                    x+=cw[i]
            y+=rh+4
        if note:
            y+=16
            for ln in wrap(d,note,F(24,'Regular'),tw):
                if not m: d.text((P,y),ln,font=F(24,'Regular'),fill=MU)
                y+=32
        return y+P+10
    canvas(fn,name)
def photo(name,src,crop=None):
    im=Image.open(src).convert("RGB")
    if crop: 
        w,h=im.size;tw=w;th=int(w*crop)
        if th>h: th=h;tw=int(h/crop)
        im=im.crop(((w-tw)//2,(h-th)//2,(w-tw)//2+tw,(h-th)//2+th))
    im.thumbnail((1200,1200),Image.LANCZOS);save(im,name)

def bulk():
    M="/workspace/mmpc/final/"
    XP=M+"Xpander/color_xpander_26my_rn_color-c31_angle45.png"
    def cut(name,src,bg=(244,244,245)):
        im=Image.open(src).convert("RGBA");im=im.crop(im.getbbox());im.thumbnail((1040,560),Image.LANCZOS)
        c=Image.new("RGB",(1200,675),bg);c.paste(im,((1200-im.width)//2,(675-im.height)//2+20),im);save(c,name)
    # B1 afford
    stats("afford-rule","Income guide","Keep the monthly at 30–35% of income",[("÷ 0.35","Monthly ÷ 0.35 = minimum gross monthly income"),("÷ 0.30","Monthly ÷ 0.30 = comfortable gross monthly income")])
    table("afford-table","October 2026 · Zero DP, 60 months","Income each monthly needs",["Unit","Zero DP / mo","Gross income"],[("L300 Dual AC","₱21,405","₱61.2K–₱71.4K"),("Xpander GLX MT","₱22,641","₱64.7K–₱75.5K"),("Xpander GLX AT","₱23,877","₱68.2K–₱79.6K"),("Xpander GLS AT","₱25,937","₱74.1K–₱86.5K"),("Xpander Cross","₱28,389","₱81.1K–₱94.6K"),("Destinator GLX","₱28,615","₱81.8K–₱95.4K"),("Triton GX AT","₱28,900","₱82.6K–₱96.3K"),("Montero GLX MT","₱30,284","₱86.5K–₱100.9K"),("Destinator GLS","₱32,942","₱94.1K–₱109.8K"),("Montero GLS","₱39,699","₱113.4K–₱132.3K"),("Destinator GT","₱39,740","₱113.5K–₱132.5K")],[0.4,0.27,0.33],"Dealer promos, all-in, subject to bank approval and change without notice.")
    table("afford-dp","Zero DP vs low DP","A bigger DP lowers the monthly",["Unit","Zero DP","With DP"],[("Xpander GLX MT","₱22,641","₱19,811 (₱148K DP)"),("Xpander GLS AT","₱25,937","₱22,695 (₱148K DP)"),("Destinator GLS","₱32,942","₱30,883 (₱123K DP)"),("Triton GX AT","₱28,900","₱25,200 (₱140K DP)")],[0.36,0.24,0.40],"October 2026 promos, 60 months, all-in.")
    tiles("afford-ways","Doesn't fit yet?","Three ways to make it fit",[("1","Add a co-borrower","Combined income"),("2","Bigger down payment","Lower monthly"),("3","Right variant","GLX MT vs GLS AT")],cols=1)
    cut("afford-xpander",M+"Xpander/color_xpander_26my_rn_color-u33_angle45.png")
    # B2 triton
    tiles("tr-glance","Triton at a glance","Built for work and family",[("1","2.4L 4N16 turbo diesel",""),("2","Manual or automatic","By variant"),("3","2WD or 4WD","By variant"),("4","Open cargo bed","")],cols=2)
    photo("tr-cargo-photo",M+"Triton/int_triton_24my_tr_the-all-new_lhd_mv_cargo_proxy_mitsubishi.jpg",9/16)
    compare("tr-2wd4wd","2WD or 4WD?","Choose by your roads",("2WD","4WD"),[("Roads","Paved highways, city, well-kept provincial roads","Mud, steep farm roads, river crossings, hills"),("Good for","Deliveries, contractors in town","Farms, resorts, rough rainy-season routes")])
    stats("tr-promo","Triton GX 2.4D 2WD A/T · October 2026","SRP ₱1,430,000",[("₱28,900/mo","Zero DP, 60 months, all-in"),("₱25,200/mo","With ₱140K DP, plus ₱20K fuel")])
    steps("tr-bed","Cargo bed","Rules for working owners",[("Stay within the rated payload","Check the spec for your variant"),("Tie down every load","Straps or cargo net"),("Protect the bed","Ask about a bed liner"),("Cover what needs cover","Keep a tarpaulin in the cab")])
    # B3 montero
    stats("ms-shared","Every Montero Sport","Same 2.4L turbo diesel",[("181 PS · 430 Nm","2.4L 4N15 MIVEC intercooled turbo diesel, Euro 4"),("7 seats","Ladder frame for long drives and heavy loads")])
    table("ms-table","October 2026 promos · 60 months","Montero Sport variants",["Variant","SRP","Lowest monthly"],[("GLX 2WD M/T","₱1,568,000","₱28,265 (₱30K DP)"),("GLS 2WD A/T","₱1,927,000","₱37,218 (₱138K DP)"),("Black Series 2WD A/T","₱2,190,000","₱42,297 (₱218K DP)"),("Black Series 4WD A/T","₱2,530,000","₱48,864 (₱283K DP)")],[0.38,0.26,0.36],"All-in, subject to bank approval and change without notice.")
    photo("ms-bs-photo",M+"Montero Sport/ext_monterosport_24my_ps_phl_black_4wd_8at_straight-front_lhd_jh3.jpg",9/16)
    tiles("ms-pick","Which variant?","Match it to how you drive",[("MT","GLX M/T","Lowest monthly, comfortable with a clutch"),("AT","GLS A/T","Daily traffic, 8-speed automatic"),("2WD","Black Series 2WD","Top trim for city and highway"),("4WD","Black Series 4WD","Rough, muddy or steep roads")],cols=2)
    # B4 xpander variants
    stats("xv-engine","Every Xpander","Same engine, different packages",[("105 PS · 141 Nm","1.5L MIVEC gasoline in all four"),("7 seats","GLX MT, GLX AT, GLS AT and Xpander Cross")])
    table("xv-table","October 2026 promos · 60 months","Xpander variants and monthlies",["Variant","Zero DP","Low DP","Fuel"],[("GLX M/T","₱22,641","₱19,811","₱30K"),("GLX A/T","₱23,877","₱20,892","₱60K"),("GLS A/T","₱25,937","₱22,695","₱60K"),("Cross A/T","₱28,389","₱24,840","₱60K")],[0.28,0.24,0.26,0.22],"Low DP: ₱148K (GLX MT, GLS, Cross) or ₱138K (GLX AT). SRP ₱1,099,000 / ₱1,159,000 / ₱1,259,000 / ₱1,378,000.")
    photo("xv-cross-photo",M+"Xpander Cross/int_xpandercross_26my_xs_lhd_mv_dashboard.jpg",9/16)
    tiles("xv-pick","Quick picker","Which Xpander fits you?",[("MT","GLX M/T","Tightest budget, manual driver"),("AT","GLX A/T","Daily traffic, many drivers"),("GLS","GLS A/T","A nicer daily cabin"),("X","Xpander Cross","Crossover look")],cols=2)
    # B5 destinator variants
    stats("dv-shared","Every Destinator","Same turbo in all three",[("163 PS · 250 Nm","1.5L turbo 4B40 with CVT"),("214 mm","Ground clearance, seven seats")],)
    table("dv-table","October 2026 promos · 60 months","Destinator GLX, GLS, GT",["Variant","SRP","Zero DP","Low DP"],[("GLX","₱1,389,000","₱28,615","₱26,827 (₱93K)"),("GLS","₱1,599,000","₱32,942","₱30,883 (₱123K)"),("GT Mono","₱1,929,000","₱39,740","₱37,256 (₱88K)"),("GT Two-Tone","₱1,939,000","₱39,740","₱37,256 (₱88K)")],[0.22,0.25,0.22,0.31],"Fuel: GLS ₱20K, GT ₱40K. All-in, subject to bank approval.")
    photo("dv-cabin",M+"Destinator/int_destinator_interior_dsyp.jpg",9/16)
    steps("dv-steps","How to choose","3 steps to the right Destinator",[("Start with your income","30–35% of gross monthly income"),("List 3 must-have features","Check them on the spec sheet"),("Test drive with the family","Bring your third-row passengers")])
    # T1 PMS
    tiles("pms-what","PMS in one line","Preventive, not repair",[("✓","Replace fluids and filters",""),("✓","Inspect wear items",""),("✓","Catch problems early",""),("✓","Protect your warranty","")],cols=2)
    stats("pms-rule","Your schedule","Whichever comes first",[("Km or months","Each PMS is due by kilometers or months, whichever comes first"),("Owner's manual","Your exact intervals are in the manual and warranty booklet")])
    tiles("pms-checks","At the service center","What PMS usually covers",[("1","Engine oil and filter",""),("2","Air and cabin filters",""),("3","Brakes and brake fluid",""),("4","Coolant and fluids",""),("5","Tires and rotation",""),("6","Battery, lights, wipers",""),("7","Underchassis","")],cols=2)
    stats("pms-free","All-in package","Included with your new car",[("Up to 5,000 km","Free labor on early services; parts and fluids usually paid"),("3 years","Warranty. Keep to the PMS schedule to protect it")])
    steps("pms-habits","Owner habits","PMS habits that pay off",[("Book ahead","Before long weekends"),("Stay on schedule","Protect your warranty"),("Keep every receipt","Helps claims and resale"),("Mention anything odd","Noises, lights, vibrations")])
    # T2 break-in
    stats("bi-1000","Break-in","The first 1,000 km",[("Gentle and varied","Vary speed and RPM, accelerate smoothly"),("Owner's manual","Follow the exact guidance for your unit")])
    compare("bi-dodont","First 1,000 km","Do's and don'ts",("Do","Don't"),[("Speed","Vary speed and RPM","Hold one speed for very long"),("Throttle","Accelerate smoothly","Full-throttle starts"),("Brakes","Gentle braking","Hard, sudden stops"),("Load","Normal loads","Tow or overload")])
    steps("bi-week","Week one","New owner checklist",[("Read the manual","Break-in, PMS, warning lights"),("Look under the car","Any drips overnight?"),("Check the freebies","Against your release list"),("Save the numbers","Service, insurer, sales executive"),("Mark your first PMS","In your calendar")])
    photo("bi-destinator",M+"Destinator/ext_destinator_new_launch_kv13_no_copy.jpg",9/16)
    # T3 insurance
    compare("ins-ctpl","Two kinds of cover","CTPL vs comprehensive",("CTPL","Comprehensive"),[("Required?","Yes, for LTO registration","Usually required by banks while financed"),("Covers","Injury or death of third parties","Your own car, theft, third-party property and more"),("Floods","No","Only with acts of nature (AON)")])
    tiles("ins-comp","Comprehensive","What it typically covers",[("1","Own damage",""),("2","Theft",""),("3","Third-party property",""),("4","Excess bodily injury",""),("5","Auto personal accident","By policy"),("?","Acts of nature","Often an add-on")],cols=2)
    tiles("ins-allin","All-in package","Insurance already included",[("✓","TPL insurance",""),("✓","1-year comprehensive","Rate locked for 3 years"),("✓","Chattel mortgage",""),("✓","3-year warranty","")],cols=2)
    steps("ins-claim","Accident?","How to file a claim",[("Stay safe and take photos","Scene, both cars, plates"),("Get a police or incident report",""),("Call your insurer right away",""),("Submit the documents","Claim form, OR/CR, license, photos"),("Pay the participation fee","Per your policy")])

def bulk2():
    M="/workspace/mmpc/final/"
    L3=M+"L300/ext_l300_l300-fb_1080_fl.png"
    # car seat
    stats("cs-rule","RA 11229 · Child Safety in Motor Vehicles Act","The car seat rule",[("12 & below","Must use an appropriate car seat while the engine is running or on the road"),("150 cm","Unless at least 150 cm (59 in) tall and secured with the regular seat belt")])
    compare("cs-front","Front or back?","Where your child should sit",("Under 150 cm","150 cm or taller"),[("Restraint","Approved car seat for age, height, weight","Regular seat belt"),("Seat","Rear seat","Front allowed if properly belted"),("Always","Never left alone in the car","Never left alone in the car")])
    steps("cs-stages","Car seat stages","Grow through the stages",[("Rear-facing infant seat","Babies"),("Forward-facing with harness","Toddlers"),("Booster seat","Older kids"),("Regular seat belt","At least 150 cm tall")])
    tiles("cs-install","Installation","Check before every trip",[("✓","Read both manuals",""),("✓","ISOFIX or correct belt path",""),("✓","Minimal side movement",""),("✓","Snug harness, clip at armpit",""),("✓","No thick jackets",""),("?","Ask me on release day","")],cols=2)
    photo("cs-cabin",M+"Xpander Cross/int_xpandercross_26my_xs_lhd_ft_2ndseat.jpg",9/16)
    # new driver
    steps("nd-plan","Step up gradually","Your first 3 months",[("Weeks 1–2: quiet, familiar routes","Off-peak, with an experienced driver"),("Weeks 3–4: busier roads","Lane discipline and signals"),("Month 2: expressway","Short off-peak stretch"),("Month 3: night and rain","One new condition at a time")])
    tiles("nd-habits","Safe habits","Drive like a pro from day one",[("3s","Following distance","More in rain"),("✓","Mirrors and blind spots",""),("✓","Signal early",""),("✓","Phone away",""),("✓","Yield to pedestrians",""),("✕","Tired or drunk","Never")],cols=2)
    tiles("nd-kit","Glovebox and trunk","Always in the car",[("✓","License, OR/CR",""),("✓","Early warning device",""),("✓","Basic tools",""),("✓","Powerbank",""),("✓","Insurer's hotline",""),("✓","Payong, water, first aid","")],cols=2)
    photo("nd-mirage",M+"Mirage G4/ext_mirageg4_easy_to_manoeuvre_1080x760.jpg",9/16)
    # commute
    tiles("cm-routes","SJDM to Metro Manila","Know your route, and a backup",[("1","Quirino Highway","Toward Fairview and Commonwealth"),("2","NLEX","Depending on where you work"),("3","Live traffic check","Before leaving and at junctions")],cols=1)
    tiles("cm-timing","Timing","Beat the peak",[("15–30","Leave earlier","Minutes make a difference"),("✓","School days, paydays","Usually heavier"),("!","Rainy days","Leave earlier still"),("✓","Shift your hours","If work allows")],cols=2)
    stats("cm-coding","Before you go","Coding and toll checks",[("Number coding","MMDA's scheme applies on covered Metro Manila roads, wherever your car is registered"),("RFID","Keep it loaded and the sticker readable")])
    stats("cm-xpander","Carpool and school-run pick","Xpander GLX A/T · October 2026",[("₱23,877/mo","Zero DP, 60 months, all-in. SRP ₱1,159,000"),("₱60K fuel","Plus ₱20,892/mo option with ₱138K DP")])
    # trade-in
    steps("ti-how","Trade-in","How it works",[("Appraisal","Condition, mileage, model, demand"),("Offer","Ask how it was computed"),("Paperwork","Deed of sale, loan payoff if any"),("Applied to your new car","Ask how it works with the promo")])
    tiles("ti-docs","Documents","Bring these to the appraisal",[("✓","Original OR/CR",""),("✓","Owner's valid IDs",""),("✓","Loan payoff amount","If financed"),("✓","Service records",""),("✓","Spare key and manual","")],cols=2)
    compare("ti-vs","Two ways to sell","Trade-in vs selling it yourself",("Trade-in","Sell privately"),[("Effort","One transaction, less paperwork","Listings, haggling, viewings"),("Price","Fair, convenient","Possibly higher"),("Risk","Low","Strangers, test drives, payment")])
    photo("ti-destinator",M+"Destinator/ext_destinator_mam.jpg",9/16)
    # resale
    tiles("rv-habits","Resale value","8 habits that protect it",[("1","PMS on schedule",""),("2","Keep service records",""),("3","Avoid floods",""),("4","Repair damage properly",""),("5","Protect paint and interior",""),("6","Easy on modifications",""),("7","Reasonable mileage",""),("8","Complete documents","")],cols=2)
    tiles("rv-buy","At purchase","Choices that help later",[("✓","Popular model and variant",""),("✓","Common colors","White, silver, black"),("✓","Right transmission",""),("✓","Warranty and records","")],cols=2)
    tiles("rv-hurts","Avoid these","What hurts resale value most",[("✕","Flood or major accident",""),("✕","Missing service records",""),("✕","Smoke and pet odor",""),("✕","Extreme modifications",""),("✕","Incomplete documents","")],cols=1)
    photo("rv-montero",M+"Montero Sport/ext_monterosport_24my_ps_lhd_mv_p1-2_lux.jpg",9/16)
    # release day
    tiles("rd-bring","Before you go","Release day prep",[("✓","Confirm the schedule",""),("✓","Valid IDs and documents",""),("✓","Driver's license",""),("✓","Arrive with daylight",""),("✓","Bring a helper","")],cols=2)
    compare("rd-inspect","Inspect the unit","Outside and inside",("Exterior","Interior"),[("Look","Paint, panels, gaps","Seats, trim, upholstery"),("Check","Glass, mirrors, tires and spare","AC, windows, locks, wipers"),("Test","All lights and hazards","Infotainment, camera, low mileage")])
    steps("rd-docs","Documents and inclusions","Before you sign off",[("Match VIN and engine number",""),("Insurance details and hotline",""),("Registration, CR and plates status",""),("Freebies on your release list",""),("Manual, warranty, PMS schedule","")])
    photo("rd-cross",M+"Xpander Cross/ext_xpandercross_mmpc-rnc-fl26_mid.jpg",9/16)
    # christmas
    tiles("xm-sg","Simbang Gabi","Early-morning drives",[("1","Leave earlier","Parking fills up fast"),("2","Watch for pedestrians","Kids and seniors in the dark"),("3","Clean windshield, proper lights",""),("4","Not puyat","Switch drivers")],cols=2)
    tiles("xm-mall","Mall runs","December parking smarts",[("✓","Weekday mornings",""),("✓","One list, one trip",""),("✓","Well-lit, busy spots",""),("✓","Bags in the trunk",""),("✓","Note your slot",""),("✓","Patience in the lot","")],cols=2)
    steps("xm-party","Christmas parties","If you drink, don't drive",[("Choose a designated driver","Before you leave the house"),("Or book a ride","Pick up the car the next day"),("Host responsibly","Help guests get home safely")])
    stats("xm-xpander","Family 7-seater · October 2026","Xpander GLS A/T",[("₱25,937/mo","Zero DP, 60 months, all-in. SRP ₱1,259,000"),("₱22,695/mo","With ₱148K DP, plus ₱60K fuel")])
    # L300 vs Triton
    TR=M+"Triton/ext_triton_24my_tr_the-all-new_lhd_mv_intro_p_proxy_mitsubishi.jpg"
    compare("lt-glance","Truck or pickup?","L300 vs Triton",("L300 Dual AC","Triton GX AT"),[("Engine","2.2L 4N14 turbo diesel","2.4L 4N16 turbo diesel"),("Gearbox","5-speed manual","Automatic"),("Best at","Daily cargo","Work plus family")],imgs=[L3,R+"/assets/img/tr_gx_u28.webp"])
    table("lt-promo","October 2026 · 60 months, all-in","Promo monthlies",["Unit","SRP","Zero DP","Low DP"],[("L300 Dual AC","₱1,039,000","₱21,405","₱18,789 (₱123K)"),("Triton GX AT","₱1,430,000","₱28,900","₱25,200 (₱140K)")],[0.27,0.24,0.20,0.29],"Both with ₱20K fuel. Subject to bank approval and change without notice.")
    compare("lt-fit","Which fits your negosyo?","Choose by the job",("L300","Triton"),[("Business","Deliveries, restocking, hardware, catering","Contractors, farms, resorts"),("Routes","City and highway","Farm roads, sites, rough roads"),("Family use","Work truck","Weekend family vehicle")])
    steps("lt-steps","Before you decide","Run the numbers both ways",[("List what you carry weekly","Heaviest regular load"),("Add up ownership costs","Fuel, insurance, PMS, driver, tolls"),("Check the income guide","30–35% of gross income"),("Test drive both","On your real routes")])

def bulk3():
    M="/workspace/mmpc/final/"
    stats("rn-3","Rainy season","See, slow, space",[("Headlights on","Not hazards while moving"),("2× distance","A 3-second gap becomes 6 or more")])
    steps("rn-hydro","Hydroplaning?","Do this, in order",[("Don't brake hard",""),("Ease off the gas",""),("Steer straight",""),("Wait for grip","")])
    tiles("rn-check","Before the rains","Pre-rain car check",[("✓","Wipers and washer fluid",""),("✓","Tire tread and pressure",""),("✓","All lights",""),("✓","Brakes at PMS","")],cols=2)
    photo("rn-road",M+"Xforce/ext_xforce_25my_xf_ft_mode_wet.jpg",9/16)
    tiles("tc-5","Tire care","5 things to check",[("1","Pressure","Monthly, when cold"),("2","Tread","Wear indicators"),("3","Damage","Bulges, cracks, nails"),("4","Rotation","Per owner's manual"),("5","Age","Date code on sidewall")],cols=2)
    compare("tc-pressure","Get it right","Tire pressure effects",("Too low","Too high"),[("Wear","Edges wear faster","Center wears faster"),("Effect","Wastes fuel, heats up","Less grip, harsher ride")])
    tiles("tc-replace","Replace when","Signs it's time",[("✕","Tread at the indicators",""),("✕","Sidewall bulge",""),("✕","Deep cuts or cracks",""),("?","Older tires","Have them inspected")],cols=2)
    photo("tc-wheel",M+"Xpander/ext_xpander_26my_xp_lhd_mv_wheel.jpg",9/16)
    tiles("ac-why","Weak or smelly AC?","Common causes",[("1","Clogged cabin filter",""),("2","Moisture in the system",""),("3","Dusty condenser",""),("4","Low refrigerant or worn part","Needs a technician")],cols=2)
    steps("ac-habits","Daily habits","Keep it cold and fresh",[("Park in the shade","Or use a sunshade"),("Vent first","Windows down for a minute"),("Recirculate once cool","Fresh air now and then"),("Dry the system","Fan only, last few minutes")])
    tiles("ac-signs","Have it checked","Warning signs",[("!","Not cold",""),("!","Noise when AC turns on",""),("!","Water dripping inside",""),("!","Smell after filter change","")],cols=2)
    tiles("dc-why","Dashcam","Why it helps",[("✓","Record of accidents",""),("✓","Insurance and reports",""),("✓","Hit-and-run footage","Parking mode on some"),("✓","Peace of mind","")],cols=2)
    steps("dc-install","Choosing and installing","Set it up right",[("Clear video, day and night","Readable plates"),("Mount behind the mirror","Don't block your view"),("Tidy, safe wiring","Away from airbags and pedals"),("Right memory card","Check it monthly")])
    tiles("dc-park","Parking","Smart habits",[("✓","Well-lit, busy areas",""),("✓","Reverse in when safe",""),("✓","Fold mirrors",""),("✓","Valuables out of sight",""),("✓","Note your slot","")],cols=2)
    steps("dc-scrape","Scraped while parked?","What to do",[("Take photos",""),("Ask for CCTV",""),("Report and claim","")])
    tiles("ek-break","Breakdown basics","Always in the trunk",[("✓","Early warning device",""),("✓","Spare, jack, lug wrench",""),("✓","Basic tools",""),("✓","Jumper cables, tow strap",""),("✓","Flashlight",""),("✓","Reflective vest","")],cols=2)
    tiles("ek-aid","First aid and personal","For your passengers",[("✓","First-aid kit",""),("✓","Maintenance medicines",""),("✓","Water and snacks",""),("✓","Wipes and alcohol","")],cols=2)
    tiles("ek-bagyo","Typhoon and long trips","Add these",[("✓","Raincoat and payong",""),("✓","Towel and clothes",""),("✓","Plastic bags",""),("✓","Blanket","")],cols=2)
    steps("ek-ready","Keep it ready","Kit maintenance",[("Pack it in one bag","Easy to find"),("Check every few months","Medicines, water, batteries"),("Check before long trips","With BLOWBAGETS")])
    tiles("cw-kit","What you need","Home car wash kit",[("✓","Two buckets",""),("✓","Car shampoo","Not dish soap"),("✓","Microfiber mitt and towels",""),("✓","Wheel brush",""),("✓","Glass and interior cleaner",""),("✓","Vacuum","")],cols=2)
    steps("cw-steps","Exterior wash","Step by step",[("Park in the shade",""),("Rinse first",""),("Wheels first",""),("Two-bucket wash, top to bottom",""),("Rinse and dry","Microfiber towel")])
    tiles("cw-protect","Protect the paint","Habits that help",[("✓","Remove droppings and sap fast",""),("✓","Wax or sealant",""),("✓","Shade and sunshade",""),("✓","Rinse the underside","After floods and mud")],cols=2)
    tiles("rt-3","From Bulacan","Three classic road trips",[("N","Baguio","NLEX, SCTEX, TPLEX, then up the mountain"),("W","Zambales","NLEX, SCTEX toward Subic"),("S","Batangas","NLEX, Skyway, SLEX, STAR")],cols=1)
    compare("rt-mb","Mountain vs beach","Drive it right",("Mountain","Beach"),[("Watch for","Blind curves, fog, rain","Soft sand, salt air"),("Do","Lower gear going down","Rinse the underside after"),("Pack","Jackets","Shade, water, sunblock")])
    steps("rt-prep","Any road trip","Prep checklist",[("BLOWBAGETS",""),("RFID loaded","For every operator"),("Rest every 2 hours",""),("Emergency kit",""),("Car seats and senior seating","")])
    photo("rt-xpander",M+"Xpander/ext_xpander_26my_x_3.jpg",9/16)
    # blogs
    compare("bf-vs","Two ways to finance","Bank vs in-house",("Bank","In-house"),[("Who lends","A bank","Seller or financing company"),("Approval","Bank evaluation","Their own criteria"),("Compare","Total cost, inclusions","Total cost, inclusions")])
    steps("bf-5","Before you sign","Compare these 5 things",[("Total amount payable","Monthly × months + DP + fees"),("Inclusions","Registration, insurance, warranty"),("Requirements",""),("Fees and penalties",""),("Flexibility","")])
    tiles("bf-allin","All-in package","Check the other offer includes these",[("✓","LTO registration",""),("✓","TPL insurance",""),("✓","1-yr comprehensive","Rate locked 3 years"),("✓","Chattel mortgage",""),("✓","Free labor to 5,000 km",""),("✓","3-year warranty","")],cols=2)
    tiles("bf-red","Red flags","Walk away if…",[("✕","No written total cost",""),("✕","Sign-today pressure",""),("✕","Unclear document holder",""),("✕","Surprise fees","")],cols=2)
    MS=R+"/assets/img/ms_white.webp";DE=M+"Destinator/color_destinator_26myrx_gls_color-d34_angle45.png"
    bars("md-bars","Engine output","Power and torque",[("Power","PS",181,163),("Torque","Nm",430,250)],("Montero Sport","Destinator"),[MS,DE])
    table("md-promo","October 2026 · 60 months, all-in","Lowest monthly per variant",["Variant","SRP","Lowest monthly"],[("Destinator GLX","₱1,389,000","₱26,827"),("Destinator GLS","₱1,599,000","₱30,883"),("Destinator GT","₱1,929,000","₱37,256"),("Montero GLX MT","₱1,568,000","₱28,265"),("Montero GLS AT","₱1,927,000","₱37,218"),("Montero BS 2WD","₱2,190,000","₱42,297"),("Montero BS 4WD","₱2,530,000","₱48,864")],[0.40,0.28,0.32],"With down payment. Subject to bank approval.")
    compare("md-fit","Which fits?","Choose by how you drive",("Montero Sport","Destinator"),[("Best for","Long drives, heavy loads, rough roads","City, highway, occasional probinsya"),("Gearbox","6MT or 8AT","CVT"),("4WD","Black Series 4WD","2WD")])
    tiles("xcp-adds","Xpander Cross","Same core, more style",[("=","7 seats, 1.5L MIVEC","105 PS, 141 Nm"),("=","4-speed automatic",""),("+","Crossover look",""),("+","Premium cabin, two-tone","")],cols=2)
    stats("xcp-promo","Xpander Cross · October 2026","SRP ₱1,378,000",[("₱28,389/mo","Zero DP, 60 months, all-in"),("₱24,840/mo","With ₱148K DP, plus ₱60K fuel")])
    photo("xcp-photo",M+"Xpander Cross/ext_xpandercross_26my_xs_lhd_mv_bold-skid-plate_1.jpg",9/16)
    steps("xcp-tips","Provincial roads","Drive it smart",[("Slow down on unpaved stretches",""),("Mind the clearance","Still a 2WD MPV"),("Watch for animals and tricycles",""),("Rinse after muddy trips","")])
    tiles("tg-diff","First pickup","What's different",[("1","Longer body","Wider turns"),("2","Higher seating","Check close to bumpers"),("3","Firmer when empty","Built for loads"),("4","Diesel torque","")],cols=2)
    stats("tg-promo","Triton GX 2.4D 2WD A/T · October 2026","SRP ₱1,430,000",[("₱28,900/mo","Zero DP, 60 months, all-in"),("₱25,200/mo","With ₱140K DP, plus ₱20K fuel")])
    steps("tg-park","Driving and parking","Learn the size",[("Practice in an open lot",""),("Take wider turns",""),("Mirrors and reverse camera",""),("Check height limits","")])
    photo("tg-photo",M+"Triton/ext_triton_24my_tr_the-all-new_lhd_mv_cover_p_proxy_mitsubishi.jpg",9/16)
    steps("yp-plan","First job, first car","The 5-step plan",[("Emergency fund first",""),("30–35% income guide",""),("Budget costs after the monthly",""),("Right car, not dream car",""),("Strengthen your application","")])
    table("yp-table","Zero DP · October 2026","Entry 7-seaters and the income they need",["Unit","Monthly","Gross income"],[("Xpander GLX MT","₱22,641","₱64.7K–₱75.5K"),("Xpander GLX AT","₱23,877","₱68.2K–₱79.6K"),("Xpander GLS AT","₱25,937","₱74.1K–₱86.5K")],[0.38,0.25,0.37],"60 months, all-in, subject to bank approval.")
    tiles("yp-costs","After the monthly","Budget these too",[("✓","Fuel",""),("✓","Parking",""),("✓","Tolls",""),("✓","PMS, tires, battery",""),("✓","Insurance renewal","")],cols=2)
    tiles("sp-access","Easy access","Check these first",[("1","Seat at hip height","Slide in, not climb"),("2","Wide door opening",""),("3","Low step-in",""),("4","Grab handles","")],cols=2)
    steps("sp-td","Test drive","With your senior or PWD family member",[("Bring the person","Try every row"),("Bring the mobility aid","Load it yourself"),("Ride, don't just sit",""),("Check seatbelt reach","")])
    photo("sp-cabin",M+"Destinator/int_destinator_spaciouscabin.jpg",9/16)

def bulk4():
    M="/workspace/mmpc/final/"
    tiles("dl-what","At SJ Legacy Motors","What you can do here",[("1","See the lineup",""),("2","Test drive",""),("3","Get the month's promo","Zero DP and low DP"),("4","Pre-check loan documents",""),("5","Release and walkthrough","")],cols=1)
    stats("dl-loc","Mitsubishi dealer Bulacan","Mitsubishi SJ Legacy Motors",[("Quirino Highway","Lot 9 Ebenezer Christian Academy, Sitio Gitna, Sto. Cristo, San Jose del Monte"),("0954 291 1201","Call or text Richard Cuagdan before you visit")])
    steps("dl-before","Before your visit","3 steps",[("Check your budget","Budget Fit Calculator"),("Book a test drive","Online"),("Bring license and IDs","Plus income documents")])
    table("mm-promo","October 2026 · 60 months, all-in","Promo highlights",["Unit","Zero DP","Low DP"],[("Xpander GLX MT","₱22,641","₱19,811"),("Xpander GLX AT","₱23,877","₱20,892"),("Xpander Cross","₱28,389","₱24,840"),("Destinator GLX","₱28,615","₱26,827"),("Montero GLX MT","₱30,284","₱28,265")],[0.42,0.27,0.31],"Low DP: ₱148K / ₱138K / ₱148K / ₱93K / ₱30K. Subject to bank approval.")
    steps("mm-steps","From Metro Manila","How buying in SJDM works",[("Check your budget online",""),("Send documents for pre-check",""),("One visit for the test drive",""),("Approval and release in SJDM","")])
    tiles("mm-ask","Ask any dealer","Before you sign",[("?","What's in the all-in?",""),("?","Total of payments?",""),("?","Which freebies?",""),("?","PMS near home?","")],cols=2)
    table("xa-month","October 2026 · 60 months, all-in","Xpander monthly amortization",["Variant","Zero DP","Low DP"],[("GLX M/T","₱22,641","₱19,811"),("GLX A/T","₱23,877","₱20,892"),("GLS A/T","₱25,937","₱22,695"),("Xpander Cross","₱28,389","₱24,840")],[0.4,0.3,0.3],"Low DP: ₱148K (GLX MT, GLS, Cross) or ₱138K (GLX AT).")
    table("xa-total","DP + 60 monthly payments","Total of payments",["Variant","Zero DP","Low DP"],[("GLX M/T","₱1,358,460","₱1,336,660"),("GLX A/T","₱1,432,620","₱1,391,520"),("GLS A/T","₱1,556,220","₱1,509,700"),("Xpander Cross","₱1,703,340","₱1,638,400")],[0.34,0.33,0.33],"All-in package included. Subject to bank approval.")
    photo("xa-photo",M+"Xpander/ext_xpander_mmpc-rn-fl26_gls_mid_drl_headlampson_foglampson.jpg",9/16)
    table("dp-srp","Destinator price Philippines 2026","SRP and promo",["Variant","SRP","Zero DP","Low DP"],[("GLX","₱1,389,000","₱28,615","₱26,827"),("GLS","₱1,599,000","₱32,942","₱30,883"),("GT Mono","₱1,929,000","₱39,740","₱37,256"),("GT Two-Tone","₱1,939,000","₱39,740","₱37,256")],[0.24,0.27,0.22,0.27],"Low DP: ₱93K / ₱123K / ₱88K. Fuel: GLS ₱20K, GT ₱40K.")
    table("dp-total","DP + 60 monthly payments","Destinator total of payments",["Variant","Zero DP","Low DP"],[("GLX","₱1,716,900","₱1,702,620"),("GLS","₱1,976,520","₱1,975,980"),("GT","₱2,384,400","₱2,323,360")],[0.3,0.35,0.35],"October 2026 promos, all-in.")
    photo("dp-photo",M+"Destinator/ext_destinator_auto-headlight.jpg",9/16)
    table("mp-srp","Montero Sport price Philippines 2026","SRP and promo",["Variant","SRP","Option 1","Option 2"],[("GLX M/T","₱1,568,000","₱30,284 (Zero)","₱28,265 (₱30K)"),("GLS A/T","₱1,927,000","₱39,699 (Zero)","₱37,218 (₱138K)"),("BS 2WD","₱2,190,000","₱45,117 (₱88K)","₱42,297 (₱218K)"),("BS 4WD","₱2,530,000","₱52,121 (₱133K)","₱48,864 (₱283K)")],[0.2,0.24,0.28,0.28],"Monthly on 60 months, all-in. Down payment in brackets.")
    table("mp-total","DP + 60 monthly payments","Montero Sport total of payments",["Variant","Option 1","Option 2"],[("GLX M/T","₱1,817,040","₱1,725,900"),("GLS A/T","₱2,381,940","₱2,371,080"),("BS 2WD","₱2,795,020","₱2,755,820"),("BS 4WD","₱3,260,260","₱3,214,840")],[0.3,0.35,0.35],"October 2026 promos, all-in.")
    photo("mp-photo",M+"Montero Sport/ext_monterosport_24my_ps_lhd_mv_styling_p25-26.jpg",9/16)
    stats("lp-promo","L300 Dual AC · October 2026","SRP ₱1,039,000",[("₱21,405/mo","Zero DP · total ₱1,284,300 over 60 months"),("₱18,789/mo","₱123K DP · total ₱1,250,340, plus ₱20K fuel")])
    compare("lp-income","Income guide","30–35% of gross income",("Zero DP","₱123K DP"),[("Monthly","₱21,405","₱18,789"),("Gross income","₱61,200 – ₱71,400","₱53,700 – ₱62,600")])
    photo("lp-photo",M+"L300/ext_l300_l300-side1.jpg",9/16)
    table("zd-list","October 2026 · lowest first","Zero down payment list",["Unit","Zero DP","Gross income"],[("L300 Dual AC","₱21,405","₱61.2K–₱71.4K"),("Xpander GLX MT","₱22,641","₱64.7K–₱75.5K"),("Xpander GLX AT","₱23,877","₱68.2K–₱79.6K"),("Xpander GLS AT","₱25,937","₱74.1K–₱86.5K"),("Xpander Cross","₱28,389","₱81.1K–₱94.6K"),("Destinator GLX","₱28,615","₱81.8K–₱95.4K"),("Triton GX AT","₱28,900","₱82.6K–₱96.3K"),("Montero GLX MT","₱30,284","₱86.5K–₱100.9K"),("Destinator GLS","₱32,942","₱94.1K–₱109.8K"),("Montero GLS","₱39,699","₱113.4K–₱132.3K"),("Destinator GT","₱39,740","₱113.5K–₱132.5K")],[0.4,0.25,0.35],"60 months, all-in, subject to bank approval.")
    compare("zd-pc","Zero DP","Pros and cons",("Pros","Cons"),[("Cash","Keep savings for emergencies","Higher monthly"),("Timing","Drive sooner","Higher total of payments"),("Approval","Simple start","Needs more income to qualify")])
    tiles("zd-allin","Zero DP all-in","What's included",[("✓","LTO registration",""),("✓","TPL insurance",""),("✓","1-yr comprehensive","Rate locked 3 years"),("✓","Chattel mortgage",""),("✓","Free labor to 5,000 km",""),("✓","3-year warranty","")],cols=2)
    tiles("la-10","Car loan approval tips","10 ways to strengthen your application",[("1","Unit that fits",""),("2","Complete documents",""),("3","Consistent details",""),("4","Pay down small debts",""),("5","Cards on time",""),("6","Stable income proof",""),("7","Co-borrower",""),("8","Down payment",""),("9","Be reachable",""),("10","Pre-check documents","")],cols=2)
    tiles("la-decline","Why loans get declined","Common reasons",[("✕","Incomplete documents",""),("✕","Monthly too high",""),("✕","High existing debt",""),("✕","Credit history",""),("✕","Unreachable","")],cols=1)
    photo("la-photo",M+"Xpander/ext_xpander_rn-fl26-gls-front-1-4-headlights-on.png",9/16)
    tiles("rf-what","Reservation fee","What it does",[("1","Holds your unit or color",""),("2","Sets it aside during processing",""),("3","Shows you're a serious buyer","")],cols=1)
    steps("rf-ask","Before you pay","5 questions to ask",[("How much, for which unit?",""),("How is it applied?",""),("Is it refundable, and when?",""),("How long is the hold?",""),("Official receipt","Always")])
    tiles("rf-when","When to reserve","You're ready if…",[("✓","You've test driven",""),("✓","The monthly fits",""),("✓","Documents are ready","")],cols=1)
    steps("td-book","Mitsubishi test drive SJDM","How to book",[("Pick a unit","Online test drive page"),("Choose date and time",""),("Richard confirms","Call or text 0954 291 1201")])
    tiles("td-bring","Bring these","For a useful test drive",[("✓","Driver's license",""),("✓","Regular passengers",""),("✓","Child car seat",""),("✓","Usual cargo","")],cols=2)
    tiles("td-check","On the drive","What to check",[("1","Seat and visibility",""),("2","Acceleration, loaded",""),("3","Ride and braking",""),("4","AC to every row",""),("5","Parking and turning",""),("6","Phone and camera","")],cols=2)

if __name__=="__main__" and len(sys.argv)>1 and sys.argv[1]=="bulk4":
    MAN.update({k:tuple(v) for k,v in json.load(open(R+"/_src/ill_sizes.json")).items()});bulk4()
    json.dump({k:list(v) for k,v in MAN.items()},open(R+"/_src/ill_sizes.json","w"),indent=0)
elif __name__=="__main__" and len(sys.argv)>1 and sys.argv[1]=="bulk3":
    MAN.update({k:tuple(v) for k,v in json.load(open(R+"/_src/ill_sizes.json")).items()});bulk3()
    json.dump({k:list(v) for k,v in MAN.items()},open(R+"/_src/ill_sizes.json","w"),indent=0)
elif __name__=="__main__" and len(sys.argv)>1 and sys.argv[1]=="bulk2":
    MAN.update({k:tuple(v) for k,v in json.load(open(R+"/_src/ill_sizes.json")).items()});bulk2()
    json.dump({k:list(v) for k,v in MAN.items()},open(R+"/_src/ill_sizes.json","w"),indent=0)
elif __name__=="__main__" and len(sys.argv)>1 and sys.argv[1]=="bulk":
    MAN.update({k:tuple(v) for k,v in json.load(open(R+"/_src/ill_sizes.json")).items()});bulk()
    json.dump({k:list(v) for k,v in MAN.items()},open(R+"/_src/ill_sizes.json","w"),indent=0)
elif __name__=="__main__":
    M="/workspace/mmpc/final/";G="/cursor/stores/store-6b56a977-1b9b-4b05-adeb-6cd0f5ea5ec8/grok-bot/agents/eb5f84df-816b-4ceb-85a4-a92853d3a24a/attachments/"
    XP=M+"Xpander/color_xpander_26my_rn_color-c31_angle45.png";DE=M+"Destinator/color_destinator_26myrx_gt_color-x3n_angle45.png"
    L3=M+"L300/color_l300_20sl-front-r_color-w50_angle135.png";MG=M+"Mirage G4/color_mirageg4_26myell_glx-mt_color-u17_angle45.png"
    # 1 Undas
    tiles("undas-blowbagets","Pre-trip check · 10 to 15 minutes","BLOWBAGETS before you leave",[(c,w,"") for c,w in zip("BLOWBAGETS",["Battery","Lights","Oil","Water","Brakes","Air","Gas","Engine","Tires","Self"])],cols=2)
    tiles("undas-rfid","Toll prep","RFID ready before the exodus",[("1","Check your balance","A day before you leave"),("2","Load for the round trip",""),("3","Check the sticker","Damaged or often fails? Fix it first")],cols=1)
    stats("undas-traffic","NLEX Undas 2026","When to expect heavy traffic",[("Oct 28 – Nov 2","Toll operators expect heavy NLEX traffic"),("Nov 1 & 2","Special non-working days, so many families leave earlier")])
    photo("undas-packing",G+"1047c2499a19ef10006b8eb7a3404fa941a00b98236100ff7d432eb3ee4d3c76.jpg")
    steps("undas-breakdown","Expressway breakdown","Tumirik? Do this in order",[("Hazards on, move to the shoulder",""),("Set up your early warning device","Well behind the car"),("Move passengers to a safer spot","Behind the guardrail if safe"),("Call the official hotline","Plus your insurer's roadside assistance"),("No risky repairs","Wait for patrol or tow")])
    photo("undas-xpander",M+"Xpander/ext_xpander_26my_x_3.jpg",9/16)
    # 2 First-time buyer
    tiles("ftb-checklist","First car checklist","6 things to settle before you sign",[("1","True cost of ownership",""),("2","A garahe",""),("3","Test drive",""),("4","Your financing",""),("5","The inclusions",""),("6","Your documents","")],cols=2)
    tiles("ftb-costs","Beyond the monthly","Budget for these, too",[("✓","Fuel",""),("✓","Insurance",""),("✓","PMS",""),("✓","Parking",""),("✓","Tolls",""),("✓","Registration","")],cols=3)
    tiles("ftb-testdrive","Test drive","What to check behind the wheel",[("1","Seat position and visibility",""),("2","Parking and turning",""),("3","Transmission feel",""),("4","Rear seat space",""),("5","Cabin noise and AC","")],cols=1)
    photo("ftb-mirage",M+"Mirage G4/ext_mirageg4_easy_to_manoeuvre_1080x760.jpg")
    # 3 Fuel
    stats("fuel-oct20","Pump prices · October 20, 2026","Opposite moves, same week",[("Gasoline ↓ ₱4.30/L","Rolled back by at least ₱4.30 per liter"),("Diesel ↑ ₱2.60/L","Up by ₱2.60 per liter")])
    tiles("fuel-habits","7 habits","Cut fuel use without changing cars",[("1","Check tire pressure",""),("2","Smooth acceleration and braking",""),("3","Remove extra weight",""),("4","Keep up with PMS",""),("5","Plan your route",""),("6","Don't idle unnecessarily",""),("7","Steady expressway speed","")],cols=2)
    compare("fuel-diesel-gas","Diesel vs gasoline","Choose by how you drive",("Diesel","Gasoline"),[("Best for","Heavy loads, hauling, high mileage","Light, short city trips"),("Strength","Strong pulling power for work","Quieter, simpler daily car")])
    compare("fuel-l300-mirage","Two different jobs","L300 vs Mirage G4",("L300","Mirage G4"),[("Engine","2.2L turbo-intercooled diesel (4N14)","1.2L gasoline"),("Gearbox","5-speed manual","Manual or CVT"),("Built for","Deliveries and hauling","Daily commuting")],imgs=[L3,MG])
    # 4 LTO
    tiles("lto-timeline","LTO in 2026","Key dates to remember",[("Feb 15","5-year initial registration","Brand-new, dealer-registered"),("Sep 1","Fake plate crackdown","Impound risk"),("Oct 9","Pedestrian memo","Licenses may be revoked")],cols=1)
    steps("lto-5year","Brand-new cars","How the 5-year registration works",[("Years 1 to 5: initial registration","Keep CTPL valid"),("Around year 4: roadworthiness check",""),("After year 5: renew yearly",""),("Used vehicles don't qualify","Check the expiry on your CR")])
    stats("lto-15days","Apprehended?","No on-the-spot license confiscation",[("15 working days","To settle your fines. Settle on time to avoid further penalties")])
    photo("lto-destinator",M+"Destinator/ext_destinator_dynamicshield.jpg",9/16)
    tiles("lto-checklist","Quick owner checklist","Save this before your next drive",[("✓","Check CR expiry",""),("✓","Keep CTPL valid",""),("✓","Official plates only",""),("✓","Set up LTMS / eGovPH",""),("✓","Settle within 15 working days",""),("✓","Yield to pedestrians","")],cols=2)
    # 5 El Nino
    stats("weather-outlook","PAGASA outlook","Heat and storms in one season",[("Very strong El Niño","Strong to very strong, may peak before end-2026"),("1–2 cyclones a month","Expected each month, October to December")])
    tiles("weather-heat","Heat care","What the init does to your car",[("1","Battery","Heat speeds up wear"),("2","Coolant","Watch the temp gauge"),("3","Tires","Check pressure cold"),("4","AC","Clean, and park in shade"),("5","Paint and interior","Use a sunshade","")[:3]],cols=2)
    photo("weather-rain",G+"b6f9847fc66e818c7ff73aa0129740150e8f19674ff878d01c189e6d9901c444.jpg")
    steps("weather-flood","Flood rules","Before you drive into water",[("Around half your tire height? Turn back",""),("Never cross moving water",""),("Go slow and steady in low gear",""),("Don't restart a stalled car in water",""),("Test your brakes after","")])
    photo("weather-clearance",M+"Destinator/ext_destinator_groundclearance.jpg",9/16)
    # 6 Myths
    tiles("myths-overview","Sabi-sabi vs fact","6 car loan myths, debunked",[("✕","Big salary needed","Banks check capacity to pay"),("✕","No self-employed","Prove income differently"),("✕","No OFWs abroad","SPA or co-borrower"),("✕","Cash always cheaper","Compare total cost"),("✕","One rejection = never","Fix the cause, reapply"),("✕","Only the monthly matters","Add ownership costs")],cols=2)
    tiles("myths-selfemployed","Self-employed","What banks commonly ask for",[("1","DTI/SEC or business permit",""),("2","Latest ITR and financial statements",""),("3","Business bank statements",""),("4","Trade references","Some banks")],cols=2)
    steps("myths-bankcheck","Approval","What banks actually check",[("Capacity","Income vs the monthly and obligations"),("Documents","Complete, consistent, verifiable"),("Credit history","Past loans and credit cards"),("Stability","Years employed or in business")])
    photo("myths-xpander",M+"Xpander/ext_xpander_mmpc-rn-fl26_gls_mid_drl_headlampson_foglampson.jpg",9/16)
    # 7 OFW
    photo("ofw-flatlay",G+"239e6799a2714539acf00dc523c72fc222e9b2b51ce7768d346c7004d9824dc3.jpg")
    compare("ofw-spa","Applying from abroad","SPA or co-borrower?",("SPA","Co-borrower"),[("Who","Trusted family member as attorney-in-fact","Family member in the PH"),("Role","Signs and transacts for you","Applies with you, shares the loan")])
    tiles("ofw-docs","OFW documents","Commonly required",[("✓","Passport and valid IDs",""),("✓","Employment or crew contract",""),("✓","Payslips or COE",""),("✓","Proof of remittance",""),("✓","PH proof of billing",""),("✓","SPA or co-borrower docs","")],cols=2)
    steps("ofw-release","While you're away","From approval to release",[("Approval","Bank evaluates your documents"),("Signing","Attorney-in-fact or co-borrower signs here"),("Registration","Dealer handles LTO; 5-year initial registration"),("Release","Your family receives the car")])
    photo("ofw-3rdrow",M+"Destinator/int_destinator_3rdrow.jpg",9/16)
    # 8 13th month
    photo("13th-flatlay",G+"1a3c386743fd3c1094d388342a0c4e61f553bee8dac9f0e77c452386b83cbce2.jpg")
    stats("13th-formula","13th month pay","How it's computed",[("Basic salary ÷ 12","Total basic salary earned in the calendar year"),("By Dec 24","Release deadline for employers")])
    steps("13th-split","A simple split","Order of priority",[("Emergency fund first",""),("Pay down high-interest debts",""),("Pasko: a fixed amount",""),("Car fund",""),("Maintenance","If you already own a car")])
    tiles("13th-costs","Hidden ownership costs","Budget beyond the monthly",[("✓","Fuel",""),("✓","Insurance renewal",""),("✓","PMS",""),("✓","Parking and tolls",""),("✓","Tires and battery",""),("?","Ask for the all-in list","")],cols=2)
    photo("13th-mirage",M+"Mirage G4/int_mirageg4_interior.png",9/16)
    # 9 L300
    compare("l300-spec","L300 at a glance","Built for negosyo",("Cab & Chassis","Dual AC"),[("Engine","2.2L 4N14 turbo diesel, Euro 4","2.2L 4N14 turbo diesel, Euro 4"),("Gearbox","5-speed manual","5-speed manual"),("Body","Build your own","Ready to work, AC front and rear")],imgs=[L3,M+"L300/ext_l300_l300-fb_1080_fl.png"])
    compare("l300-bodies","Cab and chassis","Pick the body for your cargo",("Dropside","Aluminum van"),[("Good for","Hardware, construction supplies","Goods that need protection")],imgs=[M+"L300/ext_l300_l300-drop-side_1080_fl.png",M+"L300/ext_l300_l300-alum-van_1080_fl.png"])
    tiles("l300-load","Load planning","Real-world rules",[("1","Know your heaviest regular load",""),("2","Stay within rated capacity",""),("3","Secure the cargo",""),("4","Know truck bans on your routes","")],cols=2)
    steps("l300-roi","ROI thinking","Delivery fees vs owning a truck",[("Add up what you pay now","Delivery fees, courier costs, lost orders"),("Estimate ownership costs","Amortization, fuel, insurance, PMS, driver, tolls"),("Count the upside","More orders, faster deliveries"),("Compare","Same or less, and room to grow?")])
    # 10 Xpander vs Destinator
    bars("xvd-power","Engine output","Power and torque",[("Power","PS",105,163),("Torque","Nm",141,250)],("Xpander","Destinator"),[XP,DE])
    photo("xvd-3rdrow",M+"Destinator/int_destinator_spaciouscabin.jpg",9/16)
    compare("xvd-variants","Variants and gearbox","What you can choose",("Xpander","Destinator"),[("Variants","GLX, GLS","GLX, GLS, GT"),("Transmission","5-speed MT or 4-speed AT","CVT"),("Ground clearance","High (ask for variant spec)","214 mm")])
    tiles("xvd-fit","Which fits?","Match the car to your family",[("X","Mostly city, budget-conscious","Xpander"),("D","Frequent probinsya trips, full car","Destinator"),("D","Flood-prone or rough roads","Destinator's 214 mm adds margin"),("?","Big family, growing kids","Try both third rows")],cols=2)
    photo("xvd-xpander",M+"Xpander/ext_xpander_26my_x_3.jpg",9/16)
    def cut(name,src,bg=(244,244,245)):
        im=Image.open(src).convert("RGBA");im=im.crop(im.getbbox());im.thumbnail((1040,560),Image.LANCZOS)
        c=Image.new("RGB",(1200,675),bg);c.paste(im,((1200-im.width)//2,(675-im.height)//2+20),im);save(c,name)
    cut("ftb-mirage",M+"Mirage G4/color_mirageg4_26myell_glx-cvt_color-a66_angle315.png")
    cut("undas-xpander",M+"Xpander/color_xpander_26my_rn_color-x37_angle45.png")
    cut("xvd-xpander",M+"Xpander/color_xpander_26my_rn_color-c31_angle315.png")
    json.dump({k:list(v) for k,v in MAN.items()},open(R+"/_src/ill_sizes.json","w"),indent=0)
