key=0x55
data="11 1C 18 1C 2E 2C 66 34 3D 2B 2D 65 27 0A 64 26 0A 26 65 78 30 66 26 2C 2C 28".split()
for i in data:
    print(f'{chr(int(i,16)^0x55)}',end='')

#DIMI{y3ah~x0r_1s_s0-e3syy}