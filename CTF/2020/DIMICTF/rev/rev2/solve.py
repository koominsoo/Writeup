data="""72 E2 66 45 36 AB 2B 0C 09 83 04 27 4B 86 56 77 10 81 05 70 4A D5 50 23 16 DA 04 74 46 83 07 20 44 DA 53 7D 41 D1 07 7C 17 D4 51 7C 43 83 07 7C 11 D4 56 23 16 D7 57 75 4A DA 03 74 47 87 53 24 46 D1 05 73 13 DA 5E 74 42 9F 6C""".split()
for i in range(len(data)):
    data[i]=int(data[i],16)
key=data[:4]
data=data[4:]
dec=''
for i in range(len(data)):
    dec+=chr(data[i]^key[i%4])

print(dec)