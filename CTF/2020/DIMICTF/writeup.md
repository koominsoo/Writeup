
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
### ThaNks F0r R3ading. I really regret that I couldn't solve reversing problems.
