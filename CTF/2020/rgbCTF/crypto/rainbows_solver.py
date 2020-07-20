import hashlib

sha256_data={}
md5_data={}
#len 1
for i in range(32,127):
    sha256_data[hashlib.sha256(chr(i).encode()).hexdigest()]=chr(i)
    md5_data[hashlib.md5(chr(i).encode()).hexdigest()]=chr(i)
    
#len 2
for i in range(32,127):
    for j in range(32,127):
        sha256_data[hashlib.sha256((chr(i)+chr(j)).encode()).hexdigest()]=chr(i)+chr(j)
        md5_data[hashlib.md5((chr(i)+chr(j)).encode()).hexdigest()]=chr(i)+chr(j)

f=open("rainbows.txt","r")
enc=f.read().split('\n')

flag=''

for i in enc:
    if len(i)>32:
        flag+=sha256_data[i]
    else:
        flag+=md5_data[i]

print(flag)
