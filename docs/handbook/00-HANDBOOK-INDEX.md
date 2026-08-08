# TTLLM Human Handbook — Index

**Ethos:** Down to the bone · free public core never paywalled · product is the proof  
**Audience:** Humans implementing TTLLM operations without tribal knowledge  
**Updated:** 2026-08-08  

## How to use this handbook

1. Start here for any operational task.
2. Follow the linked runbook end-to-end; run named commands from repo root unless stated.
3. Log material actions in the named register.
4. Update scorecards honestly (MET / PARTIAL / TOMBSTONE).
5. Matrix failure catalog (optional deepen): `docs/architecture-tree/eventualities/` — refine after drills, not before.

**Repo root (typical):**  
`/Users/hattr/Downloads/TTLLMS.com BUILD/01-repo/daisychainrrr`  
or clone of `github.com/mattdale-creator/daisychainrrr`

## Quality bar (every load-path doc)

| If you must… | Doc must name… |
|--------------|----------------|
| Verify / seal / canary | Exact commands + paths |
| Log incident / decision | Register + severity timeline |
| Refuse commercial ask | BOUNDARY + Domain 8 steps |
| Ship a release | Scorecard + tombstone language |
| Own the path | Owner / RACI |

## Load paths

### A. Domains 1–10 (monthly / quarterly ops)
| Domain | Handbook | Normative plan | Artefacts | Registers |
|--------|----------|----------------|-----------|-----------|
| 1 Governance | [domains/01-governance-ops.md](domains/01-governance-ops.md) | `docs/specs/01-governance.md` | `docs/specs/artefacts/01/` | `registers/decisions/` |
| 2 Ownership | [domains/02-ownership-ops.md](domains/02-ownership-ops.md) | `docs/specs/02-ownership-funding.md` | `docs/specs/artefacts/02/` | `registers/ownership/` |
| 3 Data / legal | [domains/03-data-legal-ops.md](domains/03-data-legal-ops.md) | `docs/specs/03-data-governance.md` | `docs/specs/artefacts/03/` | `registers/legal/` |
| 4 Evaluation | [domains/04-evaluation-ops.md](domains/04-evaluation-ops.md) | `docs/specs/04-evaluation.md` | `docs/specs/artefacts/04/` | model `evals/` |
| 5 Incidents | [domains/05-incident-ops.md](domains/05-incident-ops.md) | `docs/specs/05-incident-disclosure.md` | `docs/specs/artefacts/05/` | `registers/incidents/` |
| 6 Compensation | [domains/06-compensation-ops.md](domains/06-compensation-ops.md) | `docs/specs/06-compensation.md` | `docs/specs/artefacts/06/` | — |
| 7 Supply chain | [domains/07-supply-chain-ops.md](domains/07-supply-chain-ops.md) | `docs/specs/07-supply-chain.md` | `docs/specs/artefacts/07/` | `registers/supply-chain/` |
| 8 Boundary | [domains/08-boundary-ops.md](domains/08-boundary-ops.md) | `docs/specs/08-boundary-rules.md` | `docs/specs/artefacts/08/` | `commercial/` |
| 9 Stewardship | [domains/09-stewardship-ops.md](domains/09-stewardship-ops.md) | `docs/specs/09-stewardship.md` | `docs/specs/artefacts/09/` | `continuity/` |
| 10 Red-team pub | [domains/10-redteam-ops.md](domains/10-redteam-ops.md) | `docs/specs/10-red-team-publication.md` | `docs/specs/artefacts/10/` | `registers/redteam/` |

Master org scorecard: `docs/specs/artefacts/MASTER_DOMAIN_SCORECARD.md`

### B. Release / seal / train
| Runbook | Path |
|---------|------|
| Full release (nano → claim) | [release/01-ship-release.md](release/01-ship-release.md) |
| Seal & verify | [release/02-seal-and-verify.md](release/02-seal-and-verify.md) |
| Train nano (local) | [release/03-train-nano.md](release/03-train-nano.md) |
| Scale-up train (when capital) | [release/04-train-scaleup.md](release/04-train-scaleup.md) |
| Scorecard & tombstones | [release/05-scorecard-tombstones.md](release/05-scorecard-tombstones.md) |
| Inclusion proof recipe | [release/06-inclusion-proof.md](release/06-inclusion-proof.md) |

### C. Incident + red-team (High / Critical)
| Runbook | Path |
|---------|------|
| Incident playbook | [incident/01-high-critical-playbook.md](incident/01-high-critical-playbook.md) |
| Red-team finding publication | [incident/02-redteam-publication.md](incident/02-redteam-publication.md) |
| Tabletop drill | [incident/03-tabletop-drill.md](incident/03-tabletop-drill.md) |

### D. Commercial
| Runbook | Path |
|---------|------|
| Isolation | [commercial/01-isolation.md](commercial/01-isolation.md) |
| Refuse close-core ask | [commercial/02-refuse-close-core.md](commercial/02-refuse-close-core.md) |
| SKU go-live | [commercial/03-sku-go-live.md](commercial/03-sku-go-live.md) |

### E. Human gates (open when ready)
| Runbook | Path |
|---------|------|
| Gate overview | [gates/00-gates-overview.md](gates/00-gates-overview.md) |
| ttllms.org DNS | [gates/01-dns-org.md](gates/01-dns-org.md) |
| R2 enable | [gates/02-r2.md](gates/02-r2.md) |
| Workers / API routes | [gates/03-workers-routes.md](gates/03-workers-routes.md) |
| Entity + covenant | [gates/04-entity-covenant.md](gates/04-entity-covenant.md) |

## Quick commands (repo root)

```bash
python3 -m pytest -q
python3 scripts/check_seal_freshness.py          # fail if FREE_CORE_SEAL stale
python3 scripts/check_data_cards.py              # Domain 3 machine-check
python3 scripts/public_verify_harness.py         # unpaid offline proof surface
python3 scripts/oneshot_verify_all.py
python3 scripts/redteam_nano_harness.py
python3 scripts/domain_scorecard_all.py
python3 scripts/check_public_urls.py             # live HTTP inventory (network)
make fine-grain                                  # rebuild catalogs + reseal + tests
python3 -m free_core.provenance.cli verify --manifest manifests/FREE_CORE_SEAL.json --base .
```

## Fine-grain remaining gaps
After handbook load-paths: [FINE_GRAIN_GAPS.md](FINE_GRAIN_GAPS.md) — ethos-filtered worklist (proof surface, domain rituals, commercial schemas, human gates). Not soft-tissue “done.”

## Hard gates vs Grok placeholders
- **Hard only (cannot write closed):** [../HARD_TECHNOLOGICAL_GATES.md](../HARD_TECHNOLOGICAL_GATES.md)
- **Writable examples (human check):** [../placeholders/00-INDEX.md](../placeholders/00-INDEX.md)

## Contact
md@0265.au · https://ttllms.com/status
