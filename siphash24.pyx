# cython: language_level=3, boundscheck=False

from libc.stdint cimport uint64_t, int64_t, uint8_t
from libc.stdio cimport snprintf
from libc.string cimport memcpy, memset
from cpython cimport Py_buffer, PyObject_GetBuffer, PyBUF_SIMPLE, PyBuffer_Release, PyUnicode_Check, PyObject_CheckBuffer
from cpython.conversion cimport PyOS_snprintf

cdef extern from "c-siphash.h":
    ctypedef struct CSipHash:
        pass
    cdef void c_siphash_init(CSipHash *state, const uint8_t seed[16])
    cdef void c_siphash_append(CSipHash *state, const uint8_t *bytes, size_t n_bytes)
    cdef uint64_t c_siphash_finalize(CSipHash *state)


cdef bytes uint64le(uint64_t v):
    cdef uint8_t[8] r = [
        <uint8_t>(v >>  0),
        <uint8_t>(v >>  8),
        <uint8_t>(v >> 16),
        <uint8_t>(v >> 24),
        <uint8_t>(v >> 32),
        <uint8_t>(v >> 40),
        <uint8_t>(v >> 48),
        <uint8_t>(v >> 56),
    ]
    return <bytes>r[:8]


cdef bytes hexlify(uint64_t v):
    cdef char string[17]
    PyOS_snprintf(
        string, sizeof(string),
        '%02x%02x%02x%02x%02x%02x%02x%02x',
        <uint8_t>(v >>  0),
        <uint8_t>(v >>  8),
        <uint8_t>(v >> 16),
        <uint8_t>(v >> 24),
        <uint8_t>(v >> 32),
        <uint8_t>(v >> 40),
        <uint8_t>(v >> 48),
        <uint8_t>(v >> 56))
    return <bytes>string[:16]


cdef class siphash24:
    cdef CSipHash state

    cdef readonly int digest_size
    cdef readonly int block_size
    cdef readonly str name

    def __cinit__(self):
        self.digest_size = 8
        self.block_size = 8
        self.name = 'siphash24'

    def __init__(self, data=b'', /, *, key=b''):
        """Return a new SipHash24 hash object."""
        cdef const uint8_t[::1] keybytes = memoryview(key).cast('B')
        if keybytes.shape[0] > 16:
            raise ValueError("maximum key length is 16 bytes")
        cdef uint8_t padded[16]
        memset(padded, 0, sizeof(padded))
        memcpy(padded, &keybytes[0], keybytes.shape[0])
        c_siphash_init(&self.state, padded)
        cdef const uint8_t[::1] databytes = memoryview(data).cast('B')
        c_siphash_append(&self.state, &databytes[0], databytes.shape[0])

    def update(self, data=b''):
        """Update this hash object's state with the provided data."""
        cdef const uint8_t[::1] databytes = memoryview(data).cast('B')
        c_siphash_append(&self.state, &databytes[0], databytes.shape[0])

    def digest(self):
        """Return the digest value as a bytes object."""
        cdef CSipHash state
        memcpy(&state, &self.state, sizeof(state))
        cdef uint64_t hash = c_siphash_finalize(&state)
        return uint64le(hash)

    def hexdigest(self):
        """Return the digest value as a string of hexadecimal digits."""
        cdef CSipHash state
        memcpy(&state, &self.state, sizeof(state))
        cdef uint64_t hash = c_siphash_finalize(&state)
        return hexlify(hash)

    def intdigest(self):
        """Return the digest calue as a signed 64bit integer."""
        cdef CSipHash state
        memcpy(&state, &self.state, sizeof(state))
        cdef uint64_t hash = c_siphash_finalize(&state)
        return <int64_t>hash

    def copy(self):
        """Return a copy of the hash object."""
        cdef siphash24 r = siphash24.__new__()
        memcpy(&r.state, &self.state, sizeof(r.state))
        return r
