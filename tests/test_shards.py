from pathlib import Path
from free_core.security.shard import seal_shards, ShardManifest

def test_shard_seal(tmp_path):
    a = tmp_path / "s0.json"
    b = tmp_path / "s1.json"
    a.write_text('{"x":1}')
    b.write_text('{"y":2}')
    man = seal_shards([a, b], base=tmp_path)
    assert man["count"] == 2
    assert man["merkle_root"]
    sm = ShardManifest(man)
    sm.save(tmp_path / "m.json")
    assert ShardManifest.load(tmp_path / "m.json").verify_files(tmp_path)["ok"]
