from pwn import *
r=remote("mc.mandu-mandu.shop" ,40000)
context.log_level='debug'
for i in range(20):
    r.recvuntil(f"Task Number #{i}")
    r.sendline(str(eval(b''.join(r.recvuntil(":").split()[:3]))))

r.interactive()
