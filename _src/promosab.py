# /promos/ Option A / Option B (2026-10-29, Richard): every unit shows two options.
# Option A = lowest DP + monthly (LOCKED until the visitor unlocks with name/mobile/email+consent; one unlock reveals all units).
# Option B = 30% DP + low monthly, public (same figures as the saved replies). Source: /workspace/loanapp/pricelist/optionAB.json (Oct 2026).
import json, hashlib, base64, os
SRC="/workspace/loanapp/pricelist/optionAB.json"
CACHE=os.path.join(os.path.dirname(__file__),"optionAB_oct2026.json")
FAM=[("Mirage Hatchback","mirage","Mirage"),("Mirage G4","mirage-g4","Mirage G4"),("Xpander","xpander","Xpander"),("Xpander Cross","xpander-cross","Xpander Cross"),
 ("Xforce","xforce","Xforce"),("Destinator","destinator","Destinator"),("Triton","triton","Triton"),("Montero Sport","montero-sport","Montero Sport"),
 ("L300","l300","L300"),("Versa Van","versa-van","Versa Van"),("Outlander PHEV","outlander-phev","Outlander PHEV")]
# Richard's lowest-DP range per family (2026-10-29). Mirage hatchback / Xpander Cross unknown -> no range line.
RANGE={"mirage-g4":(0,18000),"xpander":(18000,33000),"xforce":(18000,48000),"destinator":(0,33000),"triton":(0,18000),
 "montero-sport":(0,33000),"l300":(18000,53000),"versa-van":(18000,48000),"outlander-phev":(68000,183000)}
# fuel points only where the current site already shows the same figure
FUEL={"Xpander GLX 1.5G 2WD M/T":30000,"L300 FB BODY WITHDUAL AC 2.2D M/T":20000}
NICE={"L300 CAB & CHASIS 2.2D M/T":"L300 Cab & Chassis 2.2D M/T","L300 FB BODY WITH SINGLE AC 2.2D M/T":"L300 FB Body Single AC 2.2D M/T",
 "L300 FB BODY WITHDUAL AC 2.2D M/T":"L300 FB Body Dual AC 2.2D M/T","OUTLANDER PHEV GT 2.4G AWD":"Outlander PHEV GT 2.4G AWD"}
MODELIMG={'mirage-g4':'mg4gls_u17','xpander':'xpglx_x37','xpander-cross':'xc_x3n','xforce':'xf_glx','destinator':'de_x3n','triton':'tr_lineup',
 'montero-sport':'ms_white','l300':'l300_fb','versa-van':'vv_glx','outlander-phev':'op_gt'}  # one picture per model module (2026-10-29)
# (old) card photos (2026-10-29): same image each /cars/ page uses per variant; Mirage hatchback has none -> no photo
IMG={"Mirage G4 GLX 1.2G M/T":"mg4glx_u17","Mirage G4 GLX 1.2G CVT":"mg4glx_a66","Mirage G4 GLS 1.2G CVT":"mg4gls_u17",
 "Xpander GLX 1.5G 2WD M/T":"xpglx_u33","Xpander GLX 1.5G 2WD A/T":"xpglx_x37","Xpander GLS 1.5G 2WD A/T":"xpgls_c31",
 "Xpander Cross 1.5G 2WD A/T (Two-Tone)":"xc_x3n","XFORCE GLX 1.5G 2WD CVT":"xf_glx","XFORCE GLS 1.5G 2WD CVT (Monotone)":"xf_gls",
 "XFORCE GLS 1.5G 2WD CVT (Two-Tone)":"xf_gls","XFORCE GT 1.5G 2WD CVT":"xf_gt","Destinator GLX 1.5G Turbo 2WD CVT":"de_p26",
 "Destinator GLS 1.5G Turbo 2WD CVT":"de_d34","Destinator GT 1.5G Turbo 2WD CVT (Monotone)":"de_jh3","Destinator GT 1.5G Turbo 2WD CVT (Two-Tone)":"de_x3n",
 "Triton GL 2.4D 2WD M/T":"tr_gl","Triton GX 2.4D 2WD A/T":"tr_gx_u28","Triton GLX 2.4D 2WD M/T":"tr_glx","Triton GLX 2.4D 2WD A/T":"tr_glx",
 "Triton GLS 2.4D 2WD A/T":"tr_gls","Triton GL 2.4D 4WD M/T":"tr_gl","Triton GLX 2.4D 4WD M/T":"tr_glx","Triton Athlete 2.4D 4WD A/T":"tr_lineup",
 "Montero Sport GLX 2.4D 2WD M/T":"ms_silver","Montero Sport GLS 2.4D 2WD A/T":"ms_white","Montero Sport Black Series 2.4D 2WD A/T":"msbs_jh3",
 "Montero Sport Black Series 2.4D 4WD A/T":"msbs_x8w","L300 CAB & CHASIS 2.2D M/T":"l300_fb","L300 FB BODY WITH SINGLE AC 2.2D M/T":"l300_fb",
 "L300 FB BODY WITHDUAL AC 2.2D M/T":"l300_fb","Versa Van GLX 2.5D 2WD M/T":"vv_glx","Versa Van GLX 2.5D 2WD M/T (UPGRADED) 18 SEATER":"vv_glx",
 "OUTLANDER PHEV GT 2.4G AWD":"op_gt"}
def rows():
    p=SRC if os.path.exists(SRC) else CACHE
    d=json.load(open(p))
    if p==SRC: json.dump(d,open(CACHE,"w"),ensure_ascii=False,indent=1)
    return [r for r in d if not any(k in r["unit"] for k in ("Quartz White","White Diamond","(White)"))]  # base colors, like the saved replies
CARSEC={}; CARPARTS={}
def build(page,e,f,R,hero_cta,ALLIN_HTML,FREE_HTML,NOTE,MSG):
    rs=rows(); A=[]; EAG=[0]; secs=""; nav=[]
    for fam,slug,name in FAM:
        vs=[r for r in rs if r["family"]==fam]
        if not vs: continue
        nav.append(f'<a href="#{slug}">{e(name)}</a>')
        rg=RANGE.get(slug)
        if rg and rg[0]==0:  # Richard 2026-10-29: show "Zero DP Promo" instead of ₱0 (still subject to approval)
            rl=f'<p class="ab-rng"><b class="ab-z">Zero DP Promo</b><span class="en">, up to <b>{f(rg[1])}</b> DP</span><span class="tl">, hanggang <b>{f(rg[1])}</b> DP</span></p>'
        else:
            rl=f'<p class="ab-rng"><span class="en">Lowest DP range</span><span class="tl">Lowest DP range</span> <b>{f(rg[0])} – {f(rg[1])}</b></p>' if rg else ""
        trs=""
        for r in vs:
            i=len(A); A.append([r["a_dp"],r["a_mo"]]); n=NICE.get(r["unit"],r["unit"].replace("XFORCE","Xforce"))
            fu=f'<span class="fuel"><span class="en">+ {FUEL[r["unit"]]:,} fuel points</span><span class="tl">+ {FUEL[r["unit"]]:,} fuel points</span></span>' if r["unit"] in FUEL else ""
            trs+=f'''<tr><th scope="row"><span class="ab-vn">{e(n)}</span>{fu}</th><td class="ab-srp"><span class="ab-l">SRP </span>{f(r["srp"])}</td>
<td class="ab-ca" data-a="{i}"><span class="ab-l">Option A</span><span class="ab-dp">DP <b class="ab-x">₱••,•••</b></span><span class="ab-mo"><b class="ab-x">₱••,•••</b>/mo</span><button type="button" class="ab-ul" data-unlock><span class="en">🔒 Unlock</span><span class="tl">🔒 I-unlock</span></button></td>
<td class="ab-cb"><span class="ab-l">Option B</span><span class="ab-dp">DP <b>{f(r["b_dp"])}</b></span><span class="ab-mo"><b>{f(r["b_mo"])}</b>/mo</span></td></tr>'''
        im=MODELIMG.get(slug); ph=""
        if im:
            EAG[0]+=1; w,h=__import__("PIL.Image",fromlist=["x"]).open(f"{R}/assets/img/{im}.webp").size
            iv=hashlib.md5(open(f"{R}/assets/img/{im}.webp","rb").read()).hexdigest()[:8]
            ph=f'<div class="ab-ph"><img src="/assets/img/{im}.webp?v={iv}" width="{w}" height="{h}" alt="Mitsubishi {e(name)}" {'fetchpriority="high"' if EAG[0]==1 else 'loading="lazy"'} decoding="async"></div>'
        tbl=f'''<div class="ab-tw"><table class="ab-t"><thead><tr><th scope="col"><span class="en">Variant</span><span class="tl">Variant</span></th><th scope="col">SRP</th><th scope="col">Option A <small class="en">· Lowest DP</small><small class="tl">· Pinakamababang DP</small></th><th scope="col">Option B <small class="en">· Low monthly</small><small class="tl">· Mababang monthly</small></th></tr></thead><tbody>{trs}</tbody></table>
<p class="muted ab-s"><span class="en">All-in, 60 months. Pre-qualified, subject to bank approval.</span><span class="tl">All-in, 60 months. Pre-qualified, subject to bank approval.</span></p><p class="row"><a class="btn sm ab-pq" href="/loan-assessment/"><span class="en">See if you're Pre-Qualified in 2 minutes →</span><span class="tl">Alamin kung Pre-Qualified ka na ngayon →</span></a> <a class="btn sm ghost dk" href="/budgetcalculator/">Compare with my own DP</a></p></div>'''
        secs+=f'<section class="pm card pad ab-m{"" if ph else " ab-np"}" id="{slug}"><h2>{e(name)}</h2>{rl}<div class="ab-mg">{ph}{tbl}</div></section>'
        CARSEC[slug]=(name,rl,tbl,[A[k] for k in range(len(A)-len(vs),len(A))])
    blob=base64.b64encode(json.dumps(A).encode()).decode()
    lv=hashlib.md5(open(R+"/assets/lead.js","rb").read()).hexdigest()[:8]
    jv=hashlib.md5(open(R+"/assets/promos.js","rb").read()).hexdigest()[:8]
    css='''<style>html[data-lang=tl] .abw .en,html:not([data-lang=tl]) .abw .tl{display:none!important}
.ab-lang{display:flex;gap:8px;margin:0 0 14px}.ab-lang button{background:none;border:1px solid #52525b;color:inherit;border-radius:999px;padding:8px 14px;min-height:40px;font:inherit;font-size:14px;cursor:pointer}html[data-lang=tl] .ab-lang [data-setlang=tl],html:not([data-lang=tl]) .ab-lang [data-setlang=en]{background:#0b0b0c;color:#fff}
.ab-m{margin:0 0 22px}.ab-m h2{margin-top:0}.ab-mg{display:grid;gap:16px}@media(min-width:900px){.ab-mg{grid-template-columns:300px 1fr;align-items:start}.ab-np .ab-mg{grid-template-columns:1fr}}.ab-tw{min-width:0}
.ab-t{width:100%;border-collapse:collapse;font-size:15px}.ab-t th,.ab-t td{padding:10px 8px;border-bottom:1px solid var(--ln);text-align:left;vertical-align:top}.ab-t thead th{font-size:12px;text-transform:uppercase;letter-spacing:.05em;color:#52525b}.ab-t thead small{text-transform:none;letter-spacing:0;font-weight:400}
.ab-vn{display:block;font-weight:700}.ab-t .fuel{display:block;font-size:13px;color:#15803d;font-weight:600}.ab-srp{white-space:nowrap}.ab-ca,.ab-cb{white-space:nowrap}.ab-ca .ab-dp,.ab-cb .ab-dp,.ab-ca .ab-mo,.ab-cb .ab-mo{display:block}.ab-mo b{font-size:18px}.ab-ca{background:#18181b;color:#fff}.ab-ca .ab-l,.ab-cb .ab-l,.ab-srp .ab-l{display:none}
.ab-t .ab-ul{margin-top:6px;padding:6px 10px;min-height:36px;font-size:13px}
@media(max-width:899px){.ab-t thead{display:none}.ab-t,.ab-t tbody{display:block}.ab-t tr{display:grid;grid-template-columns:1fr 1fr;gap:8px;padding:12px 0;border-bottom:1px solid var(--ln)}.ab-t th,.ab-t td{border:0;padding:0}.ab-t th[scope=row]{grid-column:1}.ab-srp{grid-column:2;text-align:right!important}.ab-srp .ab-l{display:inline!important;color:#71717a;font-size:13px}
.ab-ca,.ab-cb{border-radius:10px;padding:10px!important;white-space:normal}.ab-cb{border:1px solid var(--ln)!important}.ab-ca .ab-l,.ab-cb .ab-l{display:block!important;font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--redd);margin-bottom:2px}.ab-ca .ab-l{color:#fca5a5}.ab-t .ab-ul{width:100%}}
.ab-ph{aspect-ratio:3/2;background:#fff;border-radius:10px;overflow:hidden;display:flex;align-items:center;justify-content:center}.ab-ph img{width:100%;height:100%;object-fit:contain;display:block}
.ab-rng{margin:-4px 0 14px;font-size:15px;color:#3f3f46}.ab-rng b{color:var(--redd);white-space:nowrap}
.ab-o{border:1px solid var(--ln);border-radius:12px;padding:12px 14px;margin:0 0 10px;position:relative}.ab-a{background:linear-gradient(135deg,#0b0b0c,#27272a);color:#fff;border:0}
.ab-k{margin:0 0 6px;font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--redd)}.ab-a .ab-k{color:#fca5a5}
.ab-v{display:flex;justify-content:space-between;align-items:baseline;gap:8px;flex-wrap:wrap}.ab-dp{font-size:15px}.ab-mo b{font-size:22px}.ab-mo small{font-weight:400;opacity:.7}
.ab-x{filter:blur(6px);user-select:none}html.ab-open .ab-x{filter:none}html.ab-open .ab-ul{display:none}
.ab-ul{margin-top:10px;width:100%;background:var(--red);color:#fff;border:0;border-radius:999px;padding:10px 14px;min-height:44px;font:inherit;font-size:15px;font-weight:700;cursor:pointer}.ab-ul:hover{background:var(--redd)}
.ab-s{font-size:13px}.ab-box{border-left:5px solid var(--red)}.ab-box .chk{font-size:14px;display:flex;gap:10px;align-items:flex-start;margin:6px 0 14px}.ab-box .chk input{width:20px;height:20px;flex:none;margin-top:2px}.ab-box .ferr{color:#b8000e;font-size:13px;margin:4px 0 0}
.ab-ok{background:#f0fdf4;border:1px solid #bbf7d0;border-radius:14px;padding:16px}.ab-btn{width:100%;font-size:17px}.ab-fg{display:grid;gap:0 16px}@media(min-width:900px){.ab-fg{grid-template-columns:1fr 1fr 1fr}}.ab-fg>*{min-width:0}
html.ab-open .ab-lockonly{display:none}html:not(.ab-open) .ab-openonly{display:none}</style>
<script>try{if(localStorage.getItem("promos_optA_unlocked")==="1")document.documentElement.classList.add("ab-open")}catch(_){}</script>'''
    form=f'''<section class="sec" id="unlock" style="padding-bottom:0"><div class="w"><div class="card pad ab-box">
<div class="ab-lockonly"><h2 class="h3" style="margin:0 0 6px"><span class="en">Unlock Option A: the lowest down payment for every unit</span><span class="tl">I-unlock ang Option A: pinakamababang down payment ng bawat unit</span></h2>
<p class="muted" style="margin:0 0 12px"><span class="en">Option B is shown below for every unit. Leave your details once to reveal Option A (lowest DP and monthly, including Zero DP Promo on select units) on all units.</span><span class="tl">Nakalista sa baba ang Option B ng bawat unit. Iwan ang details mo isang beses para makita ang Option A (lowest DP at monthly, kasama ang Zero DP Promo sa piling units) ng lahat ng unit.</span></p>
<form id="ab-form" novalidate><div class="ab-fg">
<div class="fld"><label for="ab-name"><span class="en">Full name</span><span class="tl">Buong pangalan</span></label><input id="ab-name" autocomplete="name" required><p class="ferr" id="e_ab-name" hidden><span class="en">Please enter your name.</span><span class="tl">Pakilagay ang pangalan mo.</span></p></div>
<div class="fld"><label for="ab-mobile">Mobile number</label><input id="ab-mobile" type="tel" inputmode="tel" autocomplete="tel" placeholder="09XX XXX XXXX" required><p class="ferr" id="e_ab-mobile" hidden><span class="en">Enter a valid mobile number (09XXXXXXXXX).</span><span class="tl">Maglagay ng tamang mobile number (09XXXXXXXXX).</span></p></div>
<div class="fld"><label for="ab-email">Email</label><input id="ab-email" type="email" autocomplete="email" required><p class="ferr" id="e_ab-email" hidden><span class="en">Enter a valid email.</span><span class="tl">Maglagay ng tamang email.</span></p></div></div>
<label class="chk"><input type="checkbox" id="ab-consent"><span><span class="en">I agree to be contacted by Richard Cuagdan of Mitsubishi San Juan Motors about these promos, and to the <a href="/privacy/">privacy policy</a>.</span><span class="tl">Pumapayag akong i-contact ni Richard Cuagdan ng Mitsubishi San Juan Motors tungkol sa promos na ito, at sa <a href="/privacy/">privacy policy</a>.</span></span></label>
<p class="ferr" id="e_ab-consent" hidden><span class="en">Please tick the consent box.</span><span class="tl">Paki-check ang consent box.</span></p>
<button class="btn ab-btn" id="ab-btn" type="submit"><span class="en">Unlock Option A</span><span class="tl">I-unlock ang Option A</span></button>
<p class="muted ab-s" style="margin-top:10px">Pre-qualified, subject to bank approval. Rates, promos and DP may change without prior notice.</p></form></div>
<div class="ab-openonly ab-ok" id="ab-ok" aria-live="polite"><p style="margin:0"><b><span class="en">Option A is unlocked for every unit.</span><span class="tl">Na-unlock na ang Option A ng bawat unit.</span></b> <span class="en">Richard can send the exact all-in computation for your chosen unit.</span><span class="tl">Puwedeng i-send ni Richard ang eksaktong all-in computation ng unit na gusto mo.</span></p><p class="muted ab-s" style="margin:6px 0 0">Pre-qualified, subject to bank approval.</p></div>
</div></div></section>'''
    CARPARTS.update(css=css,form=form,lv=lv,jv=jv)
    body=css+f'''<div class="abw"><section class="ph"><div class="w"><div class="ab-lang" role="group" aria-label="Language / Wika"><button type="button" data-setlang="en">English</button><button type="button" data-setlang="tl">Taglish</button></div>
<p class="kick">October 2026</p><h1><span class="en">Mitsubishi promos this month</span><span class="tl">Mitsubishi promos ngayong buwan</span></h1><p class="lead"><span class="en">Every unit comes with two all-in options on 60 months: <b>Option A</b>, the lowest down payment (unlock to see), and <b>Option B</b>, a 30% down payment with a lower monthly.</span><span class="tl">Bawat unit may dalawang all-in option sa 60 months: <b>Option A</b>, ang pinakamababang down payment (i-unlock para makita), at <b>Option B</b>, 30% down payment na mas mababa ang monthly.</span></p>
{hero_cta("#list",src="promos")}</div></section>
{form}
<section class="sec" id="list"><div class="w"><nav class="pnav" aria-label="Jump to model">{" ".join(nav)}</nav>
{secs}
<p class="note">{NOTE}</p><p class="muted"><span class="en">Other down payment options: </span><span class="tl">Ibang DP options: </span><a href="{MSG}" rel="noopener" data-msgr="promos-other">message Richard on Messenger</a>.</p></div></section>
<section class="sec alt"><div class="w"><h2>How to use this month's promo</h2><ol class="psteps"><li><b>Pick a unit and Option A or B</b> above.</li><li><b>Estimate your own plan</b> with the <a href="/budgetcalculator/">monthly calculator</a> (standard formula: (SRP − DP) × add-on rate ÷ months; 5 years at 1.55).</li><li><b>Check your chances</b> with the free <a href="/loan-assessment/">Loan Application Assessment</a> (Pre-qualified, subject to bank approval).</li><li><b>Apply or ask</b>: <a href="/apply/">apply online</a> or <a href="{MSG}" rel="noopener" data-msgr="promos-steps">message Richard on Messenger</a>.</li></ol></div></section>
<section class="sec"><div class="w split"><div><h2>All-in includes</h2>{ALLIN_HTML}</div><div><h2>Freebies</h2>{FREE_HTML}</div></div></section></div>
<script type="text/plain" id="ab-a">{blob}</script>
<script src="/assets/lead.js?v={lv}" defer></script><script src="/assets/promos.js?v={jv}" defer></script>'''
    page("/promos/","October 2026 Promos | Mitsubishi Motors - San Juan Motors",
     "October 2026 Mitsubishi promos from San Juan Motors: two all-in options per unit on 60 months, lowest down payment or a lower monthly, with freebies. Subject to bank approval.",
     body, crumbs=[("/","Home"),("/promos/","Promos")])
    return [r["unit"] for r in rs]

# DRAFT 2026-10-29 (Richard, pending approval): "Promos for this model" module on each /cars/<model>/ page.
# Same optionAB data, same table/CSS, same unlock form + promos.js (shared localStorage flag: one unlock reveals all, site-wide).
def inject_cars(R):
    import re
    for slug,(name,rl,tbl,arows) in CARSEC.items():
        fp=f"{R}/cars/{slug}/index.html"
        if not os.path.exists(fp): continue
        h=open(fp).read()
        if 'id="promos-model"' in h: continue
        k=iter(range(len(arows)))
        t=re.sub(r'data-a="\d+"',lambda m:f'data-a="{next(k)}"',tbl)
        t=t.replace('<a class="btn sm ghost dk" href="/budgetcalculator/">','<a class="btn sm ghost dk" href="/promos/">See all promos →</a> <a class="btn sm ghost dk" href="/budgetcalculator/">',1)
        form=CARPARTS["form"].replace("Option B is shown below for every unit.","Option B is shown above for every variant.").replace("Nakalista sa baba ang Option B ng bawat unit.","Nakalista sa itaas ang Option B ng bawat variant.")
        blob=base64.b64encode(json.dumps(arows).encode()).decode()
        fin=form.replace('<section class="sec" id="unlock" style="padding-bottom:0"><div class="w"><div class="card pad ab-box">','<div id="unlock" class="ab-box pm-unl">',1)
        assert fin.endswith('</div></div></section>'); fin=fin[:-len('</div></div></section>')]+'</div>'
        # Accordion (Richard 2026-10-30): closed by default, after the car details/inclusions; #promos-model / #promos-<slug> / #unlock auto-open
        mod=CARPARTS["css"]+f'''<style>.pm-bar{{display:flex;align-items:center;gap:12px;width:100%;text-align:left;background:#0b0b0c;color:#fff;border:0;border-radius:14px;padding:16px 18px;min-height:56px;font:inherit;cursor:pointer}}.pm-bar:hover{{background:#18181b}}.pm-bar:focus-visible{{outline:3px solid var(--red);outline-offset:2px}}
.pm-bt{{flex:1;min-width:0}}.pm-bt b{{display:block;font-size:18px}}.pm-bt small{{display:block;font-size:13px;opacity:.75;margin-top:2px}}.pm-cta{{background:var(--red);border-radius:999px;padding:8px 14px;font-weight:700;font-size:14px;white-space:nowrap;display:flex;align-items:center;gap:6px}}
.pm-cta svg{{transition:transform .25s ease}}.pm-bar[aria-expanded=true] .pm-cta svg{{transform:rotate(180deg)}}
#pm-body{{display:grid;grid-template-rows:0fr;transition:grid-template-rows .3s ease}}#pm-body>div{{overflow:hidden;min-height:0}}#pm-body.open{{grid-template-rows:1fr}}#pm-body:not(.open)>div{{visibility:hidden;transition:visibility 0s .3s}}#pm-body.open>div{{padding-top:16px}}
.pm-unl{{margin-top:16px;padding:16px;border:1px solid var(--ln);border-left:5px solid var(--red);border-radius:12px}}@media(max-width:600px){{.pm-bar{{padding:14px;flex-wrap:wrap}}.pm-bt{{flex:1 1 100%}}.pm-cta{{margin-left:0}}}}@media(prefers-reduced-motion:reduce){{#pm-body,.pm-cta svg{{transition:none}}}}</style>
<div class="abw"><section class="sec" id="promos-model"><div class="w"><div class="card pad ab-m ab-np">
<button type="button" class="pm-bar" id="pm-tg" aria-expanded="false" aria-controls="pm-body"><span class="pm-bt"><b><span class="en">{name} promos</span><span class="tl">{name} promos</span></b><small><span class="en">October 2026 promos, Option A and Option B</span><span class="tl">Promos ngayong Oktubre 2026, Option A at Option B</span></small></span><span class="pm-cta"><span class="pm-ct"><span class="en">See promo</span><span class="tl">Tingnan ang promo</span></span><svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="3" d="M6 9l6 6 6-6"/></svg></span></button>
<div id="pm-body" role="region" aria-labelledby="pm-tg"><div>
<div class="ab-lang" role="group" aria-label="Language / Wika"><button type="button" data-setlang="en">English</button><button type="button" data-setlang="tl">Taglish</button></div>
<h2 class="h3" style="margin:0 0 6px"><span class="en">{name} promos this month</span><span class="tl">{name} promos ngayong buwan</span></h2>{rl}
<p class="muted ab-s" style="margin-top:-6px"><span class="en">Two all-in options per variant on 60 months: <b>Option A</b>, the lowest down payment (unlock to see), and <b>Option B</b>, a 30% down payment with a lower monthly.</span><span class="tl">Dalawang all-in options bawat variant sa 60 months: <b>Option A</b>, pinakamababang down payment (i-unlock para makita), at <b>Option B</b>, 30% down payment na mas mababa ang monthly.</span></p>
<div class="ab-mg">{t}</div>{fin}</div></div></div></div></section></div>
<script type="text/plain" id="ab-a">{blob}</script>
<script>(function(){{var b=document.getElementById("pm-tg"),p=document.getElementById("pm-body"),s=document.getElementById("promos-model");if(!b||!p)return;
function set(o,go){{b.setAttribute("aria-expanded",o?"true":"false");p.classList.toggle("open",o);try{{p.inert=!o}}catch(_){{}}if(o&&go)setTimeout(function(){{s.scrollIntoView({{behavior:"smooth",block:"start"}})}},60)}}
set(false);b.addEventListener("click",function(){{set(b.getAttribute("aria-expanded")!=="true")}});
document.querySelectorAll("[data-openpromo]").forEach(function(a){{a.addEventListener("click",function(e){{e.preventDefault();set(true,true)}})}});
function hc(){{var h=location.hash;if(h==="#promos-model"||h==="#promos-{slug}"||h==="#unlock")set(true,true)}}hc();window.addEventListener("hashchange",hc)}})();</script>'''
        h=re.sub(r'(<section class="sec alt">.*?</section>)',lambda m:m.group(1)+mod,h,count=1,flags=re.S)
        # hero CTA -> loan pre-qualification (Richard 2026-10-30); promos live in the on-page module
        h=re.sub(r'<a class="btn" href="/promos/[^"]*" data-herocta="([^"]*)">[^<]*</a>',lambda m:f'<a class="btn abw" href="/loan-assessment/" data-herocta="{m.group(1)}"><span class="en">See if you&rsquo;re Pre-Qualified in 2 minutes →</span><span class="tl">Alamin kung Pre-Qualified ka na ngayon →</span></a>',h,count=1)
        h=h.replace(f'href="/promos/#{slug}">See promo','href="#promos-model" data-openpromo>See promo').replace(f'href="/promos/#{slug}"','href="#promos-model"')
        h=h.replace('Promo down payment and monthly options are shared on the <a href="/promos/">promos page</a>.','Promo down payment and monthly options are in the <a href="#promos-model">promos section below</a>.')
        h=h.replace("</body>",f'<script src="/assets/lead.js?v={CARPARTS["lv"]}" defer></script><script src="/assets/promos.js?v={CARPARTS["jv"]}" defer></script></body>',1)
        open(fp,"w").write(h)
