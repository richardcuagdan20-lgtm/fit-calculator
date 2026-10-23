# Evergreen: how to get your car loan approved by the bank + gated PDF lead magnet. Do NOT promote zero downpayment (dealer restriction).
# Keyword research: /workspace/loanapp/zerodp_keywords.md (main kw: "bank approval for car loan philippines" / "paano ma approve sa car loan").
SLUG="paano-ma-approve-sa-car-loan"
OLD_SLUG="zero-down-payment-car-loan-requirements"
PDF="/assets/car-loan-approval-guide.pdf"
OLD_PDF="/assets/zero-dp-car-loan-approval-guide.pdf"
LA="https://mitsubishipromos.online/loan-assessment/"
def ZCTA(h,p,btn="Start the free AI Loan Assessment"):
    return f'<aside class="lacta zcta"><h2>{h}</h2><p>{p}</p><a class="btn" href="{LA}" data-cta="car-loan-guide">{btn}</a><p class="zsm">Result is a Pre-qualified estimate only. Final financing is subject to bank approval.</p></aside>\n'
def ZFORM(i):
    return f'''<form id="{i}" class="zform" novalidate>
<div class="fld"><label for="{i}_name">Full name</label><input id="{i}_name" autocomplete="name" required><p class="er" id="e_{i}_name" hidden>Please enter your name.</p></div>
<div class="fld"><label for="{i}_email">Email</label><input id="{i}_email" type="email" autocomplete="email" inputmode="email" required><p class="er" id="e_{i}_email" hidden>Please enter a valid email.</p></div>
<label class="chk"><input type="checkbox" id="{i}_consent" required> <span>I consent to Mitsubishi SJ Legacy Motors and Richard Cuagdan collecting and processing my name and email under the Data Privacy Act of 2012 (RA 10173) to send this guide and contact me about car financing. See the <a href="/privacy/">Privacy Policy</a>. Data Protection Officer: <a href="mailto:richard.cuagdan20@gmail.com">richard.cuagdan20@gmail.com</a>.</span></label><p class="er" id="e_{i}_consent" hidden>Please tick the consent box.</p>
<button class="btn" type="submit">Send me the free PDF</button>
<div class="zok" hidden><p><b>Salamat!</b> Your guide is ready.</p><p><a class="btn" href="{PDF}" download target="_blank" rel="noopener" data-pdf>Download the PDF guide</a></p><p class="zsm">Next step: <a href="{LA}">take the free AI Loan Assessment</a> or <a href="https://m.me/MitsubishiRDC" rel="noopener">message me on Messenger</a>.</p></div>
</form>'''
GATE_INLINE=f'''<aside class="zgate" id="zgate"><p class="kick">Free PDF</p><h2>Get the Car Loan Approval Checklist (PDF)</h2><p>Document checklist per employment type, a budget/DTI worksheet, bank comparison tips and a step-by-step timeline. I-save mo sa phone, dalhin sa bank.</p>{ZFORM("zf")}</aside>
'''
POP=f'''<script src="/assets/lead.js" defer></script>
<div class="zpop" id="zpop" role="dialog" aria-modal="true" aria-labelledby="zpop_t" hidden><div class="zpop_in"><button type="button" class="zx" aria-label="Close">×</button><p class="kick">Free PDF</p><h2 id="zpop_t" class="h3">Car Loan Approval Checklist</h2><p>Free download: documents, DTI worksheet and timeline in one PDF.</p>{ZFORM("zf2")}</div></div>
<script>
try{{fbq('track','ViewContent',{{content_name:'car-loan-guide'}})}}catch(_){{}}
document.addEventListener('DOMContentLoaded',function(){{
var $=function(i){{return document.getElementById(i)}},K='clg_pdf_ok',pop=$('zpop'),shown=false;
function done(){{['zf','zf2'].forEach(function(i){{var f=$(i);if(!f)return;[].forEach.call(f.children,function(c){{if(!c.classList.contains('zok'))c.hidden=true}});f.querySelector('.zok').hidden=false}})}}
try{{if(localStorage.getItem(K))done()}}catch(_){{}}
['zf','zf2'].forEach(function(i){{var f=$(i);if(!f)return;if(window.AS)AS.init(f);
 f.addEventListener('submit',function(ev){{ev.preventDefault();
  var v=function(x){{return $(i+'_'+x).value.trim()}},n=v('name'),em=v('email');
  var bad=[Lead.err(i+'_name',n.length<2),Lead.err(i+'_email',!/^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(em)),Lead.err(i+'_consent',!$(i+'_consent').checked)];
  if(bad.some(Boolean))return;
  var b=f.querySelector('button[type=submit]');b.disabled=true;b.textContent='Sending...';
  var L=Lead.base('car_loan_guide_pdf');L.name=n;L.mobile='';L.email=em;L.chosenUnit='Car Loan Guide PDF';L.usage='Lead magnet: car_loan_guide_pdf | Email: '+em;
  Lead.send(L).then(function(){{try{{localStorage.setItem(K,'1')}}catch(_){{}}
   if(!Lead.skipped()){{try{{if(typeof window.fbq==='function')window.fbq('track','Lead',{{content_name:'car-loan-guide-pdf'}})}}catch(_){{}}
    try{{if(typeof window.gtag==='function')window.gtag('event','generate_lead',{{unit:'car-loan-guide-pdf',value:0,currency:'PHP'}})}}catch(_){{}}}}
   done()}});
 }});
}});
function close(){{pop.hidden=true;document.body.classList.remove('znos')}}
pop.querySelector('.zx').addEventListener('click',close);pop.addEventListener('click',function(e){{if(e.target===pop)close()}});
document.addEventListener('keydown',function(e){{if(e.key==='Escape'&&!pop.hidden)close()}});
function seen(){{try{{return localStorage.getItem(K)||sessionStorage.getItem('clg_pop')}}catch(_){{return false}}}}
window.addEventListener('scroll',function(){{if(shown||seen())return;var h=document.documentElement,p=(h.scrollTop||document.body.scrollTop)/((h.scrollHeight-h.clientHeight)||1);
 if(p>0.4){{shown=true;try{{sessionStorage.setItem('clg_pop','1')}}catch(_){{}}pop.hidden=false}}}},{{passive:true}});
}});
</script>
'''
FAQ=[
("What do banks check before approving a car loan?","Mainly your capacity to pay (monthly amortization vs. gross income), your credit history including your CIC record, the stability of your job or business, and whether your documents are complete, consistent and verifiable."),
("Does a bigger down payment help my approval?","Usually, yes. A bigger down payment means a smaller loan and a lower monthly, which makes it easier to stay within the bank's income ratio. Down payment options depend on the bank and the current dealer offer."),
("How much salary do I need for a car loan?","There's no single number. Work backwards: your monthly amortization should stay within roughly 30% (at most about 35%) of your gross monthly income. Some banks also publish a minimum gross monthly family income, so check with the specific bank."),
("What documents do I need for a car loan as an employee?","Usually a filled-out application form, valid government ID, Certificate of Employment with compensation, latest payslips and/or ITR or BIR Form 2316, and proof of billing. Exact lists differ per bank."),
("Can self-employed people or freelancers get a car loan?","Yes. Banks usually look for business registration (DTI/SEC), ITR and financial statements, and several months of bank statements. Many banks look for at least two years of profitable operations."),
("Can OFWs apply for a car loan while abroad?","Yes. Expect to submit a contract or Certificate of Employment with income, proof of remittance and a passport. Some banks need a Special Power of Attorney or a representative in the Philippines."),
("Does my CIC credit report affect car loan approval?","Yes. Banks check your credit history, and adverse records such as unpaid loans or past-due credit cards can lead to denial. You can request your own CIC credit report through CIC's accredited partners to check it before applying."),
("How long does car loan approval take?","It depends on the bank and on how complete your documents are. Complete, consistent documents are the biggest factor you control. Your sales executive can follow up with the bank for you."),
("Why do car loans get denied?","Common reasons are a monthly that's too high for the income, adverse credit history, incomplete or inconsistent documents, short employment or business tenure, and information that can't be verified."),
("If my car loan is denied, can I apply again?","Yes. Fix the reason first: lower the loan amount with a bigger DP, add a co-borrower, complete documents or clean up your credit record, then apply with another bank or after your situation improves.")]
ZPOST=dict(base="blog",car="xpander",slug=SLUG,date="2026-10-23",by="Mitsubishi Sales Executive",img="guide/cl-hero",alt="Paano ma-approve sa car loan: bank approval guide cover with an official Mitsubishi Xpander photo",
title="Paano Ma-approve sa Car Loan: What Banks Check Before They Say Yes",
desc="Paano ma-approve sa car loan? What PH banks check: the 30% income rule, CIC credit, documents per employment type, denial reasons, timeline and a free PDF.",
answer="To get your car loan approved by the bank, keep your monthly amortization within about 30% of your gross monthly income, have a clean CIC credit record, and submit complete, consistent documents for your employment type. A bigger DP, a co-borrower or a lower-priced variant all raise your chances. Final approval is always up to the bank.",
faq=FAQ,
body=f'''<p>"Sir, ma-a-approve kaya ako sa bank?" Ito ang pinaka-common na tanong sa showroom namin sa SJDM, from buyers in Bulacan to Caloocan, Fairview and the rest of Metro Manila. The good news: bank approval isn't luck. Banks follow a fairly predictable checklist, and once you know it, you can prepare like a pro.</p>
<p>This guide covers what banks look at, the documents per employment type, the income rule that decides most applications, and the common reasons for denial. Gusto mo ng printable version? Grab the free PDF checklist below.</p>
<h2>How your down payment affects approval</h2>
<p>The bank looks first at your monthly amortization versus your income. A <b>bigger down payment</b> means a smaller loan and a lower monthly, which makes that ratio easier to meet. A smaller down payment means a bigger loan, so your income has to carry a higher monthly. Down payment options depend on the bank and the current dealer offer, so ask before you decide. (For quick tips, see my <a href="/tips/car-loan-approval-tips/">10 car loan approval tips</a>; for the application steps, see <a href="/tips/paano-mag-car-loan/">paano mag car loan</a>.)</p>
{ZCTA("Ma-a-approve ka kaya?","Check your chances in 3 minutes with the free AI Car Loan Application Assessment. Walang documents na kailangan.")}
<h2>What banks check before approving a car loan</h2>
<ul class="ticks"><li><b>Capacity to pay</b>: your gross monthly income vs. the monthly amortization.</li><li><b>Credit standing</b>: your history with loans and credit cards, including your CIC record.</li><li><b>Stability</b>: how long you've been employed or how long your business has been profitable.</li><li><b>Completeness and consistency</b>: documents that match each other and can be verified.</li><li><b>Age and residency</b>: banks set minimum and maximum ages and may ask how long you've stayed at your address.</li></ul>
<h2>The 30–35% income rule (DTI)</h2>
<p>Many Philippine banks cap the monthly car amortization at about <b>30% of gross monthly income</b>. RCBC and UCPB Savings, for example, publish a 30% ratio. Some lenders may stretch a bit, so plan for <b>30% to 35% at most</b>, and remember that other existing loans eat into that room.</p>
<div class="box"><p><b>Quick formula:</b> Gross monthly income × 0.30 = comfortable maximum monthly amortization.</p><p>Example: ₱60,000 × 0.30 = ₱18,000. If the monthly of the unit you want is higher than that, either increase the DP, add a co-borrower's income, or consider a lower variant.</p></div>
<p>Not sure where you land? See <a href="/blog/how-much-car-can-i-afford-philippines/">how much car you can afford on your salary</a>.</p>
<h2>Credit standing and your CIC report</h2>
<p>Banks check whether you have adverse credit records, such as past-due credit cards, unpaid loans or bounced checks. The Credit Information Corporation (CIC) collects this data under RA 9510, and you can request your own CIC credit report through CIC's accredited partners before you apply. If something is wrong or outdated, you can file a dispute with CIC.</p>
<ul class="ticks"><li>Pay credit cards on time for several months before applying.</li><li>Settle or restructure past-due accounts and keep the proof.</li><li>Avoid applying for many loans at once.</li></ul>
<h2>Requirements per employment type</h2>
<p>Exact lists differ per bank, but these are what most banks ask for (based on published BDO, Metrobank and RCBC requirements):</p>
<h3>Locally employed</h3>
<ul class="ticks"><li>Application form and valid government ID</li><li>Certificate of Employment with compensation (COEC)</li><li>Latest payslips and/or ITR or BIR Form 2316</li><li>Proof of billing</li><li>Often at least 1 to 2 years with your current employer, depending on the bank</li></ul>
<h3>Self-employed and business owners</h3>
<ul class="ticks"><li>DTI or SEC registration and business permit</li><li>Latest ITR and financial statements (audited for some banks)</li><li>Recent bank statements (usually several months)</li><li>Usually about 2 years or more of profitable operations</li></ul>
<h3>OFWs and seafarers</h3>
<ul class="ticks"><li>Passport and contract or Certificate of Employment with income</li><li>Proof of remittance for recent months</li><li>Special Power of Attorney or a representative/co-borrower in the Philippines, if required</li></ul>
<p>OFW ka? Read my <a href="/blog/ofw-car-buying-guide/">OFW car loan guide</a> for the full process.</p>
{GATE_INLINE}
<h2>Bank financing vs in-house financing</h2>
<p>Bank financing usually has lower interest but stricter screening. In-house or captive financing can be more flexible on requirements but may cost more over the term. I explain the trade-offs in <a href="/blog/bank-vs-in-house-car-financing-philippines/">bank vs in-house car financing</a>. My tip: always compare the <b>total amount payable</b>, not just the monthly.</p>
<h2>Tips to raise your chances</h2>
<ul class="ticks"><li><b>Right-size the loan.</b> Pick the variant and DP that keep your monthly within 30%.</li><li><b>Add a co-borrower</b>, such as a spouse, whose income can be counted (subject to the bank's rules).</li><li><b>Show all income sources</b> with proof: allowances, business income, rental, remittances.</li><li><b>Keep documents consistent.</b> Same name spelling, address and employer details on every page.</li><li><b>Clean up your credit</b> before you apply.</li><li><b>Apply with the right bank.</b> Your sales executive can submit to more than one partner bank.</li><li><b>Be reachable.</b> Answer the bank's verification call on time.</li></ul>
{ZCTA("Alamin muna bago mag-apply","The AI Loan Assessment checks your income, DP and term against your target unit and gives a Pre-qualified estimate in minutes.","Check my loan readiness")}
<h2>Common reasons car loans get denied</h2>
<ul class="ticks"><li>Monthly amortization too high for the declared income</li><li>Adverse CIC or bank credit records</li><li>Short employment tenure or new business</li><li>Incomplete, unclear or inconsistent documents</li><li>Income that can't be verified (cash income with no records)</li><li>Unanswered verification calls or failed address checks</li></ul>
<h2>Step-by-step timeline</h2>
<ol class="zsteps"><li><b>Assess</b>: compute your 30% ceiling and take the <a href="{LA}">AI Loan Assessment</a>.</li><li><b>Choose</b>: pick your unit, variant, down payment and term.</li><li><b>Prepare</b>: complete the documents for your employment type.</li><li><b>Submit</b>: I submit your application to partner banks.</li><li><b>Verify</b>: the bank checks your credit, calls you and your employer, and may visit your address.</li><li><b>Decision</b>: the bank issues its approval and terms. Timing varies per bank and on how complete your file is.</li><li><b>Release</b>: sign, settle initial costs if any, and drive home.</li></ol>
<h2>Where to start in Metro Manila and Bulacan</h2>
<p>I'm based at Mitsubishi SJ Legacy Motors in San Jose del Monte, Bulacan, and I help buyers across Bulacan and Metro Manila, including our Quezon City branch. You can do the assessment and send documents online first, then visit only when you're ready.</p>
'''+ZCTA("Ready for the next step?","Take the free assessment now and I'll walk you through the documents for your situation. Walang pressure.","Start my AI Loan Assessment")+'''<h2>Sources</h2><ul class="links"><li><a href="https://www.rcbc.com/Content/Forms/FAQs_auto.pdf" target="_blank" rel="noopener">RCBC Auto Loan FAQ (amortization not exceeding 30% of gross monthly income)</a></li><li><a href="https://www.ucpbsavings.com/auto-loan/" target="_blank" rel="noopener">UCPB Savings Auto Loan (30% credit ratio)</a></li><li><a href="https://www.metrobank.com.ph/help/loans/car-loan/loan-application-car-loan" target="_blank" rel="noopener">Metrobank Car Loan application requirements</a></li><li><a href="https://www.bdo.com.ph/personal/loans/auto-loan" target="_blank" rel="noopener">BDO Auto Loan requirements</a></li><li><a href="https://cic.gov.ph/about-your-cic-credit-report/" target="_blank" rel="noopener">CIC: About your credit report</a></li></ul>
<p class="muted">Requirements and ratios vary per bank and can change. All outcomes from our tools are Pre-qualified estimates only; financing is always subject to bank approval.</p>
'''+POP)

import json as _j,os as _o
_SZ=_j.load(open(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),"pdf","ig_sizes.json")))
IGS=[("<h2>What banks check","cl-what-banks-check","Infographic: the 4 things banks check before approving a car loan: capacity to pay, credit standing and CIC record, job or business stability, and down payment.","Ano ang tinitingnan ng bank: capacity to pay, credit, stability at down payment."),
("<h2>The 30–35% income rule","cl-income-rule","Infographic: the 30 to 35 percent income rule. Example: ₱60,000 gross monthly income times 0.30 equals ₱18,000 comfortable maximum monthly amortization.","Worked example: ₱60,000 × 0.30 = ₱18,000 max monthly (ratios vary per bank)."),
("<h2>Requirements per employment type","cl-requirements","Infographic: car loan requirements checklist for employed, self-employed and OFW applicants.","Typical documents per employment type, based on published BDO, Metrobank and RCBC requirements."),
("<h2>Bank financing vs in-house","cl-bank-vs-inhouse","Infographic comparing bank financing and in-house financing for a car loan.","Bank vs in-house: compare the total amount payable, not just the monthly."),
("<h2>Common reasons car loans get denied","cl-denial-fixes","Infographic: common car loan denial reasons and how to fix each one.","Bakit na-de-deny ang car loan, at paano ayusin."),
("<h2>Step-by-step timeline","cl-timeline","Infographic: 7-step car loan timeline from assessment, choosing a unit, preparing documents, submission, verification and bank decision to release.","From assessment to release: 7 steps. Timing varies per bank.")]
_b=ZPOST["body"]
for h,k,alt,cap in IGS:
    w,hh=_SZ[k];i=_b.index(h)
    _b=_b[:i]+f'<figure class="fig"><img src="/assets/img/guide/{k}.webp" alt="{alt}" width="{w}" height="{hh}" loading="lazy" decoding="async"><figcaption class="zsm">{cap}</figcaption></figure>\n'+_b[i:]
ZPOST["body"]=_b
