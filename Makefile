clean:
	rm -rf dist
build: clean
	python -m build
publish: build
	python -m twine upload dist/*