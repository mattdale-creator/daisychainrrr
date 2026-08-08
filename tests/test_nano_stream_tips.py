"""Multi-nano stream tip index (free_core 0.6.2)."""
from free_core.stream.nano_tips import collect_nano_stream_tips, write_nano_stream_tips
from pathlib import Path


def test_collect_nano_stream_tips_all_ok():
    tips = collect_nano_stream_tips()
    assert tips["schema"] == "ttllm.nano_stream_tips.v1"
    assert tips["nano_count"] >= 4
    assert tips["all_chain_ok"] is True
    names = {n["name"] for n in tips["nanos"]}
    assert "ttllm-nano" in names
    assert "ttllm-nano-v4" in names
    for n in tips["nanos"]:
        assert n["chain_ok"] is True
        assert n["tip"]
        assert n["count"] >= 1


def test_write_nano_stream_tips(tmp_path: Path):
    # write into real repo site path is fine; also ensure function returns ok
    tips = write_nano_stream_tips(copy_logs=True)
    assert tips["all_chain_ok"] is True
    dest = Path("site/demo/nano_stream_tips.json")
    assert dest.is_file()
    # v4 mirror should exist after publish
    assert Path("site/demo/nano-v4/public_log.json").is_file() or Path(
        "site/demo/nano/public_log.json"
    ).is_file()
