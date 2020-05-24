from PIL import Image
import binascii

img=Image.open("unimportant.png")
pixels=img.load()
i=0
bits=''

def flag(c):
    global bits
    bits+=c
    print(hex(int(bits,2)))

for x in range(img.width):
    for y in range(img.height):
        pixel=pixels[x,y]
        pixel=pixel[1]
        pixel=bin(pixel)[::-1]
        if pixel[1]=='b':
            bit=pixel[0]
        else:
            bit=pixel[1]
        flag(bit)
        if i>280:
            exit(0)
        i+=1
"""
a="0x746a6374667b6e30745f7468335f6c653473745f7369396e31666963346e767d0a6661"
for i in range(2,len(a),2):
      print(chr(int(a[i:i+2],16)),end='')

tjctf{n0t_th3_le4st_si9n1fic4nv}
fa <- out of len of the flag
"""
