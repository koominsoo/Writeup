# Fword CTF 2020 writeup
## pwn
### Welcome Pwner | 374 | [molotov](https://github.com/snwox/Writeup/blob/master/CTF/2020/FwordCTF/pwn/molotov)
Just binary file was given. 32bit ELF binary.
```c++
undefined4 vuln(void)

{
  char local_20 [24];
  
  printf("%x\n",system);
  puts("Input : ");
  gets(local_20);
  return 0;
}
```
BOF occurs in vuln function (canary was not found). The address of the **system** funcion was given, but **/bin/sh** string was not found and PIE was enable. So I can't input **/bin/sh** at **.bss** section 

https://libc.blukat.me
So I used that site and input **CTF server's system addr** in order to find the libc file on **CTF server**. **Four libc files** were found. 
```
payload : A*(0x1c+4) | system addr | DUMMY(4) | /bin/sh addr
```
I changed **/bin/sh** address in **four libc files** until I get a shell. [solve.py ](https://github.com/snwox/Writeup/blob/master/CTF/2020/FwordCTF/pwn/solve.py)

#thanks for reading
#review is on my blog https://snwo.tistory.com
