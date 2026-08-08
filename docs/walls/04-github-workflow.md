# Wall 4 — GitHub workflow scope

## Cannot agent-close
Push `.github/workflows/*.yml` when OAuth/PAT lacks **`workflow`** scope  
(error: *refusing to allow an OAuth App to create or update workflow*).

## Agent bone
| Artefact | Path |
|----------|------|
| Local CI equivalent | `make fine-grain` · `scripts/oneshot_verify_all.py` |
| Template workflows | `docs/ci-templates/verify.yml` (publishable copy) |
| Seal freshness | `scripts/check_seal_freshness.py` |
| Note in HUMAN_GATES | `ops/HUMAN_GATES.md` |

## Human close
1. GitHub → Settings → Developer settings → PAT (classic) with **`workflow`** + `repo`  
   or fix OAuth app scopes for the push token.  
2. Copy `docs/ci-templates/verify.yml` → `.github/workflows/verify.yml`  
3. Commit + push  
4. Confirm Actions tab runs green on main

## Until then
Every release still runs local:

```bash
python3 scripts/check_seal_freshness.py
python3 scripts/oneshot_verify_all.py
python3 -m pytest -q
```
