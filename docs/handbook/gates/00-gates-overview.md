# Human gates — overview

**Updated:** 2026-08-08  
**Canonical list:** `ops/HUMAN_GATES.md`  
**Principle:** Agents cannot fake DNS permissions, legal entity, capital, or HSM custody. Document the gate; wait for human.

## Why gates exist
TTLLM ethos is radical honesty. Calling a blocked Cloudflare token "deployed production multi-region" would be soft tissue. Gates are **named incomplete work**, not shame.

## Gate register (founding)

| Gate | Status | Handbook | Opens with |
|------|--------|----------|------------|
| Zone DNS Edit (esp. ttllms.org) | BLOCKED 403 | [01-dns-org](01-dns-org.md) | Token scope or dashboard |
| R2 enable | BLOCKED 10042 | [02-r2](02-r2.md) | Dashboard enable |
| Workers routes / workers.dev | BLOCKED | [03-workers-routes](03-workers-routes.md) | Token or subdomain |
| Entity + covenant | OPEN | [04-entity-covenant](04-entity-covenant.md) | Counsel + filings |
| Production HSM keys | OPEN | Domain 9 + gate 04 | After entity |
| Capital for scale train | OPEN | [release/04-train-scaleup](../release/04-train-scaleup.md) | Fundraise aligned BOUNDARY |
| Standing red team hire | OPEN | Domain 10 | Recruit / budget |
| gh workflow scope | OPTIONAL | CI docs | GitHub token scopes |

## How to close a gate
1. Human performs the action (dashboard, counsel, wire transfer, hire).
2. Evidence: screenshot path optional; better: working API result or signed doc path in vault/repo (no secrets).
3. Update `ops/HUMAN_GATES.md` status row.
4. Domain 1 decision if material (entity, capital, key ceremony).
5. Re-run relevant verify / deploy.
6. Update STATUS_HONEST if public claim changes.

## Agent policy
- **Do** prepare BIND files, scripts, runbooks, checklists.
- **Do not** claim gate closed without evidence.
- **Do not** store expanded secrets in git; use `ops/secrets.local.env` (gitignored).

## Contact
md@0265.au · https://ttllms.com/status
