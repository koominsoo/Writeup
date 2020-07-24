



# rgbCTF writeup

## REV
### Too Slow
***
### Advanced_Reversing_Mechanics_1
***
## CRYPTO
### Rainbows
[rainbows.txt](https://github.com/snwox/Writeup/blob/master/CTF/2020/rgbCTF/crypto/rainbows.txt)

There are 32 and 64 bites strings. 32byte : encrypted with **MD5**. 64byte : encrypted with **SHA256**

I guess the name 'rainbows' is related with **rainbow table**
>What is rainbow table?
>>It's a table that stores all the values that can be created using the hash function.

![md5 crack](https://github.com/snwox/Writeup/blob/master/CTF/2020/rgbCTF/crypto/rainbow%20crack.PNG)
For example, crack first 32byte string with MD5. And you can see 'r'

Then, I can solve this problem by making a Rainbow table with all the letters
>Sometimes two letters are encrypted.
>Therefore, the Rainbow table should also have a value that encodes all two letters.

Here is my Sousce code : [rainbows_solver.py](https://github.com/snwox/Writeup/blob/master/CTF/2020/rgbCTF/crypto/rainbows_solver.py)
***
## BEGINNER
### Pieces
[Pieces.java]([https://github.com/snwox/Writeup/blob/master/CTF/2020/rgbCTF/beginner/Pieces.java](https://github.com/snwox/Writeup/blob/master/CTF/2020/rgbCTF/beginner/Pieces.java))
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
It receives input which is encrypted with divide() function and compares with **"9|2/9/:|4/7|8|4/2/1/2/9/"**

Let's see divide() function.

It gets the input string one-by-one. If It is divided by two, It adds **|** to **ans**. Or, It adds **\\** to **ans**

Okay, let's decrypted that string.
If the added character is **|**,  multiplies the letter by 2 . Or, the added character is **\\**, plus 1 and multiplies by 2
>First letter, 9 is not the number 9. the 9 is 39 by ascii-code

Source code : [pieces_solve.py](https://github.com/snwox/Writeup/blob/master/CTF/2020/rgbCTF/beginner/pieces_solve.py)
***
## MISC
