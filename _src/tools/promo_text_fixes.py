# Manual-context fixes after sync_promo_text.py (Richard 2026-10-30): wording for the two-option model; lists generated via promotext.py
import re,os,sys
S=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,S)
import promotext as PT
d=PT.V
def R(fn,pairs,regex=()):
    p=os.path.join(S,fn); t=open(p).read()
    for a,b in pairs:
        if a not in t: print("MISS",fn,a[:70]); continue
        t=t.replace(a,b)
    for a,b in regex:
        t2=re.sub(a,b,t,flags=re.S)
        if t2==t: print("MISSRX",fn,a[:70])
        t=t2
    open(p,"w").write(t)
diff=PT.amo("xglxat")-PT.amo("xglxmt")
zl=", ".join(PT.SHORT.get(i,d[i]["n"]) for i in PT.zero_ids())
z0=PT.zero_ids()[0]
R("drafts.py",[
 ('# Draft blog posts (viral Oct 28 series).','import promotext as _PT  # promo figures from optionAB json (2026-10-30)\n# Draft blog posts (viral Oct 28 series).'),
 ('"Zero DP total","Low DP total"','"Option A total","Option B total"'),('"Option 1 total","Option 2 total"','"Option A total","Option B total"'),
 ('"Unit (Zero DP, Oct 2026)"','"Unit (Option A, Oct 2026)"'),
 ('with October 2026 Zero DP monthlies and the income each one needs','with October 2026 lowest-DP (Option A) monthlies and the income each one needs'),
 ('Compare the Zero DP and low DP options of the same unit.','Compare Option A (lowest DP) and Option B (30% DP) of the same unit.'),
 ('<h2>October 2026 Zero DP monthlies and the income they need</h2>','<h2>October 2026 lowest-DP (Option A) monthlies and the income they need</h2>'),
 ("Here's the rule applied to this month's Zero DP promos on a 5-year term.","Here's the rule applied to this month's Option A (lowest DP) promos on a 5-year term."),
 ('Only ₱1,236 more a month than the GLX MT at Zero DP',f'Only {PT.p(diff)} more a month than the GLX MT on Option A (lowest DP)'),
 ('<p>At Zero DP, the automatic is ₱1,236 more a month',f'<p>On Option A (lowest DP), the automatic is {PT.p(diff)} more a month'),
 ('the GLX Zero DP monthly fits roughly','the GLX Option A monthly fits roughly'),
 ('October 2026 promos include Zero DP options such as','October 2026 promos include lowest-DP Option A offers such as'),
 ('Low DP options are lower.','Option B (30% DP) monthlies are lower.'),
 ('for the Zero DP monthly:</p>','for the Option A monthly:</p>'),
 ('<li>GLX Zero DP: ','<li>GLX Option A: '),('<li>GLS Zero DP: ','<li>GLS Option A: '),('<li>GT Zero DP: ','<li>GT Option A: '),
 ('("Which units don\'t have a zero DP option?","In October 2026, the Montero Sport Black Series variants are offered with a down payment.")',
  f'("Which units don\'t have a zero DP option?","In October 2026, Zero DP Promo is on the {zl}. The other units have Option A with a low down payment. Subject to bank approval.")'),
 ('Here are all the Mitsubishi Zero DP promos for October 2026, ranked by monthly','Here are all the Mitsubishi Zero DP Promo units for October 2026, ranked by monthly'),
 ('May Zero DP all-in promos, halimbawa ang Xpander GLX AT sa','May lowest-DP all-in promos (Zero DP Promo sa piling units), halimbawa ang Xpander GLX AT na ₱23K DP sa'),
 ('Yes, through Zero DP all-in promos, subject to bank approval. Example: Xpander GLX MT at',f'Yes, on Zero DP Promo units, subject to bank approval. Example: {PT.SHORT["xcross"]} at {PT.p(PT.amo("xcross"))} a month; or a low DP, like the Xpander GLX MT at'),
 ('Get the month\'s promo: Zero DP and low DP all-in options','Get the month\'s promo: Option A (lowest DP) and Option B (30% DP) all-in options'),
 ('October 2026 Zero DP and low DP options on 60 months','October 2026 Option A (lowest DP) and Option B (30% DP) options on 60 months'),
],[
 (r'(T\(\["Unit","SRP","Option A monthly","Gross income"\]),\[\("L300 Dual AC".*?\)\]\)\+PN',r'\1,_PT.zrows())+PN'),
 (r'"Which Mitsubishi has the lowest zero down payment monthly\?","Among October 2026 promos, the L300 Dual AC at ₱[\d,]+ and the Xpander GLX MT at ₱[\d,]+ a month',
  f'"Which Mitsubishi has the lowest zero down payment monthly?","Among October 2026 Zero DP Promo units, the {PT.SHORT[z0]} at {PT.p(PT.amo(z0))} a month'),
])
R("seo.py",[
 ('Fairview and Quezon City. ₱23K DP examples:','Fairview and Quezon City. Lowest-DP (Option A) examples:'),
 ('GLX AT ₱23,592 a month at ₱18K DP, October 2026)','GLX AT ₱23,592 a month on Option A, October 2026)'),
 ('with October 2026 Zero DP monthlies for','with October 2026 lowest-DP monthlies for'),
 ('every Mitsubishi Zero DP promo ranked by monthly','every Mitsubishi Zero DP Promo unit ranked by monthly'),
],[
 (r'"zero-down-payment-car-philippines":"[^"]*"',f'"zero-down-payment-car-philippines":"For a zero down payment car in the Philippines, October 2026 Mitsubishi Zero DP Promo units start at {PT.p(PT.amo(z0))} a month ({PT.SHORT[z0]}), 60 months, all-in. {len(PT.zero_ids())} variants have Zero DP Promo this month; the others have a low Option A down payment. Subject to bank approval."'),
])
R("landing.py",[
 ('tcap="Units with a Zero DP option, lowest monthly first. Low-DP alternatives shown too."','tcap="Zero DP Promo units (Option A), lowest monthly first, with Option B (30% DP) shown too."'),
],[
 (r'table=\["mg4gls","l300","xglxmt","xglxat","xglsat","xcross","dglx","tritongxat","mglxmt","dgls","mgls","dgtm"\]','table=__import__("promotext").zero_ids()'),
 (r"textra=f'<p class=\"muted\">Montero Sport Black Series is offered with a down payment this month[^']*'",
  "textra=f'<p class=\"muted\">Other units have Option A with a low down payment this month; see the <a href=\"/promos/\">promos page</a>. Subject to bank approval.</p>'"),
])
R("illus.py",[
 ('"October 2026 · Zero DP, 60 months"','"October 2026 · Option A, 60 months"'),('"Zero DP · October 2026"','"Option A · October 2026"'),
 ('"Zero DP vs low DP","A bigger DP lowers the monthly"','"Option A vs Option B","A bigger DP lowers the monthly"'),
],[
 (r'"Low DP: ₱1\d\dK \(GLX MT, GLS, Cross\) or ₱1\d\dK \(GLX AT\)\. ','"Option B: 30% DP tier. '),
 (r'"Low DP: ₱148K / ₱138K / ₱148K / ₱93K / ₱30K\. ','"Option B: 30% DP tier. '),
 (r'"Low DP: ₱1\d\dK \(GLX MT, GLS, Cross\) or ₱1\d\dK \(GLX AT\)\."','"Option B: 30% DP tier. Option A: lowest DP."'),
 (r'"Low DP: ₱93K / ₱123K / ₱88K\. ','"Option B: 30% DP tier. '),
 (r'"Low DP: ₱148K \(MT\), ₱138K \(AT\)\. ','"Option B: 30% DP tier. '),
 (r'(table\("zd-list","October 2026 · lowest first","Zero down payment list",\["Unit","Option A","Gross income"\]),\[.*?\)\](,\[)',r'\1,__import__("promotext").zrows3()\2'),
])
R("figs.py",[('October 2026 Zero DP monthlies','October 2026 lowest-DP (Option A) monthlies'),('Zero DP vs low DP monthly comparison','Option A vs Option B monthly comparison'),
 ('October 2026 Zero DP and low DP monthlies','October 2026 Option A and Option B monthlies'),('Xpander Zero DP monthlies','Xpander Option A monthlies'),
 ('October 2026 Zero DP and low DP highlights','October 2026 Option A and Option B highlights'),('over 60 months, Zero DP vs low DP','over 60 months, Option A vs Option B'),
 ('October 2026 Mitsubishi Zero DP monthlies ranked','October 2026 Mitsubishi Zero DP Promo monthlies ranked')])
bl=PT.V["l300"]["promo"]["opts"][1][0]
R("seo.py",[("Dual AC SRP ₱1,039,000, Zero DP and ₱123K DP monthly options",f"Dual AC SRP ₱1,039,000, Zero DP Promo and {bl} monthly options")])
R("drafts.py",[("a month; the ₱123K DP option about",f"a month; the {bl} option about")])
