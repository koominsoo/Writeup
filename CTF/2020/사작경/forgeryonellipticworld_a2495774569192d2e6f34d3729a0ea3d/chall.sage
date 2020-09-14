#!/usr/bin/env sage
from hashlib import sha256
from secret import mailmsg, d

# NIST P-256
p = 2 ** 256 - 2 ** 224 + 2 ** 192 + 2 ** 96 - 1
Gx = 0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296
Gy = 0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5
a = -3
b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
print(p)

def myrandom():
    base = 1 << 128
    return randint(base + 1, base + 999)


class Chall:

    def __init__(self, p, a, b, Gx, Gy, myrandom, d):
        self.E = EllipticCurve(IntegerModRing(p), [a, b])
        self.G = self.E(Gx, Gy)
        self.n = self.E.order()
        self.d = d
        assert self.d < self.n and is_prime(self.n)
        self.Q_a = self.d * self.G
        self.myrandom = myrandom

    def sign(self, m):
        z = int.from_bytes(sha256(m).digest(), 'big')
        k = self.myrandom()
        while True:
            try:
                Q = k * self.G
                r, _ = Q.xy()
                assert r != 0
                r = r.lift()
                s = mod(inverse_mod(k, self.n) * (z + r * self.d), self.n).lift()
                assert s != 0
                break
            except Exception as e:
                print(e)
                continue
        return r, s

    def verify(self, m, sig):
        r, s = sig
        if not (1 <= r < self.n and 1 <= s < self.n):
            return False

        z = int.from_bytes(sha256(m).digest(), 'big')
        sinv = inverse_mod(s, self.n)
        u1 = z * sinv % self.n
        u2 = r * sinv % self.n
        Q = u1 * self.G + u2 * self.Q_a
        if Q == self.E(0):
            return False
        x, _ = Q.xy()

        return x == r


if __name__ == '__main__':
    c = Chall(p, a, b, Gx, Gy, myrandom, d)
    print(c.Q_a.xy())

    for _ in range(1000):
        m = mailmsg()
        sig = r, s = c.sign(m)
        print(hex(r), hex(s), sha256(m).hexdigest())
        assert c.verify(m, sig), 'ECDSA Verification Failure'

    # assert flag == 'flag{{{:s}}}'.format(sha256(str(d).encode()).hexdigest())
