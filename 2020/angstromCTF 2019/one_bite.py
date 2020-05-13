# encode = s[i]^0x3c

encoded=']_HZGUcHTURWcUQc[SUR[cHSc^YcOU_WA'

flag=''

for i in range(len(encoded)):
    flag+=chr(ord(encoded[i])^0x3c)

print flag

