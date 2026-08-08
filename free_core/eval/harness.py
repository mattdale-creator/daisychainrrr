"""Minimal public evaluation harness for nano TTLLM releases."""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Callable, List, Dict, Any
import json
from pathlib import Path


@dataclass
class EvalResult:
    name: str
    score: float
    n: int
    details: Dict[str, Any]

    def to_dict(self) -> dict:
        return asdict(self)


def exact_match_accuracy(predict_fn: Callable[[str], str], pairs: List[tuple[str, str]]) -> EvalResult:
    correct = 0
    rows = []
    for prompt, expected in pairs:
        got = predict_fn(prompt)
        ok = got.strip() == expected.strip()
        correct += int(ok)
        rows.append({"prompt": prompt, "expected": expected, "got": got, "ok": ok})
    n = len(pairs) or 1
    return EvalResult(name="exact_match", score=correct / n, n=len(pairs), details={"rows": rows})


def run_eval_suite(predict_fn: Callable[[str], str], suite: Dict[str, List[tuple[str, str]]]) -> List[EvalResult]:
    out = []
    for name, pairs in suite.items():
        r = exact_match_accuracy(predict_fn, pairs)
        r.name = name
        out.append(r)
    return out


def write_results(results: List[EvalResult], path: Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps([r.to_dict() for r in results], indent=2) + "\n", encoding="utf-8")
