# Cloudflare account

**Status:** PARTIAL  
**Architected:** 2026-08-07 19:40 UTC  
**Contact:** md@0265.au  
**Vault:** `/Users/hattr/Downloads/TTLLMS.com BUILD`  
**Primary site:** https://ttllms.com  
**Repo:** https://github.com/mattdale-creator/daisychainrrr  

## Summary

Account hosts Registrar domains, DNS, Pages (ttllms), future R2/Workers. Login context: md@0265.au. API token used by wrangler; expand scopes carefully.

## Why (ethos)

Infrastructure for public proof.

## Prerequisites

- Account access
- API token with least privilege needed

## What to do (executable instructions)

1. Store token in secrets.local.env as CLOUDFLARE_API_TOKEN — never commit.
2. Account ID documented in private env only.
3. Verify token with API; note /tokens/verify may show Invalid while token still works for some calls — test concrete APIs.
4. Grant Zone DNS Edit if automation of DNS required (currently may 403).
5. Enable R2 in dashboard when storage needed.
6. Hardware key on Cloudflare account when available.
7. Pages project name: ttllms → ttllms.pages.dev + custom domains.

## Artefacts to produce

- Working token in env
- Account hardening notes
- Pages project

## Already done in this vault/repo

- Account
- Domains purchased
- Pages site live on .com

## Deferred / external execution

- DNS API edit scope
- R2 enable

## Risks and soft-tissue anti-patterns

- Token in chat logs
- Over-scoped tokens

## Related branches

- 08-ops/03-domains-dns-pages.md
- 08-ops/04-secrets-and-tokens.md

---

*Architect mode deliverable — instruction-complete; capital/legal steps remain human gates.*
