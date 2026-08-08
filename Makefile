.PHONY: test seal install lint artefacts demo verify-all nano-data nano-train nano-seal nano-all redteam

install:
	python3 -m pip install -e ".[dev,crypto]"

test:
	python3 -m pytest -q

artefacts:
	python3 scripts/build_public_artefacts.py

seal: artefacts

demo: artefacts
	python3 -m free_core.ttlink.cli query "free public core" --index examples/ttlink_index.json
	python3 -m free_core.stream.cli verify examples/stream/public_log.json
	python3 -m free_core.provenance.cli verify --manifest manifests/FREE_CORE_SEAL.json --base .

nano-data:
	python3 models/ttllm-nano/code/prepare_data.py

nano-train:
	python3 models/ttllm-nano/code/train.py --steps 800

nano-seal:
	python3 models/ttllm-nano/code/seal_release.py

nano-all: nano-data nano-train nano-seal
	python3 models/ttllm-nano/code/generate.py --prompt "Alice " --tokens 80

redteam:
	python3 scripts/redteam_nano_harness.py

verify-all: test demo redteam
	python3 -m free_core.stream.cli verify models/ttllm-nano/stream/public_log.json
	@echo "ALL GREEN (nano manifest verify separately after seal)"

lint:
	python3 -m compileall free_core tests scripts models/ttllm-nano/code

nano-v2-data:
	python3 models/ttllm-nano-v2/code/prepare_bpe.py

nano-v2-train:
	python3 models/ttllm-nano-v2/code/train.py --steps 1200

nano-v2-seal:
	python3 models/ttllm-nano-v2/code/eval_pack.py
	python3 models/ttllm-nano-v2/code/seal_release.py
