# analysis-workbench → bulk-extract-via-ui

**Path:** `05-business/paid-layers/analysis-workbench/bulk-extract-via-ui`

## Failure mode
bulk-extract-via-ui for paid SKU **analysis-workbench**.

## Boundary test
Does remediation require closing free public core? If yes, **reject** the feature (Domain 8 precedence).

## Detection / response
- Log Domain 1 if product decision
- Log Domain 5 if incident
- Update BOUNDARY attestation if edge case

## Free core
Public weights/data/ttlink/basic stream remain free.
