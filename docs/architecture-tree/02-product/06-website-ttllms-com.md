# Website ttllms.com (primary)

**Status:** PARTIAL  
**Architected:** 2026-08-07 19:40 UTC  
**Contact:** md@0265.au  
**Vault:** `/Users/hattr/Downloads/TTLLMS.com BUILD`  
**Primary site:** https://ttllms.com  
**Repo:** https://github.com/mattdale-creator/daisychainrrr  

## Summary

Primary public surface: https://ttllms.com on Cloudflare Pages project `ttllms`. Also own ttllms.org (DNS may lag). Contact md@0265.au.

## Why (ethos)

Publish-first: the site is part of the proof.

## Prerequisites

- Cloudflare account
- Pages project
- Domain on registrar

## What to do (executable instructions)

1. Keep site content in repo `site/` and vault deploy path synced.
2. Deploy via wrangler pages with CLOUDFLARE_API_TOKEN set.
3. Canonical host: ttllms.com; www CNAME to pages; apex as designed (A/AAAA or CNAME flattened).
4. Include: definition, free core promise, repo link, contact, architecture-tree pointer, security.txt.
5. After content change: deploy, curl -I 200, visual check.
6. ttllms.org: import BIND txt when ready; either redirect to .com or mirror.
7. Do not put secrets in static site.

## Artefacts to produce

- Live site 200
- security.txt
- Deploy runbook snippet

## Already done in this vault/repo

- ttllms.com live with TTLLM content
- Pages project
- DNS for .com

## Deferred / external execution

- Full multi-page docs portal
- org DNS complete

## Risks and soft-tissue anti-patterns

- Stale claims on homepage
- Different story on .org vs .com

## Related branches

- 08-ops/03-domains-dns-pages.md
- 02-product/07-publish-founding-conversation.md

---

*Architect mode deliverable — instruction-complete; capital/legal steps remain human gates.*
