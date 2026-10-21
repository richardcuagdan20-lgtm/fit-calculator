# mitsubishipromos.online

Static site for Richard Cuagdan, Car Sales Executive, Mitsubishi SJ Legacy Motors (SJDM, Bulacan). Hosted on GitHub Pages.

- `/budgetcalculator/` – ad landing page (Meta Pixel + lead webhook). Hand-edited; NOT generated. Do not move.
- `/privacy/` – privacy policy used in Meta lead forms. Hand-edited; do not move.
- Everything else (`/`, `/cars/`, `/promos/`, `/guides/`, `/blog/`, `/about/`, `/apply/`, `/contact/`, `404.html`, `sitemap.xml`, `robots.txt`) is generated.
- Root `/` redirects to `/budgetcalculator/` (query + hash kept) when the query contains `seg=`, `unit=`, `utm_`, `adset=` or `fbclid`.

## Generator
Source lives in `_src/` (Python 3, no dependencies):
- `_src/data.py` – models, variants, SRP, monthly options, fuel freebies, all-in list, promo note.
- `_src/content.py` – guide articles (`GUIDES`) and blog posts (`POSTS`).
- `_src/build.py` – templates (header, footer, Messenger button, CTA, GA4 tag, JSON-LD) and writes the pages.

Rebuild: `python3 _src/build.py` from the repo root, then commit.

## Prices, promos and leads
- Public pages show SRP only (official MMPC price list, `srp` in `_src/data.py`; `None` renders "Ask for price").
- Promo DP/monthly figures live in each variant's `promo` and are rendered only by JS on `/promos/` (noindex) after the gate form; unlock is remembered in localStorage (`mp_promo_unlocked`).
- `/apply/` and the promo gate post to the same Apps Script webhook as the calculator via `/assets/lead.js` (via = `apply_form` / `promo_gate`). Extra apply fields (income range, email, message) go into the `usage` column; payment choice into `dpPreference`.
- Meta Pixel (PageView) + GA4 on generated pages; Lead / generate_lead fire on successful submit.

## Adding a blog post
1. Open `_src/content.py` and append a dict to `POSTS`:
   `dict(slug="my-post", date="2026-11-05", img="xpglx_x37", alt="Describe the image", title="...", desc="Meta description, ~150 chars", body='''<p>HTML…</p><h2>…</h2>''')`
   - `img` is a file name (without `.webp`) in `/assets/img/`. Use `<h2>`/`<h3>` inside the body (the title is the `<h1>`).
2. Run `python3 _src/build.py`. The post page, blog index, sitemap and Article JSON-LD update automatically.
3. Commit and push.

Monthly promo update: edit figures in `_src/data.py` and the `NOTE` text (and month mentions in `content.py`), rebuild.

## Placeholders
- Richard's photo and years of experience: HTML comments in `_src/build.py` (About page).
- Phone number: HTML comments on About and Contact pages.
- GA4 is live: `G-T89CH2TJS6` (all pages, including budgetcalculator and privacy).
