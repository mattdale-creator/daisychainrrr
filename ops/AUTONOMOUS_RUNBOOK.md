# Autonomous runbook — TTLLM / ttllms.com

**On-disk source of truth (this Mac):**  
`/Users/hattr/Downloads/TTLLMS.com BUILD`

**Code repo path:**  
`/Users/hattr/Downloads/TTLLMS.com BUILD/01-repo/daisychainrrr`  
(also symlinked at `/Users/hattr/daisychainrrr`)


**Contact for all project email:** **md@0265.au**  
**Primary site:** https://ttllms.com  
**Secondary:** https://ttllms.org  
**Repo:** https://github.com/mattdale-creator/daisychainrrr  
**Pages project:** `ttllms` → https://ttllms.pages.dev  
**Cloudflare account:** `03bac8b3a49fc4605ede89f35f792819` (Md@0265.au)

## Already done

| Item | Status |
|------|--------|
| Domains ttllms.com + ttllms.org | **registrationActive** (expires ~2027-08-07) |
| Zones on Cloudflare NS | dahlia / george |
| Free-core monorepo + founding pack | yes |
| Pages project `ttllms` | created; site deployed |
| Custom domains on Pages | attached; **ttllms.com apex HTTPS live** |
| Secrets | `ops/secrets.local.env` (gitignored) |
| Contact policy | **md@0265.au** |
| free_core | **0.6.2** (local + ttllms.com status) |

## DNS status (honest, 2026-08-08 reevaluation)

| Host | Status |
|------|--------|
| https://ttllms.com | **Live** (200) |
| https://www.ttllms.com | **Live** |
| https://ttllms.pages.dev | **Live** |
| ttllms.org / www | **Not resolving** — hard gate **T1** |

API token still **cannot** edit DNS (403). For **.org** only:

1. Add **Zone → DNS → Edit** to the API token and say **DNS token updated**, or  
2. Manually add org CNAMEs in `ops/DNS_CNAMES_REQUIRED.md` (~2 minutes)

Primary site does **not** wait on that step.

## After DNS — agent continues alone

1. Confirm Pages domains **Active**  
2. Optional: redirect ttllms.org → ttllms.com  
3. Optional: Email Routing `@ttllms.com` → **md@0265.au**  
4. Optional: Enable R2 + bucket for public-core artefacts  
5. Optional: gh `workflow` scope → push Actions  
6. Keep redeploying site with wrangler as content evolves  

## Deploy anytime

```bash
cd /Users/hattr/daisychainrrr
set -a && source ops/secrets.local.env && set +a
npx wrangler pages deploy site --project-name=ttllms --branch=main --commit-dirty=true
```
