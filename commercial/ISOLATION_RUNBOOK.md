# Commercial arm isolation runbook (founding turn 17)

## Hard rules
1. Separate infrastructure identity, databases, and signing keys from public core.
2. Customer compromise must not alter public skeleton; public compromise must not leak tenant data.
3. Same provenance philosophy *inside* customer boundary without publishing private weights/data.
4. Red-team commercial surface with equal intensity to public transparency layer.
5. No commercial feature may require closing public TTLLM / basic ttlink / manifests.

## Checklist before any paid feature ships
- [ ] Boundary Specification updated if needed (Domain 8)
- [ ] Decision Log entry (Domain 1)
- [ ] Tenant isolation design reviewed
- [ ] Signing keys not shared with public release keys
- [ ] Contracts lack core-closure clauses
- [ ] Scorecard row: commercial impact on free core = none
