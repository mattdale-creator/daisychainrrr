# ttlink Architecture

## Purpose

Make the real process **human-viewable**: from any output span (or decision id) to source documents, checkpoint versions, and provenance.

## Layers

1. **Corpus layer** — content-addressed documents/shards (`sha256`)  
2. **Index layer** — exact-match structure (production: suffix array / FM-index / infini-gram family; reference: substring index in this repo)  
3. **Binding layer** — Merkle manifest of indexed docs + index shards  
4. **Query layer** — span → hits with offsets, context, doc hashes  
5. **Surface layer** — UI/API/Matrix visual that *only* points at real links  

## Non-goals for the free core

- Pretty lies  
- Approximate “inspired by” without exact match disclosure when exact match exists  
- Enterprise-only linking for the public model  

## Reference implementation

See `free_core/ttlink/` — intentionally small-scale, interface-complete, testable.
