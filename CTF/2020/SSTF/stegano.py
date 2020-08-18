from PIL import Image

image=Image.open("challenge.bmp")
rgb=image.load()
bits=''
width,height=image.size
c=0
a=[]
r,g,b=map(a,image.split())

print(a)
"""for i in range(height-1):
	for j in range(width-1):
		r,g,b=rgb.getpixel((i,j))
		bits+=str((r^g^b)&1)
		c+=1
print(c)
"""
"""h=int(bits,2)
h=hex(h)[2:]
f=open("out.bmp","wb")
#f.write(h.encode('hex'))
f.write(bytes.fromhex(h))
f.close()
"""
"""
from PIL import Image
import numpy as np
image=Image.open("challenge.bmp")
r,g,b=map(np.array,image.split())
binstr='0b'
d=0
e=0
for a,b,c in zip(r,g,b):
	e+=1
	for i in range(0,image.width):
		binstr+=str(int(a[i]^b[i]^c[i])&1)
		d+=1
	print(d)
	d=0

print(e)
print(image.width)
print(image.height)
"""
