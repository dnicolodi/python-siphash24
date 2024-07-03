.. SPDX-FileCopyrightText: Daniele Nicolodi <daniele@grinta.net>
.. SPDX-License-Identifier: Apache-2.0 OR LGPL-2.1-or-later

===================================================
siphash24: Streaming-capable SipHash Implementation
===================================================

.. currentmodule:: siphash24

This module provides a C-based streaming-capable implementation of
`SipHash`__ with an interface compatible with the hash functions
provided by the :mod:`hashlib` standard library module.  SipHash-1-3
and SipHash-2-4 variants are currently implemented.  Others can be
added as needed.

This module differs from other similar modules by providing a
streaming-capable implementation (data can be passed to the hash
object in chunnks and a digest extracted at the end) and by providing
an interface compatible to the hash functions provided by the
:mod:`hashlib` standard library module.  Binary wheels are provied for
all supported Python releases on the most common platforms.  More
platforms can be added to the build job as needed.

Following the :mod:`hashlib` interface, the return value of the
:meth:`digest() <hash.digest>` method is a bytes object.  SipHash
values are customarily stored as 64-bit integers.  This module extends
the :mod:`hashlib` interface with an additional :meth:`intdigest()
<hash.intdigest>` method that returns the hash values as a 64-bit
signed int object.

This module is implemented as a thin `Cython`__-based wrapper around
the `c-siphash library`__ by David Rheinsberg and co-authors.  The
c-siphash library is based on the SipHash `reference implementation`__
by Jean-Philippe Aumasson and Daniel J. Bernstein released to the
Public Domain.  This module is distributed with the same license as
the c-siphash library: `Apache-2.0`__ or `LGPL-2.1-or-later`__.

Despite implementing other SipHash variants, this module is named
``siphash24`` because the ``siphash`` name was already taken on PyPI
at the time this project was created.

__ https://cr.yp.to/siphash/siphash-20120918.pdf
__ https://cython.org/
__ https://github.com/c-util/c-siphash
__ https://github.com/veorq/SipHash
__ https://spdx.org/licenses/Apache-2.0.html
__ https://spdx.org/licenses/LGPL-2.1-or-later.html


API
===

Hash objects implementing the SipHash-1-3 and SipHash-2-4 variants are
created by calling the constructor functions

.. function:: siphash13(data=b'', /, *, key=b'')
.. function:: siphash24(data=b'', /, *, key=b'')

respectively. These functions take two optional parameters:

* **data** -- initial chunk of data to hash, which must be
  bytes-like object. It can be passed only as positional argument.

* **key** -- key for keyed hashing, which must be a bytes-like
  object. The passed key can be up to 16 bytes in lenght. Shorter keys
  are zero padded to 16 bytes. It can be passed only as a keyword
  argument.

The hash objects returned but the constructor functions implement the
methods provided by the hash objects in the standard library
:mod:`hashlib` module:

.. method:: hash.update(data)

   Update the hash object with the bytes-like object.

.. method:: hash.digest()

   Return the digest of the data passed to the :meth:`update`
   method so far. This is an 8-bytes bytes object.

.. method:: hash.hexdigest()

   Like :meth:`digest` except the digest is returned as a string object
   of double length, containing only hexadecimal digits.

.. method:: hash.copy()

   Return a copy of the hash object. This can be used to efficiently
   compute the digests of data sharing a common initial substring.

The interface provided by hash objects in the :mod:`hashlib` module is
extended with an additional method for easy access to the hash value
as a Python integer object:

.. method:: hash.intdigest()

   Like :meth:`digest` except the digest is returned as an int
   object. The returned value is a signed integer up to 64 bits in
   length.

To conform to the interface of the hash objects in the standard
library :mod:`hashlib` module, the following values are provided as
constant attributes:

.. data:: hash.digest_size

   The size of the resulting hash in bytes. This is 8 for SipHash.

.. data:: hash.block_size

   The internal block size of the hash algorithm in bytes.  This is 8
   for SipHash.

.. attribute:: hash.name

   The canonical name of the hash as a lower-case string.


Release notes
=============

.. include:: ../CHANGELOG.rst
