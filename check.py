# SPDX-FileCopyrightText: Daniele Nicolodi <daniele@grinta.net>
# SPDX-License-Identifier: Apache-2.0 OR LGPL-2.1-or-later

import os
import sys
import siphash24

# Python uses a randomized seed unless told otherwise
assert int(os.environ.get('PYTHONHASHSEED', '')) == 0

# Ensure that Python is built to use Sip Hash as internal hashing function.
# The FNV hashing function is used on platforms that require aligned memory
# access for integers. See PEP-456 for details
algorithm = sys.hash_info.algorithm
assert algorithm in {'siphash13', 'siphash24'}

# Python up to release 3.10 uses Sip Hash 13, Python 3.11 and later uses Sip Hash 13
siphash = getattr(siphash24, algorithm)

DATA = b'spam'

assert siphash(DATA).intdigest() == hash(DATA)
assert int.from_bytes(siphash(DATA).digest(), 'little', signed=True) == hash(DATA)
