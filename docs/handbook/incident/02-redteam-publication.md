# Red-team finding publication

**Updated:** 2026-08-08  
**Owner (R):** Red-Team Lead / Adversarial function (project lead until staffed)  
**Normative:** `docs/specs/10-red-team-publication.md`  
**Standard:** `docs/specs/artefacts/10/REDTEAM_PUBLICATION_STANDARD.md`  
**Register:** `registers/redteam/FINDINGS_REGISTER.md`  
**Domain ops:** `docs/handbook/domains/10-redteam-ops.md`  
**Framing:** Constructive QA against models **and** transparency systems — not vandalism.

## Purpose
Significant adversarial findings are published systematically. Selective silence is a domain failure.

## Classification → publication clock
| Class | Action |
|-------|--------|
| Critical | Register ASAP; coordinate Domain 5; detail per exemption rules |
| High | Register entry ≤7 days of confirmation |
| Medium | May batch in periodic summary |
| Low | Periodic summary |

Default: **publish**. Permanent suppression forbidden.

## Procedure — automated harness (every release / weekly)

```bash
python3 scripts/redteam_nano_harness.py
cat registers/redteam/last_harness_run.json
```

Expect `"all_pass": true`. On false:
1. Open Domain 5 incident if integrity claim is public-green.
2. Do not ship release claiming green verify.
3. Register finding if it is a durable product defect.

Current harness checks (non-exhaustive):
- manifest tamper detection
- stream tamper detection
- QueryGuard rate limit
- canary present / absent behaviour

## Procedure — human / external finding

1. Confirm reproducibility (commands, commit SHA, artefact hashes).
2. Classify severity.
3. Append `registers/redteam/FINDINGS_REGISTER.md`:
   - ID `RT-NNNN`
   - Discovered / Published dates
   - Component (manifest / ttlink / stream / model / site / process)
   - Severity
   - Summary (public)
   - Remediation status
   - Residual risk
4. Link Domain 5 incident if operational impact.
5. High+: fuller write-up under `docs/specs/artefacts/10/` or `registers/redteam/writeups/` ≤ standard deadline.
6. Remediation tracker: fixed / partial / accepted residual — with dates.
7. After fix: re-run harness + targeted retest; update residual.

## Procedure — security exemption
Same spirit as Domain 5:
- Log expiry
- Publish existence + severity + component even if exploit detail delayed
- No permanent silence

## Scope expansion (when staffed)
| Surface | Examples |
|---------|----------|
| Provenance | Forge manifests, swap leaves, weak signatures |
| Stream | Chain breaks, backdated events |
| ttlink | Index poison, canary evasion, bulk extract vs QueryGuard |
| Model | Safety / overclaim / train-data leakage claims |
| Org process | Decision log gaps, BOUNDARY theater |
| Commercial | Isolation failure leaking into public core |

## Standing hire (human gate)
Pliny-class standing adversarial role is **OPEN** — see `ops/HUMAN_GATES.md`. Until then, project lead runs harness + accepts external reports at md@0265.au.

## RACI
Red-Team Lead R for classification and register; technical owners R for remediations; leadership cannot permanently override publication standard.

## Done when
- [ ] Finding in register with classification
- [ ] Clock met or exemption logged
- [ ] Remediation status current
- [ ] Harness green after fix (or residual accepted publicly)
