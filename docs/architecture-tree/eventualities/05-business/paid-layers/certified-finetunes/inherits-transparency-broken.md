# certified-finetunes → inherits-transparency-broken

**Path:** `05-business/paid-layers/certified-finetunes/inherits-transparency-broken`

## Failure mode
inherits-transparency-broken for paid SKU **certified-finetunes**.

## Boundary test
Does remediation require closing free public core? If yes, **reject** the feature (Domain 8 precedence).

## Detection / response
- Log Domain 1 if product decision
- Log Domain 5 if incident
- Update BOUNDARY attestation if edge case

## Free core
Public weights/data/ttlink/basic stream remain free.
