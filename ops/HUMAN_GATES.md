# Human gates (cannot be agent-faked)

**Updated:** 2026-08-08  
**Detail:** `docs/walls/00-WALLS-INDEX.md` · site: https://ttllms.com/walls

| # | Gate | Status | Agent bone | Action to close |
|---|------|--------|------------|-----------------|
| 1 | Zone DNS Edit (ttllms.org) | BLOCKED / pending records | `scripts/check_dns_status.py`, BIND, `apply_dns_ttllms.sh` | Dashboard CNAME or token DNS Edit |
| 2 | R2 enable | BLOCKED 10042 historically | `ops/r2/*` design + upload runbook | Dashboard enable R2 |
| 3 | Workers routes / stable API | PARTIAL | repo `functions/` + static `site/api/*` + CLI | Confirm Functions or expand token |
| 4 | GitHub `workflow` scope | BLOCKED for push | `docs/ci-templates/verify.yml`, `make fine-grain` | PAT with workflow |
| 5 | Entity formation | OPEN | formation checklist, draft covenant | Counsel + file |
| 6 | Production HSM / multi-party keys | OPEN | ceremony runbook, key inventory | After entity |
| 7 | Capital for 32B / scale | OPEN | budget skeleton, fundraise bone | Raise BOUNDARY-safe |
| 8 | Standing red team hire | OPEN | harness, SOW, intake | Hire |
| 9 | Second custodian | OPEN | dead-man procedure, inventory | Name + access |
| 10 | First revenue SKU | OPEN | dry-run packs, BOUNDARY | Customer + billing |

Site is redeployed via `wrangler pages deploy site` → project **ttllms** → **ttllms.com**.
