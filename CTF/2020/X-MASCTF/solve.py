def route_2(c,i):
	return c^(i+5)

def route_1(c,i):
    for j in range(3):
        c=((c>>7)|(2*c))&0xff
    return c
def route_3(c,i):
    for j in range(2):
        v5=c&1
        c=c>>1
        c=c|(v5<<7)
    return c
flag=''
ar=[251, 209, 81, 138, 238, 126, 84, 105, 155, 111, 119, 176, 128, 238, 112, 193, 41, 103, 113, 228, 156, 234, 114, 237, 147, 95, 17, 234, 164, 120]
for i in range(len(ar)):
    for j in range(0xff):
        if (route_3(route_2(route_1(j,i),i),i)^0xa) == ar[i]:
            flag+=chr(j)
print(flag)