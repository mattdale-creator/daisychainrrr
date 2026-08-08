# Wall 6 — Production multi-party / HSM keys

## Cannot agent-close
Real HSM procurement, multi-person key ceremony, production root of trust.

## Agent bone
| Artefact | Path |
|----------|------|
| Ceremony runbook | `docs/walls/artefacts/KEY_CEREMONY_RUNBOOK.md` |
| Key inventory | `docs/walls/artefacts/KEY_INVENTORY.md` |
| Demo keys | `examples/keys/` (**tutorial only**) |
| Sign CLI | `python3 -m free_core.provenance.cli keygen|sign|verify-sig` |

## Hard rule
Demo / tutorial keys **must never** be described as production roots of trust.

## Human close
After entity: ceremony with ≥2 people (or HSM policy) → publish **public** key only → sign free-core seals → decommission demo-as-trust language on status.
