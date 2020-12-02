from pwn import *
from z3 import *
r=remote("mc.mandu-mandu.shop" ,40004)
for i in range(100):
    r.recvuntil(f"Task Number #{i}")
    data=r.recvuntil(":").split()
    s=Solver()
    x=Int("x")
    y=Int("y")
    s.add(b''.join(data[:3]))
    s.add(b''.join(data[3:6]))

