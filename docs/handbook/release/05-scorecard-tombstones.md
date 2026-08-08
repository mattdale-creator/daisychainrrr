# Scorecard & tombstones

**Updated:** 2026-08-08  
**Owner (R):** Transparency Custodian / project lead  
**Normative:** Domains 1–10 · `docs/specs/artefacts/MASTER_DOMAIN_SCORECARD.md`  
**Code:** `free_core/release/scorecard.py` · `scripts/domain_scorecard_all.py`

## Purpose
Empty honesty beats soft tissue. Every public claim is **MET**, **PARTIAL**, or **TOMBSTONE** with evidence — never silent omission.

## Status vocabulary
| Status | Meaning |
|--------|---------|
| **MET** | Artefact exists; verification or process executed as claimed |
| **PARTIAL** | Structure or partial process exists; material gap remains |
| **TOMBSTONE** | Explicitly not done; reason published; not claimed |

## Procedure — generate / refresh domain scorecard

```bash
python3 scripts/domain_scorecard_all.py
# updates / prints master scorecard paths under docs/specs/artefacts/
```

Manual release scorecard (Python helper):
```python
from free_core.release.scorecard import build_scorecard
print(build_scorecard(
    "ttllm-nano-0.1.0",
    domains=[
        ("1 Governance", "PARTIAL", "log path exists; monthly audit not yet ritualised"),
        ("4 Evaluation", "TOMBSTONE", "nano not frontier-competitive"),
        # ...
    ],
    tombstones=[
        "nano ≠ OLMo-scale",
        "production HSM keys not issued",
        "no multi-TB ttlink",
    ],
    merkle_root="<from RELEASE_MANIFEST>",
))
```

Write output to `models/<name>/cards/SCORECARD.md` or `docs/specs/artefacts/releases/`.

## Required tombstones (founding era — keep until false)
- Nano models are **not** frontier or OLMo-class capability
- Demo signing keys are **not** production roots of trust
- Multi-trillion-token / multi-TB production ttlink **not** built
- Legal entity / signed covenant **not** complete
- Standing external red team **not** hired
- Commercial SKUs **designed, not sold**
- Workers routes / R2 / some DNS org records may still be **human-gated**

## Procedure — claim change
1. Re-run verify + harness.
2. Update scorecard rows with evidence links (paths, commit SHAs, merkle roots).
3. If upgrading TOMBSTONE → MET: Domain 1 log if material.
4. Update `STATUS_HONEST.md` and site status page same day.
5. Never remove a tombstone by deleting the line — mark superseded with date + evidence.

## Forbidden patterns
| Pattern | Why it fails ethos |
|---------|-------------------|
| Green marketing with red harness | Proof is the product |
| "Coming soon" without tombstone | Soft tissue |
| Scorecard only in private docs | Opacity |
| Backdating MET without artefacts | Fraud against self |

## RACI
Transparency Custodian R; domain owners supply evidence; leadership cannot force MET without artefacts.

## Done when
- [ ] Master domain scorecard current
- [ ] Per-release scorecard for every public model claim
- [ ] STATUS_HONEST and site/status agree with scorecard
