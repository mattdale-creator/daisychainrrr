from free_core.provenance.manifest import build_merkle_manifest
from free_core.provenance.proof import inclusion_proof, verify_inclusion

def test_inclusion_proof(tmp_path):
    files = []
    for i, t in enumerate(["alpha", "beta", "gamma", "delta"]):
        p = tmp_path / f"{i}.txt"
        p.write_text(t)
        files.append(p)
    m = build_merkle_manifest(files, base=tmp_path)
    digests = [x["sha256"] for x in sorted(m["leaves"], key=lambda x: x["path"])]
    for i in range(len(digests)):
        proof = inclusion_proof(digests, i)
        assert verify_inclusion(proof["leaf_hash"], proof["proof"], m["merkle_root"])
        assert proof["root"] == m["merkle_root"]
