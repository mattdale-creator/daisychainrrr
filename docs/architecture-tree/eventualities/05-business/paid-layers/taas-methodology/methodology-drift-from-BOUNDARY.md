# taas-methodology → methodology-drift-from-BOUNDARY

**Path:** `05-business/paid-layers/taas-methodology/methodology-drift-from-BOUNDARY`

## Failure mode
methodology-drift-from-BOUNDARY for paid SKU **taas-methodology**.

## Boundary test
Does remediation require closing free public core? If yes, **reject** the feature (Domain 8 precedence).

## Detection / response
- Log Domain 1 if product decision
- Log Domain 5 if incident
- Update BOUNDARY attestation if edge case

## Free core
Public weights/data/ttlink/basic stream remain free.
