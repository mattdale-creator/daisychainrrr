# High / Critical incident playbook

**Updated:** 2026-08-08  
**Owner (R):** Incident Response Owner (project lead until staffed)  
**Normative:** `docs/specs/05-incident-disclosure.md`  
**Policy:** `docs/specs/artefacts/05/INCIDENT_DISCLOSURE_POLICY.md`  
**Severity:** `docs/specs/artefacts/05/SEVERITY_THRESHOLDS.md`  
**Register:** `registers/incidents/INCIDENT_LOG.md`  
**Domain ops:** `docs/handbook/domains/05-incident-ops.md`

## Purpose
Transparency-system failures (manifest forge, index poison, key compromise, seal lie) use the **same** severity ladder as model failures. Disclose on clock; no permanent secrecy.

## Severity recap
| Level | Examples | Clock |
|-------|----------|-------|
| **Critical** | Manifest forge, signing-key compromise, public index poison, false green verify in public claim | Ack ≤72h; fuller ≤30d unless logged exemption |
| **High** | Significant free-core integrity/availability failure | Ack ≤72h |
| Medium / Low | See Domain 5 ops | Register + periodic |

## Immediate actions (T+0)

1. **Stop the bleeding**
   - If key compromise: stop using key; revoke public trust language for that key.
   - If bad deploy: roll back site / unpublish false claim pages.
   - If index poison: take query surface offline or pin last known-good index hash.

2. **Classify** using `SEVERITY_THRESHOLDS.md`. If unsure between High and Critical → treat as Critical until proven lower.

3. **Open register row** in `registers/incidents/INCIDENT_LOG.md`:
   - ID: next `I-NNNN`
   - Identified (UTC)
   - Disclosed (UTC or "pending ≤72h")
   - Category (integrity / availability / confidentiality-of-keys / process)
   - Summary (one line, public-safe)
   - Status: `open`

4. **Verify detectability**
```bash
python3 -m free_core.provenance.cli verify --manifest manifests/FREE_CORE_SEAL.json --base .
python3 scripts/oneshot_verify_all.py
python3 scripts/redteam_nano_harness.py
# Model-specific:
python3 -m free_core.provenance.cli verify \
  --manifest models/ttllm-nano/manifests/RELEASE_MANIFEST.json \
  --base models/ttllm-nano
python3 -m free_core.stream.cli verify models/ttllm-nano/stream/public_log.json
```

5. **Tombstone public claims** that depend on broken integrity (status page + SCORECARD). Prefer "broken and investigating" over silent 200 OK.

## Within 72 hours — public ack
- Publish minimal facts: what class of failure, what is still trustworthy, what is not.
- Contact: md@0265.au · site status · stream event if stream is still trusted.
- Do **not** invent root cause.

## Within 30 days — fuller disclosure / post-mortem
Unless time-limited security exemption logged:
1. Timeline of detection → containment → fix.
2. Root cause and contributing factors.
3. Merkle roots / commits for good and bad states.
4. Customer/commercial impact (if any) without leaking tenant data.
5. Remediation + residual risk.
6. Domain 1 decision if process/BOUNDARY change required.
7. Close or reclassify register row.

## Security exemption (withhold exploit detail)
1. Document **concrete** immediate exploitation risk.
2. Log exemption with **expiry** in incident register + decision log if material.
3. Still publish: that incident exists, severity, component.
4. On expiry: publish detail or renew with justification — **no permanent hold**.

## Stream events (if stream intact)
Append events such as: `incident_opened`, `claim_tombstoned`, `incident_mitigated`, `incident_closed` with artefact hashes where possible.

## Commercial isolation
Customer compromise must not alter public skeleton; public incident must not dump tenant data. See `commercial/ISOLATION_RUNBOOK.md`.

## RACI
| Role | R | A | C | I |
|------|---|---|---|---|
| Incident Response Owner | ✓ | | | |
| Project lead | | ✓ | | |
| Provenance / ttlink owners | | | ✓ | |
| Boundary Custodian | | | ✓ | if claim/BOUNDARY |
| Public | | | | ✓ |

## Done when
- [ ] Register row complete
- [ ] 72h ack met (High/Critical)
- [ ] Claims match remaining trustworthy seals
- [ ] Post-mortem or logged exemption path set
