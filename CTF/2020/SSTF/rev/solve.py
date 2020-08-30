enc='Dtd>=mhpNCqz?N!j(Z?B644[.$~96b6zjS*2t&'
xor='u7fl(3JC=UkJGEhPk{q`/X5UzTI.t&A]2[rPM9'

flag=''.join(chr(ord(a)^ord(b)) for a,b in zip(enc[::-1],xor))
print(flag)
