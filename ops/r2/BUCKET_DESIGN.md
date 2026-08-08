# R2 bucket design (pre-enable)

| Item | Value |
|------|--------|
| Proposed bucket | `ttllm-public-releases` |
| Visibility | Public read for free-core artefacts only |
| Forbidden | Customer prompts, tenant weights, secrets |
| Naming | `releases/<model>/<version>/<file>` |
| Integrity | SHA-256 in RELEASE_MANIFEST or separate object manifest |
| Versioning | On |
| Delete policy | Domain 3 process only; no silent wipe of published bone |

## Related objects (later)
- `ttllm-public-ttlink-shards` — large shard packs when scale exists
- Private commercial buckets — **separate** account prefix / isolation (commercial wall)
