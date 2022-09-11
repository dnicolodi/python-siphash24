project(
  'python-siphash24', 'c', 'cython',
  license: 'Apache-2.0 or LGPL-2.1-or-later',
  meson_version: '>= 0.63.0',
  default_options: [
    'buildtype=debugoptimized',
    'c_std=c99',
  ]
)

libcsiphash = dependency('libcsiphash-1', static: true)

py = import('python').find_installation()

py.extension_module(
  'siphash24',
  'siphash24.pyx',
  dependencies: libcsiphash,
  install: true
)
