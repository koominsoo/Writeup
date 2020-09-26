f=open("c:/Users/황선우/OneDrive/문서/GitHub/Writeup/CTF/2020/정보보호올림피아드/Q5/picture","rb")

a=f.read()
f.close()
b=b''
f=open("c:/Users/황선우/OneDrive/문서/GitHub/Writeup/CTF/2020/정보보호올림피아드/Q5/out","wb")
for i in range(len(a)):
	b+=bytes([0xff-a[i]])
f.write(b)
f.close()