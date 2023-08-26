SHELL=/bin/bash

MMD_FILES=$(wildcard docs/graphs/*.mmd)
MMD_SVG_FILES=$(foreach wrd,$(MMD_FILES),$(wrd).svg)

all: build-docs build-packages

clean-packages:
	hatch clean
build-packages: clean-packages
	hatch build
publish-packages: build-packages
	python -m twine upload dist/packages/*

clean-docs:
	rm -rf dist/docs
docs/graphs/%.mmd.svg: docs/graphs/%.mmd
	mmdc --input $^ --output "$@" --backgroundColor transparent --pdfFit --width 800 --height 800
build-docs: clean-docs $(MMD_SVG_FILES)
	source venv/bin/activate && sphinx-build -b html docs dist/docs
publish-docs: build-docs
	./docs/publish.sh
