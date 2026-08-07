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
| Custom domains on Pages | attached (pending CNAME) |
| Secrets | `ops/secrets.local.env` (gitignored) |
| Contact policy | **md@0265.au** |

## One human step left for apex HTTPS

API token **cannot** edit DNS (403). Either:

1. Add **Zone → DNS → Edit** to the API token and say **DNS token updated**, or  
2. Manually add the 4 CNAMEs in `ops/DNS_CNAMES_REQUIRED.md` (~2 minutes)

Until then: **https://ttllms.pages.dev** is live; **ttllms.com** waits on CNAME.

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
