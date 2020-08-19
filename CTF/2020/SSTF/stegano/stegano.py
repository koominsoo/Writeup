from PIL import Image

img=Image.open("challenge.bmp")
rgb=img.load()
height=img.height
width=img.width

bits=''
img.getpixel((2,1))
for i in range(height):
    for j in range(width):
        #print(f'{i},{j}')
        r,g,b=img.getpixel((j,i))
        bits+=str((r^g^b)&1)

f=open("out.bmp",'wb')
f.write(bytes.fromhex(hex(int(bits,2))[2:]))
f.close()