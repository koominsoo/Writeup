import os
filepath=os.path.dirname(os.path.realpath(__file__))
with open(filepath+'\\manduu23.png',"rb") as f:
    data=f.read()
    data=b''.join(bytes([data[i]]) for i in range(len(data)-1,-1,-1))
with open(filepath+"\\manduu23_reversed.png","wb") as f:
    f.write(data)
