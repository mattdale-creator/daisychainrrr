# Eval honesty template (Domain 4)

Copy into each public model release as `cards/EVAL_HONESTY.md` or generate via:

```python
from free_core.eval.honesty import build_honesty_pack, honesty_markdown
pack = build_honesty_pack(
    "ttllm-nano",
    tasks_run=[{"name": "ttlink_exact_span", "result": "pass", "note": "retrieval not capability"}],
    merkle_root="<from RELEASE_MANIFEST>",
    tombstones=["nano ≠ frontier"],
)
print(honesty_markdown(pack))
```

## Required sections
1. **Tasks run** — name, result, note (what was actually measured)
2. **Explicit non-claims** — at minimum founding defaults:
   - Not frontier-competitive
   - Not OLMo/LLM360 scale
   - Not multi-trillion production ttlink
   - Not production HSM-rooted
3. **Tombstones** — release-specific honesty
4. **merkle_root** — bind to sealed release

## Forbidden
- Soft capability adjectives without tasks_run rows
- Comparing to frontier models without numbers
- Omitting non-claims because “obvious”

Schema: `ttllm.eval_honesty.v1` (`free_core/eval/honesty.py`)
