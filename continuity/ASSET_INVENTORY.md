# Public Core Asset Inventory (Domain 9)

**Updated:** 2026-08-08  
**Status:** Pre-entity draft — succession is operational intent, not a signed legal instrument  
**Primary contact:** md@0265.au  

| Asset | Path / ID | Primary | Backup (30d) | Recovery if founder unavailable 30d | Continuity |
|-------|-----------|---------|--------------|-------------------------------------|------------|
| Domain ttllms.com | Cloudflare Registrar | founder (md@0265.au) | *unnamed — TOMBSTONE until second custodian* | CF account recovery + registrar lock; document in vault | PARTIAL |
| Domain ttllms.org | Cloudflare (DNS pending) | founder | *unnamed* | same as .com; complete DNS via handbook gate 01 | PARTIAL |
| Pages project ttllms | Cloudflare Pages | founder | *unnamed* | Redeploy `site/` from GitHub main | PARTIAL |
| GitHub daisychainrrr | mattdale-creator/daisychainrrr | founder | *unnamed* | Public clone survives; admin access needs GH recovery | PARTIAL |
| free_core package | free_core/ | repo maintainers | public forks | Reinstall from git tag | yes |
| Architecture tree | docs/architecture-tree/ | repo | public | git history | yes |
| Human handbook | docs/handbook/ | repo | public | git history | yes |
| Founding conversation | founding/conversation/ | repo | vault SoT | vault + git | yes |
| Proof RIP reports | founding/proof_rip/ | repo/vault | vault | vault | yes |
| Domain specs 1–10 | docs/specs/ | repo | public | git | yes |
| Decision log | registers/decisions/ | project lead | public append-only | git; continue IDs | yes |
| Incident register | registers/incidents/ | IR owner | public | git | yes |
| Red-team register | registers/redteam/ | RT lead | public | git | yes |
| Supply lock | registers/supply-chain/ | release owner | public | rebuild via `scripts/build_supply_lock.py` | yes |
| ttllm-nano family | models/ttllm-nano* | training owner | public | retrain nano from prepare_data | yes |
| FREE_CORE_SEAL | manifests/FREE_CORE_SEAL.json | provenance owner | public | `seal-repo` / `check_seal_freshness.py --write` | yes |
| Demo signing keys | examples/keys/ | tutorial only | n/a | **not** production roots of trust | n/a prod |
| Production signing keys | *not issued* | — | multi-party after entity | ceremony TBD | TOMBSTONE |
| Vault SoT | TTLLMS.com BUILD | founder | *unnamed* | Desktop/vault path; not sole copy of public git | PARTIAL |
| Contact email | md@0265.au | founder | *unnamed* | domain email recovery | PARTIAL |
| Covenant | continuity/COVENANT.md | draft unsigned | entity when formed | counsel | TOMBSTONE legal |

## Succession notes (honest)
1. Single-human concentration risk is **public**. Closing it requires naming a backup custodian and/or entity officers.
2. Public git history is the strongest continuity for free-core bone.
3. Cloudflare/GitHub org transfer procedures must be written after second custodian exists (Domain 1 decision).
4. Demo keys must never be the only recovery path for public trust.

## Related
- `continuity/COVENANT.md`
- `docs/handbook/gates/04-entity-covenant.md`
- `docs/handbook/domains/09-stewardship-ops.md`
