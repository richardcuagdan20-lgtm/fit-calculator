"""Generate the private /update/ website editor (noindex, not in public nav)."""
import json, os
from data import SITE, MODELS

GOOGLE_CLIENT_ID = "1028793506920-3arv7cdvlgglr0v9r2kcoobj1c3npofp.apps.googleusercontent.com"

FAM = [
    ("Mirage Hatchback", "mirage", "Mirage"),
    ("Mirage G4", "mirage-g4", "Mirage G4"),
    ("Xpander", "xpander", "Xpander"),
    ("Xpander Cross", "xpander-cross", "Xpander Cross"),
    ("Xforce", "xforce", "Xforce"),
    ("Destinator", "destinator", "Destinator"),
    ("Triton", "triton", "Triton"),
    ("Montero Sport", "montero-sport", "Montero Sport"),
    ("L300", "l300", "L300"),
    ("Versa Van", "versa-van", "Versa Van"),
    ("Outlander PHEV", "outlander-phev", "Outlander PHEV"),
]

def write(R):
    src = os.path.dirname(os.path.abspath(__file__))
    ab = json.load(open(os.path.join(src, "optionAB_oct2026.json"), encoding="utf-8"))
    models = []
    for m in MODELS:
        models.append({
            "slug": m["slug"],
            "name": m["name"],
            "cat": m["cat"],
            "blurb": m.get("blurb") or "",
            "who": m.get("who") or "",
            "specs": [list(x) for x in (m.get("specs") or [])],
        })
    site = json.loads(json.dumps(SITE))
    site["models"] = {m["slug"]: {k: m[k] for k in ("name", "cat", "blurb", "who", "specs")} for m in models}
    payload = {
        "site": site,
        "models": models,
        "optionAB": ab,
        "families": [{"family": f, "slug": s, "name": n} for f, s, n in FAM],
    }
    raw = json.dumps(payload, ensure_ascii=False).replace("<", "\\u003c")
    tmpl = open(os.path.join(src, "update_page.html"), encoding="utf-8").read()
    html = tmpl.replace("__PAYLOAD__", raw).replace("__GOOGLE_CLIENT_ID__", GOOGLE_CLIENT_ID)
    out = os.path.join(R, "update")
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(html)
    robots = os.path.join(out, "robots.txt")
    open(robots, "w").write("User-agent: *\nDisallow: /\n")
