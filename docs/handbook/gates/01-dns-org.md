# Gate — ttllms.org (and apex) DNS

**Updated:** 2026-08-08  
**Status:** BLOCKED without Zone DNS Edit (API 403) or manual dashboard  
**Related:** `ops/DNS_CNAMES_REQUIRED.md` · `ops/ORG_DNS_PENDING.md` · `ops/apply_dns_ttllms.sh`  
**Vault BIND:** `05-dns-bind-import/ttllms.org.txt` (use **.txt**, not .zone)

## Purpose
Attach custom domains to Cloudflare Pages project **ttllms** so https://ttllms.com and https://ttllms.org resolve cleanly (primary = .com).

## Zone IDs (reference)
| Zone | Zone ID |
|------|---------|
| ttllms.com | `4f6b122b7a63280290b3a321071e4049` |
| ttllms.org | `01c9852c3864cf80765c835091147fef` |

## Manual dashboard procedure (always works)

### ttllms.com
Cloudflare → zone **ttllms.com** → DNS → Records:

| Type | Name | Target | Proxy |
|------|------|--------|-------|
| CNAME | `@` | `ttllms.pages.dev` | Proxied |
| CNAME | `www` | `ttllms.pages.dev` | Proxied |

### ttllms.org
| Type | Name | Target | Proxy |
|------|------|--------|-------|
| CNAME | `@` | `ttllms.pages.dev` | Proxied |
| CNAME | `www` | `ttllms.pages.dev` | Proxied |

Alternatively import vault BIND text for org zone.

### After save
1. Wait 1–5 minutes.
2. Workers & Pages → **ttllms** → Custom domains → should become **Active**.
3. Check:
   - https://ttllms.pages.dev/status
   - https://ttllms.com/status
   - https://ttllms.org/status

## Optional: grant agent DNS Edit
1. https://dash.cloudflare.com/profile/api-tokens  
2. Edit token or create new  
3. **Zone → DNS → Edit**  
4. Zone Resources: Include → All zones (or both ttllms zones)  
5. Save; put token in **gitignored** `ops/secrets.local.env`:
   ```bash
   CLOUDFLARE_API_TOKEN=...
   ```
6. Run:
```bash
cd "/Users/hattr/Downloads/TTLLMS.com BUILD/01-repo/daisychainrrr"
# or your clone path
set -a && source ops/secrets.local.env && set +a
./ops/apply_dns_ttllms.sh
```

## Done when
- [ ] Custom domains Active on Pages
- [ ] HTTPS loads site content (not pending CNAME error)
- [ ] `ops/HUMAN_GATES.md` / `ORG_DNS_PENDING.md` updated
- [ ] No secrets committed

## Notes
- Trailing dots in BIND absolute names matter when importing.
- Registrar ownership already obtained for both domains historically; this gate is **DNS record write**, not purchase.
