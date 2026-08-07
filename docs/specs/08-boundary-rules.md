# 8. Boundary Rules Between Public Core and Commercial Layers

**TTLLM Total Transparency Specification**

## Purpose
Define the hard line so commercial needs cannot erode the free core.

## Artefacts
- Public/Commercial Boundary Specification (this document + `commercial/BOUNDARY.md`)
- Allowed Commercial Privacy List
- Prohibited Opacity List
- Boundary Decision Log

## Hard rules
1. Public core artefacts stay free and re-hashable.
2. Paid features may not be the only path to verify core claims.
3. Fine-tunes sold commercially that claim TTLLM inheritance must publish their delta lineage.
4. Moving a feature from free→paid if it removes a core guarantee requires public decision + waiting period.

## Tensions
- Edge-case fine-tunes; rate limits vs public access; customer confidential prompts (allowed private) vs model weights (public)
