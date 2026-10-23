#!/bin/sh
# Regenerate the Zero DP guide lead-magnet PDF (run from repo root), then python3 _src/build.py
google-chrome --headless=new --no-sandbox --disable-gpu --no-pdf-header-footer --print-to-pdf=assets/zero-dp-car-loan-approval-guide.pdf "file://$PWD/_src/pdf/zerodp_guide.html"
