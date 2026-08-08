# Transparency scorecard — ttllm-nano 0.1.0-nano

Generated: 2026-08-08T08:40:58Z

| Domain | Status | Notes |
|--------|--------|-------|
| Free core: weights | PARTIAL | Nano char-LM weights + dense checkpoints (not 32B) |
| Free core: data | MET | PG public-domain slices + full files + DATA_CARD + hashes |
| Free core: code | MET | models/ttllm-nano/code/ |
| Free core: checkpoints | MET | dense step_*.pt |
| Free core: metrics | MET | metrics/train.jsonl + hyperparams |
| Free core: ttlink | MET (corpus-scale) | index over train docs + shard manifest |
| Free core: stream | MET | real train/seal events hash-chained |
| Free core: crypto | MET | RELEASE_MANIFEST merkle |
| 1 Governance | PARTIAL | Decision log entries for nano release |
| 2 Ownership | PARTIAL | founder disclosure artefact |
| 3 Data governance | MET | DATA_CARD + sources.json + legal log ready |
| 4 Evaluation | PARTIAL | eval_pack; no capability cosplay |
| 5 Incidents | PARTIAL | register ready; none yet |
| 6 Compensation | PARTIAL | philosophy published |
| 7 Supply chain | MET | dependency register for this release |
| 8 Boundary | MET | nano is free core; no paid enclosure |
| 9 Stewardship | PARTIAL | inventory lists nano artefacts |
| 10 Red-team pub | PARTIAL | harness + empty findings register |

**Tombstones (honest):**
- Not multi-trillion-token data
- Not frontier capability
- Not production FM-index
- Demo signing keys ≠ production HSM
