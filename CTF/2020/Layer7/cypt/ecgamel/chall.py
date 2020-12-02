from sage.all import random_prime,EllipticCurve,GF,Integer,is_prime,next_prime
from secrets import randbelow,randbits
from math import isqrt
import subprocess

def bytes_to_int(x:bytes)->int:
    return int.from_bytes(x,'big')


def random_safe_prime(bits):
    p=random_prime(2**(bits-1))
    while not is_prime(2*p+1):
        p=next_prime(p)
    return 2*p+1


def generate_curve(bits):
    p=random_safe_prime(bits)
    rng=int(isqrt(int(p)))
    a=randbelow(rng)-rng//2
    b=randbelow(rng)-rng//2
    E=EllipticCurve(GF(p),[a,b])
    return E,p

def compress(x:bytes)->int:
    res=0
    for v in x:
        assert v&128 == 0
        res<<=7
        res|=v&127
    return res

ipt=input().encode('ascii')
iptint=compress(ipt)
bits=256
secret_key=randbits(bits-16)
for i in range(50):
    while True:
        E,p=generate_curve(bits)
        if E.is_x_coord(iptint):
            break
    M=E.lift_x(Integer(iptint))
    G=E.gens()[0]
    Y=secret_key*G
    print(G.xy(),p,Y.xy())
    xp=randbits(bits-16)
    C1=xp*G
    C2=xp*Y+M
    print(C1.xy(),C2.xy())

