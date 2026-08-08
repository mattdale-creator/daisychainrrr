# Decision Log (append-only)

| ID | Date (UTC) | Title | Options | Rationale | Outcome | Roles |
|----|------------|-------|---------|-----------|---------|-------|
| D-0001 | 2026-08 | Publish founding conversation | Delay / publish | Founding ethos: generative process visible | Publish in repo+site | founder |
| D-0002 | 2026-08 | Free core never paywalled | Dual-license close | Bone must stay public | BOUNDARY.md | founder |
| D-0003 | 2026-08 | Primary domain ttllms.com | .org only | Brand + continuity | Own both; .com primary | founder |
| D-0004 | 2026-08 | Architect tree + public HOWTOs | Silent private plan | Down to the bone plan | docs/architecture-tree | founder |
| D-0005 | 2026-08 | free_core 0.2 reference tools | Docs only | Product is the proof | Ship CLIs + demos | founder |
| D-0006 | 2026-08 | Demo keys tutorial-only | Fake HSM root | No false trust | examples/keys README | founder |
| D-0007 | 2026-08-08 | Admit prior completion claims were soft tissue | Defend shallow ship | Radical honesty | GAP_AUDIT + deep rebuild | founder+agent |
| D-0008 | 2026-08-08 | Ship Mac-local ttllm-nano with PG public-domain data | Wait for capital 32B | Conversation requires working skeleton shape | models/ttllm-nano | founder+agent |
| D-0009 | 2026-08-08 | Domain specs = full founding turn plans | Keep thin stubs | Turns 37–46 are normative | docs/specs/01–10 | founder+agent |
| D-0010 | 2026-08-08 | Ship ttllm-nano-v2 with pure-Python BPE | Stay on char-only nano | Better tokenizer still fully public/verifiable | models/ttllm-nano-v2 | founder+agent |
| D-0011 | 2026-08-08 | Publish Domain quarterly bootstrap report | Wait for entity | Honesty about partial ops history | docs/specs/artefacts/00_QUARTERLY_BOOTSTRAP_2026Q3.md | founder+agent |
| D-0012 | 2026-08-08 | Local ttlink HTTP API (stdlib) | Wait for Workers | Runnable reference without cloud | free_core/ttlink/server.py | founder+agent |
| D-0013 | 2026-08-08 | Expand PG corpus to 6 sources | Stay at 3 | More verifiable public-domain bone | models/*/data | founder+agent |
| D-0014 | 2026-08-08 | Ship nano-v3 on expanded data | Only retrain BPE v2 | Faster iteration on data expansion | models/ttllm-nano-v3 | founder+agent |
| D-0015 | 2026-08-08 | Deploy ttlink API via Pages Functions | Wait for workers.dev | Public query path without subdomain | site/functions | founder+agent |
| D-0016 | 2026-08-08 | Domain artefact packs filled for 1-10 | Leave scaffolds empty | Down to the bone ops | docs/specs/artefacts | founder+agent |
| D-0017 | 2026-08-08 | Continuous bone loop: reseal all nanos + master domain scorecard | Stop | Product is the proof | free_core/release/pipeline.py | agent |
| D-0018 | 2026-08-08 | Cross-product + actor eventuality matrices | Thin tree | Founding demand for deep paths | docs/architecture-tree/eventualities | agent |
| D-0021 | 2026-08-08 | Fill eventuality leaves with real procedures | Leave path stubs | User: real filling of leaves; remove structure-without-content | docs/architecture-tree/eventualities/ | agent |
| D-0022 | 2026-08-08 | Human load-path handbook over 10k leaf novels | Unique essay per eventuality | Ethos: implementable procedures + shared skeleton; bespoke where required | docs/handbook/ (domains, release, incident, commercial, gates) | founder+agent |
| D-0023 | 2026-08-08 | Execute fine-grain proof automation to the wall | Stop at handbook prose | Product is the proof; cover until capital/entity/token gates only | check_seal_freshness, data_cards, public_verify, stream catalog, supply lock, CI verify.yml, reseal nanos | founder+agent |
