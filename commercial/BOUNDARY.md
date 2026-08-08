# Public/Commercial Boundary Specification (Domain 8)

**Version:** 0.2.0  
**Status:** Normative  
**Precedence:** Free public core > commercial convenience  

## Free public core (must remain free & public)
- Model weights and intermediate checkpoints under the TTLLM promise (including ttllm-nano)
- Training data / mixture docs and DATA_CARD (Domain 3 tombstones where required)
- Training code for public releases
- Basic ttlink for public models (query over public corpus)
- Cryptographic manifests and verification tooling
- Public stream of process events for public core
- Transparency specs, decision logs, founding conversation
- Evaluation artefacts used for public capability claims

## Allowed commercial privacy
- Customer prompts and private documents
- Customer VPC configs and tenant secrets
- Private commercial fine-tune weights *only if* lineage to public core is published and customer-private data is not laundered into silent public-core claims
- Non-core HR below influence thresholds (bands still public per Domain 6)
- Proprietary UX/ops that does not gate core verification
- Contract pricing negotiations
- Internal commercial metrics not used as public capability claims

## Prohibited opacity
- Paywall on verifying a public-core claim
- Secret fine-tune claiming TTLLM inheritance without lineage
- Undisclosed training data for a TTLLM-marketed model
- Quiet removal of public artefacts without Domain 3 process
- Investor or customer terms that force core closure
- Using commercial APIs to silently alter public index/manifests

## Boundary change process
Any movement of an artefact from public → private commercial privacy is a material Domain 1 decision and requires updated Boundary Specification before implementation.

## Attestation
Annual public boundary attestation required once selling. Pre-revenue: this document + decision log entries suffice.
