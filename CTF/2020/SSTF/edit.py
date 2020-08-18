f=open("output.txt")
msg=f.readline().strip()
flag=f.readline().strip()

print(msg)
print(flag)
for i in range(0,len(msg),2):
    print(chr(int(msg[i:i+2],16)),end='')

print('\n\n')
for i in range(0,len(flag),2):
    print(chr(int(flag[i:i+2],16)),end='')
