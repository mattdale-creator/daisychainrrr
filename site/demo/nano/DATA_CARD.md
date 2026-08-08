# Data card — ttllm-nano

**Fetched:** 2026-08-08T08:36:57Z  
**License of sources:** Public domain (US) via Project Gutenberg  
**Mixture:** Character-concatenated train slices of the listed PG texts (headers stripped).  
**Full downloads** retained under `data/raw/*.full.txt` with sha256 in `sources.json` for verification against URL content at fetch time.  
**Train slice** is a prefix of cleaned text to keep Mac nano training tractable — this limitation is a **tombstone**, not hidden soft tissue.

## Sources

### pg1342_pride_prejudice_excerpt
- URL: https://www.gutenberg.org/files/1342/1342-0.txt
- Title: Pride and Prejudice (Jane Austen) — full text PG
- License: Public domain (US) — Project Gutenberg
- full_sha256: `a5666f87abf2cbfdaa27ea8c73bd284da9649b9a2ab27b4e6c8f6aeab1bd1c88`
- trainslice_sha256: `e8035130fcf49aabdbff8d1c63b86d0a097d51c74d25a4edef095984611386b6`
- trainslice_chars: 120000

### pg11_alice_excerpt
- URL: https://www.gutenberg.org/files/11/11-0.txt
- Title: Alice's Adventures in Wonderland (Lewis Carroll)
- License: Public domain (US) — Project Gutenberg
- full_sha256: `a3a27f8edbf7fcd9b8ba8435494440e24952deaa3e2f2d65192d4cb7ca403754`
- trainslice_sha256: `02c34df7cb8614058b8570c4586588d28e51fb57bc51da3ce10a2bf86198fab5`
- trainslice_chars: 80000

### pg84_frankenstein_excerpt
- URL: https://www.gutenberg.org/files/84/84-0.txt
- Title: Frankenstein (Mary Shelley)
- License: Public domain (US) — Project Gutenberg
- full_sha256: `06c37d2c52d208d3d81eb12c3b10b5edbd7728b73554325ddceadbe2fb427e77`
- trainslice_sha256: `a02b29c4e829dd61101a94ffc67c3393b18dcc01ad3c3a6da07380fa16073b66`
- trainslice_chars: 100000

## Corpus
- path: `data/processed/corpus.txt`
- sha256: `aa1b7083c28c0f133778d4dd8bac02c8e37fa419d47be821537c4ae32f71046a`
- chars: 300142
- vocab_size: 95

## Legal / takedown
See Domain 3. Any removal must be logged in `registers/legal/`.
