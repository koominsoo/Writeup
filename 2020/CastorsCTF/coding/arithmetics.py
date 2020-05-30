from pwn import *

r=remote("chals20.cybercastors.com",14429)
r.recv()
r.sendline("\n")
d={'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
d2={'multiplied-by':'*','plus':'+','divided-by':'//','minus':'-'}
c=0
def calc(a,op,b):
    global d
    global d2
    if a in d:
        a=d[a]
    if b in d:
        b=d[b]
    if op in d2:
        op=d2[op]

    if op=='+':
        return int(a)+int(b)
    if op=='-':
        return int(a)-int(b)
    if op=='//':
        return int(a)/int(b)
    if op=='*':
        return int(a)*int(b)


for i in range(100):
    s=r.recv()
    s=s.split()
    print(s)
    r.sendline(str(calc(s[2],s[3],s[4])))
    print(r.recvline(timeout=1)+str(i))

r.interactive()
