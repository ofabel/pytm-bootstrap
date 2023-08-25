import datetime
import importlib
import pathlib
import sys
import tomllib

base = pathlib.Path(__file__).parent.parent
src = base.joinpath('src').__str__()
pytmlib = base.joinpath('src', 'pytmlib').__str__()
pyproject = base.joinpath('pyproject.toml')
config = dict()
now = datetime.datetime.now()

sys.path.append(src)
sys.path.append(pytmlib)

with pyproject.open('rb') as fp:
    data = tomllib.load(fp)

    config.update(**data)

project = config.get('project').get('name')
author = config.get('project').get('authors').pop(0).get('name')
copyright = str(now.year) + ', ' + author
version = release = importlib.__import__('pytmlib').version.__version__
language = 'en'
extensions = [
    'sphinx.ext.autodoc',
    'myst_parser'
]
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown'
}

html_theme_options = {
    'fixed_sidebar': True
}
html_show_sourcelink = False
exclude_patterns = [
    '**/_**'
]
