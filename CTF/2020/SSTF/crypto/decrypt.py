from binascii import *
import binascii
msg="RC4 is a Stream Cipher, which is very simple and fast."
e_msg='634c3323bd82581d9e5bbfaaeb17212eebfc975b29e3f4452eefc08c09063308a35257f1831d9eb80a583b8e28c6e4d2028df5d53df8'
e_flag='624c5345afb3494cdd6394bbbf06043ddacad35d28ceed112bb4c8823e45332beb4160dca862d8a80a45649f7a96e9cb'

e_msg=binascii.unhexlify(e_msg)
e_flag=binascii.unhexlify(e_flag)

key=''
flag=''
for i in range(len(e_msg)):
    key+=chr(ord(msg[i])^e_msg[i])

for i in range(len(e_flag)):
    flag+=chr(e_flag[i]^ord(key[i]))
print(flag)