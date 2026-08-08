# weights · paywalled · pre-release

**Path:** `eventualities/cross-product/weights/paywalled/pre-release/README.md`  
**Updated:** 2026-08-08  
**Ethos:** down to the bone / free public core / product is the proof

## What this eventuality is
The **model weights / checkpoints** is compromised by: **verification path is gated behind payment or private access**.  
Lifecycle phase: **before public release or claim**.  
Primary actor context: **any actor (founder default)**.

## Why it matters
Open weights or polished demos without verifiable model weights / checkpoints are soft tissue.  
This path exists so the failure mode cannot hide in tribal knowledge.

## Where the bone lives
| Item | Location |
|------|----------|
| Artefacts | `models/*/checkpoints/*.pt` |
| Domain / policy | Domain 4 eval gate + release scorecard |
| Verify | `manifests/CHECKPOINTS_MANIFEST.json` |
| Register on failure | registers/incidents/ + model scorecard |

## Detection signals
1. Automated: `python3 -m free_core.provenance.cli verify --manifest <manifest> --base .` fails; or stream verify fails; or canary check fails; or scorecard claims MET without file.
2. Manual: release checklist incomplete; public URL/claim lacks linked artefact; actor (any actor (founder default)) reports inconsistency.
3. Phase-specific (before public release or claim): pre-release CI/manual gate; release seal script; post-release monitor; incident response; acquisition due-diligence freeze.
4. Threat-specific: re-hash files; compare to published root; confirm no paywall on verification; confirm tombstone exists if incomplete.

## Immediate response (ordered)
1. **Stop the soft tissue:** pause any public claim that depends on healthy model weights / checkpoints.
2. **Classify:** integrity (Domain 5) vs process gap (Domain 1) vs data/legal (Domain 3) vs boundary (Domain 8).
3. **Log** in the appropriate register within Domain 5 timelines if material (ack ≤72h for High/Critical).
4. **Contain:** restore from last good sealed commit/tag; do not rewrite history silently.
5. **Remediate:** restore or re-generate artefact; re-seal (`free_core.release.pipeline.seal_model_tree` or `ttllm-manifest`); fix scorecard.
6. **Disclose:** tombstone if gap remains; stream event if public core affected.
7. **Close:** only after verify green and scorecard honest.

## Prevention controls
- Release gate: no “TTLLM” branding without scorecard MET or explicit tombstones for this layer.
- Seals: Merkle manifests for releases/checkpoints; canaries on ttlink indexes.
- BOUNDARY: commercial features cannot require opacity of model weights / checkpoints if it is free-core.
- Cadence: quarterly domain report; monthly decision-log audit.
- Culture: reward deletion of false claims (“remember you’re on drugs”).

## Tests and drills
```bash
# Integrity (examples)
python3 -m free_core.provenance.cli verify --manifest manifests/FREE_CORE_SEAL.json --base .
python3 -m free_core.stream.cli verify models/ttllm-nano/stream/public_log.json
python3 -m free_core.ttlink.cli canary-check --index models/ttllm-nano/ttlink/index.json
python3 scripts/redteam_nano_harness.py
python3 scripts/oneshot_verify_all.py
```
- [ ] Tabletop this scenario once before major public push
- [ ] Confirm owner can run verify without tribal knowledge
- [ ] Confirm tombstone language is ready if artefact cannot be restored same day

## Owner
**Primary:** project lead (md@0265.au) until dedicated free-core / security role is staffed.  
**Escalation:** Domain 5 incident owner; Domain 8 boundary custodian if commercial pressure caused the failure.

## Related branches
- Sibling leaves: `detect.md`, `respond.md`, `prevent.md`, `test.md` under the same node
- Normative domain specs: `docs/specs/`
- Human gates that may block full remediations: `ops/HUMAN_GATES.md`
