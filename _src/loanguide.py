# Evergreen car loan approval guide in 2 languages (FB ad A/B test): TL (Taglish) + EN, gated PDF per language.
# Do NOT promote zero downpayment (dealer restriction). Our results = "Pre-qualified"; financing always "subject to bank approval".
# Keyword research: /workspace/loanapp/zerodp_keywords.md
import json as _j,os as _o
SLUGS={"tl":"paano-ma-approve-sa-car-loan","en":"how-to-get-car-loan-approved-philippines"}
SLUG=SLUGS["tl"]
OLD_SLUG="zero-down-payment-car-loan-requirements"
PDFS={"tl":"/assets/car-loan-approval-guide-tl.pdf","en":"/assets/car-loan-approval-guide-en.pdf"}
LA0="https://mitsubishipromos.online/loan-assessment/"
_SZ=_j.load(open(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),"pdf","ig_sizes.json")))
SRC='''<h2>Sources</h2><ul class="links"><li><a href="https://www.rcbc.com/Content/Forms/FAQs_auto.pdf" target="_blank" rel="noopener">RCBC Auto Loan FAQ (amortization not exceeding 30% of gross monthly income)</a></li><li><a href="https://www.ucpbsavings.com/auto-loan/" target="_blank" rel="noopener">UCPB Savings Auto Loan (30% credit ratio)</a></li><li><a href="https://www.metrobank.com.ph/help/loans/car-loan/loan-application-car-loan" target="_blank" rel="noopener">Metrobank Car Loan application requirements</a></li><li><a href="https://www.bdo.com.ph/personal/loans/auto-loan" target="_blank" rel="noopener">BDO Auto Loan requirements</a></li><li><a href="https://cic.gov.ph/about-your-cic-credit-report/" target="_blank" rel="noopener">CIC: About your credit report</a></li></ul>\n'''

def build(L):
    tl=L=="tl"; T=lambda a,b: a if tl else b
    LA=LA0+"?lang="+L; PDF=PDFS[L]; LANG_TAG=f"car_loan_guide_pdf_{L}"
    def ZCTA(h,p,btn):
        return f'<aside class="lacta zcta"><h2>{h}</h2><p>{p}</p><a class="btn" href="{LA}" data-cta="car-loan-guide-{L}">{btn}</a><p class="zsm">{T("Ang resulta ay Pre-qualified estimate lamang. Ang final financing ay subject to bank approval.","Your result is a Pre-qualified estimate only. Final financing is subject to bank approval.")}</p></aside>\n'
    def ZFORM(i):
        return f'''<form id="{i}" class="zform" novalidate>
<div class="fld"><label for="{i}_name">{T("Buong pangalan","Full name")}</label><input id="{i}_name" autocomplete="name" required><p class="er" id="e_{i}_name" hidden>{T("Pakilagay ang pangalan mo.","Please enter your name.")}</p></div>
<div class="fld"><label for="{i}_email">Email</label><input id="{i}_email" type="email" autocomplete="email" inputmode="email" required><p class="er" id="e_{i}_email" hidden>{T("Pakilagay ang valid na email.","Please enter a valid email.")}</p></div>
<label class="chk"><input type="checkbox" id="{i}_consent" required> <span>{T("Pumapayag ako na kolektahin at i-process ng Mitsubishi SJ Legacy Motors at ni Richard Cuagdan ang aking pangalan at email ayon sa Data Privacy Act of 2012 (RA 10173), para maipadala ang guide na ito at ma-contact ako tungkol sa car financing.","I consent to Mitsubishi SJ Legacy Motors and Richard Cuagdan collecting and processing my name and email under the Data Privacy Act of 2012 (RA 10173) to send this guide and contact me about car financing.")} {T("Basahin ang","See the")} <a href="/privacy/">Privacy Policy</a>. Data Protection Officer: <a href="mailto:richard.cuagdan20@gmail.com">richard.cuagdan20@gmail.com</a>.</span></label><p class="er" id="e_{i}_consent" hidden>{T("Paki-check ang consent box.","Please tick the consent box.")}</p>
<button class="btn" type="submit">{T("I-send ang libreng PDF","Send me the free PDF")}</button>
<div class="zok" hidden><p><b>{T("Salamat!","Thank you!")}</b> {T("Ready na ang guide mo.","Your guide is ready.")}</p><p><a class="btn" href="{PDF}" download target="_blank" rel="noopener" data-pdf>{T("I-download ang PDF guide","Download the PDF guide")}</a></p><p class="zsm">{T("Next step:","Next step:")} <a href="{LA}">{T("i-try ang libreng AI Loan Assessment","take the free AI Loan Assessment")}</a> {T("o","or")} <a href="https://m.me/MitsubishiRDC" rel="noopener">{T("mag-message sa akin sa Messenger","message me on Messenger")}</a>.</p></div>
</form>'''
    GATE=f'''<aside class="zgate" id="zgate"><p class="kick">{T("Libreng PDF","Free PDF")}</p><h2>{T("Kunin ang Car Loan Approval Checklist (PDF)","Get the Car Loan Approval Checklist (PDF)")}</h2><p>{T("Document checklist per employment type, budget/DTI worksheet, bank comparison tips at step-by-step timeline. I-save sa phone, dalhin sa bank.","Document checklist per employment type, a budget/DTI worksheet, bank comparison tips and a step-by-step timeline. Save it on your phone and bring it to the bank.")}</p>{ZFORM("zf")}</aside>\n'''
    POP=f'''<script src="/assets/lead.js" defer></script>
<div class="zpop" id="zpop" role="dialog" aria-modal="true" aria-labelledby="zpop_t" hidden><div class="zpop_in"><button type="button" class="zx" aria-label="{T("Isara","Close")}">×</button><p class="kick">{T("Libreng PDF","Free PDF")}</p><h2 id="zpop_t" class="h3">Car Loan Approval Checklist</h2><p>{T("Libreng download: documents, DTI worksheet at timeline sa iisang PDF.","Free download: documents, DTI worksheet and timeline in one PDF.")}</p>{ZFORM("zf2")}</div></div>
<script>
try{{fbq('track','ViewContent',{{content_name:'car-loan-guide-{L}'}})}}catch(_){{}}
try{{gtag('event','view_guide',{{guide:'car-loan-guide',language:'{L}'}})}}catch(_){{}}
document.addEventListener('DOMContentLoaded',function(){{
var $=function(i){{return document.getElementById(i)}},K='clg_pdf_ok_{L}',pop=$('zpop'),shown=false;
function done(){{['zf','zf2'].forEach(function(i){{var f=$(i);if(!f)return;[].forEach.call(f.children,function(c){{if(!c.classList.contains('zok'))c.hidden=true}});f.querySelector('.zok').hidden=false}})}}
try{{if(localStorage.getItem(K))done()}}catch(_){{}}
['zf','zf2'].forEach(function(i){{var f=$(i);if(!f)return;if(window.AS)AS.init(f);
 f.addEventListener('submit',function(ev){{ev.preventDefault();
  var v=function(x){{return $(i+'_'+x).value.trim()}},n=v('name'),em=v('email');
  var bad=[Lead.err(i+'_name',n.length<2),Lead.err(i+'_email',!/^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(em)),Lead.err(i+'_consent',!$(i+'_consent').checked)];
  if(bad.some(Boolean))return;
  var b=f.querySelector('button[type=submit]');b.disabled=true;b.textContent='{T("Sine-send...","Sending...")}';
  var L=Lead.base('{LANG_TAG}');L.name=n;L.mobile='';L.email=em;L.chosenUnit='Car Loan Guide PDF ({L.upper()})';L.usage='Lead magnet: {LANG_TAG} | Language: {L} | Email: '+em;
  Lead.send(L).then(function(){{try{{localStorage.setItem(K,'1')}}catch(_){{}}
   if(!Lead.skipped()){{try{{if(typeof window.fbq==='function')window.fbq('track','Lead',{{content_name:'car-loan-guide-pdf-{L}'}})}}catch(_){{}}
    try{{if(typeof window.gtag==='function')window.gtag('event','generate_lead',{{unit:'car-loan-guide-pdf-{L}',language:'{L}',value:0,currency:'PHP'}})}}catch(_){{}}}}
   done()}});
 }});
}});
function close(){{pop.hidden=true}}
pop.querySelector('.zx').addEventListener('click',close);pop.addEventListener('click',function(e){{if(e.target===pop)close()}});
document.addEventListener('keydown',function(e){{if(e.key==='Escape'&&!pop.hidden)close()}});
function seen(){{try{{return localStorage.getItem(K)||sessionStorage.getItem('clg_pop')}}catch(_){{return false}}}}
window.addEventListener('scroll',function(){{if(shown||seen())return;var h=document.documentElement,p=(h.scrollTop||document.body.scrollTop)/((h.scrollHeight-h.clientHeight)||1);
 if(p>0.4){{shown=true;try{{sessionStorage.setItem('clg_pop','1')}}catch(_){{}}pop.hidden=false}}}},{{passive:true}});
}});
</script>
'''
    other="en" if tl else "tl"
    if tl:
        FAQ=[("Ano ang tinitingnan ng bank bago i-approve ang car loan?","Pangunahin: ang capacity to pay mo (monthly amortization vs. gross income), ang credit history mo kasama ang CIC record, gaano ka-stable ang trabaho o negosyo mo, at kung kumpleto, consistent at nave-verify ang documents mo."),
("Nakakatulong ba ang mas malaking down payment?","Kadalasan, oo. Mas malaking DP = mas maliit na loan at mas mababang monthly, kaya mas madaling pumasok sa income ratio ng bank. Ang down payment options ay depende sa bank at sa current dealer offer."),
("Magkano ang kailangang sahod para sa car loan?","Walang iisang sagot. Mag-compute pabalik: ang monthly amortization mo ay dapat nasa mga 30% (hanggang mga 35% lang) ng gross monthly income mo. May mga bank din na may minimum gross monthly family income, kaya i-check sa mismong bank."),
("Anong documents ang kailangan kung employed ako?","Kadalasan: application form, valid government ID, Certificate of Employment with compensation, latest payslips at/o ITR o BIR Form 2316, at proof of billing. Iba-iba ang eksaktong listahan per bank."),
("Pwede ba mag-car loan ang self-employed o freelancer?","Oo. Karaniwang hinihingi ang business registration (DTI/SEC), ITR at financial statements, at ilang buwang bank statements. Maraming bank ang naghahanap ng at least 2 taon na profitable ang negosyo."),
("Pwede bang mag-apply ang OFW habang nasa abroad?","Oo. Maghanda ng contract o Certificate of Employment with income, proof of remittance at passport. May mga bank na humihingi ng Special Power of Attorney o representative dito sa Pilipinas."),
("Nakaka-apekto ba ang CIC credit report sa approval?","Oo. Chine-check ng bank ang credit history mo, at ang adverse records gaya ng unpaid loans o past-due credit cards ay pwedeng maging dahilan ng denial. Pwede mong i-request ang sarili mong CIC credit report sa accredited partners ng CIC bago mag-apply."),
("Gaano katagal bago ma-approve ang car loan?","Depende sa bank at sa pagkakumpleto ng documents mo. Ang kumpleto at consistent na documents ang pinakamalaking factor na kontrolado mo. Ako na ang magfo-follow up sa bank para sa'yo."),
("Bakit nade-deny ang car loan?","Karaniwang dahilan: masyadong mataas ang monthly para sa income, adverse credit history, kulang o hindi tugmang documents, maikling tenure sa trabaho o negosyo, at impormasyong hindi ma-verify."),
("Kung na-deny ako, pwede ba ulit mag-apply?","Oo. Ayusin muna ang dahilan: babaan ang loan amount gamit ang mas malaking DP, magdagdag ng co-borrower, kumpletuhin ang documents o linisin ang credit record, tapos mag-apply ulit sa ibang bank o kapag umayos na ang sitwasyon mo.")]
        title="Paano Ma-approve sa Car Loan: Ano ang Tinitingnan ng Bank"
        desc="Paano ma-approve sa car loan? Ang tinitingnan ng bank: 30% income rule, CIC credit, documents per employment type, denial reasons, timeline at libreng PDF."
        answer="Para ma-approve sa car loan, panatilihin ang monthly amortization sa mga 30% ng gross monthly income mo, siguraduhing malinis ang CIC credit record, at magsumite ng kumpleto at consistent na documents para sa employment type mo. Mas malaking DP, co-borrower o mas abot-kayang variant ang nagpapataas ng chances mo. Ang final approval ay laging nasa bank."
        alt="Paano ma-approve sa car loan: guide cover na may official Mitsubishi Xpander photo"
        body=f'''<p>"Sir, ma-a-approve kaya ako sa bank?" Ito ang pinaka-common na tanong sa showroom namin sa SJDM, mula sa mga buyer sa Bulacan hanggang Caloocan, Fairview at buong Metro Manila. Good news: hindi swerte ang bank approval. May sinusundang checklist ang mga bank, at kapag alam mo na ito, makakapaghanda ka na parang pro.</p>
<p>Sa guide na ito: ano ang tinitingnan ng bank, ang documents per employment type, ang income rule na nagdedesisyon sa karamihan ng applications, at ang mga karaniwang dahilan ng denial. Gusto mo ng printable version? Kunin ang libreng PDF checklist sa ibaba.</p>
<h2>Paano naaapektuhan ng down payment ang approval</h2>
<p>Unang tinitingnan ng bank ang monthly amortization mo kumpara sa income mo. Kapag <b>mas malaki ang down payment</b>, mas maliit ang loan at mas mababa ang monthly, kaya mas madaling pumasok sa ratio. Kapag maliit ang down payment, mas malaki ang loan, kaya kailangang kayanin ng income mo ang mas mataas na monthly. Depende sa bank at sa current dealer offer ang down payment options, kaya magtanong muna bago magdesisyon. (Para sa quick tips, basahin ang <a href="/tips/car-loan-approval-tips/">10 car loan approval tips</a>; para sa application steps, basahin ang <a href="/tips/paano-mag-car-loan/">paano mag car loan</a>.)</p>
{ZCTA("Ma-a-approve ka kaya?","Alamin ang chances mo sa loob ng 3 minuto gamit ang libreng AI Car Loan Application Assessment. Walang documents na kailangan.","Simulan ang libreng AI Loan Assessment")}
<h2>Ano ang tinitingnan ng bank bago mag-approve</h2>
<ul class="ticks"><li><b>Capacity to pay</b>: ang gross monthly income mo vs. ang monthly amortization.</li><li><b>Credit standing</b>: ang history mo sa loans at credit cards, kasama ang CIC record.</li><li><b>Stability</b>: gaano ka na katagal sa trabaho, o ilang taon nang kumikita ang negosyo mo.</li><li><b>Kumpleto at consistent</b>: documents na tugma sa isa't isa at nave-verify.</li><li><b>Edad at residency</b>: may minimum at maximum age ang bank at pwedeng itanong kung gaano ka na katagal sa address mo.</li></ul>
<h2>Ang 30–35% income rule (DTI)</h2>
<p>Maraming bank sa Pilipinas ang naglilimita ng monthly car amortization sa mga <b>30% ng gross monthly income</b>. Halimbawa, ang RCBC at UCPB Savings ay may published na 30% ratio. May mga lender na medyo flexible, kaya mag-plano sa <b>30% hanggang 35% lang</b>, at tandaan na kasama sa bilang ang ibang existing loans mo.</p>
<div class="box"><p><b>Quick formula:</b> Gross monthly income × 0.30 = komportableng maximum monthly amortization.</p><p>Halimbawa: ₱60,000 × 0.30 = ₱18,000. Kung mas mataas dito ang monthly ng gusto mong unit, pwedeng lakihan ang DP, magdagdag ng income ng co-borrower, o pumili ng mas abot-kayang variant.</p></div>
<p>Hindi sigurado kung saan ka papasok? Basahin ang <a href="/blog/how-much-car-can-i-afford-philippines/">how much car can I afford</a>.</p>
<h2>Credit standing at ang CIC report mo</h2>
<p>Chine-check ng bank kung may adverse credit records ka, gaya ng past-due credit cards, unpaid loans o bounced checks. Ang Credit Information Corporation (CIC) ang nag-iipon ng data na ito sa ilalim ng RA 9510, at pwede mong i-request ang sarili mong CIC credit report sa accredited partners nila bago ka mag-apply. Kung may mali o outdated, pwede kang mag-file ng dispute sa CIC.</p>
<ul class="ticks"><li>Magbayad ng credit cards on time nang ilang buwan bago mag-apply.</li><li>I-settle o i-restructure ang past-due accounts at itago ang proof.</li><li>Iwasang mag-apply sa maraming loans nang sabay-sabay.</li></ul>
<h2>Requirements per employment type</h2>
<p>Iba-iba ang eksaktong listahan per bank, pero ito ang karaniwang hinihingi (base sa published requirements ng BDO, Metrobank at RCBC):</p>
<h3>Locally employed</h3>
<ul class="ticks"><li>Application form at valid government ID</li><li>Certificate of Employment with compensation (COEC)</li><li>Latest payslips at/o ITR o BIR Form 2316</li><li>Proof of billing</li><li>Kadalasan at least 1 hanggang 2 taon sa current employer, depende sa bank</li></ul>
<h3>Self-employed at business owners</h3>
<ul class="ticks"><li>DTI o SEC registration at business permit</li><li>Latest ITR at financial statements (audited sa ibang bank)</li><li>Recent bank statements (karaniwang ilang buwan)</li><li>Kadalasan mga 2 taon o higit na profitable ang negosyo</li></ul>
<h3>OFWs at seafarers</h3>
<ul class="ticks"><li>Passport at contract o Certificate of Employment with income</li><li>Proof of remittance sa mga nakaraang buwan</li><li>Special Power of Attorney o representative/co-borrower dito sa Pilipinas, kung kailangan</li></ul>
<p>OFW ka? Basahin ang <a href="/blog/ofw-car-buying-guide/">OFW car loan guide</a> para sa buong proseso.</p>
{GATE}
<h2>Bank financing vs in-house financing</h2>
<p>Ang bank financing ay kadalasang mas mababa ang interest pero mas mahigpit ang screening. Ang in-house o captive financing ay pwedeng mas flexible sa requirements pero baka mas mahal sa kabuuan ng term. Detalyado ito sa <a href="/blog/bank-vs-in-house-car-financing-philippines/">bank vs in-house car financing</a>. Tip ko: laging ikumpara ang <b>total amount payable</b>, hindi lang ang monthly.</p>
<h2>Tips para tumaas ang chances mo</h2>
<ul class="ticks"><li><b>Tamang laki ng loan.</b> Pumili ng variant at DP na pasok sa 30% ng income.</li><li><b>Magdagdag ng co-borrower</b>, gaya ng asawa, na pwedeng isama ang income (subject sa rules ng bank).</li><li><b>Ipakita lahat ng income</b> na may proof: allowances, negosyo, rental, remittances.</li><li><b>Consistent na documents.</b> Parehong spelling ng pangalan, address at employer details sa bawat page.</li><li><b>Linisin ang credit</b> bago mag-apply.</li><li><b>Tamang bank.</b> Pwede kong i-submit sa higit sa isang partner bank.</li><li><b>Maging reachable.</b> Sagutin agad ang verification call ng bank.</li></ul>
{ZCTA("Alamin muna bago mag-apply","Chine-check ng AI Loan Assessment ang income, DP at term mo laban sa target unit mo, at nagbibigay ng Pre-qualified estimate sa loob ng ilang minuto.","I-check ang loan readiness ko")}
<h2>Karaniwang dahilan kung bakit nade-deny ang car loan</h2>
<ul class="ticks"><li>Masyadong mataas ang monthly para sa declared income</li><li>Adverse CIC o bank credit records</li><li>Maikling tenure sa trabaho o bagong negosyo</li><li>Kulang, malabo o hindi tugmang documents</li><li>Income na hindi ma-verify (cash income na walang records)</li><li>Hindi nasagot ang verification calls o bagsak sa address check</li></ul>
<h2>Step-by-step timeline</h2>
<ol class="zsteps"><li><b>Assess</b>: i-compute ang 30% ceiling mo at i-try ang <a href="{LA}">AI Loan Assessment</a>.</li><li><b>Choose</b>: pumili ng unit, variant, down payment at term.</li><li><b>Prepare</b>: kumpletuhin ang documents para sa employment type mo.</li><li><b>Submit</b>: ako ang magsa-submit ng application mo sa partner banks.</li><li><b>Verify</b>: chine-check ng bank ang credit mo, tatawagan ka at ang employer mo, at pwedeng bisitahin ang address mo.</li><li><b>Decision</b>: maglalabas ang bank ng approval at terms. Iba-iba ang timing per bank at depende sa pagkakumpleto ng file mo.</li><li><b>Release</b>: pirma, bayad ng initial costs kung meron, at drive home na.</li></ol>
<h2>Saan magsisimula sa Metro Manila at Bulacan</h2>
<p>Nasa Mitsubishi SJ Legacy Motors ako sa San Jose del Monte, Bulacan, at tumutulong ako sa mga buyer sa buong Bulacan at Metro Manila, kasama ang aming Quezon City branch. Pwede mong gawin muna online ang assessment at pag-send ng documents, tapos bumisita kapag ready ka na.</p>
'''+ZCTA("Ready ka na sa next step?","I-try na ang libreng assessment at gagabayan kita sa documents na kailangan para sa sitwasyon mo. Walang pressure.","Simulan ang AI Loan Assessment ko")+SRC+'<p class="muted">Iba-iba ang requirements at ratios per bank at pwedeng magbago. Lahat ng resulta mula sa aming tools ay Pre-qualified estimates lamang; ang financing ay laging subject to bank approval.</p>\n'+POP
        IGC=[("Infographic: ang 4 na tinitingnan ng bank bago mag-approve ng car loan: capacity to pay, credit standing at CIC record, stability ng trabaho o negosyo, at down payment.","Ano ang tinitingnan ng bank: capacity to pay, credit, stability at down payment."),
("Infographic: ang 30–35% income rule. Halimbawa: ₱60,000 gross monthly income × 0.30 = ₱18,000 komportableng maximum monthly amortization.","Halimbawa: ₱60,000 × 0.30 = ₱18,000 max monthly (iba-iba ang ratio per bank)."),
("Infographic: car loan requirements checklist para sa employed, self-employed at OFW.","Karaniwang documents per employment type, base sa published requirements ng BDO, Metrobank at RCBC."),
("Infographic: paghahambing ng bank financing at in-house financing.","Bank vs in-house: ikumpara ang total amount payable, hindi lang ang monthly."),
("Infographic: mga karaniwang dahilan ng car loan denial at paano ayusin ang bawat isa.","Bakit nade-deny ang car loan, at paano ayusin."),
("Infographic: 7-step car loan timeline mula assessment hanggang release.","Mula assessment hanggang release: 7 steps. Iba-iba ang timing per bank.")]
        H2S=["<h2>Ano ang tinitingnan ng bank","<h2>Ang 30–35% income rule","<h2>Requirements per employment type","<h2>Bank financing vs in-house","<h2>Karaniwang dahilan","<h2>Step-by-step timeline"]
    else:
        FAQ=[("What do banks check before approving a car loan?","Mainly your capacity to pay (monthly amortization vs. gross income), your credit history including your CIC record, the stability of your job or business, and whether your documents are complete, consistent and verifiable."),
("Does a bigger down payment help my approval?","Usually, yes. A bigger down payment means a smaller loan and a lower monthly, which makes it easier to stay within the bank's income ratio. Down payment options depend on the bank and the current dealer offer."),
("How much salary do I need for a car loan?","There's no single number. Work backwards: your monthly amortization should stay within roughly 30% (at most about 35%) of your gross monthly income. Some banks also publish a minimum gross monthly family income, so check with the specific bank."),
("What documents do I need for a car loan as an employee?","Usually a filled-out application form, valid government ID, Certificate of Employment with compensation, latest payslips and/or ITR or BIR Form 2316, and proof of billing. Exact lists differ per bank."),
("Can self-employed people or freelancers get a car loan?","Yes. Banks usually look for business registration (DTI/SEC), ITR and financial statements, and several months of bank statements. Many banks look for at least two years of profitable operations."),
("Can OFWs apply for a car loan while abroad?","Yes. Expect to submit a contract or Certificate of Employment with income, proof of remittance and a passport. Some banks need a Special Power of Attorney or a representative in the Philippines."),
("Does my CIC credit report affect car loan approval?","Yes. Banks check your credit history, and adverse records such as unpaid loans or past-due credit cards can lead to denial. You can request your own CIC credit report through CIC's accredited partners before applying."),
("How long does car loan approval take?","It depends on the bank and on how complete your documents are. Complete, consistent documents are the biggest factor you control. I can follow up with the bank for you."),
("Why do car loans get denied?","Common reasons are a monthly that's too high for the income, adverse credit history, incomplete or inconsistent documents, short employment or business tenure, and information that can't be verified."),
("If my car loan is denied, can I apply again?","Yes. Fix the reason first: lower the loan amount with a bigger DP, add a co-borrower, complete your documents or clean up your credit record, then apply with another bank or once your situation improves.")]
        title="How to Get Your Car Loan Approved in the Philippines: What Banks Check"
        desc="How to get a car loan approved in the Philippines: what banks check, the 30% income rule, CIC credit, documents per employment type, denial reasons and a free PDF."
        answer="To get your car loan approved, keep your monthly amortization within about 30% of your gross monthly income, keep a clean CIC credit record, and submit complete, consistent documents for your employment type. A bigger down payment, a co-borrower or a more affordable variant all improve your chances. Final approval always rests with the bank."
        alt="How to get your car loan approved: guide cover with an official Mitsubishi Xpander photo"
        body=f'''<p>"Will the bank approve me?" It's the question I hear most at our showroom in San Jose del Monte, from buyers across Bulacan, Caloocan, Fairview and the rest of Metro Manila. The good news: bank approval isn't luck. Banks follow a fairly predictable checklist, and once you know it, you can prepare like a pro.</p>
<p>This guide covers what banks look at, the documents for each employment type, the income rule behind most decisions, and the most common reasons for denial. Want a printable version? Get the free PDF checklist below.</p>
<h2>How your down payment affects approval</h2>
<p>The bank looks first at your monthly amortization versus your income. A <b>bigger down payment</b> means a smaller loan and a lower monthly, which makes that ratio easier to meet. A smaller down payment means a bigger loan, so your income has to carry a higher monthly. Down payment options depend on the bank and the current dealer offer, so ask before you decide. (For quick tips, see my <a href="/tips/car-loan-approval-tips/">10 car loan approval tips</a>; for the application steps, see <a href="/tips/paano-mag-car-loan/">how to apply for a car loan</a>.)</p>
{ZCTA("Will the bank approve you?","Check your chances in 3 minutes with the free AI Car Loan Application Assessment. No documents needed.","Start the free AI Loan Assessment")}
<h2>What banks check before approving a car loan</h2>
<ul class="ticks"><li><b>Capacity to pay</b>: your gross monthly income vs. the monthly amortization.</li><li><b>Credit standing</b>: your history with loans and credit cards, including your CIC record.</li><li><b>Stability</b>: how long you've been employed or how long your business has been profitable.</li><li><b>Completeness and consistency</b>: documents that match each other and can be verified.</li><li><b>Age and residency</b>: banks set minimum and maximum ages and may ask how long you've lived at your address.</li></ul>
<h2>The 30–35% income rule (DTI)</h2>
<p>Many Philippine banks cap the monthly car amortization at about <b>30% of gross monthly income</b>. RCBC and UCPB Savings, for example, publish a 30% ratio. Some lenders may stretch a little, so plan for <b>30% to 35% at most</b>, and remember that your other existing loans count against that limit.</p>
<div class="box"><p><b>Quick formula:</b> Gross monthly income × 0.30 = comfortable maximum monthly amortization.</p><p>Example: ₱60,000 × 0.30 = ₱18,000. If the monthly for the unit you want is higher, increase the down payment, add a co-borrower's income, or consider a more affordable variant.</p></div>
<p>Not sure where you stand? See <a href="/blog/how-much-car-can-i-afford-philippines/">how much car you can afford on your salary</a>.</p>
<h2>Credit standing and your CIC report</h2>
<p>Banks check for adverse credit records such as past-due credit cards, unpaid loans or bounced checks. The Credit Information Corporation (CIC) collects this data under RA 9510, and you can request your own CIC credit report through CIC's accredited partners before you apply. If anything is wrong or outdated, you can file a dispute with CIC.</p>
<ul class="ticks"><li>Pay your credit cards on time for several months before applying.</li><li>Settle or restructure past-due accounts and keep the proof.</li><li>Avoid applying for several loans at once.</li></ul>
<h2>Requirements per employment type</h2>
<p>Exact lists differ per bank, but these are what most banks ask for (based on published BDO, Metrobank and RCBC requirements):</p>
<h3>Locally employed</h3>
<ul class="ticks"><li>Application form and valid government ID</li><li>Certificate of Employment with compensation (COEC)</li><li>Latest payslips and/or ITR or BIR Form 2316</li><li>Proof of billing</li><li>Often at least 1 to 2 years with your current employer, depending on the bank</li></ul>
<h3>Self-employed and business owners</h3>
<ul class="ticks"><li>DTI or SEC registration and business permit</li><li>Latest ITR and financial statements (audited for some banks)</li><li>Recent bank statements (usually several months)</li><li>Usually about 2 years or more of profitable operations</li></ul>
<h3>OFWs and seafarers</h3>
<ul class="ticks"><li>Passport and contract or Certificate of Employment with income</li><li>Proof of remittance for recent months</li><li>Special Power of Attorney or a representative/co-borrower in the Philippines, if required</li></ul>
<p>Working abroad? Read my <a href="/blog/ofw-car-buying-guide/">OFW car loan guide</a> for the full process.</p>
{GATE}
<h2>Bank financing vs in-house financing</h2>
<p>Bank financing usually has lower interest but stricter screening. In-house or captive financing can be more flexible on requirements but may cost more over the term. I explain the trade-offs in <a href="/blog/bank-vs-in-house-car-financing-philippines/">bank vs in-house car financing</a>. My tip: always compare the <b>total amount payable</b>, not just the monthly.</p>
<h2>Tips to improve your chances</h2>
<ul class="ticks"><li><b>Right-size the loan.</b> Choose the variant and down payment that keep your monthly within 30% of income.</li><li><b>Add a co-borrower</b>, such as a spouse, whose income can be counted (subject to the bank's rules).</li><li><b>Show all income sources</b> with proof: allowances, business income, rental, remittances.</li><li><b>Keep documents consistent.</b> Same name spelling, address and employer details on every page.</li><li><b>Clean up your credit</b> before you apply.</li><li><b>Apply with the right bank.</b> I can submit to more than one partner bank.</li><li><b>Stay reachable.</b> Answer the bank's verification call promptly.</li></ul>
{ZCTA("Know before you apply","The AI Loan Assessment checks your income, down payment and term against your target unit and gives you a Pre-qualified estimate in minutes.","Check my loan readiness")}
<h2>Common reasons car loans get denied</h2>
<ul class="ticks"><li>Monthly amortization too high for the declared income</li><li>Adverse CIC or bank credit records</li><li>Short employment tenure or a new business</li><li>Incomplete, unclear or inconsistent documents</li><li>Income that can't be verified (cash income with no records)</li><li>Missed verification calls or failed address checks</li></ul>
<h2>Step-by-step timeline</h2>
<ol class="zsteps"><li><b>Assess</b>: compute your 30% ceiling and take the <a href="{LA}">AI Loan Assessment</a>.</li><li><b>Choose</b>: pick your unit, variant, down payment and term.</li><li><b>Prepare</b>: complete the documents for your employment type.</li><li><b>Submit</b>: I submit your application to partner banks.</li><li><b>Verify</b>: the bank checks your credit, calls you and your employer, and may visit your address.</li><li><b>Decision</b>: the bank issues its approval and terms. Timing varies per bank and depends on how complete your file is.</li><li><b>Release</b>: sign, settle any initial costs, and drive home.</li></ol>
<h2>Where to start in Metro Manila and Bulacan</h2>
<p>I'm based at Mitsubishi SJ Legacy Motors in San Jose del Monte, Bulacan, and I help buyers across Bulacan and Metro Manila, including our Quezon City branch. You can complete the assessment and send documents online first, then visit when you're ready.</p>
'''+ZCTA("Ready for the next step?","Take the free assessment now and I'll walk you through the documents for your situation. No pressure.","Start my AI Loan Assessment")+SRC+'<p class="muted">Requirements and ratios vary per bank and can change. All results from our tools are Pre-qualified estimates only; financing is always subject to bank approval.</p>\n'+POP
        IGC=[("Infographic: the 4 things banks check before approving a car loan: capacity to pay, credit standing and CIC record, job or business stability, and down payment.","What banks check: capacity to pay, credit, stability and down payment."),
("Infographic: the 30 to 35 percent income rule. Example: ₱60,000 gross monthly income × 0.30 = ₱18,000 comfortable maximum monthly amortization.","Worked example: ₱60,000 × 0.30 = ₱18,000 max monthly (ratios vary per bank)."),
("Infographic: car loan requirements checklist for employed, self-employed and OFW applicants.","Typical documents per employment type, based on published BDO, Metrobank and RCBC requirements."),
("Infographic comparing bank financing and in-house financing for a car loan.","Bank vs in-house: compare the total amount payable, not just the monthly."),
("Infographic: common car loan denial reasons and how to fix each one.","Why car loans get denied, and how to fix each reason."),
("Infographic: 7-step car loan timeline from assessment to release.","From assessment to release in 7 steps. Timing varies per bank.")]
        H2S=["<h2>What banks check","<h2>The 30–35% income rule","<h2>Requirements per employment type","<h2>Bank financing vs in-house","<h2>Common reasons","<h2>Step-by-step timeline"]
    KEYS=["what-banks-check","income-rule","requirements","bank-vs-inhouse","denial-fixes","timeline"]
    for h,k,(a,c) in zip(H2S,KEYS,IGC):
        f=f"cl-{k}-{L}";w,hh=_SZ[f];i=body.index(h)
        body=body[:i]+f'<figure class="fig"><img src="/assets/img/guide/{f}.webp" alt="{a}" width="{w}" height="{hh}" loading="lazy" decoding="async"><figcaption class="zsm">{c}</figcaption></figure>\n'+body[i:]
    return dict(base="blog",car="xpander",slug=SLUGS[L],date="2026-10-23",by="Mitsubishi Sales Executive",img=f"guide/cl-hero-{L}",alt=alt,title=title,desc=desc,answer=answer,faq=FAQ,body=body,lang=L)
POSTS_L=[build("en"),build("tl")]  # EN = main version (listed first)
SWITCH={"en":'<p class="zlang"><a href="/blog/paano-ma-approve-sa-car-loan/" hreflang="fil-PH" lang="fil">Basahin sa Taglish →</a></p>',"tl":'<p class="zlang"><a href="/blog/how-to-get-car-loan-approved-philippines/" hreflang="en-PH" lang="en">Read in English →</a></p>'}
