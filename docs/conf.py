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

html_favicon = './graphs/favicon.png'
html_logo = './graphs/logo.png'
html_theme_options = {
    'show_powered_by': False,
    'description': config.get('project').get('description'),
    'extra_nav_links': {
        'Source Code': 'https://www.github.com/ofabel/pytm-bootstrap',
        'Bugtracker': 'https://www.github.com/ofabel/pytm-bootstrap/issues',
        'Releases': 'https://pypi.org/project/pytmlib'

    }
}
html_copy_source = False
html_show_copyright = False
html_show_sphinx = False
exclude_patterns = [
    '**/_**'
]
