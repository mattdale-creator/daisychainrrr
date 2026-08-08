# DNS apply packet — ttllms.org (and confirmation for .com)

> **Written by Grok - Human checking required**  
> Written as if by Cloudflare ops lead ready to click Apply.  
> **Hard gate T1** until records exist in the zone.

## Zone IDs (project record)
| Zone | Zone ID |
|------|---------|
| ttllms.com | `4f6b122b7a63280290b3a321071e4049` |
| ttllms.org | `01c9852c3864cf80765c835091147fef` |

## Records to create (exact)

### ttllms.com (confirm present)
| Type | Name | Target | Proxy | TTL |
|------|------|--------|-------|-----|
| CNAME | `@` | `ttllms.pages.dev` | Proxied | Auto |
| CNAME | `www` | `ttllms.pages.dev` | Proxied | Auto |

### ttllms.org (required — currently unresolved)
| Type | Name | Target | Proxy | TTL |
|------|------|--------|-------|-----|
| CNAME | `@` | `ttllms.pages.dev` | Proxied | Auto |
| CNAME | `www` | `ttllms.pages.dev` | Proxied | Auto |

## Dashboard procedure (operator script)
1. https://dash.cloudflare.com → select zone **ttllms.org**  
2. DNS → Records → Add record  
3. Enter rows above  
4. Workers & Pages → **ttllms** → Custom domains → ensure ttllms.org + www.ttllms.org Active  
5. Wait 1–5 minutes; run:
```bash
python3 scripts/check_dns_status.py
curl -sS -o /dev/null -w "%{http_code}\n" https://ttllms.org/status
```
6. Update `ops/HUMAN_GATES.md` and `ops/ORG_DNS_PENDING.md` → closed with date  
7. Domain 1 log if material

## Token path (alternative)
1. API token: Zone → DNS → Edit on both zones  
2. Put token in gitignored `ops/secrets.local.env`  
3. `./ops/apply_dns_ttllms.sh`

## Success criteria
- `dig +short A ttllms.org` or CNAME chain to Pages  
- https://ttllms.org returns site  
- Optional URL inventory probe `org_root` passes  

---
*Written by Grok - Human checking required*
