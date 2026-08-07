"""CLI: ttllm-stream"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from .schema import demo_events, StreamEvent
from .log import StreamLog


def main(argv=None):
    p = argparse.ArgumentParser(prog="ttllm-stream")
    sub = p.add_subparsers(dest="cmd", required=True)

    d = sub.add_parser("demo", help="print example public stream events (JSON lines)")
    b = sub.add_parser("build-demo-log", help="build hash-chained demo log file")
    b.add_argument("-o", "--out", default="examples/stream/public_log.json")
    v = sub.add_parser("verify", help="verify hash chain of a stream log")
    v.add_argument("path")
    a = sub.add_parser("append", help="append event to log file")
    a.add_argument("path")
    a.add_argument("--type", required=True)
    a.add_argument("--payload", default="{}", help="JSON object string")
    a.add_argument("--sha", default=None)

    args = p.parse_args(argv)
    if args.cmd == "demo":
        for e in demo_events():
            print(e.to_json())
    elif args.cmd == "build-demo-log":
        log = StreamLog()
        for e in demo_events():
            log.append(e)
        out = Path(args.out)
        log.save(out)
        print(json.dumps(log.verify_chain(), indent=2))
        print(f"wrote {out}")
    elif args.cmd == "verify":
        log = StreamLog.load(Path(args.path))
        result = log.verify_chain()
        print(json.dumps(result, indent=2))
        sys.exit(0 if result["ok"] else 1)
    elif args.cmd == "append":
        path = Path(args.path)
        log = StreamLog.load(path) if path.exists() else StreamLog()
        payload = json.loads(args.payload)
        log.append(StreamEvent(event_type=args.type, artefact_sha256=args.sha, payload=payload))
        log.save(path)
        print(json.dumps(log.verify_chain(), indent=2))


if __name__ == "__main__":
    main()
