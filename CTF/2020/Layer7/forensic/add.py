import os
base=os.path.dirname(os.path.realpath(__file__))
f=[0]*18
data=b''
for i in range(1,19):
    f[i-1]=open(base+f'\\f{i}.png','rb')
    data+=f[i-1].read()

for i in range(18):
    f[i].close()

with open(base+'\\outout.png','wb') as f:
    f.write(data)