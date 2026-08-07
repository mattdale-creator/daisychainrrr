"""
Reference ttlink engine.

Production ttlink at multi-trillion-token scale needs suffix arrays / FM-index
(infini-gram family). This reference implements exact substring → document
linking over a small tokenised corpus so the *interface* and *provenance
binding* are real and testable — the skeleton, not soft tissue theatre.
"""
from __future__ import annotations
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional
from free_core.provenance.hashing import sha256_bytes


@dataclass
class Hit:
    doc_id: str
    path: str
    start: int
    end: int
    context: str
    doc_sha256: str
    match: str


class TtlinkIndex:
    def __init__(self):
        self.docs: Dict[str, dict] = {}  # id -> {path, text, sha256}

    def add_document(self, doc_id: str, text: str, path: str = "") -> None:
        self.docs[doc_id] = {
            "path": path or doc_id,
            "text": text,
            "sha256": sha256_bytes(text.encode("utf-8")),
            "bytes": len(text.encode("utf-8")),
        }

    def add_file(self, path: Path, doc_id: Optional[str] = None) -> None:
        path = Path(path)
        text = path.read_text(encoding="utf-8", errors="replace")
        self.add_document(doc_id or path.name, text, str(path))

    def index_directory(self, root: Path) -> int:
        root = Path(root)
        n = 0
        for p in sorted(root.rglob("*")):
            if p.is_file() and p.suffix.lower() in {".txt", ".md", ".json", ".csv"}:
                self.add_file(p, doc_id=str(p.relative_to(root)))
                n += 1
        return n

    def query(
        self,
        span: str,
        *,
        context_chars: int = 80,
        max_hits: int = 20,
        case_sensitive: bool = True,
    ) -> List[Hit]:
        if not span:
            return []
        hits: List[Hit] = []
        for doc_id, doc in self.docs.items():
            text = doc["text"]
            hay = text if case_sensitive else text.lower()
            needle = span if case_sensitive else span.lower()
            start = 0
            while True:
                i = hay.find(needle, start)
                if i < 0:
                    break
                a = max(0, i - context_chars)
                b = min(len(text), i + len(span) + context_chars)
                hits.append(Hit(
                    doc_id=doc_id,
                    path=doc["path"],
                    start=i,
                    end=i + len(span),
                    context=text[a:b],
                    doc_sha256=doc["sha256"],
                    match=text[i:i + len(span)],
                ))
                if len(hits) >= max_hits:
                    return hits
                start = i + 1
        return hits

    def stats(self) -> dict:
        return {
            "documents": len(self.docs),
            "total_bytes": sum(d["bytes"] for d in self.docs.values()),
            "doc_ids": sorted(self.docs.keys()),
        }

    def save(self, path: Path) -> None:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "schema": "ttllm.ttlink_index.v1",
            "docs": self.docs,
        }
        path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    def save_public_bundle(self, path: Path) -> None:
        """Bundle safe for browser demos (same as save; explicit name)."""
        self.save(path)

    @classmethod
    def load(cls, path: Path) -> "TtlinkIndex":
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        idx = cls()
        idx.docs = data["docs"]
        return idx

    def manifest_binding(self) -> dict:
        leaves = sorted(
            [{"path": d["path"], "sha256": d["sha256"], "bytes": d["bytes"]} for d in self.docs.values()],
            key=lambda x: x["path"],
        )
        return {"schema": "ttllm.ttlink_binding.v1", "count": len(leaves), "leaves": leaves}
