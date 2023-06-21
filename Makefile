clean:
	hatch clean
build: clean
	hatch build
publish: build
	python -m twine upload dist/*
