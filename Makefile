SHELL=/bin/bash

all: build-docs build-packages

clean-packages:
	hatch clean
build-packages: clean-packages
	hatch build
publish-packages: build-packages
	python -m twine upload dist/packages/*

clean-docs:
	rm -rf dist/docs
build-docs: clean-docs
	source venv/bin/activate && sphinx-build -b html docs dist/docs
