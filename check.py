import os
import sys
import siphash24

if sys.hash_info.algorithm != 'siphash24': sys.exit(0)
assert int(os.environ['PYTHONHASHSEED']) == 0

data = b'spam'
h = int.from_bytes(siphash24.siphash24(data).digest(), 'little', signed=True)
assert h == hash(data)
