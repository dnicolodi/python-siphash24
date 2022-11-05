import os
import sys
import siphash24

if sys.hash_info.algorithm != 'siphash24': sys.exit(0)
assert int(os.environ['PYTHONHASHSEED']) == 0

DATA = b'spam'

assert siphash24.siphash24(DATA).intdigest() == hash(DATA)
assert int.from_bytes(siphash24.siphash24(DATA).digest(), 'little', signed=True) == hash(DATA)
