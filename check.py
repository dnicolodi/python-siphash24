# SPDX-FileCopyrightText: Daniele Nicolodi <daniele@grinta.net>
# SPDX-License-Identifier: Apache-2.0 OR LGPL-2.1-or-later

import os
import sys
import siphash24

# Python uses a randomized seed unless told otherwise
assert int(os.environ['PYTHONHASHSEED']) == 0

# Python up to release 3.10 uses Sip Hash 13, Python 3.11 and later uses Sip Hash 13
siphash = getattr(siphash24, sys.hash_info.algorithm)

DATA = b'spam'

assert siphash(DATA).intdigest() == hash(DATA)
assert int.from_bytes(siphash(DATA).digest(), 'little', signed=True) == hash(DATA)
