# One-shot codemod (2026-11-04, draft-nov): replace hardcoded promo-month labels in generator
# string literals with data.py constants (_PL=PROMO_LABEL, _PLS=PROMO_SHORT, _PM=PROMO_MONTH).
# Comments, dates (date="2026-10-..") and dated news facts ("October 20, 2026", "Oct 9, 2026") are untouched.
import tokenize, io, re, sys, os, glob, json
R=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RULES=[(re.compile(r'October 2026'),'_PL'),(re.compile(r'\bOct 2026\b'),'_PLS'),
       (re.compile(r'\bOctober(?= promo| figure)'),'_PM'),(re.compile(r'(?<=this )October\b'),'_PM')]
SKIP_TOKEN=[r'Mar 2027']                      # Cebu Daily News source title (dated)
SKIP_LINES={"content.py":range(111,123)}      # dated article /blog/mitsubishi-october-2026-promos-bulacan/
IMPORT="from data import PROMO_LABEL as _PL, PROMO_SHORT as _PLS, PROMO_MONTH as _PM  # promo month (data.py)\n"
counts={}
def conv(src,name):
    toks=list(tokenize.generate_tokens(io.StringIO(src).readline))
    lines=src.splitlines(keepends=True); off=[0]
    for l in lines: off.append(off[-1]+len(l))
    pos=lambda rc: off[rc[0]-1]+rc[1]
    edits=[]; n=0; i=0
    while i<len(toks):
        t=toks[i]
        if t.type==tokenize.FSTRING_START:
            d=1; j=i+1
            while d: 
                d+= toks[j].type==tokenize.FSTRING_START; d-= toks[j].type==tokenize.FSTRING_END; j+=1
            a,b=pos(t.start),pos(toks[j-1].end); kind='f'; i=j
        elif t.type==tokenize.STRING: a,b=pos(t.start),pos(t.end); kind='s'; i+=1
        else: i+=1; continue
        ln=src.count('\n',0,a)+1
        if name in SKIP_LINES and ln in SKIP_LINES[name]: continue
        seg=src[a:b]
        if any(re.search(x,seg) for x in SKIP_TOKEN) or seg.lstrip('rRbBuU')[:1] not in '\'"' and kind=='s': continue
        if 'b' in seg.split(seg.lstrip('rRbBuUfF')[0])[0].lower(): continue
        hits=sum(len(r.findall(seg)) for r,_ in RULES)
        if not hits: continue
        n+=hits
        if kind=='f':
            new=seg
            for r,v in RULES: new=r.sub('{'+v+'}',new)
        else:
            pre=re.match(r'[rRuU]*',seg).group(0); body=seg[len(pre):]
            q=body[:3] if body[:3] in ("'''",'"""') else body[0]
            new=seg
            for r,v in RULES: new=r.sub(lambda m: q+'+'+v+'+'+pre+q,new)
            new='('+new+')'
        edits.append((a,b,new))
    for a,b,new in reversed(edits): src=src[:a]+new+src[b:]
    return src,n
for p in sorted(glob.glob(R+"/_src/*.py")):
    name=os.path.basename(p); s=open(p).read()
    if name=="data.py": continue
    o,n=conv(s,name)
    if not n: continue
    if name not in ("build.py","landing.py","loanapp.py","applyform.py","statuspage.py","card.py"):  # exec'd files share build.py globals
        o=IMPORT+o
    else:
        o=o.replace("from data import *\n","from data import *\n"+IMPORT,1) if name=="build.py" else o
    compile(o,p,"exec"); open(p,"w").write(o); counts[name]=n
print(json.dumps(counts,indent=1),sum(counts.values()))
