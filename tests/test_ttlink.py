from pathlib import Path
from free_core.ttlink.index import TtlinkIndex

def test_query_hits(tmp_path):
    corpus = tmp_path / "c"
    corpus.mkdir()
    (corpus / "x.txt").write_text("The free public core cannot be monetised by closing the skeleton.")
    idx = TtlinkIndex()
    idx.index_directory(corpus)
    hits = idx.query("free public core")
    assert len(hits) == 1
    assert hits[0].doc_sha256
    assert hits[0].match == "free public core"

def test_ignore_case(tmp_path):
    corpus = tmp_path / "c"
    corpus.mkdir()
    (corpus / "x.txt").write_text("TTLINK Provenance")
    idx = TtlinkIndex()
    idx.index_directory(corpus)
    assert idx.query("ttlink", case_sensitive=True) == []
    assert len(idx.query("ttlink", case_sensitive=False)) == 1
