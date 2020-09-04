from z3 import *
v2=BitVec("v2",24)
v3=BitVec("v3",24)
s=Solver()
s.add(v3 - 10000 < 1000,v2 - 26000 < 1000)
s.add(v2 - 10000 <= 89999,v3 - 10000 <= 89999)
s.add(v2 + v3*(v2 - 1) - 3*(v3/2) ^ 11468462 == 15313472)
s.add( v2 > 10000,v3 > 10000)

if s.check():
    print(s.model())
