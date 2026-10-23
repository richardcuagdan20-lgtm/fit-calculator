#!/bin/sh
# Regenerate the car loan guide lead-magnet PDF (run from repo root), then python3 _src/build.py
google-chrome --headless=new --no-sandbox --disable-gpu --no-pdf-header-footer --print-to-pdf=assets/car-loan-approval-guide.pdf "file://$PWD/_src/pdf/car_loan_guide.html"
