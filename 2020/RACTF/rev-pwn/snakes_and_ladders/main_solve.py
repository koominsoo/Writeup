

flag='fqtbjfub4uj_0_d00151a52523e510f3e50521814141c'
dec=''
num2=[]
num=[]
alphabet='abcdefghijklmnopqrstuvwxyz'

for i in range(15,len(flag),2):
    num.append(int(flag[i:i+2],16))

for i in range(len(num)):
    num[i]=chr(num[i]^ord('a'))

for i in range(0,15):
    if flag[i] in alphabet:
        num2.append(alphabet[ord(flag[i])-14-97])
    else:
        num2.append(chr(ord(flag[i])))
c1=0
c2=0

for i in range(30):
    if i%2==0:
        dec+=num2[c1]
        c1+=1
    else:
        dec+=num[c2]
        c2+=1
print(dec)
