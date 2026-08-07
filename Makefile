.PHONY: test seal install lint tree artefacts demo verify-all

install:
	python3 -m pip install -e ".[dev,crypto]"

test:
	python3 -m pytest -q

artefacts:
	python scripts/build_public_artefacts.py

seal: artefacts

demo: artefacts
	python3 -m free_core.ttlink.cli query "free public core" --index examples/ttlink_index.json
	python3 -m free_core.stream.cli verify examples/stream/public_log.json
	python3 -m free_core.provenance.cli verify --manifest manifests/FREE_CORE_SEAL.json --base .

verify-all: test demo
	@echo "ALL GREEN"

lint:
	python3 -m compileall free_core tests scripts

tree:
	@find . -type f -not -path './.git/*' -not -path './.venv/*' -not -path './__pycache__/*' | sort
