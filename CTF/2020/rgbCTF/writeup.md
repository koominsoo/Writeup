# rgbCTF writeup


# REV
### Too Slow
[**Too_Slow**](https://github.com/snwox/Writeup/blob/master/CTF/2020/rgbCTF/rev/Too_Slow) ELF file is given.
### main
```c++
undefined8 main(void)

{
  uint uVar1;
  
  puts("Flag Decryptor v1.0");
  puts("Generating key...");
  uVar1 = getKey();
  win((ulong)uVar1);
  return 0;
}

```
Generate Key by **getKey()** function and call **win(Key)**
### getKey()
```c++
ulong getKey(void)

{
  uint local_10;
  uint local_c;
  
  local_10 = 0;
  while (local_10 < 0x265d1d23) {
    local_c = local_10;
    while (local_c != 1) {
      if ((local_c & 1) == 0) {
        local_c = (int)local_c / 2;
      }
      else {
        local_c = local_c * 3 + 1;
      }
    }
    local_10 = local_10 + 1;
  }
  return (ulong)local_10;
}
```
while local_10 < 0x265d1d23, perform a certain operation. It takes a great deal of time. But local_10 increases by 1. So, you can see that Key is **0x265d1d23**
### win ( uint *param_1 )
```c++
void win(uint param_1)

{
  long in_FS_OFFSET;
  uint local_3c;
  undefined8 local_38;
  undefined8 local_30;
  undefined8 local_28;
  undefined8 local_20;
  undefined4 local_18;
  undefined local_14;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_38 = 0x12297e12426e6f53;
  local_30 = 0x79242e48796e7141;
  local_28 = 0x49334216426e2e4d;
  local_20 = 0x473e425717696a7c;
  local_18 = 0x42642a41;
  local_14 = 0;
  local_3c = 0;
  while (local_3c < 9) {
    *(uint *)((long)&local_38 + (ulong)local_3c * 4) =
         *(uint *)((long)&local_38 + (ulong)local_3c * 4) ^ param_1;
    local_3c = local_3c + 1;
  }
  printf("Your flag: rgbCTF{%36s}\n",&local_38);
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}
```
Xor EBP-0x38~0x18 with Key. (by 4 byte), and print xored string with Flag Format.

Just xor the numbers with 0x265d1d23. [**Too_Slow_solve.py**](https://github.com/snwox/Writeup/blob/master/CTF/2020/rgbCTF/rev/Too_Slow_solve.py)

***
### Advanced_Reversing_Mechanics_1
[**Advanced_Reversing_Mechanics_1.o**](https://github.com/snwox/Writeup/blob/master/CTF/2020/rgbCTF/rev/Advanced_Reversing_Mechanics_1.o) object file is given. output is also given.
>71, 66, 61, 42, 53, 45, 7A, 40, 51, 4C, 5E, 30, 79, 5E, 31, 5E, 64, 59, 5E, 38, 61, 36, 65, 37, 63, 7C,
### encryptFlag ( char *param_1 )
```c++
void encryptFlag(char *param_1)

{
  char cVar1;
  
  cVar1 = *param_1;
  if (cVar1 == '\0') {
    return;
  }
  do {
    *param_1 = cVar1 + -1;
    param_1 = param_1 + 1;
    cVar1 = *param_1;
  } while (cVar1 != '\0');
  return;
}
```
This program encrypts flag with encryptFlag() function. but I can't run this ARM binary. Encrypt routine is so simple. Decreses the values of characters by 1. Conversely, if you increse those by 1, you can get a Flag.
```
=> 71,66,61,42,53,45,7A,40,51,4C,5E,30,79,5E,31,5E,64,59,5E,38,61,36,65,37,63,7C,
=> 72,67,62,43,54,46,7b,41,52,4d,5f,31,7a,5f,32,5f,65,5a,5f,39,62,37,66,38,64,7d
=> rgbCTF{ARM_1z_2_eZ_9b7f8d}
```
***
# CRYPTO
### Rainbows
[**rainbows.txt**](https://github.com/snwox/Writeup/blob/master/CTF/2020/rgbCTF/crypto/rainbows.txt)

There are 32 and 64 bites strings. 32byte : encrypted with **MD5**. 64byte : encrypted with **SHA256**

I guess the name 'rainbows' is related with **rainbow table**
>What is the rainbow table?
>>It's a table that stores all the values that can be created using the hash function.

![md5 crack](https://github.com/snwox/Writeup/blob/master/CTF/2020/rgbCTF/crypto/rainbow%20crack.PNG)
For example, crack the first 32byte string with MD5. And you can see 'r'

Then, I can solve this problem by making a Rainbow table with all the letters
>Sometimes two letters are encrypted.
>Therefore, the Rainbow table should also have a value that encodes all two letters.

Here is my S0usce c0de. [**rainbows_solver.py**](https://github.com/snwox/Writeup/blob/master/CTF/2020/rgbCTF/crypto/rainbows_solver.py)
***
# BEGINNER
### Pieces
[**Pieces.java**]([https://github.com/snwox/Writeup/blob/master/CTF/2020/rgbCTF/beginner/Pieces.java](https://github.com/snwox/Writeup/blob/master/CTF/2020/rgbCTF/beginner/Pieces.java))
A java source code is given.

```java
import java.io.*;
public class Main {
public static void main(String[] args) throws IOException {
BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
String input = in.readLine();
if (divide(input).equals("9|2/9/:|4/7|8|4/2/1/2/9/")) {
System.out.println("Congratulations! Flag: rgbCTF{" + input + "}");
} else {
System.out.println("Incorrect, try again.");
}
}
public static String divide(String text) {
String ans = "";
for (int i = 0; i < text.length(); i++) {
ans += (char)(text.charAt(i) / 2);
ans += text.charAt(i) % 2 == 0 ? "|" : "/";
}
return ans;
}
}
```
It receives an input which is encrypted with divide() function and compares with **"9|2/9/:|4/7|8|4/2/1/2/9/"**

Let's see divide() function.

It gets the input string one-by-one. If It is divided by two, It adds **|** to **ans**. Or, It adds **\\** to **ans**

Okay, let's decrypted that string. If the added character is **|** ,  multiplies the letter by 2 . Or, if the added character is **\\**, plus 1 and multiplies by 2
>comparing string is char code, not a number

Source code : [**pieces_solve.py**](https://github.com/snwox/Writeup/blob/master/CTF/2020/rgbCTF/beginner/pieces_solve.py)
***
# MISC
### Differences
[**DifferenceTest.java**](https://github.com/snwox/Writeup/blob/master/CTF/2020/rgbCTF/misc/DifferenceTest.java)

I don't know about java very well, but look at the code
#### code
```java
imporæ ÑÃva.util.*;

p¸bli· class DifferenceTest {

pub²ic static void main(String[Ø args) {

Scanner çÕ = Ÿew ScanÞÑr(Sy¦Óem.in);

System.out.priná("Enter first number: ");

int num1 = sc.nextInt();

System.out.pri¡t("Enter second ¢umber: ");

int num2 = sc.nexâIŸt();

int answer = num1 - num2;

Áystem.out.×rintln("The difference is: " + answer);

}

ú
```
There are some strange code. Using a little knowledge of Java, I can restore to original code.
#### original code
```java
import java.util.*;
public class DifferenceTest {

public static void main(String[] args) {

Scanner sc = Ÿew Scanner(System.in);

System.out.print("Enter first number: ");

int num1 = sc.nextInt();

System.out.print("Enter second ¢umber: ");

int num2 = sc.nextInt();

int answer = num1 - num2;

System.out.println("The difference is: " + answer);

}

}
```
Than, make two strings which have strange letters and original letters. like **æ** : **t,** **ÑÃ** : **ja**,  and two strings are **"æÑÃ"** and **"tja"**. And I found relatioinship between strange char and original char. **æ : 0xE6** by extended-ascii-code. **t : 0x74** by ascii-code. 0xE6 - 0x74 = **0x72 ('r')**. 'r' is the first Flag Format (rgbCTF{~~})

I made the two strings and wrote minus each string one-by-one

[**Diff_solve.py**](https://github.com/snwox/Writeup/blob/master/CTF/2020/rgbCTF/misc/Diff_solve.py)
***
