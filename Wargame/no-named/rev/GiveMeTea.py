# uncompyle6 version 2.11.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.9 (default, Oct  8 2020, 12:12:24)
# [GCC 8.4.0]
# Embedded file name: GiveMeTea.py
# Compiled at: 2016-12-31 18:23:55
import base64
import ctypes
import itertools
import math

def encrypt(plaintext, key):
    if not plaintext:
        return ''
    v = _str2vec(plaintext.encode())
    k = _str2vec(key.encode()[:16])
    bytearray = ''.join((_vec2str(_encipher(chunk, k)) for chunk in _chunks(v, 2)))
    return base64.b64encode(bytearray).decode()


def _encipher(v, k):
    y, z = [ ctypes.c_uint32(x) for x in v
           ]
    sum = ctypes.c_uint32(0)
    delta = 2654435769
    for n in range(32, 0, -1):
        sum.value += delta
        y.value += (z.value << 4) + k[0] ^ z.value + sum.value ^ (z.value >> 5) + k[1]
        z.value += (y.value << 4) + k[2] ^ y.value + sum.value ^ (y.value >> 5) + k[3]

    return [
     y.value, z.value]


def _chunks(iterable, n):
    it = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(it, n))
        if not chunk:
            return
        yield chunk


def _str2vec(value, l=4):
    n = len(value)
    num_chunks = math.ceil(n / l)
    chunks = [ value[l * i:l * (i + 1)] for i in range(num_chunks)
             ]
    return [ sum([ character << 8 * j for j, character in enumerate(chunk) ]) for chunk in chunks
           ]


def _vec2str(vector, l=4):
    return bytes((element >> 8 * i & 255 for element in vector for i in range(l))).replace('\x00', '')


def main():
    print 'Input : '
    key = 'HeyYou1GiveMeTea'
    message = input()
    if len(message) == 16:
        encrypt(message, key)
        cipher = encrypt(message, key)
        if cipher == 'Ganymd1ITx+0jKt+BU6+qA==':
            print 'flag : %s' % message
        else:
            print 'Try Again!'
    else:
        print 'Try Again!!'


if __name__ == '__main__':
    main()
