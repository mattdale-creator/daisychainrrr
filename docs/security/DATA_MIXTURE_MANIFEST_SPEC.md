# Data mixture manifest spec (pre-scale)

**Schema name:** `ttllm.data_mixture.v1`  
**Purpose:** Re-hashable publication of training mixture at scale without soft tissue.

## Required fields (JSON)
```json
{
  "schema": "ttllm.data_mixture.v1",
  "mixture_id": "mix-YYYY-MM-DD-name",
  "sources": [
    {
      "source_id": "stable-id",
      "license": "SPDX or prose",
      "url_or_locator": "https://...",
      "sha256": "64hex of exact bytes used OR null if tree",
      "merkle_root": "64hex if directory tree",
      "sampling_rate": 1.0,
      "known_exclusions": ["..."],
      "bytes": 0
    }
  ],
  "global_exclusions": [],
  "card_path": "data/DATA_CARD.md",
  "created_utc": "ISO-8601"
}
```

## Rules
1. Every trained byte class must appear as a source or explicit exclusion.
2. Prefer content hashes over “we used Common Crawl” with no locator.
3. Nano DATA_CARD markdown is the human form; this JSON is the scale form.
4. Domain 3 process for removal/alteration after publication.

## Nano bridge
`scripts/check_data_cards.py` enforces URL + sha256 on markdown cards today.
Scale runners should emit `ttllm.data_mixture.v1` beside the card.

## Related
- `docs/handbook/domains/03-data-legal-ops.md`
- `scripts/check_data_cards.py`
