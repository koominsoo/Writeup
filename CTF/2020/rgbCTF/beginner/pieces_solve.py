a='9|2/9/:|4/7|8|4/2/1/2/9/'
for i in range(0,len(a),2):
    if a[i+1]=='|':
    	print(chr(ord(a[i])*2),end='')
    else:
    	print(chr(ord(a[i])*2+1),end='')
