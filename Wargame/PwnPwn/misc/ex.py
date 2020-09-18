from pwn import *

#r=process("./brain_storm")
r=remote("ctf.subhack.xyz" ,1001)
context.log_level='debug'
r.recvuntil(b"(What? you solve these just with your hands? boo ----)\n")
r.recvline()
for i in range(300):
	data=r.recv(8).split()
	log.info(data)
	result=int(data[0])+int(data[2])
	r.sendline(str(result))

r.interactive()
