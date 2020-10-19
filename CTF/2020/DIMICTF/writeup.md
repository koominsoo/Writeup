

# DIMICTF 2020 writeup
## MISC 100 | [logo](https://github.com/snwox/Writeup/blob/master/CTF/2020/DIMICTF/misc/m1.png)
![사진](https://github.com/snwox/Writeup/blob/master/CTF/2020/DIMICTF/res/1.JPG)
This is an image file of the logo of **Korea Digital Media High School.**
![사진](https://github.com/snwox/Writeup/blob/master/CTF/2020/DIMICTF/res/2.JPG)
Open with **HxD** to find flag at the end of the file.
## PWN 100 | [binary](https://github.com/snwox/Writeup/blob/master/CTF/2020/DIMICTF/pwn/pwn_100_cdbc21aa77e4d37d),[libc-2.27.so](https://github.com/snwox/Writeup/blob/master/CTF/2020/DIMICTF/pwn/libc-2.27.so)
```asm
   0x0000000000401214 <+94>:    lea    rax,[rbp-0x40]
   0x0000000000401218 <+98>:    mov    rdi,rax
   0x000000000040121b <+101>:   mov    eax,0x0
   0x0000000000401220 <+106>:   call   0x4010b0 <gets@plt>
   0x0000000000401225 <+111>:   lea    rax,[rbp-0x40]
   0x0000000000401229 <+115>:   mov    edx,0x4
   0x000000000040122e <+120>:   mov    rsi,rax
   0x0000000000401231 <+123>:   lea    rdi,[rip+0xdcc]        # 0x402004
   0x0000000000401238 <+130>:   call   0x401080 <strncmp@plt>
   0x000000000040123d <+135>:   test   eax,eax
   0x000000000040123f <+137>:   je     0x40124f <main+153>
   0x0000000000401241 <+139>:   lea    rax,[rbp-0x40]
   0x0000000000401245 <+143>:   mov    rdi,rax
   0x0000000000401248 <+146>:   call   0x401090 <puts@plt>
   0x000000000040124d <+151>:   jmp    0x4011fe <main+72>
   0x000000000040124f <+153>:   nop
   0x0000000000401250 <+154>:   mov    eax,0x0
   0x0000000000401255 <+159>:   leave
   0x0000000000401256 <+160>:   ret

```
Just get the input and end. (**simple ROP**). Get libcbase address and return to **oneshot_gadget**.

After ubuntu 18.04, at do_system+1094, It can occurs error, because the stack must be arranged in 16 bytes. So just add a ret; gadget before return to One-shot gadget.
<br>exploit file : [ex1.py](https://github.com/snwox/Writeup/blob/master/CTF/2020/DIMICTF/pwn/ex1.py)
## PWN 200 | [binary](https://github.com/snwox/Writeup/blob/master/CTF/2020/DIMICTF/pwn/pwn_200_f03f3d4ad43a422a)
```asm
   0x00000000004011b4 <+34>:    mov    DWORD PTR [rbp-0x10],0x0
   0x00000000004011bb <+41>:    call   0x401080 <getchar@plt>
   0x00000000004011c0 <+46>:    mov    BYTE PTR [rbp-0x1],al
   0x00000000004011c3 <+49>:    cmp    BYTE PTR [rbp-0x1],0xa
   0x00000000004011c7 <+53>:    je     0x4011de <main+76>
   0x00000000004011c9 <+55>:    mov    eax,DWORD PTR [rbp-0x10]
   0x00000000004011cc <+58>:    lea    edx,[rax+0x1]
   0x00000000004011cf <+61>:    mov    DWORD PTR [rbp-0x10],edx
   0x00000000004011d2 <+64>:    cdqe
   0x00000000004011d4 <+66>:    movzx  edx,BYTE PTR [rbp-0x1]
   0x00000000004011d8 <+70>:    mov    BYTE PTR [rbp+rax*1-0x50],dl
   0x00000000004011dc <+74>:    jmp    0x4011bb <main+41>
   0x00000000004011de <+76>:    nop
   0x00000000004011df <+77>:    mov    eax,0x0
   0x00000000004011e4 <+82>:    leave
   0x00000000004011e5 <+83>:    ret
```
Get the input until '\n' . There is a **shell** function executing shell. My input value goes into [rbp-0x50+rax]. (rax = rbp-0x10)
- ret address =  rbp+8
- rax = rbp-0x10

Input until **[rbp-0x10]** and manipulate **[rbp-0x10]** to point **[rbp+8]**. **[rbp-0x50+rax]** -> **rbp+8**, **rax=0x50+8=0x58**. and Input the address of **shell function**

<br>exploit file : [ex2.py](https://github.com/snwox/Writeup/blob/master/CTF/2020/DIMICTF/pwn/ex2.py)

## REV 100 | [binary](https://github.com/snwox/Writeup/blob/master/CTF/2020/DIMICTF/rev/rev_100_704dc40c5c240202)
I used 'string' command to find flag, but "UPX" is found. So I unpacked it with UPX.
```html
   0x0000000000401d8d <+88>:    mov    eax,DWORD PTR [rbp-0x58]
   0x0000000000401d90 <+91>:    cdqe
   0x0000000000401d92 <+93>:    movzx  eax,BYTE PTR [rbp+rax*1-0x50]
   0x0000000000401d97 <+98>:    movsx  edx,al
   0x0000000000401d9a <+101>:   mov    eax,DWORD PTR [rbp-0x58]
   0x0000000000401d9d <+104>:   cdqe
   0x0000000000401d9f <+106>:   lea    rcx,[rip+0xbe35a]        # 0x4c0100 <data>
   0x0000000000401da6 <+113>:   movzx  eax,BYTE PTR [rax+rcx*1]
   0x0000000000401daa <+117>:   movsx  ecx,al
   0x0000000000401dad <+120>:   mov    eax,DWORD PTR [rip+0xbe33d]        # 0x4c00f0 <key>
   0x0000000000401db3 <+126>:   cmp    ecx,eax
   0x0000000000401db5 <+128>:   setne  al
   0x0000000000401db8 <+131>:   movzx  eax,al
   0x0000000000401dbb <+134>:   cmp    edx,eax
   0x0000000000401dbd <+136>:   je     0x401dd5 <main+160>
   0x0000000000401dbf <+138>:   lea    rdi,[rip+0x9323e]        # 0x495004
   0x0000000000401dc6 <+145>:   call   0x418960 <puts>
   0x0000000000401dcb <+150>:   mov    edi,0xffffffff
   0x0000000000401dd0 <+155>:   call   0x4101e0 <exit>
   0x0000000000401dd5 <+160>:   add    DWORD PTR [rbp-0x58],0x1
   0x0000000000401dd9 <+164>:   mov    eax,DWORD PTR [rbp-0x58]
   0x0000000000401ddc <+167>:   cmp    eax,DWORD PTR [rbp-0x54]
   0x0000000000401ddf <+170>:   jl     0x401d8d <main+88>
```
It read input and repeat this until it's len
```html
   0x0000000000401db3 <+126>:   cmp    ecx,eax
   0x0000000000401db5 <+128>:   setne  al
   0x0000000000401db8 <+131>:   movzx  eax,al
   0x0000000000401dbb <+134>:   cmp    edx,eax
```
- ecx = data[i]
- eax = key (0x55)
- edx = input[i]
If **data[i]** is different from **key**, It sets **al** = 1 and compares It with edx(input[i]). If not same, just call exit()
```html
0x4c0100 <data>:        0x34662c2e1c181c11      0x26640a27652d2b3d
0x4c0110 <data+16>:     0x2c2666307865260a      0x000000000000282c
```
see this data. All datas are differ from **key**(0x55). So my Input always must be '\x01'.  After roop, It prints "flag : {my input ('\x01\x01\x01 ....')}", and I can't find correct flag. So In my study groups, one expert thought **XOR** operation.
```python
key=0x55

data="11 1C 18 1C 2E 2C 66 34 3D 2B 2D 65 27 0A 64 26 0A 26 65 78 30 66 26 2C 2C 28".split()
for i in data:
    print(f'{chr(int(i,16)^0x55)}',end='')
#DIMI{y3ah~x0r_1s_s0-e3syy}
```
He was right. Those assembly-codes were trick. It was so simple
## REV 200 | [binary](https://github.com/snwox/Writeup/blob/master/CTF/2020/DIMICTF/rev/rev2/rev_200_9d619620c1b9888f),[enc file](https://github.com/snwox/Writeup/blob/master/CTF/2020/DIMICTF/rev/rev2/rev_200_88a1665152fbe898_enc)
![DIMICTF](https://github.com/snwox/Writeup/blob/master/CTF/2020/DIMICTF/res/dimi_rev_2_1.png)
<br>
symbols are disappeard.
![ddimictf](https://github.com/snwox/Writeup/blob/master/CTF/2020/DIMICTF/res/dimi_rev_2_2.png)
<br>
I opened the binary and restored functions.
![enter image description here](https://github.com/snwox/Writeup/blob/master/CTF/2020/DIMICTF/res/dimi_rev_2_3.png)
<br>
Now I can analyze the code more easily.

- v6 = v7 = /dev/urandom file.
- v11 = v17 = encoded file
- v10 = v16 = original file 
- v20 = random 4bytes in /dev/urandom
First, write random 4bytes in encoded file. And write each one byte XORed with random 4 byte. (random[ i%4 ]).

I can know random 4 byte used to encrypt. So gets first 4 bytes and XOR again with other data to decrypt "~_enc" file.
```python
data="""72 E2 66 45 36 AB 2B 0C 09 83 04 27 4B 86 56 77 10 81 05 70 4A D5 50 23 16 DA 04 74 46 83 07 20 44 DA 53 7D 41 D1 07 7C 17 D4 51 7C 43 83 07 7C 11 D4 56 23 16 D7 57 75 4A DA 03 74 47 87 53 24 46 D1 05 73 13 DA 5E 74 42 9F 6C""".split()
for i in  range(len(data)):
    data[i]=int(data[i],16)
key=data[:4]
data=data[4:]
dec=''
for i in  range(len(data)):
dec+=chr(data[i]^key[i%4]) 
print(dec)

#DIMI{abb9d02bcc5876fd8b14aae685833a9e6791aa9c60fd51088e15e5a43c6a8810
```
### ThaNks F0r R3ading. I really regret that I couldn't solve reversing problems. 
> \+ 2020 10 19 , after exam, I added rev writeup.
