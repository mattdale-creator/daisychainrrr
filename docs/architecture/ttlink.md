# ttlink architecture

**Updated:** 2026-08-07

## Purpose

Make provenance **usable**. Exact (or honestly approximate) links from a model output span to training or reference sources, with document hashes bound into Merkle manifests.

## Reference implementation

Package: `free_core.ttlink`

```bash
ttllm-ttlink index examples/corpus -o examples/ttlink_index.json
ttllm-ttlink query "free public core"
```

Browser demo: https://ttllms.com/demo.html

## Production path (deferred)

Suffix-array / FM-index / infini-gram class systems over multi-trillion token corpora. See architecture-tree `03-technology/05-ttlink-engine-production.md` and Epoch 03.

## Honesty rules

- Exact match vs approximate must be labeled  
- Basic public linking for free-core models is not paywalled  
- Index leaves bind to sha256 of source docs  
