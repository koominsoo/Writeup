


# rgbCTF writeup

## REV
### Too Slow
***
### Advanced_Reversing_Mechanics_1
***
## CRYPTO
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
## BEGINNER
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
## MISC
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
