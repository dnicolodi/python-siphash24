# SPDX-FileCopyrightText: Daniele Nicolodi <daniele@grinta.net>
# SPDX-License-Identifier: Apache-2.0 OR LGPL-2.1-or-later

import array
import binascii
import unittest
import siphash24


class TestSipHas24(unittest.TestCase):

    def test_siphash24(self):
        h = siphash24.siphash24()
        self.assertEqual(h.digest(), b'\xd7\x00ws\x9dK\x92\x1e')

    def test_siphash24_data(self):
        h = siphash24.siphash24(b'')
        self.assertEqual(h.digest(), b'\xd7\x00ws\x9dK\x92\x1e')

    def test_siphash24_key(self):
        h = siphash24.siphash24(key=b'')
        self.assertEqual(h.digest(), b'\xd7\x00ws\x9dK\x92\x1e')

    def test_siphash24_long_key(self):
        with self.assertRaises(ValueError):
            h = siphash24.siphash24(key=b'\x00' * 17)

    def test_siphash24_data_and_key(self):
        h = siphash24.siphash24(b'', key=b'')
        self.assertEqual(h.digest(), b'\xd7\x00ws\x9dK\x92\x1e')

    def test_siphash24_hexdigest(self):
        h = siphash24.siphash24()
        self.assertIsInstance(h.digest(), bytes)
        self.assertEqual(h.hexdigest(), binascii.hexlify(h.digest()).decode('ascii'))

    def test_siphash24_name(self):
        h = siphash24.siphash24()
        self.assertIsInstance(h.name, str)
        self.assertEqual(h.name, 'siphash24')

    def test_siphash24_digest_size(self):
        h = siphash24.siphash24()
        self.assertEqual(len(h.digest()), h.digest_size)
        self.assertEqual(len(h.hexdigest()), 2 * h.digest_size)

    def test_siphash24_reference(self):
        key = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'
        data = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e'
        self.assertEqual(siphash24.siphash24(data, key=key).digest(), b'\xe5\x45\xbe\x49\x61\xca\x29\xa1')

    def test_siphahs24_reference_chunked(self):
        key = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'
        data = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e'
        for i in range(len(data)):
            for j in range(i, len(data)):
                h = siphash24.siphash24(key=key)
                h.update(data[ :i])
                h.update(data[i:j])
                h.update(data[j: ])
                self.assertEqual(data[:i] + data[i:j] + data[j:], data)
                self.assertEqual(int.from_bytes(h.digest(), 'little'), 0xa129ca6149be45e5)

    def test_siphash24_update(self):
        key = b'\x22\x24\x41\x22\x55\x77\x88\x07\x23\x09\x23\x14\x0c\x33\x0e\x0f'
        data = b'\x01\x02\x03\x04\x05\x06\x07\x08\x09\x10\x11\x12\x13\x14\x15\x16'
        for i in range(len(data)):
            h = siphash24.siphash24(key=key)
            h.update(data[:i])
            h.update(data[i:])
            self.assertEqual(h.digest(), siphash24.siphash24(data, key=key).digest())

    def test_siphash24_types(self):
        with self.assertRaises(TypeError):
            h = siphash24.siphash24('spam')
        with self.assertRaises(TypeError):
            h = siphash24.siphash24(key='spam')
        with self.assertRaises(TypeError):
            h = siphash24.siphash24(1)
        with self.assertRaises(TypeError):
            h = siphash24.siphash24(key=1)

    def test_siphash24_buffer_interface(self):
        data = array.array('i', range(32))
        self.assertEqual(siphash24.siphash24(data).digest(), siphash24.siphash24(data.tobytes()).digest())


if __name__ == '__main__':
    unittest.main()
