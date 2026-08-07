# Domains, DNS, Pages

**Status:** PARTIAL  
**Architected:** 2026-08-07 19:40 UTC  
**Contact:** md@0265.au  
**Vault:** `/Users/hattr/Downloads/TTLLMS.com BUILD`  
**Primary site:** https://ttllms.com  
**Repo:** https://github.com/mattdale-creator/daisychainrrr  

## Summary

ttllms.com primary live; ttllms.org owned. BIND import files as .txt (not .zone) with trailing dots on FQDNs; cf-proxied notes as documented in vault 05-dns-bind-import.

## Why (ethos)

Wrong DNS file type was a real failure mode — document the fix permanently.

## Prerequisites

- Cloudflare Registrar zones
- Pages project

## What to do (executable instructions)

1. Use vault `05-dns-bind-import/ttllms.com.txt` and `ttllms.org.txt` for imports.
2. Dashboard DNS for .com already serves site; keep apex/www correct for Pages.
3. Import .org when ready; prefer redirect to .com or identical content.
4. After DNS changes: check public resolvers, not only local cache (NXDOMAIN traps).
5. Redeploy Pages after site content changes: wrangler pages deploy with token.
6. Document zone IDs in private env if needed — not in public MD if sensitive ops prefer.

## Artefacts to produce

- BIND txt files
- Live 200 on ttllms.com
- Deploy notes

## Already done in this vault/repo

- .com live
- BIND txt in vault
- Pages project

## Deferred / external execution

- .org full DNS parity
- API DNS automation

## Risks and soft-tissue anti-patterns

- Uploading .zone rejected format
- Missing trailing dots on CNAMEs

## Related branches

- 02-product/06-website-ttllms-com.md
- 08-ops/02-cloudflare-account.md

---

*Architect mode deliverable — instruction-complete; capital/legal steps remain human gates.*
