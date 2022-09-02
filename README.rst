siphash24: Streaming-capable SipHash Implementation
===================================================

This modules provides a C-based implementation of SipHash with an
interface compatible with the hash functions provided by the
``hashlib`` standard library module.  Only SipHash24 is currently
implemented.  For API documentation, see the ``hashlib``
documentation__ and the docstrings of the ``siphahs24`` class and its
methods.

This module differs from other similar modules by providing a
streaming-capable implementation and an interface compatible to the
hash functions provided by the ``hashlib`` standard library module and
by providing binary wheels for all supported Python releases on the
most common platforms.  More platforms can be added to the build job
as needed.

Following the ``hashlib`` interface, the return value of the
``digest()`` method is a ``bytes`` object.  It can be easily converted
to an ``int`` with minimal overhead::

  integer = int.from_bytes(siphash24(b'spam').digest(), 'little')

The SipHash implementation is copied, with minimal modifications to
allow compilation with MSCV, from the `c-siphash library`__, in turn
based on the reference implementation of SipHash, written by
Jean-Philippe Aumasson and Daniel J. Bernstein, and released to the
Public Domain.  This module is distributed with the same license as
the ``c-siphash`` library: Apache-2.0 or LGPL-2.1-or-later, see
AUTHORS__ for details.

__ https://docs.python.org/3/library/hashlib.html
__ https://github.com/c-util/c-siphash
__ https://github.com/c-util/c-siphash/blob/v1/AUTHORS
