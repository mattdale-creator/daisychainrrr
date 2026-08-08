#!/usr/bin/env python3
"""Machine-check Domain 3 DATA_CARD.md files.

Each ## source section must have URL + at least one *sha256* hash line.
Optional: verify trainslice_sha256 against on-disk raw files when present.
"""
from __future__ import annotations
import argparse
import hashlib
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SHA_RE = re.compile(r"`([a-f0-9]{64})`")
# bare 64-hex also accepted (e.g. `- sha256: abc...`)
SHA_BARE_RE = re.compile(r"\b([a-f0-9]{64})\b")
URL_RE = re.compile(r"URL:\s*(\S+)", re.I)
# ## or ### headings — source sections often ### under ## Sources
HEAD_RE = re.compile(r"^#{2,3}\s+(.+?)\s*$")

# Non-source section titles (case-insensitive start)
SKIP_SECTION_PREFIXES = (
    "sources",
    "corpus",
    "legal",
    "takedown",
    "notes",
    "mixture",
    "license",
    "overview",
    "summary",
)


def _is_source_heading(title: str) -> bool:
    t = title.strip()
    low = t.lower()
    for p in SKIP_SECTION_PREFIXES:
        if low == p or low.startswith(p + " ") or low.startswith(p + "/") or low.startswith(p + ":"):
            return False
    # source ids: pg…, or id-like tokens
    if low.startswith("pg") or "_" in t or t.endswith("_excerpt"):
        return True
    # if heading looks like a catalog id
    if re.match(r"^[A-Za-z0-9][A-Za-z0-9._-]{2,}$", t):
        return True
    return False


def parse_card(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    sections: list[dict] = []
    cur = None
    for line in text.splitlines():
        m = HEAD_RE.match(line.strip())
        if m:
            title = m.group(1).strip()
            # strip trailing markdown bold/noise
            title = title.strip("*").strip()
            if not _is_source_heading(title):
                cur = None
                continue
            cur = {"id": title.split()[0], "url": None, "hashes": [], "raw": []}
            sections.append(cur)
            continue
        if cur is None:
            continue
        cur["raw"].append(line)
        um = URL_RE.search(line)
        if um:
            cur["url"] = um.group(1).strip().rstrip(")")
        for h in SHA_RE.findall(line):
            cur["hashes"].append(h)
        if "sha256" in line.lower() and not SHA_RE.search(line):
            for h in SHA_BARE_RE.findall(line.lower()):
                cur["hashes"].append(h)
    return sections


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def check_card(path: Path, *, verify_files: bool) -> list[str]:
    errs: list[str] = []
    if not path.is_file():
        return [f"missing {path}"]
    sections = parse_card(path)
    if not sections:
        errs.append(f"{path}: no ## source sections")
        return errs
    model_root = path.parent.parent if path.parent.name == "data" else path.parent
    raw_dir = path.parent / "raw"
    for sec in sections:
        sid = sec["id"]
        if not sec["url"]:
            errs.append(f"{path}: {sid}: missing URL")
        if not sec["hashes"]:
            errs.append(f"{path}: {sid}: missing sha256 hash")
        if verify_files and raw_dir.is_dir():
            # Prefer trainslice file named by id
            candidates = list(raw_dir.glob(f"*{sid}*")) + list(raw_dir.glob(f"{sid}*"))
            # also *.trainslice.txt
            if not candidates:
                candidates = [p for p in raw_dir.glob("*.trainslice.txt") if sid.split("_")[0] in p.name]
            if candidates and sec["hashes"]:
                disk = sha256_file(candidates[0])
                if disk not in sec["hashes"]:
                    # trainslice may match one of the hashes
                    errs.append(
                        f"{path}: {sid}: on-disk {candidates[0].name} sha256={disk} "
                        f"not listed in card hashes"
                    )
    return errs


def find_cards(root: Path) -> list[Path]:
    cards = []
    models = root / "models"
    if models.is_dir():
        for p in sorted(models.glob("*/data/DATA_CARD.md")):
            cards.append(p)
    return cards


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(REPO))
    ap.add_argument("--verify-files", action="store_true", help="Hash raw train slices vs card")
    args = ap.parse_args(argv)
    root = Path(args.root)
    cards = find_cards(root)
    if not cards:
        print("NO_DATA_CARDS_FOUND")
        return 1
    all_errs: list[str] = []
    for c in cards:
        errs = check_card(c, verify_files=args.verify_files)
        status = "OK" if not errs else "FAIL"
        print(f"{status} {c.relative_to(root)} sections_checked")
        all_errs.extend(errs)
    if all_errs:
        for e in all_errs:
            print("ERR", e)
        return 1
    print("ALL_DATA_CARDS_OK", len(cards))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
