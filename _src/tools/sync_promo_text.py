# One-shot codemod (2026-10-30, Richard item 5): rewrite hand-typed promo figures in article/SEO/illustration sources
# from the OLD data.py promo pairs ("Zero DP"/"₱XK DP" + monthly) to the new Option A / Option B from _src/optionAB_oct2026.json
# (via data.py's promo override). Derived figures on the same line (gross income at 30-35%, 60-month totals) are recomputed.
# Usage: python3 _src/tools/sync_promo_text.py <old_data.py>   (old = git show 24b15ab:_src/data.py)
import re,sys,os,types
S=os.path.dirname(os.path.dirname(os.path.abspath(__file__)));sys.path.insert(0,S)
import data as NEW
src=open(sys.argv[1]).read(); OLD=types.ModuleType("old"); exec(src,OLD.__dict__)
nv={v["id"]:v for m in NEW.MODELS for v in m["variants"]}
SL=[]  # (old_mo, old_label, new_mo, new_label, unit_name)
for m in OLD.MODELS:
    for v in m["variants"]:
        if not v["promo"]: continue
        ab=nv[v["id"]]["ab"]; o=v["promo"]["opts"]
        zero_first = o[0][0].startswith("Zero")
        for k,(l,mo) in enumerate(o):
            slot = "A" if (k==0 and (zero_first or len(o)>1)) else "B"
            if len(o)==1: slot="B" if mo==ab["b_mo"] else "A"
            dp,nmo=(ab["a_dp"],ab["a_mo"]) if slot=="A" else (ab["b_dp"],ab["b_mo"])
            SL.append((mo,l,nmo,NEW.dplabel(dp),v["n"]))
def fm(n): return format(n,",")
def inc(v): return [int(v/0.35/100+0.5)*100,int(v/0.30/100+0.5)*100]
def k1(n): return f"{n/1000:.1f}K"
def lab_rx(l):
    if l.startswith("Zero"): return r"Zero DP(?! Promo)|\(Zero\)"
    k=re.search(r"([\d.]+)K",l).group(1); return r"₱?"+re.escape(k)+r"K(?: DP)?"
def newlab(found,nl):
    z=nl.startswith("Zero")
    if found=="(Zero)": return "(Zero DP Promo)" if z else "("+nl.replace(" DP","")+")"
    peso=found.startswith("₱") or found.startswith("Zero"); hasdp=found.endswith("DP")
    if z: return "Zero DP Promo"
    x=nl if hasdp else nl.replace(" DP","")
    return x if peso else x.lstrip("₱")
HDR=[('"Zero DP monthly"','"Option A monthly"'),('"Zero DP / mo"','"Option A / mo"'),('"Low DP monthly"','"Option B monthly"'),
     ('["Unit","Zero DP","','["Unit","Option A","'),('"SRP","Zero DP","Low DP"','"SRP","Option A","Option B"'),('"Zero DP","Low DP"','"Option A","Option B"'),
     ('"Zero DP","With DP"','"Option A","Option B"'),('"Zero DP","With down payment"','"Option A","Option B"'),('"Gross income (30–35%)"','"Gross income (30–35%)"')]
log=[]
def fix_line(L):
    edits=[]
    for (omo,ol,nmo,nl,un) in SL:
        for mm in re.finditer(r"(?<![\d,.])(₱?)"+re.escape(fm(omo))+r"(?!\d|,\d)",L):
            if omo in (39740,37256):  # Destinator GT monotone / two-tone share old figures
                tt="two-tone" in L[max(0,mm.start()-40):mm.start()].lower()
                if ("Two-Tone" in un)!=tt: continue
            edits.append((mm.start(),mm.end(),mm.group(1)+fm(nmo),un))
            best=None
            for lm in re.finditer(lab_rx(ol),L):
                d=min(abs(lm.start()-mm.end()),abs(mm.start()-lm.end()))
                if d<=32 and (best is None or d<best[0]): best=(d,lm)
            if best: edits.append((best[1].start(),best[1].end(),newlab(best[1].group(0),nl),un))
            # derived on same line
            for a,b in zip(inc(omo),inc(nmo)):
                for pat,rep in ((fm(a),fm(b)),(k1(a),k1(b))):
                    for dm in re.finditer(r"(?<![\d,.])"+re.escape(pat)+r"(?!\d|,\d)",L): edits.append((dm.start(),dm.end(),rep,un))
    edits.sort(key=lambda e:(e[0],-e[1])); out=[]; last=-1
    for e in edits:
        if e[0]>=last and not any(x[0]==e[0] for x in out): out.append(e); last=e[1]
    for s,e,r,un in sorted(out,reverse=True): L=L[:s]+r+L[e:]
    return L,len(out)
for fn in ["drafts.py","illus.py","figs.py","seo.py","landing.py","content.py","loanguide.py"]:
    p=os.path.join(S,fn); t=open(p).read().split("\n"); n=0
    for i,L in enumerate(t):
        L2,c=fix_line(L)
        if "T([" in L2 or "table(" in L2 or c:
            for a,b in HDR: L2=L2.replace(a,b)
        if c: L2=re.sub(r"(₱[\d,]+(?:/mo)?) (₱[\d.]+K DP)",r"\1 with \2",L2)
        if L2!=L: t[i]=L2; n+=1
    open(p,"w").write("\n".join(t)); print(fn,"lines changed",n)
# ---- pass 2: derived figures quoted without their monthly on the same line (income ranges, 60-month totals)
def P2(t):
    for (omo,ol,nmo,nl,un) in SL:
        if omo==nmo: continue
        a,b=inc(omo); c,d=inc(nmo)
        for sep in (" to ₱"," – ₱","–₱"," - ₱"):
            t=t.replace(f"₱{fm(a)}{sep}{fm(b)}",f"₱{fm(c)}{sep}{fm(d)}")
        t=t.replace(f"₱{k1(a)}–₱{k1(b)}",f"₱{k1(c)}–₱{k1(d)}").replace(f"₱{k1(a)} – ₱{k1(b)}",f"₱{k1(c)} – ₱{k1(d)}")
    for (omo,ol,nmo,nl,un) in SL:  # totals = DP + 60 monthlies
        od=0 if ol.startswith("Zero") else int(float(re.search(r"([\d.]+)K",ol).group(1))*1000)
        nd=0 if nl.startswith("Zero") else int(float(re.search(r"([\d.]+)K",nl).group(1))*1000)
        if od+omo*60!=nd+nmo*60: t=re.sub(r"(?<![\d,.])₱"+re.escape(fm(od+omo*60))+r"(?!\d|,\d)","₱"+fm(nd+nmo*60),t)
    return t
for fn in ["drafts.py","illus.py","figs.py","seo.py","landing.py","content.py","loanguide.py"]:
    p=os.path.join(S,fn); t=open(p).read(); t2=P2(t)
    if t2!=t: open(p,"w").write(t2); print("pass2",fn)
