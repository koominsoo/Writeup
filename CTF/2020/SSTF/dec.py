s='u7fl(3JC=UkJGEhPk{q`/X5UzTI.t&A]2[rPM9'
enc='Dtd>=mhpNCqz?N!j(Z?B644[.$~96b6zjS*2t&'
flag=''
for i in range(len(s)):
	flag=chr(ord(s[len(s)-i-1])^ord(enc[i]))+flag

print(flag)
