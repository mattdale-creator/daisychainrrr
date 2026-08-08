# Fundraise pitch — Totally Transparent LLMs (full ethos draft)

> **Written by Grok - Human checking required**  
> Written as if by the founder for serious capital, at founding-conversation depth (turns 12–23: free core + monetise outside; scholarly + extreme business nous; math/physics/code; never close the bone).  
> **Hard gate T8** until real capital moves. This page is a diligence-ready *draft*, not a live raise or securities offer in any jurisdiction.  
> Human check target: “Yes — this matches what we believe and what we have already built,” or mark line-level corrections.

---

## 0. One sentence

We build **Totally Transparent LLMs**: systems whose free public core (weights and checkpoints under the TTLLM promise, training code, data composition or lawful access path, metrics, cryptographic manifests, basic **ttlink**, and public process stream) stays inspectable and free forever — and we monetise only the institutional layers that sit **outside** that core without ever requiring its closure.

---

## 1. The problem (epistemic, not marketing)

The dominant trajectory of large-scale AI has produced systems of extraordinary capability wrapped in **structural opacity**. Training data mixtures, intermediate states, optimisation decisions, and provenance remain largely inaccessible. Even many “open” releases stop at final weights. The result is a growing epistemic gap: as these systems mediate knowledge work, decision-making, and culture, the public — and most institutions — lack a rigorous way to inspect what the systems are actually made of.

In that gap, mystification thrives. Anthropomorphism, ungrounded trust, and ungrounded fear all flourish when the skeleton stays hidden. Soft tissue (narrative, aesthetic, “trust us”) substitutes for load-bearing structure.

**TTLLM rejects that substitution.** The only durable way for humans to know AI is a machine is for an organisation to produce a system whose skeleton is continuously available for inspection — and to hold the organisation to the same standard.

This is not transparency as PDF documentation. It is transparency as **topology optimisation** applied to knowledge systems: the systematic removal of every non-load-bearing layer until only the essential structure remains. Founding language: **down to the bone** / **down to the binary**.

---

## 2. The product definition (load-bearing)

A **Totally Transparent LLM (TTLLM)** release, at the standard we defend, includes:

| Layer | Requirement | Why it is load-bearing |
|-------|-------------|------------------------|
| Weights + intermediate checkpoints | Public under the TTLLM promise (or honest tombstone) | Without intermediates, “open weights” is still a black box of the path |
| Training code + hyperparameters | Public for public releases | Reproducibility of process, not mythology |
| Data composition / lawful access path | DATA_CARD, hashes, licenses, mixture docs | Capability claims without data path are soft tissue |
| Metrics / process logs | Public loss curves, train events | The stream must be real, not aesthetic |
| Cryptographic provenance | SHA-256 leaves, Merkle manifests, optional signatures | Anyone can re-hash; trust is not a brand claim |
| **ttlink** | Human-viewable linkage from spans to source docs | “Human viewable” is operational, not a slogan |
| Public stream | Hash-chained process events | Matrix irony inverted: show real data, not cosplay rain |
| Org transparency | Domains 1–10 | The organisation itself must be as transparent as the model |

**Prior art we stand on, not against:** Ai2 OLMo / OLMoTrace and LLM360 (dense intermediate checkpoints). We add organisational transparency domains, BOUNDARY discipline, and human-viewable ttlink as first-class product surface.

**Honesty about scale today (non-negotiable in any pitch):**  
We have shipped **Mac-scale nano models** that implement the *shape* of total transparency (public-domain data, open train code, dense checkpoints, metrics, seals, ttlink, stream, eval honesty packs). Nano is **not** OLMo-class capability. Claiming otherwise violates ethos. Capital (hard gate **T8**) is required for competitive-scale public training — and that capital must never purchase the right to close the free core.

---

## 3. What already exists (proof, not promise)

Diligence can start tonight without an NDA:

```bash
git clone https://github.com/mattdale-creator/daisychainrrr
cd daisychainrrr
python3 -m pip install -e ".[dev,crypto]"
python3 scripts/public_verify_harness.py
python3 scripts/ttllm_status.py --quiet-ok
python3 scripts/redteam_nano_harness.py
```

Public site (updated as we ship): **https://ttllms.com**  
- Status, hard gates, free core, demo (real ttlink + stream + seal snapshot), economics, movement, founding prompts  
- Canonical BOUNDARY: `commercial/BOUNDARY.md`  
- Domains 1–10 specs, handbook load-paths, decision log, incident/red-team registers  
- free_core 0.6 tools: manifests, stream, ttlink, QueryGuard, canaries, scorecards  

**The product is the proof.** Investors do not have to believe a transparency story; they can re-hash it.

---

## 4. Business model (monetise outside the bone)

### 4.1 Free public core (never the SKU)

Must remain free and public:

- Model weights and intermediate checkpoints under the TTLLM promise  
- Training data / mixture docs and DATA_CARDs (Domain 3 tombstones where required)  
- Training code for public releases  
- Basic ttlink for public models  
- Cryptographic manifests and verification tooling  
- Public stream of process events for public core  
- Transparency specs, decision logs, founding conversation  
- Evaluation artefacts used for public capability claims  

**Precedence (public, non-negotiable):**  
**Free public core and BOUNDARY take precedence over commercial convenience and revenue.**

### 4.2 Paid layers (outside only)

Institutions pay for operational reality once they accept inspectability:

| Layer | What they buy | What they never buy |
|-------|---------------|---------------------|
| Hosted / managed infra | SLA, capacity, private networking, ops | Exclusive free-core weights |
| Enterprise ttlink / audit | Compliance exports, richer ops, governance integration | Paywalled verification of public claims |
| Certified fine-tunes | Supported derivatives with **published lineage** to public core | Silent inheritance without lineage |
| Transparency-as-a-service | Methodology transfer to their stacks | Permission to close *our* core |
| Analysis workbenches | Tools on the public skeleton | Private alteration of public indexes |
| Priority support | Human expertise and response times | Side letters that force opacity |

Isolation rules: tenant data never launders into free-core claims; commercial signing keys ≠ public release keys; customer compromise must not rewrite public seals.

### 4.3 Why this is commercially coherent

Closed labs optimise capability under secrecy. Most open efforts stop at weights. We optimise **verifiable structure**. In a world of regulation, procurement, and institutional distrust of black boxes, the organisation that can *prove* what its model is made of — repeatedly, under adversarial pressure, without retreating when revenue appears — holds a structural advantage.

The moat is not a single release. It is the **accumulated public record** of having done the work under the same standard, plus process switching costs for institutions that wire inspectability into governance.

---

## 5. Economics and trajectory (honest)

### 5.1 Nano actuals (already measured)

Local Mac trains publish wall-clock, estimated kWh, and checkpoint bytes (`scripts/nano_cost_ledger.py`). Cloud GPU invoice for nano demo: **$0**. That is honesty, not a substitute for scale budgets.

### 5.2 Scale (requires T8 capital)

Competitive transparent training is capital-intensive: multi-million-dollar runs on multi-year cadence, plus verifiable indexes, public infra, and standing adversarial function. Early years can run material losses while public proof and first enterprise relationships form. Gross margins on commercial layers can be high once trust compounds; training cost does not scale with revenue the same way pure closed-frontier labs experience if the free core is the trust engine rather than the billable exclusive asset.

Illustrative first-epoch budget ranges and ten-year narrative live in sibling packs (`SCALE_BUDGET_FILLED_EXAMPLE.md`, `TEN_YEAR_FINANCIAL_MODEL_EXAMPLE.md`). Those numbers are **scenarios for human check**, not invoices or guarantees.

### 5.3 What capital is *not* allowed to buy

Any term sheet that:

- Paywalls verification of a public-core claim  
- Forces privatisation of already-public free-core artefacts  
- Grants exclusive control to remove public artefacts without Domain 3 process  
- Requires silent alteration of public indexes/manifests  
- Side-letters free-core closure “later”  

…is rejected. See `TERM_SHEET_EXAMPLE.md` and `docs/security/TERM_SHEET_RED_LINES.md`.

---

## 6. Organisation as demonstration (Domains 1–10)

A TTLLM company cannot be transparent about the model and opaque about itself. Founding turns 30–46 make organisational transparency normative:

1. **Governance** — material decisions public ≤7 days  
2. **Ownership / funding** — influence rights disclosed; no silent side letters  
3. **Data governance** — legal process, DATA_CARDs, tombstones  
4. **Evaluation** — claim gate; no frontier adjectives without artefacts  
5. **Incidents** — same severity ladder for model and transparency-system failures  
6. **Compensation** — influence thresholds; bands for influential roles when payroll exists  
7. **Supply chain** — dependency honesty; sealed supply lock for free_core  
8. **Boundary** — free core > revenue; annual attestation when selling  
9. **Stewardship** — covenant, succession, change-of-control triggers  
10. **Red-team publication** — systematic publication; standing hire is hard gate T10, harness is not a person  

These domains are product surface, not wallpaper.

---

## 7. Security and adversarial standard

Founding demand: frontier-level red-team pressure on **model and transparency infrastructure**. Cryptographic provenance, canaries, QueryGuard, seal freshness automation, and a public findings register exist now. Standing Pliny-class adversarial hire remains hard gate **T10** (SOW/CCO packs are written for human check). Demo keys are **not** production roots of trust (ceremony is hard gate **T5**).

**Remember you are on drugs:** measure; multi-angle check; never declare “complete” while harness is red or hard gates are silently marked closed.

---

## 8. The ask (structure for human fill)

| Field | Example structure (human fills numbers) |
|-------|----------------------------------------|
| Instrument | SAFE / priced equity — **human** |
| Amount | **$ human** (must map to public training + people + RT + legal) |
| Use of funds | Public train compute; people (train/data/CCO); public infra; legal/entity; reserve |
| Board / governance | Must not enable BOUNDARY override without public Domain 1 process |
| Covenant | Free Public Core Covenant attached as schedule |

Diligence checklist for any investor who claims to care about ethos:

1. Run public verify harness  
2. Read BOUNDARY end-to-end  
3. Read hard gates page (what is still open)  
4. Read decision log  
5. Confirm term sheet contains free-core covenants  

---

## 9. Strategic alternative we reject

Continued scaling of systems whose internal structure remains inaccessible by design. We regard that trajectory as strategically unstable and epistemically costly. The corrective is not better marketing of opacity. It is production of systems whose skeleton is available for inspection, sustained by an organisation that holds itself to the same standard **under commercial pressure**.

---

## 10. Closing

We are building the organisation willing to treat radical structural transparency as a non-negotiable engineering and cultural standard, and to construct a commercially robust envelope around that standard without compromising it.

The technical path for the *shape* is already public. The economic path is viable if discipline holds. The remaining variables are **execution under pressure** and the hard gates only humans can open (entity, capital, keys, hire, DNS/R2 where still blocked).

**Contact:** md@0265.au  
**Site:** https://ttllms.com  
**Repo:** https://github.com/mattdale-creator/daisychainrrr  

---

*Written by Grok - Human checking required — full text also published on https://ttllms.com/placeholders/*
