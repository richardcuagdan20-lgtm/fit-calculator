# ---------- /apply/ : Official Application Form (static; leads via /assets/lead.js). exec'd from build.py after loanapp.py
AFU=[]
for m in MODELS:
    for v in m["variants"]:
        price=v["srp"] or (v["promo"] or {}).get("srp")
        AFU.append({"id":v["id"],"slug":m["slug"],"model":m["name"],"n":v["n"],"price":price,"colors":_cl(v["id"]),
                    "opts":[{"dp":_dp(l),"mo":mo} for l,mo in (v["promo"] or {}).get("opts",[])]})
def O(v,tl,en=None): en=en or tl; return f'<option value="{e(v)}" data-tl="{e(tl)}" data-en="{e(en)}">{e(en)}</option>'
def SEL(i,lbl,opts,req=True,extra=""):
    return f'<div class="fld"><label for="{i}">{lbl}{" *" if req else ""}</label><select id="{i}" name="{i}"{" required" if req else ""}{extra}><option value="" data-tl="Pumili" data-en="Select">Pumili</option>{"".join(opts)}</select></div>'
def INP(i,lbl,t="text",req=True,extra=""):
    return f'<div class="fld"><label for="{i}">{lbl}{" *" if req else ""}</label><input type="{t}" id="{i}" name="{i}"{" required" if req else ""}{extra}></div>'
def YM(i,lbl):
    return (f'<div class="fld"><label>{lbl} *</label><div class="af-ym"><select id="{i}_y" name="{i}_y" required aria-label="Years"><option value="" data-tl="Taon" data-en="Years">Taon</option>'
            +"".join(f'<option value="{y}">{y}{"+" if y==40 else ""}</option>' for y in range(0,41))+f'</select><select id="{i}_m" name="{i}_m" aria-label="Months"><option value="0" data-tl="0 buwan" data-en="0 months">0 buwan</option>'
            +"".join(f'<option value="{x}" data-tl="{x} buwan" data-en="{x} month{"s" if x>1 else ""}">{x} buwan</option>' for x in range(1,12))+'</select></div></div>')
MOB=' inputmode="tel" autocomplete="tel" placeholder="09XX XXX XXXX" data-v="mobile"'
NUM=' inputmode="decimal" min="0" step="500" data-v="num"'
CIV=[O("single","Single"),O("married","Married"),O("widowed","Widowed"),O("separated","Separated")]
REL=[O("parent","Magulang","Parent"),O("sibling","Kapatid","Sibling"),O("relative","Kamag-anak","Relative"),O("friend","Kaibigan","Friend"),O("coworker","Katrabaho","Co-worker"),O("neighbor","Kapitbahay","Neighbor"),O("other","Iba pa","Other")]
EMPT=[O("employed","Employed (may employer)","Employed"),O("business_owner","Business owner"),O("ofw","OFW (land-based)","OFW (land-based)"),O("seafarer","Seafarer"),O("freelancer","Freelancer / VA"),O("pensioner","Pensioner"),O("other","Iba pa","Other")]
def REF(n):
    return (f'<fieldset class="af-sub"><legend>{B("Reference","Reference")} {n}</legend>'+INP(f"ref{n}_name",B("Buong pangalan","Full name"),extra=' autocomplete="off"')
            +SEL(f"ref{n}_rel",B("Relasyon sa iyo","Relationship to you"),REL)+INP(f"ref{n}_mobile","Mobile",t="tel",extra=MOB.replace('autocomplete="tel"','autocomplete="off"'))
            +INP(f"ref{n}_addr",B("Address (city / municipality)","Address (city / municipality)"),extra=' autocomplete="off"')+'</fieldset>')
AF_CSS='''<style>.af-off{display:none!important}.af-prog{position:sticky;top:0;z-index:5;background:#f4f4f5;padding:8px 0 10px;margin-bottom:8px}.af-pl{margin:0 0 6px;font-size:15px}.af-bar{height:8px;background:#e4e4e7;border-radius:99px;overflow:hidden}.af-bar span{display:block;height:100%;background:#E60012;width:0;transition:width .25s}.af-nav{margin:6px 0 18px}.af-navb{display:flex;gap:10px}.af-navb .btn{flex:1;min-height:52px;font-size:17px}.af-rv{border:1px solid var(--ln);border-radius:12px;padding:10px 12px;margin-bottom:10px}.af-rv h3{display:flex;justify-content:space-between;align-items:center;font-size:16px;margin:0 0 6px}.af-rv h3 button{background:none;border:0;color:#E60012;font-weight:700;font-size:15px;padding:6px;cursor:pointer;text-decoration:underline}.af-rv dl{margin:0;display:grid;grid-template-columns:42% 1fr;gap:4px 8px;font-size:14px}.af-rv dt{color:#52525b}.af-rv dd{margin:0;font-weight:600;word-break:break-word}.la-docs li.af-rq{display:block}.af-rq .af-rn{font-weight:600;display:block;margin-bottom:8px}.af-st{display:flex;gap:8px;flex-wrap:wrap}.af-st label{flex:1 1 140px;border:1px solid var(--ln);border-radius:10px;padding:10px;min-height:44px;white-space:normal!important;font-size:14px}.af-st label:has(input:checked){border-color:#E60012;background:#fff1f2}.af-fl{margin-top:8px;font-size:14px}.af-fl input{width:auto!important;height:auto!important;max-width:100%}.af-cam{display:flex;gap:8px;flex-wrap:wrap}.af-cam label{flex:1 1 130px;border:1px dashed #a1a1aa;border-radius:10px;padding:10px;text-align:center;font-weight:600;font-size:14px;cursor:pointer;min-height:44px;position:relative}.af-cam input{position:absolute;width:1px!important;height:1px!important;opacity:0}.af-fn{font-size:13px;color:#555;margin:4px 0 0}
.af form{display:block}.af fieldset{border:0;margin:0 0 6px;padding:0}.af .la-card{margin-bottom:16px}.af h2.h3{margin-top:0}.af .fld select,.af .fld input[type=date],.af .fld input[type=number],.af .fld textarea{width:100%;padding:12px;border:1px solid var(--ln);border-radius:12px;font:inherit;background:#fff}
.af-sub{border:1px solid var(--ln)!important;border-radius:14px;padding:12px!important;margin:10px 0!important}.af-sub legend{font-weight:700;padding:0 6px}
.af-ym{display:flex;gap:8px}.af-ym select{flex:1}.af-g2{display:grid;grid-template-columns:1fr 1fr;gap:0 12px}@media(max-width:520px){.af-g2{grid-template-columns:1fr}}
.af [aria-invalid=true]{border-color:#c00!important;background:#fff5f5}.af .er{color:#b91c1c;font-size:14px;margin:4px 0 0}.af-hint{font-size:14px;color:#52525b;margin:4px 0 0}
.af-pre{background:#ecfdf5;border:1px solid #a7f3d0;border-radius:12px;padding:10px 12px;margin:0 0 14px;font-size:15px}.af-ref{font-size:30px;font-weight:800;letter-spacing:2px;background:#0b0b0c;color:#fff;border-radius:14px;padding:12px;text-align:center;margin:10px 0}
.af-tu{display:flex;gap:8px;margin:0 0 6px}.af-tu label{font-weight:500;display:flex;gap:6px;align-items:center;margin:0}.af-big{width:100%;font-size:18px;padding:16px!important;justify-content:center}
.cta{display:none!important}.af-errsum{background:#fef2f2;border:1px solid #fecaca;border-radius:12px;padding:10px 12px;color:#991b1b}
</style>'''
AF_BODY=f'''<section class="la-hero"><div class="w">
<div class="la-lang" role="group" aria-label="Language / Wika"><button type="button" data-setlang="en">English</button><button type="button" data-setlang="tl">Tagalog / Taglish</button></div>
<p class="kick" style="color:#fca5a5">San Juan Motors · Mitsubishi</p>
<h1>Official Application Form</h1>
<p class="lead">{B("Car loan application para sa iyong Mitsubishi. Mga 8–10 minuto. Ang final decision ay sa bank; ire-review namin ang application mo at tutulungan ka ni Fina sa documents.","Car loan application for your Mitsubishi. About 8–10 minutes. The final decision is the bank's; we will review your application and Fina will help you with documents.")}</p>
<div class="rxm"><picture><source type="image/webp" srcset="/assets/img/richard/xpander-avatar-320.webp"><img src="/assets/img/richard/xpander-avatar-320.jpg" alt="Richard Cuagdan, Mitsubishi Car Sales Executive" width="320" height="320" loading="lazy" decoding="async"></picture><p class="rx1">{B("Ang sales executive mo: <b>Richard Cuagdan</b>","Your sales executive: <b>Richard Cuagdan</b>")}</p></div>
</div></section>
<section class="sec ccsec"><div class="w"><details class="ccwrap" id="calc"><summary>Not sure about the monthly yet? <b>Estimate it first</b></summary>{CALC("apply")}</details></div></section>
<script>if(location.hash==="#calc")document.getElementById("calc").open=true;addEventListener("hashchange",function(){{if(location.hash==="#calc")document.getElementById("calc").open=true}})</script>
<section class="la af"><div class="w" style="padding-top:18px">
<div id="af-wrap"><p id="af-pre" class="af-pre" hidden>{B("✓ Na-fill na namin ang ilang sagot mula sa assessment mo. Pakicheck at kumpletuhin.","✓ We pre-filled some answers from your assessment. Please check and complete.")}</p>
<form id="af" novalidate>
<div class="af-prog" id="af-prog" aria-live="polite"><p class="af-pl"><b id="af-pn"></b> <span id="af-pt"></span></p><div class="af-bar"><span id="af-pb"></span></div></div>
<div class="la-card" data-step="1"><h2 class="h3"><span data-num></span>{B("Unit at payment plan","Unit and payment plan")}</h2>
<div class="af-g2">{SEL("model","Model",[])}{SEL("variant","Variant",[])}</div>
{SEL("color",B("Color (subject sa availability)","Color (subject to availability)"),[])}
<p id="af-price" class="af-hint"></p>
{INP("dp",B("Down payment (₱)","Down payment (₱)"),t="number",extra=' inputmode="numeric" min="0" step="1000" data-v="num"')}<p id="af-dphint" class="af-hint"></p>
<div class="fld"><label>{B("Term (ilang taon babayaran)","Term (years to pay)")} *</label><div class="af-tu"><label><input type="radio" name="tu" value="y" checked> {B("Taon","Years")}</label><label><input type="radio" name="tu" value="m"> {B("Buwan","Months")}</label></div>
<select id="term_y" aria-label="Term (years)">{"".join(f'<option value="{n*12}" data-tl="{n} taon ({n*12} buwan)" data-en="{n} year{"s" if n>1 else ""} ({n*12} months)"{" selected" if n==5 else ""}>{n} taon</option>' for n in range(1,6))}</select>
<select id="term_m" aria-label="Term (months)" hidden>{"".join(f'<option value="{n}" data-tl="{n} buwan" data-en="{n} months"{" selected" if n==60 else ""}>{n}</option>' for n in (12,18,24,30,36,42,48,54,60))}</select></div>
<p id="af-plan" class="af-pre" hidden></p>
<div class="af-g2">{SEL("purpose",B("Gagamitin para sa","Vehicle use"),[O("personal","Personal / family"),O("business","Business"),O("tnvs","Grab / TNVS"),O("other","Iba pa","Other")])}
{SEL("bank",B("Preferred bank","Preferred bank"),[O("no_preference","Wala, kayo na bahala","No preference"),O("MMPF","Mitsubishi Motors Finance PH")]+[O(x,x) for x in ["BPI","BDO","Metrobank","Security Bank","PSBank","RCBC","EastWest"]])}</div>
{SEL("source",B("Paano mo kami nahanap?","How did you find us?"),[O("facebook","Facebook"),O("google","Google"),O("referral","Referral"),O("walk_in","Walk-in"),O("other","Iba pa","Other")],req=False)}
</div>
<div class="la-card" data-step="2"><h2 class="h3"><span data-num></span>{B("Personal na impormasyon","Personal information")}</h2>
<p class="af-hint">{B("Ayon sa iyong valid ID.","As shown on your valid ID.")}</p>
<div class="af-g2">{INP("first",B("First name","First name"),extra=' autocomplete="given-name"')}{INP("middle",B("Middle name","Middle name"),req=False,extra=' autocomplete="additional-name"')}{INP("last",B("Last name","Last name"),extra=' autocomplete="family-name"')}{INP("suffix",B("Suffix (Jr., III)","Suffix (Jr., III)"),req=False)}</div>
<div class="af-g2">{INP("dob",B("Birthday","Date of birth"),t="date",extra=' data-v="dob"')}{SEL("gender","Gender",[O("female","Babae","Female"),O("male","Lalaki","Male"),O("na","Ayokong sabihin","Prefer not to say")],req=False)}
{SEL("civil",B("Civil status","Civil status"),CIV)}{INP("nationality",B("Nationality","Nationality"),extra=' value="Filipino"')}
{INP("dependents",B("Bilang ng dependents","Number of dependents"),t="number",extra=' inputmode="numeric" min="0" max="20" value="0" data-v="num"')}{INP("tin","TIN",req=False,extra=' inputmode="numeric" placeholder="###-###-###-###" autocomplete="off"')}
</div>
</div>
<div class="la-card" data-step="3"><h2 class="h3"><span data-num></span>{B("Address at contact","Address and contact")}</h2>
<div class="af-g2">{INP("mobile","Mobile number",t="tel",extra=MOB)}{INP("email","Email",t="email",req=False,extra=' autocomplete="email" data-v="email"')}</div>
<fieldset class="af-sub"><legend>{B("Kasalukuyang address","Current address")}</legend>
{INP("addr1",B("House no. / street / subdivision","House no. / street / subdivision"),extra=' autocomplete="address-line1"')}<div class="af-g2">{INP("brgy","Barangay")}{INP("city",B("City / municipality","City / municipality"),extra=' autocomplete="address-level2"')}{INP("prov","Province",extra=' autocomplete="address-level1" value="Bulacan"')}{INP("zip","ZIP",req=False,extra=' inputmode="numeric" autocomplete="postal-code"')}</div>
{YM("stay",B("Gaano ka na katagal nakatira dito?","How long have you lived here?"))}
{SEL("res",B("Ang bahay ay","Home is"),[O("owned","Sariling bahay (owned)","Owned"),O("mortgaged","Hinuhulugan (mortgaged)","Mortgaged"),O("rented","Rented / nangungupahan","Rented"),O("living_with_relatives","Kasama ang family","Living with family"),O("company_provided","Company-provided")])}
<div id="af-rentw" class="fld" hidden>{INP("rent",B("Buwanang upa (₱)","Monthly rent (₱)"),t="number",req=False,extra=NUM)}</div></fieldset>
</div>
<div class="la-card" data-step="4"><h2 class="h3"><span data-num></span>{B("Trabaho / negosyo at income","Employment / business and income")}</h2>
{SEL("emp",B("Source of income","Source of income"),EMPT)}
<div data-show="emp:employed">{SEL("estat",B("Employment status","Employment status"),[O("permanent","Permanent / regular"),O("probationary","Probationary"),O("contractual","Contractual")])}</div>
<div data-show="emp:employed,business_owner,ofw,seafarer,freelancer,other">
{INP("employer",B("Pangalan ng employer / negosyo / agency","Employer / business / agency name"),extra=' autocomplete="organization"')}
<div class="af-g2">{INP("position",B("Position / trabaho","Position / job title"),extra=' autocomplete="organization-title"')}{INP("nature",B("Nature of business ng company","Company's nature of business"),extra=' placeholder="hal. BPO, retail, construction"')}</div>
{YM("ten",B("Gaano ka na katagal dito?","How long have you been here?"))}
{INP("oaddr",B("Address ng office / negosyo","Office / business address"))}<div class="af-g2">{INP("otel",B("Office telephone / mobile","Office phone / mobile"),req=False,extra=' inputmode="tel"')}{INP("oemail",B("Office email","Office email"),t="email",req=False,extra=' data-v="email"')}</div></div>
<fieldset class="af-sub" data-show="emp:ofw,seafarer"><legend>{B("OFW / Seafarer contract","OFW / Seafarer contract")}</legend>
<div class="af-g2">{INP("ofw_country",B("Bansa / vessel","Country / vessel"))}{INP("ofw_agency",B("Manning / recruitment agency","Manning / recruitment agency"),req=False)}
{INP("ofw_start",B("Contract start","Contract start"),t="date")}{INP("ofw_end",B("Contract end","Contract end"),t="date")}</div>
{SEL("ofw_remit",B("May 3–6 months remittance proof?","Do you have 3–6 months remittance proof?"),[O("yes","Oo","Yes"),O("no","Wala pa","Not yet")])}
<p class="fl"><b>{B("Attorney-in-fact (AIF) dito sa PH","Attorney-in-fact (AIF) in the PH")}</b></p>
<div class="af-g2">{INP("aif_name",B("Pangalan ng AIF","AIF name"))}{SEL("aif_rel",B("Relasyon","Relationship"),[O("spouse","Asawa","Spouse")]+REL)}{INP("aif_mobile","AIF mobile",t="tel",extra=MOB)}</div></fieldset>
<div class="af-g2">{INP("gross",B("Gross monthly income (₱)","Gross monthly income (₱)"),t="number",extra=NUM)}{INP("otherinc",B("Iba pang household income (₱/buwan)","Other household income (₱/month)"),t="number",req=False,extra=NUM)}</div>
{INP("oblig",B("Kabuuang buwanang hulog sa ibang loans / credit card minimum (₱)","Total monthly payments on other loans / credit card minimum (₱)"),t="number",extra=NUM+' value="0"')}
<div class="af-g2">{INP("mainbank",B("Main bank","Main bank"),req=False,extra=' placeholder="hal. BDO, BPI, GCash"')}{SEL("car",B("May sasakyan ka na ba?","Do you own a vehicle now?"),[O("none","Wala","None"),O("owned_paid","Meron, fully paid","Yes, fully paid"),O("owned_financed","Meron, hinuhulugan pa","Yes, still financed")],req=False)}</div>
</div>
<div class="la-card" data-step="5" data-show="civil:married"><h2 class="h3"><span data-num></span>{B("Asawa (spouse)","Spouse")}</h2>
<div class="af-g2">{INP("sp_name",B("Buong pangalan","Full name"))}{INP("sp_dob",B("Birthday","Date of birth"),t="date",req=False)}{INP("sp_mobile","Mobile",t="tel",req=False,extra=MOB)}
{SEL("sp_emp",B("Source of income","Source of income"),[O("none","Walang income","No income")]+EMPT)}{INP("sp_employer",B("Employer / negosyo","Employer / business"),req=False)}{INP("sp_inc",B("Gross monthly income (₱)","Gross monthly income (₱)"),t="number",req=False,extra=NUM)}</div></div>
<div class="la-card" data-step="5"><h2 class="h3"><span data-num></span>{B("Co-maker at references","Co-maker and references")}</h2>
{SEL("cm",B("May co-maker / co-borrower ka ba?","Do you have a co-maker / co-borrower?"),[O("no","Wala","No"),O("spouse","Oo, ang asawa ko (nasa itaas)","Yes, my spouse (above)"),O("yes","Oo, ibang tao","Yes, someone else")])}
<fieldset class="af-sub" data-show="cm:yes"><legend>Co-maker</legend><div class="af-g2">{INP("cm_name",B("Buong pangalan","Full name"))}{SEL("cm_rel",B("Relasyon","Relationship"),REL)}{INP("cm_mobile","Mobile",t="tel",extra=MOB)}{INP("cm_dob",B("Birthday","Date of birth"),t="date",req=False)}
{SEL("cm_emp",B("Source of income","Source of income"),EMPT)}{INP("cm_inc",B("Gross monthly income (₱)","Gross monthly income (₱)"),t="number",extra=NUM)}</div>{INP("cm_addr","Address",req=False)}</fieldset>
<p class="af-hint">{B("2 personal references: hindi kasama sa bahay, at mas maganda kung hindi kamag-anak.","2 personal references: not living with you, preferably not relatives.")}</p>
{REF(1)}{REF(2)}
</div>
<div class="la-card" data-step="6"><h2 class="h3"><span data-num></span>{B("Requirements checklist","Requirements checklist")}</h2>
<p>{B("Lalabas dito ang requirements batay sa employment type mo. Sa bawat isa, piliin kung <b>meron ka na</b> o <b>susunod na lang</b> (to follow). Okay lang kung kulang pa; pwede mong ipadala ang kulang na documents kay Richard sa Messenger pagkatapos mong mag-submit.","The requirements below are based on your employment type. For each one, choose whether you <b>already have it</b> or <b>will submit it later</b> (to follow). It's okay if some are missing; you can send them to Richard on Messenger after you submit.")}</p>
<p class="af-up" hidden>{B("Pwede mong i-upload ang malinaw na photo o PDF (max 5 files, 5MB bawat isa).","You can upload a clear photo or PDF (max 5 files, 5MB each).")}</p>
<ul class="la-docs" id="af-docs"></ul><p class="la-cnt" id="af-cnt"></p><p class="muted small">🔒 {B("Privacy: ang impormasyon at documents mo ay gagamitin lang para sa loan processing ng application mo, alinsunod sa Data Privacy Act.","Privacy: your information and documents are used only to process your loan application, in line with the Data Privacy Act.")}</p></div>
<div class="la-card" data-step="7"><h2 class="h3">{B("Review at submit","Review and submit")}</h2><p class="af-hint">{B("Pakicheck ang mga sagot mo. I-tap ang Edit para baguhin.","Please check your answers. Tap Edit to change anything.")}</p><div id="af-review"></div></div>
<div class="la-card" data-step="7"><h2 class="h3">Data Privacy Consent</h2><div class="la-cons" tabindex="0">{LA_CONSENT}</div>
<label class="chk"><input type="checkbox" id="consent" name="consent"> <span>{B("Sumasang-ayon ako at kinukumpirma kong tama ang lahat ng impormasyon sa form na ito.","I agree, and I confirm that all information in this form is true and correct.")}</span></label><p class="er" id="e_consent" hidden>{B("Kailangan ang consent para ma-submit.","Consent is required to submit.")}</p>
<div id="af-errsum" class="af-errsum" hidden role="alert">{B("May kulang o mali sa form. Pakicheck ang mga naka-pula.","Some fields are missing or invalid. Please check the fields in red.")}</div>
<button class="btn af-big" type="submit" id="af-btn" style="margin-top:12px">{B("I-submit ang application","Submit application")}</button>
<p class="muted small">{B("Pre-qualification at review lang ito, hindi pa bank decision. Subject sa bank evaluation at promo validity.","This is for pre-qualification and review only, not yet a bank decision. Subject to bank evaluation and promo validity.")} ({e(NOTE)})</p></div>
<div class="af-nav" id="af-nav"><p class="er" id="af-serr" hidden role="alert">{B("May kulang o mali sa step na ito. Pakicheck ang mga naka-pula.","Some fields in this step are missing or invalid. Please check the fields in red.")}</p><div class="af-navb"><button type="button" class="btn ghost" id="af-back">← {B("Bumalik","Back")}</button><button type="button" class="btn" id="af-next">{B("Next","Next")} →</button></div><p class="af-hint" id="af-saved" hidden>💾 {B("Naka-save ang sagot mo sa device na ito habang hindi pa nasa-submit.","Your answers are saved on this device until you submit.")}</p></div>
</form></div>
<div id="af-done" class="la-card" hidden aria-live="polite"></div>
</div></section>
<script type="application/json" id="af-units">{json.dumps(AFU,ensure_ascii=False)}</script>
<script src="/assets/lead.js" defer></script>
<script src="/assets/apply-form.js" defer></script>'''
page("/apply/","Official Application Form | Mitsubishi Motors - San Juan Motors",
 "Official car loan Application Form for Mitsubishi at San Juan Motors, San Jose del Monte: personal, employment, co-maker, references and unit details. Tagalog or English.",
 LA_CSS+AF_CSS+AF_BODY, crumbs=[("/","Home"),("/apply/","Official Application Form")])
_ap=R+"/apply/index.html"; _s=open(_ap).read()
_s=_s.replace('src="/assets/apply-form.js"',f'src="/assets/apply-form.js?v={_vh("/assets/apply-form.js")}"').replace('src="/assets/lead.js"',f'src="/assets/lead.js?v={_vh("/assets/lead.js")}"').replace('href="/assets/site.css"',f'href="/assets/site.css?v={_vh("/assets/site.css")}"')
open(_ap,'w').write(_s)
