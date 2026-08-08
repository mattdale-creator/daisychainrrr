# Wall 1 — DNS (ttllms.org)

## Cannot agent-close
Writing zone records without **Zone → DNS → Edit** (API 403) or human dashboard click.

## Agent bone (done / maintained)
| Artefact | Path |
|----------|------|
| CNAME recipe | `ops/DNS_CNAMES_REQUIRED.md` |
| Apply script | `ops/apply_dns_ttllms.sh` |
| Org pending note | `ops/ORG_DNS_PENDING.md` |
| BIND import | `ops/dns-import/` |
| Handbook | `docs/handbook/gates/01-dns-org.md` |
| Probe | `scripts/check_dns_status.py` |
| URL inventory | `ops/public_url_inventory.json` (org optional) |

## Current observed state (re-probe)
Run: `python3 scripts/check_dns_status.py`

Expected founding state:
- **ttllms.com** / **www** → Pages (Active on project domains)
- **ttllms.org** → often NXDOMAIN or no useful A/CNAME until human gate

## Human close steps
1. Cloudflare → ttllms.org → DNS → CNAME `@` and `www` → `ttllms.pages.dev` (proxied)  
2. Or grant token Zone DNS Edit and run `./ops/apply_dns_ttllms.sh`  
3. Pages → ttllms → custom domains → Active  
4. Flip `ops/HUMAN_GATES.md` row
