# Web push notifications (OneSignal) – how-to

## 1. One-time setup (free)
1. Sign up at https://onesignal.com (free plan).
2. New App/Website → name "Mitsubishi Promos" → platform **Web**.
3. Choose **Typical Site**. Site URL: `https://www.mitsubishi-sjdm.com`. Upload the site icon (assets/android-chrome-192x192.png).
4. **Permission prompt setup: remove / turn off all OneSignal prompts** (no slide prompt, no bell, no auto-prompt). The site has its own branded "Notify me" bar.
5. Service worker: leave defaults (`/OneSignalSDKWorker.js`, scope `/`). The file is already at the site root.
6. Save. Copy the **App ID** (Settings → Keys & IDs) and create/copy a **REST API key**.
7. Put the App ID in `_src/push_config.json` → `{"app_id": "YOUR-APP-ID"}`, run `python3 _src/build.py`, preview, commit. (The App ID is public; the REST key is secret and NEVER goes in the repo.)

## 2. Sending a notification (when a new promo or blog is posted)
```
export ONESIGNAL_APP_ID=your-app-id
export ONESIGNAL_REST_API_KEY=your-rest-key      # keep private
python3 _src/tools/notify.py --title "Xpander November promo" \
  --message "Low DP and freebies this month. See the details." \
  --url https://www.mitsubishi-sjdm.com/promos/ --image https://www.mitsubishi-sjdm.com/assets/og/... --dry-run
```
Check the preview, then run again without `--dry-run` and type YES.
- Only people who viewed a model: `--interest xpander` (tags: interest = model slug, `promos`, `blog` or `general`; plus source_page).
- Keep it to 1–3 pushes a week; too many makes people unsubscribe.

## 3. Drafts, never auto-send
New promo/blog builds may produce notification drafts (e.g. a `notify_drafts.json` list of title/message/url). Drafts are **never sent automatically**. Every send needs Richard's OK, then the command above.

## Privacy
When the App ID is set, the build adds a "Push notifications" section to /privacy/. Visitors unsubscribe by blocking notifications for the site in browser settings.
