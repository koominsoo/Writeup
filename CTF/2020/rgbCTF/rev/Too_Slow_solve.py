import binascii

p='42642a41473e425717696a7c49334216426e2e4d79242e48796e714112297e12426e6f53'
t=''
for i in range(0,len(p),8):
    t=p[i:i+8]+t
flag=''
for i in range(0,len(t),8):
    a=hex(int(t[i:i+8],16)^0x265d1d23)[2:]
    temp=''
    for i in range(0,len(a),2):
        temp=a[i:i+2]+temp
    flag+=temp
flag=binascii.unhexlify(flag)
print('rgbCTF{{{}}}'.format(flag))
