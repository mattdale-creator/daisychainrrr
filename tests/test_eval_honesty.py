from free_core.eval.honesty import build_honesty_pack, honesty_markdown


def test_honesty_pack():
    pack = build_honesty_pack(
        "ttllm-nano",
        tasks_run=[{"name": "span", "result": "ok", "note": "ttlink"}],
        merkle_root="a" * 64,
    )
    assert pack["schema"] == "ttllm.eval_honesty.v1"
    assert any("frontier" in c.lower() for c in pack["non_claims"])
    md = honesty_markdown(pack)
    assert "Eval honesty" in md
    assert "non-claims" in md.lower() or "Non-claims" in md
