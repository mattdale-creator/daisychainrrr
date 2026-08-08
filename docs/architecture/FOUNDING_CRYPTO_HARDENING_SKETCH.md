# Cryptographic hardening sketch (founding turn 16)

Here’s a concrete technical sketch of the hardening layer that actually matters for a TTLLM + ttlink system.

The goal is not “security theatre.” It is to make the public skeleton *verifiable* and *hard to silently corrupt*.

### 1. Core principle: everything important must be cryptographically attributable

Every released artefact (training data shards, intermediate checkpoints, final weights, ttlink index shards, data manifests) gets a verifiable provenance chain.

**Minimal viable structure:**

```text
data/                  → content-addressed (hash of each document or shard)
checkpoints/           → model weights + metadata, signed
indexes/               → ttlink index shards, signed
manifests/             → Merkle trees + signatures that bind everything together
```

### 2. Content-addressed data + Merkle manifests

```python
import hashlib
import json
from pathlib import Path
from typing import List, Dict

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def build_merkle_manifest(file_paths: List[Path]) -> Dict:
    """Build a simple Merkle-style manifest of content hashes."""
    leaves = sorted([
        {"path": str(p), "sha256": sha256_file(p)}
        for p in file_paths
    ], key=lambda x: x["path"])
    
    # Very simple binary Merkle tree over the leaf hashes
    level = [bytes.fromhex(leaf["sha256"]) for leaf in leaves]
    while len(level) > 1:
        next_level = []
        for i in range(0, len(level), 2):
            left = level[i]
            right = level[i+1] if i+1 < len(level) else left
            next_level.append(hashlib.sha256(left + right).digest())
        level = next_level
    
    root = level[0].hex() if level else None
    return {
        "merkle_root": root,
        "leaves": leaves,
        "count": len(leaves)
    }
```

Anyone can re-hash the released files and confirm they match the published Merkle root.

### 3. Signed releases (model, data, index)

```python
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization

def sign_manifest(manifest: dict, private_key: ed25519.Ed25519PrivateKey) -> dict:
    payload = json.dumps(manifest, sort_keys=True, separators=(",", ":")).encode()
    signature = private_key.sign(payload)
    return {
        "manifest": manifest,
        "signature": signature.hex(),
        "public_key": private_key.public_key().public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw
        ).hex()
    }

def verify_signed_manifest(signed: dict) -> bool:
    public_key = ed25519.Ed25519PublicKey.from_public_bytes(
        bytes.fromhex(signed["public_key"])
    )
    payload = json.dumps(signed["manifest"], sort_keys=True, separators=(",", ":")).encode()
    try:
        public_key.verify(bytes.fromhex(signed["signature"]), payload)
        return True
    except Exception:
        return False
```

Every public release (data dump, checkpoint, index shard) ships with a signed manifest. The public keys are published and preferably also anchored (e.g. transparency log or multiple independent mirrors).

### 4. ttlink index integrity

The dangerous part is the mapping from model output spans → training documents.  
If an attacker can silently alter that mapping, the entire “down to the bone” claim collapses.

Practical approach:

- Shard the index.
- Each shard carries its own content hash and is signed.
- The top-level index manifest contains the Merkle root of all shard hashes.
- When the system returns “this span came from document X”, it also returns the shard ID + proof that the shard is part of the signed root.

This does not make the suffix-array/FM-index itself homomorphic, but it makes *tampering* detectable.

### 5. Query layer hardening (practical controls)

```python
# Conceptual rate-limiting + abuse signals
from collections import defaultdict
import time

class QueryGuard:
    def __init__(self):
        self.requests = defaultdict(list)  # key → timestamps
        self.suspicious = set()

    def allow(self, client_id: str, query_cost: float = 1.0) -> bool:
        now = time.time()
        window = [t for t in self.requests[client_id] if now - t < 60]
        self.requests[client_id] = window
        
        if len(window) > 120:          # hard rate limit
            self.suspicious.add(client_id)
            return False
        if client_id in self.suspicious and len(window) > 30:
            return False
            
        self.requests[client_id].append(now)
        return True
```

Real systems need more (token buckets, proof-of-work for heavy queries, anomaly detection on query patterns that look like bulk extraction or index probing). The above is only the skeleton.

### 6. What “frontier red-team hardened” looks like in code terms

You need continuous adversarial testing *against your own transparency layer*, not just against the model. That means automated and human red-team pipelines that try to:

- Corrupt or swap index shards and see if the verification catches it
- Craft queries that force the system into inconsistent provenance answers
- Use the public data + model to perform membership inference or targeted extraction at scale
- Stress the public streaming / query endpoints under realistic attack traffic

The code above gives you the *detection* substrate. The red-teaming process is what forces you to keep improving it.

### Summary of the minimal hardened stack

1. Content-addressed data + Merkle manifests  
2. Ed25519 (or stronger) signatures on every release artefact  
3. Signed, sharded ttlink indexes with verifiable membership  
4. Query-layer controls that do not destroy the transparency promise  
5. Continuous adversarial testing aimed at the transparency system itself

Without the cryptographic and verification layer, “public stream of real data” is just a claim. With it, outsiders can independently confirm that what they are looking at is the same skeleton the organisation claims to have released.

That is the core of what needs to be coded.
