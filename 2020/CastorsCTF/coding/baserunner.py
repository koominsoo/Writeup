from pwn import *
r=remote("chals20.cybercastors.com",14430)
r.recv(4096)
r.recv(4096)
r.sendline('\n')
b=r.recv()
b=b.split()

t=''

for i in range(len(b)):
    if chr(int(b[i],2))!=' ':
        t+=chr(int(b[i],2))
    else:
        b[i]=t
	t=''


print(b)
