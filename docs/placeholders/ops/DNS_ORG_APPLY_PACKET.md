# DNS apply packet — ttllms.com / ttllms.org (full operator pack)

> **Written by Grok - Human checking required**  
> Cloudflare ops voice. **Hard gate T1** until records exist and probes pass.  
> Exact records below are the intended production state; agent cannot write them without Zone DNS Edit / valid token.

---

## 1. Why DNS is load-bearing

Public proof surfaces (status, demo, security policy, verify instructions) must resolve under the primary brand domain. **ttllms.com** is primary; **ttllms.org** is owned secondary. Soft tissue is claiming “domains live” when org NXDOMAINs.

---

## 2. Zone IDs (project record)

| Zone | Zone ID |
|------|---------|
| ttllms.com | `4f6b122b7a63280290b3a321071e4049` |
| ttllms.org | `01c9852c3864cf80765c835091147fef` |

Pages project: **ttllms** → `ttllms.pages.dev`

---

## 3. Records to create / confirm

### ttllms.com (confirm Active)

| Type | Name | Target | Proxy | TTL |
|------|------|--------|-------|-----|
| CNAME | `@` | `ttllms.pages.dev` | Proxied | Auto |
| CNAME | `www` | `ttllms.pages.dev` | Proxied | Auto |

### ttllms.org (required — historically unresolved)

| Type | Name | Target | Proxy | TTL |
|------|------|--------|-------|-----|
| CNAME | `@` | `ttllms.pages.dev` | Proxied | Auto |
| CNAME | `www` | `ttllms.pages.dev` | Proxied | Auto |

BIND import alternative: vault `05-dns-bind-import/ttllms.org.txt` (use **.txt**).

---

## 4. Dashboard procedure

1. Cloudflare dashboard → zone **ttllms.org** → DNS → Records  
2. Add rows above  
3. Workers & Pages → **ttllms** → Custom domains → ttllms.org + www → Active  
4. Wait 1–5 minutes  
5. Verify:
```bash
python3 scripts/check_dns_status.py
curl -sS -o /dev/null -w "%{http_code}\n" https://ttllms.org/status
python3 scripts/check_public_urls.py
```
6. Update `ops/HUMAN_GATES.md` / `ops/ORG_DNS_PENDING.md` with closed date  
7. Domain 1 if material  

---

## 5. Token automation path

1. API token: Zone → DNS → Edit on both zones (+ Pages as needed)  
2. Store only in gitignored `ops/secrets.local.env`  
3. `./ops/apply_dns_ttllms.sh`  
4. Confirm token verify succeeds (T3)  

---

## 6. Success criteria

- dig resolves org to Pages/proxy addresses  
- https://ttllms.org serves TTLLM site  
- optional URL inventory `org_root` passes  
- Hard gate T1 marked closed **only after** above  

---

*Written by Grok - Human checking required — also on https://ttllms.com/placeholders/*
