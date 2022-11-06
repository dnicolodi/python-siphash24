project = 'siphash24'
copyright = '2022, Daniele Nicolodi'
author = 'Daniele Nicolodi'
version = '1.1'
exclude_patterns = []
language = 'en'
html_theme = 'furo'
html_title = f'{project} {version}'
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.githubpages',
]
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}
