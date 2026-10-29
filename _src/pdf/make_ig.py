# Branded infographics for /blog/paano-ma-approve-sa-car-loan/ (white & red, no black). Run from repo root: python3 _src/pdf/make_ig.py
import asyncio,os,json
from playwright.async_api import async_playwright
from PIL import Image
R=os.path.abspath(".");OUT=R+"/assets/img/guide"
CSS="""*{box-sizing:border-box;margin:0}body{font-family:'Noto Sans','Helvetica Neue',Arial,sans-serif;color:#4a4a52;background:#fff}
.c{width:1080px;padding:56px 60px;background:linear-gradient(170deg,#fff 70%,#fff0f1);border-top:14px solid #E60012}
.k{color:#E60012;font-weight:800;letter-spacing:.2em;font-size:22px;text-transform:uppercase}h1{color:#b8000e;font-size:54px;line-height:1.1;margin:10px 0 8px}.s{font-size:26px;margin-bottom:30px}
.g{display:grid;gap:22px}.g3{grid-template-columns:1fr 1fr 1fr}.g2{grid-template-columns:1fr 1fr}
.cd{border:3px solid #f6c3c7;border-radius:22px;padding:24px;background:#fff}.cd h2{color:#E60012;font-size:30px;margin-bottom:12px}
.cd li{font-size:23px;list-style:none;padding:7px 0 7px 36px;position:relative;line-height:1.3}.cd li:before{content:"✓";position:absolute;left:0;color:#E60012;font-weight:900}
.n{display:inline-flex;width:56px;height:56px;border-radius:50%;background:#E60012;color:#fff;font-size:28px;font-weight:800;align-items:center;justify-content:center;flex:none}
.row{display:flex;gap:20px;align-items:center;margin:0 0 16px}.row b{color:#b8000e;font-size:30px}.row p{font-size:23px}
.f{margin-top:30px;display:flex;justify-content:space-between;font-size:20px;color:#b8000e;border-top:2px solid #f6c3c7;padding-top:16px}.f b{color:#E60012}
.big{font-size:70px;color:#E60012;font-weight:900}.bar{height:46px;border-radius:23px;background:#ffe3e6;overflow:hidden;margin:10px 0}.bar i{display:block;height:100%;background:#E60012}
.x li:before{content:"✕"}
"""
FOOT='<div class="f"><span>Richard Cuagdan · Mitsubishi Sales Executive · San Juan Motors</span><b>Drive your Ambition</b></div>'
def card(t,items,cls=""):return f'<div class="cd {cls}"><h2>{t}</h2><ul>'+"".join(f"<li>{i}</li>" for i in items)+'</ul></div>'
def gen(L):
  tl=L=="tl";T=lambda a,b:a if tl else b;G={}
  G["cl-what-banks-check"]=f'''<p class="k">Bank approval</p><h1>{T("Ano ang tinitingnan ng bank?","What do banks check?")}</h1><p class="s">{T("Ang 4 na bagay na nagdedesisyon sa karamihan ng car loan applications","The 4 things that decide most car loan applications")}</p>
<div class="g g2">{card("1 · Capacity to pay",[T("Monthly amortization vs. gross income","Monthly amortization vs. gross income"),T("Kasama ang existing loans","Existing loans count too")])}{card("2 · Credit standing",[T("CIC record, cards, dating loans","CIC record, cards, past loans"),T("Walang past-due o adverse records","No past-due or adverse records")])}{card("3 · Stability",[T("Tenure sa trabaho (madalas 1–2 taon)","Job tenure (often 1–2 yrs)"),T("Negosyo: profitable na taon (madalas 2+)","Business: profitable years (often 2+)")])}{card("4 · Down payment",[T("Mas malaking DP = mas maliit na loan","Bigger DP = smaller loan"),T("Mas mababang monthly, mas madaling ratio","Lower monthly, easier ratio")])}</div>'''
  G["cl-income-rule"]=f'''<p class="k">Capacity to pay</p><h1>{T("Ang 30–35% income rule","The 30–35% income rule")}</h1><p class="s">{T("Maraming bank sa PH ang naglilimita ng monthly amortization sa mga 30% ng gross monthly income.","Many PH banks cap the monthly amortization at about 30% of gross monthly income.")}</p>
<div class="cd"><p style="font-size:26px">{T("Halimbawa: gross monthly income","Example: gross monthly income")}</p><p class="big">₱60,000</p><div class="bar"><i style="width:30%"></i></div><p style="font-size:26px">× 0.30 = <b style="color:#E60012;font-size:40px">₱18,000</b> {T("komportableng max monthly","comfortable max monthly")}</p><p style="font-size:22px;margin-top:10px">{T("Stretch limit sa 35%: ₱21,000 · bawas ang existing loan payments","Stretch limit at 35%: ₱21,000 · minus existing loan payments")}</p></div>
<div class="g g3" style="margin-top:22px">{card(T("Mataas ang monthly?","Monthly too high?"),[T("Lakihan ang DP","Bigger DP")])}{card(T("Kulang ang income?","Need more income?"),[T("Magdagdag ng co-borrower","Add a co-borrower")])}{card(T("Masikip pa rin?","Still tight?"),[T("Mas abot-kayang variant","Choose a lower variant")])}</div>
<p style="font-size:18px;margin-top:16px">{T("Sources: RCBC Auto Loan FAQ; UCPB Savings Auto Loan (30% ratio). Iba-iba ang ratio per bank.","Sources: RCBC Auto Loan FAQ; UCPB Savings Auto Loan (30% ratio). Ratios vary per bank.")}</p>'''
  G["cl-requirements"]=f'''<p class="k">Documents</p><h1>Requirements checklist</h1><p class="s">{T("Per employment type · karaniwang listahan mula BDO, Metrobank at RCBC","Per employment type · typical lists from BDO, Metrobank &amp; RCBC")}</p>
<div class="g g3">{card("Employed",["Valid gov't ID","COE with compensation","Latest payslips","ITR / BIR 2316","Proof of billing"])}{card("Self-employed",["Valid gov't ID","DTI/SEC + permit","Latest ITR","Financial statements","Bank statements"])}{card("OFW",["Passport","Contract / COE","Proof of remittance",T("SPA / PH rep kung kailangan","SPA / PH rep if needed"),"Proof of billing"])}</div>'''
  steps=[("Assess",T("I-compute ang 30% ceiling, i-try ang AI Loan Assessment","Compute your 30% ceiling, take the AI Loan Assessment")),("Choose",T("Unit, variant, down payment at term","Unit, variant, down payment and term")),("Prepare",T("Documents para sa employment type mo","Documents for your employment type")),("Submit",T("Isa-submit sa partner banks","Submitted to partner banks")),("Verify",T("Credit check, tawag, address visit","Credit check, calls, address visit")),("Decision",T("Maglalabas ang bank ng approval at terms","Bank issues approval and terms")),("Release",T("Pirma, initial costs, drive home","Sign, settle initial costs, drive home"))]
  G["cl-timeline"]=f'''<p class="k">Step by step</p><h1>{T("Mula assessment hanggang release","From assessment to release")}</h1><p class="s">{T("Iba-iba ang timing per bank at depende sa pagkakumpleto ng documents.","Timing varies per bank and on how complete your documents are.")}</p>'''+"".join(f'<div class="row"><span class="n">{i+1}</span><div><b>{a}</b><p>{b}</p></div></div>' for i,(a,b) in enumerate(steps))
  G["cl-denial-fixes"]=f'''<p class="k">{T("Iwas denial","Avoid a denial")}</p><h1>{T("Bakit nade-deny? At paano ayusin","Why loans get denied, and the fix")}</h1><p class="s">{T("Karaniwang dahilan at ano ang gagawin","Common reasons and what to do")}</p>
<div class="g g2">{card(T("Dahilan","Reason"),[T("Mataas ang monthly para sa income","Monthly too high for income"),T("Adverse CIC / credit record","Adverse CIC / credit record"),T("Maikling tenure sa trabaho/negosyo","Short job or business tenure"),T("Kulang o hindi tugmang docs","Incomplete or inconsistent docs"),T("Income na hindi ma-verify","Income can't be verified")],"x")}{card("Fix",[T("Mas malaking DP, co-borrower, ibang variant","Bigger DP, co-borrower, lower variant"),T("I-settle ang dues, i-check ang CIC report","Settle dues, check your CIC report"),T("Maghintay, o magdagdag ng co-borrower","Wait, or add a co-borrower"),T("Parehong name/address sa bawat page","Same name/address on every page"),T("Ipakita ang ITR, bank statements, payslips","Show ITR, bank statements, payslips")])}</div>'''
  G["cl-bank-vs-inhouse"]=f'''<p class="k">{T("Financing options","Financing options")}</p><h1>Bank vs in-house financing</h1><p class="s">{T("Ikumpara ang total amount payable, hindi lang ang monthly.","Compare the total amount payable, not just the monthly.")}</p>
<div class="g g2">{card("Bank financing",[T("Kadalasang mas mababa ang interest","Usually lower interest"),T("Mas mahigpit ang requirements","Stricter requirements"),T("May credit at income checks","Credit and income checks"),T("Karaniwan sa brand-new units","Common for brand-new units")])}{card("In-house / captive",[T("Pwedeng mas flexible","Can be more flexible"),T("Baka mas mahal sa buong term","May cost more over the term"),T("I-check ang fees at penalties","Check fees and penalties"),T("Basahin nang buo ang contract","Read the contract fully")])}</div>'''
  hero=dict(k=T("Car loan guide 2026","Car loan guide 2026"),h=T("Paano Ma&#8209;approve<br>sa Car Loan","How to Get Your<br>Car Loan Approved"),s=T("Ano ang tinitingnan ng bank: requirements, CIC, 30% rule, timeline.","What banks check: requirements, CIC, the 30% rule, timeline."),p=T("Libreng checklist PDF","Free checklist PDF"))
  return G,hero
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"]);pg=await b.new_page(viewport={"width":1080,"height":800})
    sizes={}
    for L in ("tl","en"):
     G,HE=gen(L)
     for k,h in G.items():
      await pg.set_content(f"<style>{CSS}</style><div class='c' id='c'>{h}{FOOT}</div>");await pg.wait_for_timeout(150)
      await pg.locator("#c").screenshot(path=f"/tmp/{k}-{L}.png")
     # hero: official Xpander photo + title
     await pg.set_viewport_size({"width":1200,"height":800})
     await pg.set_content(f"""<style>{CSS}.h{{width:1200px;height:800px;position:relative;background:#fff;border-top:14px solid #E60012;overflow:hidden}}.h img{{position:absolute;right:-40px;bottom:40px;width:760px}}.t{{position:absolute;left:60px;top:70px;width:600px;z-index:2}}.t .s{{width:470px}}.t h1{{font-size:60px}}.pill{{display:inline-block;background:#E60012;color:#fff;border-radius:40px;padding:12px 26px;font-size:24px;font-weight:800;margin-top:14px}}</style>
     <div class="h" id="c"><div class="t"><p class="k">{HE["k"]}</p><h1>{HE["h"]}</h1><p class="s">{HE["s"]}</p><span class="pill">{HE["p"]}</span></div><img src="data:image/webp;base64,{__import__("base64").b64encode(open(R+"/assets/img/xpgls_c31.webp","rb").read()).decode()}"><div style="position:absolute;left:60px;right:60px;bottom:24px">{FOOT}</div></div>""")
     await pg.wait_for_timeout(300);await pg.locator("#c").screenshot(path=f"/tmp/cl-hero-{L}.png")
     await pg.set_viewport_size({"width":1080,"height":800})
    await b.close()
  import glob
  for old in glob.glob(OUT+"/*.webp"): os.remove(old)
  for L in ("tl","en"):
   for k0 in list(gen(L)[0])+["cl-hero"]:
    k=f"{k0}-{L}";im=Image.open(f"/tmp/{k}.png").convert("RGB")
    if k0!="cl-hero": im=im.resize((900,round(im.height*900/im.width)),Image.LANCZOS)
    im.save(f"{OUT}/{k}.webp","WEBP",quality=82,method=6);sizes[k]=im.size
  json.dump(sizes,open(R+"/_src/pdf/ig_sizes.json","w"))
  print(sizes)
asyncio.run(main())
