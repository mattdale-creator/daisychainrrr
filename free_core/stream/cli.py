"""CLI: ttllm-stream"""
from __future__ import annotations
import argparse
from .schema import demo_events


def main(argv=None):
    p = argparse.ArgumentParser(prog="ttllm-stream")
    p.add_argument("cmd", choices=["demo"], help="demo: print example public stream events")
    args = p.parse_args(argv)
    if args.cmd == "demo":
        for e in demo_events():
            print(e.to_json())


if __name__ == "__main__":
    main()
