# Data governance policy

**Updated:** 2026-08-08

## Principles
1. Public training data for TTLLM-branded releases stays public.
2. Removal/alteration is exceptional and must be logged (Domain 3).
3. Prefer tombstone over silent deletion.
4. Document sources, licenses, filters, and mixture for every release.
5. Nano releases use Project Gutenberg public-domain texts with full URL + sha256 provenance.

## Selection
- Prefer public domain / clearly licensed corpora for Mac-local demos.
- Scale-up training must publish data cards before run starts.

## Legal demands
See `registers/legal/` intake. Default preservation; restoration bias when basis ends.
