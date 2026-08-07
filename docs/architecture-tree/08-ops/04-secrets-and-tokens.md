# Secrets and tokens

**Status:** PARTIAL  
**Architected:** 2026-08-07 19:40 UTC  
**Contact:** md@0265.au  
**Vault:** `/Users/hattr/Downloads/TTLLMS.com BUILD`  
**Primary site:** https://ttllms.com  
**Repo:** https://github.com/mattdale-creator/daisychainrrr  

## Summary

All secrets in gitignored local env; never architecture tree, never git, never site.

## Why (ethos)

Leaked tokens destroy trust and infrastructure.

## Prerequisites

- gitignore present

## What to do (executable instructions)

1. Use ops/secrets.local.env (gitignored) for CLOUDFLARE_API_TOKEN, account IDs, R2 keys.
2. Rotate if pasted into chat logs; prefer re-issue over hope.
3. Document required env vars in ops README without values.
4. R2 keys only after R2 enabled.
5. gh workflow scope separate from ordinary push — do not force without user.
6. Precompact freezes must not copy secrets files into public Desktop packs.

## Artefacts to produce

- secrets.local.env (private)
- env example without values
- Rotation log private

## Already done in this vault/repo

- gitignore patterns
- token usage via env for wrangler

## Deferred / external execution

- Full secrets manager (1Password/CF secrets) at org stage

## Risks and soft-tissue anti-patterns

- Committing secrets
- Printing tokens in MD

## Related branches

- 00-meta/SOURCE-OF-TRUTH.md
- 08-ops/02-cloudflare-account.md

---

*Architect mode deliverable — instruction-complete; capital/legal steps remain human gates.*
