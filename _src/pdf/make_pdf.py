# Build car-loan-approval-guide-{tl,en}.pdf from car_loan_guide.html (base = English body). Run from repo root after make_ig.py.
import subprocess,os,re,shutil
R=os.path.abspath(".");base=open(R+"/_src/pdf/car_loan_guide.html").read()
COMMON=[(f'cl-{k}.webp',f'cl-{k}-@L.webp') for k in ["what-banks-check","income-rule","requirements","timeline","denial-fixes","bank-vs-inhouse"]]+[('href="https://mitsubishipromos.online/loan-assessment/"','href="https://mitsubishipromos.online/loan-assessment/?lang=@L"')]
EN=[('<h1>Paano Ma-approve<br>sa Car Loan</h1>','<h1>How to Get Your<br>Car Loan Approved</h1>'),('– para handa ka bago mag-apply sa bank.','– so you are ready before you apply at the bank.')]
TL=[('<html>','<html lang="fil">'),('font-size:10.5pt;line-height:1.45','font-size:9.8pt;line-height:1.4'),('style="width:42%','style="width:34%'),('style="width:58%','style="width:46%'),('Requirements, documents, budget worksheet &amp; timeline – para handa ka bago mag-apply sa bank.','Requirements, documents, budget worksheet at timeline – para handa ka bago mag-apply sa bank.'),
('(also serving Quezon City &amp; Metro Manila)','(nagse-serve din sa Quezon City at Metro Manila)'),
('guide summary · document checklist per employment type · budget/DTI worksheet · bank comparison tips · step-by-step timeline','buod ng guide · document checklist per employment type · budget/DTI worksheet · bank comparison tips · step-by-step timeline'),
('1. The guide in one page','1. Ang guide sa isang page'),
('a bigger DP means a smaller loan and lower monthly, making the income ratio easier to meet. Options depend on the bank and current dealer offer.','mas malaking DP = mas maliit na loan at mas mababang monthly, kaya mas madaling pumasok sa income ratio. Depende sa bank at current dealer offer ang options.'),
('many PH banks cap the monthly amortization at about 30% of gross monthly income (RCBC and UCPB Savings publish 30%). Plan for 30–35% at most, including other loans.','maraming bank sa PH ang naglilimita ng monthly amortization sa mga 30% ng gross monthly income (30% ang published ng RCBC at UCPB Savings). Mag-plano sa 30–35% lang, kasama ang ibang loans.'),
("adverse records (past-due cards, unpaid loans) can lead to denial. Get your own CIC credit report via CIC's accredited partners before applying.","ang adverse records (past-due cards, unpaid loans) ay pwedeng maging dahilan ng denial. Kunin ang sarili mong CIC credit report sa accredited partners ng CIC bago mag-apply."),
('banks look at employment tenure (often 1–2 years) or profitable business years (often 2+).','tinitingnan ng bank ang tenure sa trabaho (madalas 1–2 taon) o ilang taon nang profitable ang negosyo (madalas 2+).'),
('complete, consistent and verifiable. Same name, address and employer details everywhere.','kumpleto, consistent at nave-verify. Parehong pangalan, address at employer details sa lahat.'),
('<b>Raise your chances:</b> right-size the unit/DP, add a co-borrower, show all income with proof, clean your credit, answer verification calls.','<b>Pataasin ang chances:</b> tamang unit/DP, magdagdag ng co-borrower, ipakita lahat ng income na may proof, linisin ang credit, sagutin ang verification calls.'),
('<b>Common denial reasons:</b> monthly too high for income, adverse credit, short tenure, incomplete/inconsistent docs, unverifiable income.','<b>Karaniwang dahilan ng denial:</b> mataas ang monthly para sa income, adverse credit, maikling tenure, kulang/hindi tugmang docs, income na hindi ma-verify.'),
('Want to know where you stand? Take the free','Gusto mong malaman kung saan ka papasok? I-try ang libreng'),('Result is a Pre-qualified estimate only; financing is subject to bank approval.','Ang resulta ay Pre-qualified estimate lamang; ang financing ay subject to bank approval.'),
('Typical lists based on published BDO, Metrobank and RCBC requirements. Each bank may ask for more or less.','Karaniwang listahan base sa published requirements ng BDO, Metrobank at RCBC. Pwedeng mas marami o mas kaunti ang hingin ng bawat bank.'),
('SPA / representative in PH (if required)','SPA / representative sa PH (kung kailangan)'),
('<th>Your numbers</th>','<th>Numbers mo</th>'),('A. Gross monthly income (you)','A. Gross monthly income (ikaw)'),('B. Co-borrower gross monthly income','B. Gross monthly income ng co-borrower'),('<td>If any</td>','<td>Kung meron</td>'),
('D. Max total monthly debt (30%)','D. Max na total monthly utang (30%)'),('E. Existing loan payments','E. Existing na hulog sa loans'),('F. Room for car amortization','F. Natitirang room para sa car amortization'),
('G. Monthly of target unit, DP option 1','G. Monthly ng target unit, DP option 1'),('H. Monthly of target unit, DP option 2 (bigger DP)','H. Monthly ng target unit, DP option 2 (mas malaking DP)'),('Ask your sales executive','Itanong sa sales executive'),
('<b>Reading it:</b> if G ≤ F, option 1 fits your income. If only H ≤ F, the bigger DP is the safer choice. If neither, consider a lower variant, a co-borrower or a bigger DP. Also budget for fuel, insurance renewal, PMS and parking.','<b>Paano basahin:</b> kung G ≤ F, pasok ang option 1 sa income mo. Kung H ≤ F lang, mas safe ang mas malaking DP. Kung wala sa dalawa, pag-isipan ang mas abot-kayang variant, co-borrower o mas malaking DP. Mag-budget din para sa gas, insurance renewal, PMS at parking.'),
('Compare the <b>total amount payable</b> over the term, not just the monthly.','Ikumpara ang <b>total amount payable</b> sa buong term, hindi lang ang monthly.'),
('Ask for the add-on or effective rate, term options and any fees.','Itanong ang add-on o effective rate, term options at fees.'),
("Check the bank's minimum income, tenure and age rules before applying.","I-check ang minimum income, tenure at age rules ng bank bago mag-apply."),
("Ask what's in the all-in package (registration, insurance, chattel mortgage).","Itanong kung ano ang kasama sa all-in package (registration, insurance, chattel mortgage)."),
('Ask about penalties for late payment and for paying off early.','Itanong ang penalties sa late payment at sa maagang pagbayad.'),
('Bank vs in-house: banks are usually cheaper but stricter; in-house may be more flexible but may cost more.','Bank vs in-house: kadalasang mas mura pero mas mahigpit ang bank; pwedeng mas flexible ang in-house pero baka mas mahal.'),
('Let your sales executive submit to more than one partner bank.','Ipa-submit sa sales executive sa higit sa isang partner bank.'),
('Visual summary','Buod sa larawan'),
('fill in the worksheet and take the AI Loan Assessment.','sagutan ang worksheet at i-try ang AI Loan Assessment.'),('unit, variant, down payment and term.','unit, variant, down payment at term.'),
('complete the checklist for your employment type.','kumpletuhin ang checklist para sa employment type mo.'),('your sales executive submits to partner banks.','isa-submit ng sales executive sa partner banks.'),
('the bank checks credit, calls you/your employer, may visit your address.','chine-check ng bank ang credit, tatawagan ka/ang employer mo, pwedeng bisitahin ang address mo.'),
('the bank issues approval and terms (timing varies per bank and on how complete your file is).','maglalabas ang bank ng approval at terms (iba-iba ang timing per bank at depende sa pagkakumpleto ng file mo).'),
('sign, settle initial costs if any, drive home.','pirma, bayad ng initial costs kung meron, drive home.'),
('<b>Ready? Two easy next steps:</b>','<b>Ready ka na? Dalawang madaling next step:</b>'),('1) Free AI Car Loan Application Assessment:','1) Libreng AI Car Loan Application Assessment:'),('2) Message me on Messenger:','2) Mag-message sa akin sa Messenger:'),
('>Start my AI Loan Assessment<','>Simulan ang AI Loan Assessment<'),('>Message Richard<','>I-message si Richard<'),
('This guide is general information, not a loan offer. Requirements, ratios and rates vary per bank and may change. Any result from our tools is a Pre-qualified estimate only; all financing is subject to bank approval.','Pangkalahatang impormasyon lamang ang guide na ito, hindi loan offer. Iba-iba ang requirements, ratios at rates per bank at pwedeng magbago. Ang anumang resulta mula sa aming tools ay Pre-qualified estimate lamang; lahat ng financing ay subject to bank approval.')]
for L,reps in (("en",EN),("tl",TL)):
    s=base
    for a,b in reps:
        assert a in s,(L,a[:60]); s=s.replace(a,b)
    for a,b in COMMON: s=s.replace(a,b.replace("@L",L))
    assert "zero" not in s.lower()
    h=R+f"/_src/pdf/_tmp_{L}.html";open(h,"w").write(s)
    subprocess.run(["google-chrome","--headless=new","--no-sandbox","--disable-gpu","--no-pdf-header-footer",f"--print-to-pdf={R}/assets/car-loan-approval-guide-{L}.pdf","file://"+h],stderr=subprocess.DEVNULL,check=True)
    os.remove(h)
# legacy URL from the previous release keeps working (TL version)
shutil.copy(R+"/assets/car-loan-approval-guide-tl.pdf",R+"/assets/car-loan-approval-guide.pdf")
print("pdfs ok")
