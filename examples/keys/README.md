# Demo keys — not production roots of trust

## What these are
| File | Purpose |
|------|---------|
| `demo.public.pem` | Public key for **tutorial** signature verification |
| `demo.private.pem` | Private key for **local demos only** |

## Ethos rules
1. **Never** describe these as HSM-backed or production roots of trust on status/marketing surfaces.  
2. **Never** use demo private key for a release you claim is production-signed.  
3. Production ceremony is hard gate **T5** — see `docs/placeholders/security/KEY_CEREMONY_TRANSCRIPT_EXAMPLE.md` (full text on site).  
4. Public verify of **unsigned** Merkle seals remains valid content addressing; signatures are an additional layer.

## Tutorial verify pattern
```bash
python3 -m free_core.provenance.cli verify --manifest manifests/FREE_CORE_SEAL.json --base .
# optional, if you have a signed artefact + matching keys:
# python3 -m free_core.provenance.cli verify-sig --signed ... --pubkey examples/keys/demo.public.pem --base .
```

## Rotation
Before any production release claiming signatures: multi-party or HSM policy, publish new public key, retire demo-as-trust language on https://ttllms.com/status.
