# Gate — Workers routes / API routes

**Updated:** 2026-08-08  
**Status:** BLOCKED — token lacked zone Workers Routes; Pages Functions partial  
**Site:** Cloudflare Pages project **ttllms** · `site/` · `site/functions/`

## Purpose
Dynamic endpoints (API, stream tips, verify helpers) on ttllms.com without claiming full Workers production when permissions fail.

## Observed constraints (founding)
- Zone **Workers Routes** permission missing → API 403 class failures
- Pages **Functions** can serve some routes but routing was flaky (HTML/405) depending on config
- Prefer honest static + documented Function paths over fake "full API platform"

## Human options (pick one)

### Option A — Expand API token
1. Cloudflare API tokens → add permissions:
   - Workers Scripts (edit) as needed
   - Workers Routes (edit) on ttllms.com / ttllms.org zones
2. Update `ops/secrets.local.env` (gitignored)
3. Deploy with wrangler per project config

### Option B — workers.dev subdomain
1. Enable workers.dev subdomain for account
2. Deploy worker to `*.workers.dev` for experimentation
3. Later attach custom route when Option A ready

### Option C — Pages Functions only
1. Keep logic under `site/functions/`
2. Document exact paths that work in `site/README.md` / status
3. Tombstone any path that 405s until fixed

## Verification after open
```bash
# Adjust paths to real functions once live
curl -sS -o /dev/null -w "%{http_code}\n" https://ttllms.pages.dev/
curl -sS -o /dev/null -w "%{http_code}\n" https://ttllms.com/
# Example function probe (replace with real route):
# curl -sS https://ttllms.com/api/<endpoint>
```

## Ethos
- Do not advertise endpoints that return wrong content-type or 405 as "API live"
- Public verify must remain possible via **CLI + published manifests** even if HTTP API is down

## Done when
- [ ] Chosen option implemented
- [ ] Documented routes return expected status/body
- [ ] HUMAN_GATES updated
- [ ] STATUS_HONEST matches reality
