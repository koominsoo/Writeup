from binascii import unhexlify

f=open("pooh.jpg","r")


hexdata=""
while 1:
    t=f.readline().split()
    if t[0]=='0000ccc0:':
        hexdata+=t[1]+t[2]+t[3]
        break
    for j in range(1,9):
        hexdata+=t[j]

firstformat="ffd8ffe000104a46494600010101012c"
hexdata=firstformat+hexdata
hexdata=unhexlify(hexdata)
f.close()

f=open("pooh_solve.jpg","wb")
f.write(hexdata)
f.close()


