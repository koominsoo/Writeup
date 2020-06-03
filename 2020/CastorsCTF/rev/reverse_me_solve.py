from pwn import *

r=remote("chals20.cybercastors.com",14427)
r.recvuntil("memory...\n")

flag=r.recvline().strip()

k='abcdefghijklmnopqrstuvwxyz'
key=10
flag=flag.split()

for i in range(len(flag)):
    if chr(int(flag[i],16)) in k:
        flag[i]=chr(ord(k[int(flag[i],16)-0x61-key])-2)
    else:
        flag[i]=chr(int(flag[i],16)-2)

#print(''.join(flag))

r.sendline(''.join(flag))
r.interactive()
