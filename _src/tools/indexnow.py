#!/usr/bin/env python3
"""Submit sitemap URLs to IndexNow (Bing, Yandex, Seznam, Naver...; shared via api.indexnow.org).
Run ONLY after the pages are live on main:  python3 _src/tools/indexnow.py [--dry-run] [url ...]
The key file /<key>.txt at the site root must be live (https://www.mitsubishi-sjdm.com/<key>.txt)."""
import glob, json, os, re, sys, urllib.request
ROOT=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HOST="www.mitsubishi-sjdm.com"; ENDPOINT="https://api.indexnow.org/indexnow"
def key():
    ks=[os.path.basename(p)[:-4] for p in glob.glob(os.path.join(ROOT,"*.txt")) if re.fullmatch(r"[0-9a-f]{32}\.txt",os.path.basename(p))]
    if len(ks)!=1: sys.exit(f"expected exactly one IndexNow key file at site root, found {len(ks)}")
    return ks[0]
def urls():
    return re.findall(r"<loc>([^<]+)</loc>",open(os.path.join(ROOT,"sitemap.xml")).read())
def main():
    dry="--dry-run" in sys.argv; args=[a for a in sys.argv[1:] if not a.startswith("--")]
    k=key(); u=args or urls()
    body={"host":HOST,"key":k,"keyLocation":f"https://{HOST}/{k}.txt","urlList":u[:10000]}
    print(f"{len(body['urlList'])} URLs -> {ENDPOINT}")
    if dry: print(json.dumps(body,indent=1)[:600]); return
    req=urllib.request.Request(ENDPOINT,data=json.dumps(body).encode(),headers={"Content-Type":"application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req,timeout=30) as r: print("HTTP",r.status,"(200/202 = accepted)")
    except urllib.error.HTTPError as e: print("HTTP",e.code,e.read()[:300])
if __name__=="__main__": main()
