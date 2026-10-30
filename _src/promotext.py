# Promo figures for article text, generated from data.py (which reads _src/optionAB_oct2026.json). Richard 2026-10-30.
import sys,os; sys.path.insert(0,os.path.dirname(__file__))
from data import MODELS
V={v["id"]:v for m in MODELS for v in m["variants"]}
SHORT={"l300":"L300 Dual AC","l300cc":"L300 Cab & Chassis","xcross":"Xpander Cross","tritongxat":"Triton GX AT","trath":"Triton Athlete 4WD AT",
 "mglxmt":"Montero Sport GLX MT","dgtm":"Destinator GT (Monotone)","dgtt":"Destinator GT (Two-Tone)"}
def p(n): return "₱"+format(n,",")
def k(n): return f"₱{n/1000:.1f}K"
def srp(v): return v["srp"] or v["ab"]["srp"]
def zero_ids(): return sorted([i for i,v in V.items() if v.get("ab",{}).get("a_dp")==0],key=lambda i:V[i]["ab"]["a_mo"])
def zrows(income_fmt="K"):
    out=[]
    for i in zero_ids():
        mo=V[i]["ab"]["a_mo"]; lo,hi=int(mo/0.35/100+0.5)*100,int(mo/0.30/100+0.5)*100
        out.append((SHORT.get(i,V[i]["n"]),p(srp(V[i])),p(mo),f"{k(lo)}–{k(hi)}" if income_fmt=="K" else f"{p(lo)} – {p(hi)}"))
    return out
def zrows3(): return [(a,c,d) for a,b,c,d in zrows()]
def amo(i): return V[i]["ab"]["a_mo"]
