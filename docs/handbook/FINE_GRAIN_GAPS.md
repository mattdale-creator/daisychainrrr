# Fine-grain gaps (ethos-aligned)

**Updated:** 2026-08-08 (execution wave)  
**After:** Human handbook load-paths complete (`00-HANDBOOK-INDEX.md`)  
**Rule:** Prefer precise unfinished bone over soft-tissue “done.” This is a **worklist**, not a claim that capital/entity/model scale are closed.

## Executed this wave (no longer soft gaps)
| Item | Artefact |
|------|----------|
| Seal freshness | `scripts/check_seal_freshness.py` + CI + `free_core/provenance/seal_targets.py` |
| DATA_CARD machine-check | `scripts/check_data_cards.py` + tests |
| Stream event catalog | `free_core/stream/catalog.py` → `docs/specs/artefacts/stream/STREAM_EVENT_CATALOG.md` |
| Synthetic incident stream | `examples/stream/incident_drill_log.json` |
| Public URL inventory | `ops/public_url_inventory.json` + `scripts/check_public_urls.py` |
| Inclusion proof recipe | `docs/handbook/release/06-inclusion-proof.md` + harness |
| Canary/QueryGuard policy | `docs/security/CANARY_QUERYGUARD_POLICY.md` |
| Domain 1 monthly audit | `docs/specs/artefacts/01/audits/MONTHLY_AUDIT_2026-08.md` |
| Eval honesty template + packs | `free_core/eval/honesty.py` + `models/*/cards/EVAL_HONESTY.*` |
| Supply lock | `registers/supply-chain/SUPPLY_LOCK.json` |
| security intake | `docs/security/REPORT_INTAKE.md` + `site/security-policy.html` |
| ASSET_INVENTORY succession | `continuity/ASSET_INVENTORY.md` |
| Finetune lineage schema | `free_core/schemas/finetune_lineage.schema.json` |
| Public unpaid verify | `scripts/public_verify_harness.py` |
| Term-sheet red lines | `docs/security/TERM_SHEET_RED_LINES.md` |
| Mixture / checkpoint / reproduce specs | `docs/security/DATA_MIXTURE_*` etc. |
| CI verify workflow | `.github/workflows/verify.yml` |
| Self-hash seal fix | `free_core/release/pipeline.py` excludes manifests/ |

## Ethos filter (what deserves more grain)

| Deserve fine grain | Do **not** expand into novels |
|--------------------|-------------------------------|
| Free-core verification paths | 10k unique eventuality essays |
| BOUNDARY refuse / isolation | Marketing narrative |
| Incident clocks + registers | Fake green status |
| Key / seal trust story | Demo keys as production |
| Data legality (Domain 3) | Capability theater for nano |
| Human gates with exact steps | Agent-pretend DNS/entity |
| Scorecard MET/PARTIAL/TOMBSTONE | Silent omission |

---

## P0 — Proof surface (product *is* the proof)

### 1. FREE_CORE_SEAL freshness discipline
- **Gap:** Seal goes stale on any docs/README/site change; humans may claim green without reseal.
- **Fine grain needed:** CI job or pre-commit that fails if `seal-repo` targets differ from `FREE_CORE_SEAL.json`; status page shows merkle root + seal time.
- **Handbook already:** `release/02-seal-and-verify.md` staleness rule — **enforce in tooling**, not only prose.

### 2. Public HTTP verify / ttlink route honesty
- **Gap:** Pages Functions routing historically flaky (HTML/405); workers routes gated.
- **Fine grain:** Enumerate every public URL that claims API behaviour; for each: expected status, content-type, sample curl, tombstone if broken.
- **Gate:** `gates/03-workers-routes.md`

### 3. Canary + QueryGuard production parameters
- **Gap:** Canary string and QueryGuard limits exist in code; public **policy card** (rates, abuse, research access) is thin.
- **Fine grain:** Domain 10/7 note: published limits, false-positive path, how researchers request higher quota without destroying transparency.

### 4. Stream schema completeness
- **Gap:** Nano seal emits a subset of event types; no normative catalog of required events per release class.
- **Fine grain:** Table: event_type → required payload fields → when mandatory (nano vs scale) → verify rule.

### 5. Inclusion-proof UX
- **Gap:** CLI `proof` exists; site/demo path for “prove this file is in FREE_CORE_SEAL” is not first-class for non-CLI humans.
- **Fine grain:** One demo page or scripted recipe with copy-paste commands + expected JSON shape.

---

## P1 — Ten domains (ops ritual, not more stubs)

### 6. Domain 1 — first real monthly audit
- **Gap:** Procedure written; **no dated audit execution** yet.
- **Fine grain:** One filled audit note under `docs/specs/artefacts/01/` with commit range checked.

### 7. Domain 2 — ownership / funding register depth
- **Gap:** Ownership register path exists; funding transparency still pre-entity thin.
- **Fine grain:** Exact fields for pre-revenue (who controls domains, GH, CF, keys) vs post-raise (instruments, % without doxxing where law requires privacy + tombstone).

### 8. Domain 3 — DATA_CARD machine-check
- **Gap:** DATA_CARDs are markdown; no automated “every train source has URL+license+hash” gate in CI.
- **Fine grain:** Schema + pytest that fails seal if card rows missing hashes.

### 9. Domain 4 — eval honesty pack standard
- **Gap:** Nano eval prioritises transparency over capability (correct) but **comparison language** vs founding OLMo ambition can drift.
- **Fine grain:** Fixed template: tasks run, scores, **explicit non-claims**, link to tombstones; required in every `seal_release`.

### 10. Domain 5 — first High path with real stream event
- **Gap:** Tabletop done; production incident path unexercised (good), but stream event types for incidents not sealed into public examples.
- **Fine grain:** Example incident stream events in `examples/` marked synthetic.

### 11. Domain 6 — compensation bands (pre-hire)
- **Gap:** Spec exists; no numeric bands because no payroll — OK, but **influence threshold** language needs one worked example.
- **Fine grain:** “If contractor X can merge to free_core or hold signing key → public role disclosure template.”

### 12. Domain 7 — supply-chain SBOM for free_core
- **Gap:** Register path; Python deps not continuously hashed into public supply artefact.
- **Fine grain:** Generate and seal `supply/REQUIREMENTS.lock.sha256` or equivalent on release.

### 13. Domain 8 — annual attestation calendar
- **Gap:** Attestation required once selling; pre-revenue relies on BOUNDARY + decisions.
- **Fine grain:** Calendar row + owner even pre-revenue (“next review date”) so it cannot be forgotten at first invoice.

### 14. Domain 9 — succession for every asset row
- **Gap:** `ASSET_INVENTORY.md` lists assets; succession contacts incomplete without entity.
- **Fine grain:** Per asset: primary, backup, recovery steps if founder unavailable 30 days (still draft-labelled).

### 15. Domain 10 — external report intake path
- **Gap:** Email md@0265.au; no public `security.txt` workflow detail beyond file presence.
- **Fine grain:** security.txt + site page: scope, safe harbor intent language (counsel), PGP optional later, SLA clocks aligned Domain 5/10.

---

## P2 — Commercial bone (before first dollar)

### 16. SKU “free core unaffected” test harness
- **Gap:** Checklists are human; no automated test that public verify paths stay unpaid.
- **Fine grain:** Script that hits public URLs/CLIs without auth and asserts verify still works.

### 17. Contract clause bank (refuse + allow)
- **Gap:** Refuse template exists in handbook; no counsel-reviewed clause bank.
- **Fine grain:** After entity: appendix of must-have / must-not clauses for SOWs (still BOUNDARY-subordinate).

### 18. Lineage format for certified fine-tunes
- **Gap:** SKU designed; **exact lineage manifest schema** (base merkle, delta description, what stays private) not frozen.
- **Fine grain:** JSON schema under `free_core/schemas/` + example.

---

## P3 — Human / capital gates (cannot agent-close)

| Gap | Detail still needed when human opens |
|-----|--------------------------------------|
| DNS Edit | Confirm both zones Active; HTTP→HTTPS; apex edge cases |
| R2 | Public vs private bucket policy text; malware scanning stance |
| Workers | Stable route map; rate limits; CORS if browser demos |
| Entity | Jurisdiction; who signs covenant; IP assignment |
| HSM / multi-sig | Ceremony script; recovery; demo key decommission notice |
| Capital | BOUNDARY-safe term sheet red lines (written before pitch) |
| Standing red team | Scope SOW; publication rights; retainer vs bounty |

Handbooks for gates exist under `docs/handbook/gates/` — **execution** is the remaining grain.

---

## P4 — Scale training (deferred epoch)

### 19. Data mixture publication format (pre-scale)
- **Gap:** Nano uses PG; scale needs mixture card that can be re-hashed at TB scale.
- **Fine grain:** Spec for mixture manifest: source id, license, hash or hash-tree root, sampling rate, known exclusions.

### 20. Checkpoint publication policy
- **Gap:** Dense nano ckpts OK; scale needs interval/cost policy before train starts.
- **Fine grain:** Decision template: which steps public, cold-storage SLA, verify cost.

### 21. Third-party reproduce grant
- **Gap:** Ethos wants others to re-hash; no “reproduce budget” or partner lab path.
- **Fine grain:** One-page invite: what we publish, what recompute costs, contact.

---

## Explicit non-gaps (do not gold-plate)

- Writing unique prose for every combinatorial eventuality leaf
- Claiming nano is frontier
- Building full corporate HR before entity
- Fake HSM or fake DNS “success”
- Red-team as vandalism theater (constructive QA only)

---

## Suggested next human-implementable slices (ordered)

1. **CI seal freshness + DOMAIN 3 data-card check** (P0.1 + P1.8)  
2. **Public URL inventory with curl expectations** (P0.2)  
3. **First Domain 1 monthly audit note** (P1.6)  
4. **Stream event catalog + synthetic incident examples** (P0.4 + P1.10)  
5. **Certified-finetune lineage schema** (P2.18) when commercial path is real  
6. Open human gates when ready (DNS → R2 → entity → keys)

---

## Related
- Handbook index: `docs/handbook/00-HANDBOOK-INDEX.md`
- Human gates: `ops/HUMAN_GATES.md`
- Gap audit vs founding: `docs/audits/GAP_AUDIT_vs_FOUNDING_TRANSCRIPT.md`
- Decision: D-0022 (handbook over 10k novels)
