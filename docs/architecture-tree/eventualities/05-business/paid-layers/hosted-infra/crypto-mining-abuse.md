# hosted-infra → crypto-mining-abuse

**Path:** `05-business/paid-layers/hosted-infra/crypto-mining-abuse`

## Failure mode
crypto-mining-abuse for paid SKU **hosted-infra**.

## Boundary test
Does remediation require closing free public core? If yes, **reject** the feature (Domain 8 precedence).

## Detection / response
- Log Domain 1 if product decision
- Log Domain 5 if incident
- Update BOUNDARY attestation if edge case

## Free core
Public weights/data/ttlink/basic stream remain free.
