/**
 * Private publish API for the website editor.
 * Secrets (set in the Cloudflare dashboard, never in this file):
 *   PUBLISH_KEY — private key Richard enters on the Update page
 *   GITHUB_PAT — fine-grained token with Contents: Read and write on fit-calculator
 * Auth: X-Publish-Key matching PUBLISH_KEY, or Cloudflare Access email
 * (richard.cuagdan20@gmail.com) if Access is later enabled.
 */
const ALLOWED_EMAILS = ["richard.cuagdan20@gmail.com"];
const ALLOWED_ORIGINS = new Set([
  "https://www.mitsubishi-sjdm.com",
  "https://mitsubishi-sjdm.com",
]);
const REPO = "richardcuagdan20-lgtm/fit-calculator";

function corsHeaders(origin) {
  const allow = ALLOWED_ORIGINS.has(origin) ? origin : "https://www.mitsubishi-sjdm.com";
  return {
    "Access-Control-Allow-Origin": allow,
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, X-Publish-Key",
    "Access-Control-Allow-Credentials": "true",
    "Vary": "Origin",
  };
}

function json(status, body, origin) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { ...corsHeaders(origin), "Content-Type": "application/json" },
  });
}

function timingSafeEqual(a, b) {
  const enc = new TextEncoder();
  const aa = enc.encode(String(a));
  const bb = enc.encode(String(b));
  const len = Math.max(aa.length, bb.length);
  let out = aa.length === bb.length ? 0 : 1;
  for (let i = 0; i < len; i++) {
    out |= (aa[i] || 0) ^ (bb[i] || 0);
  }
  return out === 0;
}

function authorized(request, env) {
  const email = (request.headers.get("Cf-Access-Authenticated-User-Email") || "").trim().toLowerCase();
  if (email && ALLOWED_EMAILS.includes(email)) return true;
  const sent = (request.headers.get("X-Publish-Key") || "").trim();
  const expected = (env.PUBLISH_KEY || "").trim();
  if (expected && sent && timingSafeEqual(sent, expected)) return true;
  return false;
}

export default {
  async fetch(request, env) {
    const origin = request.headers.get("Origin") || "";
    if (request.method === "OPTIONS") {
      return new Response(null, { status: 204, headers: corsHeaders(origin) });
    }
    if (request.method !== "POST") {
      return json(405, { error: "Method not allowed" }, origin);
    }
    if (!authorized(request, env)) {
      return json(401, { error: "Unauthorized" }, origin);
    }
    if (!env.GITHUB_PAT) {
      return json(500, { error: "Publish is not connected yet" }, origin);
    }
    let payload;
    try {
      payload = await request.json();
    } catch {
      return json(400, { error: "Invalid JSON" }, origin);
    }
    if (!payload || typeof payload !== "object" || !payload.site || !Array.isArray(payload.optionAB)) {
      return json(400, { error: "Invalid payload" }, origin);
    }
    const raw = JSON.stringify(payload);
    if (raw.length > 60000) {
      return json(413, { error: "Payload too large" }, origin);
    }
    const gh = await fetch(`https://api.github.com/repos/${REPO}/dispatches`, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${env.GITHUB_PAT}`,
        Accept: "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "mitsu-site-update",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        event_type: "site-update",
        client_payload: payload,
      }),
    });
    if (!gh.ok) {
      return json(502, { error: "Could not start the website update" }, origin);
    }
    return json(200, { ok: true }, origin);
  },
};
