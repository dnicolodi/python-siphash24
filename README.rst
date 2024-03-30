.. SPDX-FileCopyrightText: Daniele Nicolodi <daniele@grinta.net>
.. SPDX-License-Identifier: Apache-2.0 OR LGPL-2.1-or-later

siphash24: Streaming-capable SipHash Implementation
===================================================

This module provides a C-based implementation of `SipHash`__ with an
interface compatible with the hash functions provided by the
`hashlib`__ standard library module.  SipHash-1-3 and SipHash-2-4
variants are currently implemented.  The module `documentation`__
provides a detailed description of the API.

This module differs from other similar modules by providing a
streaming-capable implementation and an interface compatible to the
hash functions provided by the ``hashlib`` standard library module and
by providing binary wheels for all supported Python releases on the
most common platforms.  More platforms can be added to the build job
as needed.

Following the ``hashlib`` interface, the return value of the
``digest()`` method is a ``bytes`` object.  SipHash values are
customarily stored as 64-bit integers.  This module extends the
``hashlib`` interface with an additional ``intdigest()`` method that
returns the hash values as a 64-bit signed int object.

This module is implemented as a thin `Cython`__-based wrapper around a
C language SipHash implementation copied, with minimal modifications
to allow compilation with MSCV, from the `c-siphash library`__ by
David Rheinsberg and co-authors.  The c-siphash library is based on
the SipHash `reference implementation`__ by Jean-Philippe Aumasson and
Daniel J. Bernstein released to the Public Domain.  This module is
distributed with the same license as the c-siphash library:
`Apache-2.0`__ or `LGPL-2.1-or-later`__.

__ https://cr.yp.to/siphash/siphash-20120918.pdf
__ https://docs.python.org/3/library/hashlib.html
__ https://dnicolodi.github.io/python-siphash24/
__ https://cython.org/
__ https://github.com/c-util/c-siphash
__ https://github.com/veorq/SipHash
__ https://spdx.org/licenses/Apache-2.0.html
__ https://spdx.org/licenses/LGPL-2.1-or-later.html
