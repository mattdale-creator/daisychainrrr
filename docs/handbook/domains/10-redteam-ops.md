# Domain 10 — Red-team publication operations (human handbook)

**Updated:** 2026-08-08  
**Owner (R):** Red-Team Lead / Adversarial function (project lead until staffed)  
**Normative:** `docs/specs/10-red-team-publication.md`  
**Standard:** `docs/specs/artefacts/10/REDTEAM_PUBLICATION_STANDARD.md`  
**Classification:** `docs/specs/artefacts/10/FINDINGS_CLASSIFICATION.md`  
**Register:** `registers/redteam/FINDINGS_REGISTER.md`  
**Harness:** `scripts/redteam_nano_harness.py`  
**Deep playbook:** `docs/handbook/incident/02-redteam-publication.md`

## Purpose
Significant adversarial findings against models **and** transparency systems must be published systematically—not selectively.

## Classification (summary)
| Class | Publication |
|-------|-------------|
| Critical | Register ASAP; detail per exemption rules |
| High | Register entry ≤7 days of confirmation |
| Medium | May batch in periodic summary |
| Low | Periodic summary |

Default: **publish**. Permanent suppression forbidden. Time-limited security exemption only (logged).

## Procedure — run automated transparency harness (now)

```bash
python3 scripts/redteam_nano_harness.py
# writes registers/redteam/last_harness_run.json
```

Expect all_pass true. If false: open Domain 5 incident; do not claim green verify.

## Procedure — register a finding

1. Classify (Critical/High/Medium/Low).
2. Append `registers/redteam/FINDINGS_REGISTER.md` (ID, dates, component, severity, summary, remediation, residual).
3. High+: initial entry ≤7 days; fuller write-up per standard.
4. Link affected checkpoint/index/manifest hashes when possible.
5. Remediation tracker: fixed / partial / accepted residual — with dates.
6. Align with Domain 5 if it is also an incident.
7. Semi-annual activity summary when volume exists.

## Procedure — security exemption (withhold exploit detail)

1. Document concrete immediate exploitation risk.
2. Log exemption with expiry.
3. Publish that a finding exists + severity + component even if detail delayed.
4. Renew or publish detail by expiry — no silent permanent hold.

## Commands
```bash
python3 scripts/redteam_nano_harness.py
cat registers/redteam/last_harness_run.json
ls registers/redteam/
```

## RACI
Red-Team Lead R for classification and register; technical owners update remediation status; leadership cannot permanently override standard.

## Done when
- [x] Standard + harness + register path
- [ ] First High+ finding published under process (none yet)
- [ ] Standing adversarial hire (human gate)
