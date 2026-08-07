# TTLLM — Totally Transparent LLMs

**Down to the binary. Down to the bone.**

> The product *is* the proof.

Primary site: **https://ttllms.com** · secondary **https://ttllms.org**  
Project email: **md@0265.au**  
Pages: **https://ttllms.pages.dev**  

Public monorepo: [`mattdale-creator/daisychainrrr`](https://github.com/mattdale-creator/daisychainrrr)  
Intended home domain: **ttllms.com**

This repository is the organisational skeleton for the TTLLM project: free public core, **ttlink** human-viewable provenance, cryptographic manifests, commercial boundary rules, and the founding conversation published without soft tissue.

---

## Ethos (non-negotiable)

1. **Down to the bone** — delete soft tissue. Prefer artefacts over narrative.
2. **Free public core** — weights, data, checkpoints, training code, basic ttlink, public stream: free. Never monetise by closing the skeleton.
3. **Monetise outside the core** — hosted SLAs, enterprise audit, TaaS, certified fine-tunes, analysis tools, methodology licensing.
4. **Cryptographic provenance** — content-addressed artefacts, Merkle manifests, signed releases. Anyone can re-hash and verify.
5. **Organisation as transparent as the model** — decisions, failures, funding, incentives: published by default where possible.
6. **Publish the generative process** — founding conversation and process logs are part of the skeleton.

---


---

## Architecture tree (architect-complete)

Full executable HOWTO for every founding branch (ethos, product, technology, security, business, ten transparency domains, org, ops, epochs 00–05):

- **[docs/architecture-tree/00-MASTER-TREE.md](docs/architecture-tree/00-MASTER-TREE.md)** — start here
- [STATUS.md](docs/architecture-tree/STATUS.md) — rollup
- [ARCHITECT-COMPLETE.md](docs/architecture-tree/10-checklists/ARCHITECT-COMPLETE.md) — checklist
- [HUMAN-CAPITAL-GATES.md](docs/architecture-tree/10-checklists/HUMAN-CAPITAL-GATES.md) — what only humans/money open

Vault mirror (local SoT): `TTLLMS.com BUILD/11-architecture-tree/`

## Repository map (every major branch)

```
daisychainrrr/
├── README.md                          ← you are here
├── LICENSE                            ← Apache-2.0 + free-core notice
├── pyproject.toml                     ← installable free-core tools
├── Makefile
├── docs/
│   ├── manifesto.md                   ← public principle
│   ├── glossary.md
│   ├── architecture/
│   ├── architecture-tree/             ← FULL HOWTO tree (architect-complete)
│   │   ├── 00-MASTER-TREE.md
│   │   ├── 00-meta/ … 10-checklists/
│   │   └── STATUS.md
│   │   ├── free-public-core.md
│   │   ├── ttlink.md
│   │   ├── stream.md
│   │   ├── matrix-surface.md          ← visual is surface; links are real
│   │   └── commercial-layers.md
│   ├── business/
│   │   ├── pitch.md
│   │   ├── sales-pitch.md
│   │   ├── financial-model-10y.md
│   │   ├── mba-business-plan.md
│   │   └── paid-layers.md
│   ├── culture/
│   │   ├── down-to-the-bone.md
│   │   ├── company-culture.md
│   │   └── remember-youre-on-drugs.md
│   ├── security/
│   │   ├── threat-model.md
│   │   ├── red-team-standard.md
│   │   └── pliny-cco-notes.md
│   └── specs/                         ← Total Transparency Specification
│       ├── 00-master.md
│       ├── 01-governance.md
│       ├── 02-ownership-funding.md
│       ├── 03-data-governance.md
│       ├── 04-evaluation.md
│       ├── 05-incident-disclosure.md
│       ├── 06-compensation.md
│       ├── 07-supply-chain.md
│       ├── 08-boundary-rules.md
│       ├── 09-stewardship.md
│       └── 10-red-team-publication.md
├── free_core/                         ← reference implementation (public)
│   ├── provenance/                    ← SHA-256, Merkle, sign, verify
│   ├── ttlink/                        ← span → source linking (reference)
│   ├── stream/                        ← public stream schema + demo
│   └── schemas/
├── commercial/                        ← boundary only (no closed secrets)
│   └── BOUNDARY.md                    ← what may be private; what may not
├── founding/                          ← generative process made public
│   ├── conversation/                  ← SuperGrok founding thread
│   ├── proof_rip/                     ← screenshot time/origin evidence
│   └── PROVENANCE.md                  ← binds conversation + proof_rip
├── site/                              ← static manifesto site for ttllms.com
├── prompts/                           ← frozen founding prompt battery
├── registers/                         ← empty public registers (append-only)
├── continuity/                        ← stewardship covenant stubs
└── tests/
```

---

## Quick start

```bash
# install free-core tools
pip install -e ".[dev]"

# build a Merkle manifest of any directory
ttllm-manifest hash ./path/to/artefacts
ttllm-manifest verify ./path/to/artefacts --manifest manifests/example.json

# demo ttlink over a tiny corpus
ttllm-ttlink index examples/corpus
ttllm-ttlink query "exact span text"

# run tests
make test

# seal this repository's free-core tree
make seal
```

---

## Founding proof

| Layer | Location |
|-------|----------|
| Full founding conversation | [`founding/conversation/`](founding/conversation/) |
| Device capture + metadata (Proof RIP) | [`founding/proof_rip/`](founding/proof_rip/) |
| Binding provenance document | [`founding/PROVENANCE.md`](founding/PROVENANCE.md) |

Conversation ID: `8a75e0b4-1a78-4926-a7e5-7227e9ff3b33`  
Title: *Totally Transparent LLMs: OLMo and LLM360*  
Created: `2026-08-07T15:48:49Z`

---

## Related prior art (honest attribution)

- **Ai2 OLMo / OLMoTrace** — full stack openness + output→data linking
- **LLM360** — dense intermediate checkpoints as standard
- **IBM Granite / Stanford FMTI** — structured transparency scoring

TTLLM’s contribution is organisational: the company itself must go down to the bone, stream the real process, and monetise only outside a free public core.

---

## Status

Scaffold + reference tools + full specification set + founding publication.  
Not yet: production-scale model training, multi-TB suffix index, live public stream infrastructure.

Built into this tree: **2026-08-07 18:06:32 UTC**
