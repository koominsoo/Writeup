str="1101111102120222020120111110101222022221022202022211"
s='abcdefghijklmnopqrstuvwxyz'*2
flag=''
c=0
dic=[x for x in range(13)]
for i in range(0,len(str),4):
    n=0
    d=str[i:i+4]
    for i in range(4):
        if i==0:
            n+=i
        else:
            n+=int(d[i])*(3*i)
    dic[c]=n
    c+=1

for j in range(0,97):
	flag=''
	for i in range(len(dic)):
    		flag+=chr((dic[i]+j)%27)

	print flag
print dic



