#!/usr/bin/env python3
"""Send a OneSignal web push to mitsubishi-sjdm.com subscribers. Stdlib only.
Reads ONLY env vars ONESIGNAL_APP_ID and ONESIGNAL_REST_API_KEY. The key is never printed.
Example:
  python3 notify.py --title "November promo" --message "Xpander from P..." --url https://mitsubishi-sjdm.com/promos/ --dry-run
  python3 notify.py ... --interest xpander      # only subscribers who were on the Xpander page
  python3 notify.py ... --segment "Total Subscriptions"
"""
import argparse, json, os, sys, urllib.request, urllib.error
API="https://api.onesignal.com/notifications?c=push"
a=argparse.ArgumentParser(description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter)
a.add_argument("--title",required=True);a.add_argument("--message",required=True);a.add_argument("--url",required=True)
a.add_argument("--image",help="large image URL (https)");a.add_argument("--segment",default="Total Subscriptions",help="OneSignal segment name")
a.add_argument("--interest",help="filter by tag interest=VALUE (e.g. xpander, promos, blog) instead of segment")
a.add_argument("--dry-run",action="store_true",help="print the payload, send nothing");a.add_argument("--yes",action="store_true",help="skip the confirm question")
o=a.parse_args()
if not o.url.startswith("https://mitsubishi-sjdm.com/"): sys.exit("url must be on https://mitsubishi-sjdm.com/")
app=os.environ.get("ONESIGNAL_APP_ID","").strip();key=os.environ.get("ONESIGNAL_REST_API_KEY","").strip()
p={"app_id":app or "<ONESIGNAL_APP_ID not set>","target_channel":"push","headings":{"en":o.title},"contents":{"en":o.message},"web_url":o.url}
if o.image: p["chrome_web_image"]=o.image
if o.interest: p["filters"]=[{"field":"tag","key":"interest","relation":"=","value":o.interest}]
else: p["included_segments"]=[o.segment]
print(json.dumps(p,indent=2,ensure_ascii=False))
if o.dry_run: print("DRY RUN: nothing sent. API key set:", "yes" if key else "no"); sys.exit(0)
if not app or not key: sys.exit("Set ONESIGNAL_APP_ID and ONESIGNAL_REST_API_KEY env vars first.")
if not o.yes and input("Send this to subscribers? type YES: ").strip()!="YES": sys.exit("Cancelled.")
r=urllib.request.Request(API,data=json.dumps(p).encode(),method="POST",headers={"Content-Type":"application/json; charset=utf-8","Authorization":"Key "+key})
try:
    with urllib.request.urlopen(r,timeout=30) as f: res=json.load(f)
    print("Sent. id:",res.get("id"),"errors:",res.get("errors"))
except urllib.error.HTTPError as e:
    sys.exit(f"OneSignal error {e.code}: {e.read().decode(errors='replace')[:500]}")
