# SPDX-FileCopyrightText: Daniele Nicolodi <daniele@grinta.net>
# SPDX-License-Identifier: Apache-2.0 OR LGPL-2.1-or-later

project(
  'python-siphash24', 'c', 'cython',
  license: 'Apache-2.0 or LGPL-2.1-or-later',
  meson_version: '>= 1.0.0',
  default_options: [
    'buildtype=release',
    'c_std=c99',
  ]
)

libcsiphash = dependency('libcsiphash-1', version: '>= 1.1.0', static: true)

py = import('python').find_installation()

tempita = files('tempita.py')

pyx = custom_target(
  'siphash24.pyx',
  input: 'siphash24.pyx.in',
  output: 'siphash24.pyx',
  command: [py, tempita, '@INPUT@', '@OUTPUT@']
)

py.extension_module(
  'siphash24',
  pyx,
  dependencies: libcsiphash,
  install: true
)
