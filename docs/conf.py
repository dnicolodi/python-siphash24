# SPDX-FileCopyrightText: Daniele Nicolodi <daniele@grinta.net>
# SPDX-License-Identifier: Apache-2.0 OR LGPL-2.1-or-later

import datetime
import os

try:
    import tomllib
except ImportError:
    import tomli as tomllib

path = os.path.join(os.path.dirname(__file__), '..', 'pyproject.toml')
with open(path, 'rb') as fd:
    pyproject = tomllib.load(fd)['project']

project = pyproject['name']
version = pyproject['version']
copyright = f'2021\N{EN DASH}{datetime.date.today().year} Daniele Nicolodi'
author = 'Daniele Nicolodi'
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
