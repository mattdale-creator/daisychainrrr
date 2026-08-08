# Wall 3 — Stable JSON API / Workers routes

## Cannot agent-close
Zone **Workers Routes** permission if that is the only path. Full multi-route Workers platform.

## Agent bone (can still ship)
1. **CLI verify never depends on HTTP** — `public_verify_harness.py` (unpaid, offline).
2. **Browser demo** — `site/demo.html` + static index.
3. **Pages Functions** at repo `functions/api/*` (sibling of `site/`, correct wrangler layout).
4. **Static fallbacks** — `site/api/ttlink/index.json`, `site/api/health/index.json`.
5. **_routes.json** — `site/_routes.json` include `/api/*`.
6. Probe in `check_public_urls.py`.

## Deploy shape
```bash
# functions/ at repo root; static assets in site/
npx wrangler pages deploy site --project-name=ttllms
```

## Human close (if Functions still fail)
- Confirm Pages project Functions tab shows routes
- Or enable workers.dev / Workers Routes on token
- See `docs/handbook/gates/03-workers-routes.md`
