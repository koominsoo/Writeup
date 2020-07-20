#!/usr/bin/env python3

from PIL import Image
import binascii
img = Image.open("un.png")
pixels = img.load()
bits=''
for i in range(img.width):
    for j in range(img.height):
        pixel=pixels[i,j]
        pixel=pixel[1]>>1
        pixel=bin(pixel)
        bit=pixel[len(pixel)-1]
        bits+=bit
        t=hex(int(bits,2))[2:]
        if len(t)%2!=0 or t==0:
            continue
        flag=binascii.unhexlify(t)
        if b'}' in flag:
            print(flag)
            exit(0)
