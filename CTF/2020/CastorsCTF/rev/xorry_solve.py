en='67687d775f7b615044536d6b24636826722b41682d26467c147a115015101d521e'
flag=''
c=0
for i in range(0,len(en),2):
    flag+=chr((int(en[i:i+2],16)+2)^c+10)
    c+=1

print(flag)
