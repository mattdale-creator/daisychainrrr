.PHONY: test seal install lint artefacts demo verify-all nano-data nano-train nano-seal nano-all redteam fine-grain reseal-core public-urls supply stream-catalog

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

# Fine-grain automated bone (no capital)
fine-grain:
	python3 scripts/build_stream_catalog.py
	python3 scripts/build_incident_drill_stream.py
	python3 scripts/build_supply_lock.py
	python3 scripts/check_data_cards.py
	python3 scripts/check_dns_status.py || true
	python3 scripts/check_public_urls.py --write-default --offline || python3 scripts/check_public_urls.py --write-default
	python3 scripts/check_seal_freshness.py --write
	python3 scripts/public_verify_harness.py
	python3 scripts/redteam_nano_harness.py
	python3 -m pytest -q

dns:
	python3 scripts/check_dns_status.py

deploy-site:
	npx wrangler pages deploy site --project-name=ttllms

cost-ledger:
	python3 scripts/nano_cost_ledger.py --write

placeholders-check:
	python3 scripts/check_placeholder_labels.py

reseal-core:
	python3 scripts/check_seal_freshness.py --write

public-urls:
	python3 scripts/check_public_urls.py

supply:
	python3 scripts/build_supply_lock.py

stream-catalog:
	python3 scripts/build_stream_catalog.py
	python3 scripts/build_incident_drill_stream.py

verify-all: test demo redteam fine-grain
	python3 scripts/oneshot_verify_all.py
	python3 -m free_core.stream.cli verify models/ttllm-nano/stream/public_log.json
	@echo "ALL GREEN"

lint:
	python3 -m compileall free_core tests scripts models/ttllm-nano/code

nano-v2-data:
	python3 models/ttllm-nano-v2/code/prepare_bpe.py

nano-v2-train:
	python3 models/ttllm-nano-v2/code/train.py --steps 1200

nano-v2-seal:
	python3 models/ttllm-nano-v2/code/eval_pack.py
	python3 models/ttllm-nano-v2/code/seal_release.py

domain-scorecard:
	python3 scripts/domain_scorecard_all.py

reseal-nanos:
	python3 -c "from free_core.release.pipeline import seal_model_tree; import pathlib; \
[print(seal_model_tree(pathlib.Path('models')/n, version='auto')['release']['count']) for n in ['ttllm-nano','ttllm-nano-v2','ttllm-nano-v3'] if (pathlib.Path('models')/n).exists()]"
