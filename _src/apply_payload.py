#!/usr/bin/env python3
"""Apply a website-editor payload to _src/site.json and _src/optionAB_oct2026.json."""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_src")

def as_int(v, name, allow_none=False):
    if v in (None, "") and allow_none:
        return None
    if isinstance(v, bool):
        raise ValueError(name)
    try:
        return int(v)
    except (TypeError, ValueError) as err:
        raise ValueError(f"{name} must be a whole number") from err

def apply(payload):
    if not isinstance(payload, dict):
        raise ValueError("payload must be an object")
    site = payload.get("site")
    ab = payload.get("optionAB")
    if not isinstance(site, dict):
        raise ValueError("site is required")
    if not isinstance(ab, list) or not ab:
        raise ValueError("optionAB is required")
    for k in ("phone_e164", "phone_display", "email", "facebook", "messenger", "hours"):
        if not str(site.get(k) or "").strip():
            raise ValueError("missing " + k)
    if not str(site.get("phone_e164","")).startswith("+"):
        raise ValueError("phone_e164 must start with +")
    labels = site.get("promo_labels") or {}
    if not str(labels.get("lowest_dp") or "").strip() or not str(labels.get("lowest_monthly") or "").strip():
        raise ValueError("promo option names are required")
    pr = site.get("promo") or {}
    site["promo"] = {
        "year": as_int(pr.get("year"), "promo.year"),
        "month": as_int(pr.get("month"), "promo.month"),
        "updated": str(pr.get("updated") or "").strip(),
    }
    if not (1 <= site["promo"]["month"] <= 12):
        raise ValueError("promo.month must be 1-12")
    if site["promo"]["year"] < 2020:
        raise ValueError("promo.year looks invalid")
    if not isinstance(site.get("inclusions"), list) or not site["inclusions"]:
        raise ValueError("inclusions are required")
    if not isinstance(site.get("freebies"), list) or not site["freebies"]:
        raise ValueError("freebies are required")
    for r in ab:
        if not isinstance(r, dict) or not r.get("unit") or not r.get("family"):
            raise ValueError("each promo row needs family and unit")
        for k in ("srp", "a_dp", "a_mo", "b_dp", "b_mo"):
            r[k] = as_int(r.get(k), f"{r.get('unit')} {k}")
            if r[k] < 0:
                raise ValueError(f"{r.get('unit')} {k} cannot be negative")
        r["fuel"] = as_int(r.get("fuel"), f"{r.get('unit')} fuel", allow_none=True)
        if r["fuel"] is not None and r["fuel"] < 0:
            raise ValueError(f"{r.get('unit')} fuel cannot be negative")
        r["flags"] = r.get("flags") or ""
    site_path = os.path.join(SRC, "site.json")
    ab_path = os.path.join(SRC, "optionAB_oct2026.json")
    with open(site_path, "w", encoding="utf-8") as f:
        json.dump(site, f, indent=2, ensure_ascii=False)
        f.write("\n")
    with open(ab_path, "w", encoding="utf-8") as f:
        json.dump(ab, f, indent=2, ensure_ascii=False)
        f.write("\n")
    return site_path, ab_path

if __name__ == "__main__":
    raw = os.environ.get("CLIENT_PAYLOAD")
    payload = json.loads(raw) if raw else json.load(sys.stdin)
    if isinstance(payload, str):
        payload = json.loads(payload)
    paths = apply(payload)
    print("wrote", paths[0], paths[1])
