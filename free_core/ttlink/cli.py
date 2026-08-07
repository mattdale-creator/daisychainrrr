"""CLI: ttllm-ttlink"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from .index import TtlinkIndex


def main(argv=None):
    p = argparse.ArgumentParser(prog="ttllm-ttlink", description="Reference ttlink engine")
    sub = p.add_subparsers(dest="cmd", required=True)

    ix = sub.add_parser("index", help="Index a corpus directory")
    ix.add_argument("corpus")
    ix.add_argument("-o", "--out", default="examples/ttlink_index.json")

    q = sub.add_parser("query", help="Query span against an index")
    q.add_argument("span")
    q.add_argument("--index", default="examples/ttlink_index.json")
    q.add_argument("--max", type=int, default=20)
    q.add_argument("-i", "--ignore-case", action="store_true")

    st = sub.add_parser("stats", help="Index statistics")
    st.add_argument("--index", default="examples/ttlink_index.json")

    args = p.parse_args(argv)
    if args.cmd == "index":
        idx = TtlinkIndex()
        n = idx.index_directory(Path(args.corpus))
        out = Path(args.out)
        idx.save(out)
        print(f"indexed {n} documents → {out}")
        print(json.dumps(idx.manifest_binding(), indent=2))
        print(json.dumps(idx.stats(), indent=2))
    elif args.cmd == "query":
        idx = TtlinkIndex.load(Path(args.index))
        hits = idx.query(args.span, max_hits=args.max, case_sensitive=not args.ignore_case)
        print(json.dumps([h.__dict__ for h in hits], indent=2))
        print(f"{len(hits)} hit(s)")
    elif args.cmd == "stats":
        idx = TtlinkIndex.load(Path(args.index))
        print(json.dumps(idx.stats(), indent=2))


if __name__ == "__main__":
    main()
