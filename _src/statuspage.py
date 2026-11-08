# ---------- /status/ : redirect stub to /contact/ (tracker removed; old links and NFC URLs keep working).
# exec'd from build.py after applyform.py.
import os
_sp = os.path.join(R, "status")
os.makedirs(_sp, exist_ok=True)
open(os.path.join(_sp, "index.html"), "w").write("""<!doctype html>
<html lang="en-PH">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,follow">
<meta http-equiv="refresh" content="0;url=/contact/">
<link rel="canonical" href="https://www.mitsubishi-sjdm.com/contact/">
<title>Contact Richard</title>
<script>location.replace("/contact/"+location.search+location.hash)</script>
</head>
<body>
<p>This page has moved. <a href="/contact/">Contact Richard</a>.</p>
</body>
</html>
""")
