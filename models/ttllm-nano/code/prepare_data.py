#!/usr/bin/env python3
"""Download and seal verifiable public-domain training corpus.

Sources: Project Gutenberg plain text (public domain US).
Each file is hashed; DATA_CARD.md records URLs and licenses.
"""
from __future__ import annotations
import hashlib
import json
import ssl
import urllib.request
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROC = ROOT / "data" / "processed"
RAW.mkdir(parents=True, exist_ok=True)
PROC.mkdir(parents=True, exist_ok=True)

# Small, reputable, public-domain texts (Gutenberg)
SOURCES = [
    {
        "id": "pg1342_pride_prejudice_excerpt",
        "url": "https://www.gutenberg.org/files/1342/1342-0.txt",
        "title": "Pride and Prejudice (Jane Austen) — full text PG",
        "license": "Public domain (US) — Project Gutenberg",
        "max_chars": 120_000,  # keep nano train tractable; full file still hashed for provenance of source URL
    },
    {
        "id": "pg11_alice_excerpt",
        "url": "https://www.gutenberg.org/files/11/11-0.txt",
        "title": "Alice's Adventures in Wonderland (Lewis Carroll)",
        "license": "Public domain (US) — Project Gutenberg",
        "max_chars": 80_000,
    },
    {
        "id": "pg84_frankenstein_excerpt",
        "url": "https://www.gutenberg.org/files/84/84-0.txt",
        "title": "Frankenstein (Mary Shelley)",
        "license": "Public domain (US) — Project Gutenberg",
        "max_chars": 100_000,
    },
]


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def fetch(url: str) -> bytes:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": "ttllm-nano-data-prep/0.1 (research; md@0265.au)"})
    with urllib.request.urlopen(req, context=ctx, timeout=120) as r:
        return r.read()


def main():
    manifests = []
    corpus_parts = []
    for src in SOURCES:
        print("fetch", src["url"])
        try:
            raw = fetch(src["url"])
        except Exception as e:
            print("FAIL", src["id"], e)
            # offline fallback: fail hard so we don't silently train on empty
            raise
        full_hash = sha256_bytes(raw)
        text = raw.decode("utf-8", errors="replace")
        # strip PG header/footer lightly
        if "*** START OF" in text:
            text = text.split("*** START OF", 1)[1]
            text = text.split("***", 1)[-1]
        if "*** END OF" in text:
            text = text.split("*** END OF", 1)[0]
        text = text.strip() + "\n"
        use = text[: src["max_chars"]]
        raw_path = RAW / f"{src['id']}.full.txt"
        use_path = RAW / f"{src['id']}.trainslice.txt"
        raw_path.write_bytes(raw)
        use_path.write_text(use, encoding="utf-8")
        entry = {
            "id": src["id"],
            "url": src["url"],
            "title": src["title"],
            "license": src["license"],
            "full_sha256": full_hash,
            "full_bytes": len(raw),
            "trainslice_sha256": sha256_bytes(use.encode("utf-8")),
            "trainslice_chars": len(use),
            "trainslice_path": str(use_path.relative_to(ROOT)),
            "fetched_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        manifests.append(entry)
        corpus_parts.append(f"\n\n##### SOURCE {src['id']} #####\n\n" + use)
        print(" ", src["id"], "full", full_hash[:16], "slice", entry["trainslice_chars"])

    corpus = "".join(corpus_parts)
    corpus_path = PROC / "corpus.txt"
    corpus_path.write_text(corpus, encoding="utf-8")
    # char vocab
    chars = sorted(set(corpus))
    stoi = {ch: i for i, ch in enumerate(chars)}
    itos = {i: ch for ch, i in stoi.items()}
    meta = {
        "schema": "ttllm.nano.vocab.v1",
        "vocab_size": len(chars),
        "stoi": stoi,
        "itos": {str(k): v for k, v in itos.items()},
        "corpus_sha256": sha256_bytes(corpus.encode("utf-8")),
        "corpus_chars": len(corpus),
    }
    (PROC / "meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    (PROC / "sources.json").write_text(json.dumps(manifests, indent=2) + "\n", encoding="utf-8")

    card = f"""# Data card — ttllm-nano

**Fetched:** {datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}  
**License of sources:** Public domain (US) via Project Gutenberg  
**Mixture:** Character-concatenated train slices of the listed PG texts (headers stripped).  
**Full downloads** retained under `data/raw/*.full.txt` with sha256 in `sources.json` for verification against URL content at fetch time.  
**Train slice** is a prefix of cleaned text to keep Mac nano training tractable — this limitation is a **tombstone**, not hidden soft tissue.

## Sources
"""
    for m in manifests:
        card += f"\n### {m['id']}\n- URL: {m['url']}\n- Title: {m['title']}\n- License: {m['license']}\n- full_sha256: `{m['full_sha256']}`\n- trainslice_sha256: `{m['trainslice_sha256']}`\n- trainslice_chars: {m['trainslice_chars']}\n"
    card += f"\n## Corpus\n- path: `data/processed/corpus.txt`\n- sha256: `{meta['corpus_sha256']}`\n- chars: {meta['corpus_chars']}\n- vocab_size: {meta['vocab_size']}\n"
    card += "\n## Legal / takedown\nSee Domain 3. Any removal must be logged in `registers/legal/`.\n"
    (ROOT / "data" / "DATA_CARD.md").write_text(card, encoding="utf-8")
    print("corpus chars", len(corpus), "vocab", len(chars))
    print("wrote", corpus_path)


if __name__ == "__main__":
    main()
