SHELL=/bin/bash

MMD_FILES=$(wildcard docs/graphs/*.mmd)
MMD_SVG_FILES=$(foreach wrd,$(MMD_FILES),$(wrd).svg)

all: build-docs build-packages

init:
	test -d examples && exit 0 || git clone https://github.com/ofabel/pytm-example examples

install: init
	test -d venv && exit 0 || \
		python -m venv venv && \
		source venv/bin/activate && \
		pip install -r requirements.txt && \
		pip install -r requirements-dev.txt
	test -d examples/venv && exit 0 || \
		python -m venv examples/venv && \
		source examples/venv/bin/activate && \
		pip install -r examples/requirements.txt && \
		pip install -r examples/requirements-test.txt

clean-packages:
	hatch clean
build-packages: install clean-packages
	hatch build
publish-packages: build-packages
	python -m twine upload dist/packages/*

clean-docs:
	rm -rf dist/docs
docs/graphs/%.mmd.svg: docs/graphs/%.mmd
	mmdc --input $^ --output "$@" --backgroundColor transparent --pdfFit --width 800 --height 800
build-docs: install clean-docs $(MMD_SVG_FILES)
	source venv/bin/activate && sphinx-build -b html docs dist/docs
publish-docs: build-docs
	./docs/publish.sh
