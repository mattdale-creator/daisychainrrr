# certified-finetunes → silent-customer-data-in-public

**Path:** `05-business/paid-layers/certified-finetunes/silent-customer-data-in-public`

## Failure mode
silent-customer-data-in-public for paid SKU **certified-finetunes**.

## Boundary test
Does remediation require closing free public core? If yes, **reject** the feature (Domain 8 precedence).

## Detection / response
- Log Domain 1 if product decision
- Log Domain 5 if incident
- Update BOUNDARY attestation if edge case

## Free core
Public weights/data/ttlink/basic stream remain free.
