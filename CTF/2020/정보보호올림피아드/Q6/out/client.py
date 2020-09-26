# Embedded file name: client.py
import Tkinter as tk
import tkMessageBox
import socket
from time import sleep
import threading
your_name = ''
opponent_name = ''
game_round = 0
game_timer = 4
your_choice = ''
opponent_choice = ''
TOTAL_NO_OF_ROUNDS = 1000
client = None
flag = None
window_main = tk.Tk()
window_main.title('Game Client')
serverFrame = tk.Frame(window_main)
lblHOST = tk.Label(serverFrame, text='Address:').pack(side=tk.LEFT)
entHost = tk.Entry(serverFrame)
entHost.pack(side=tk.LEFT)
lblPORT = tk.Label(serverFrame, text='Port:').pack(side=tk.LEFT)
entPort = tk.Entry(serverFrame)
entPort.pack(side=tk.LEFT)
serverFrame.pack(side=tk.TOP, pady=(5, 0))
top_welcome_frame = tk.Frame(window_main)
lbl_name = tk.Label(top_welcome_frame, text='Name:')
lbl_name.pack(side=tk.LEFT)
ent_name = tk.Entry(top_welcome_frame)
ent_name.pack(side=tk.LEFT)
btn_connect = tk.Button(top_welcome_frame, text='Connect', command=lambda : connect())
btn_connect.pack(side=tk.LEFT)
top_welcome_frame.pack(side=tk.TOP)
top_message_frame = tk.Frame(window_main)
lbl_line = tk.Label(top_message_frame, text='***********************************************************').pack()
lbl_welcome = tk.Label(top_message_frame, text='')
lbl_welcome.pack()
lbl_line_server = tk.Label(top_message_frame, text='***********************************************************')
lbl_line_server.pack_forget()
top_message_frame.pack(side=tk.TOP)
top_frame = tk.Frame(window_main)
top_left_frame = tk.Frame(top_frame, highlightbackground='green', highlightcolor='green', highlightthickness=1)
lbl_your_name = tk.Label(top_left_frame, text='Your name: ' + your_name, font='Helvetica 13 bold')
lbl_opponent_name = tk.Label(top_left_frame, text='Opponent: ' + opponent_name)
lbl_your_name.grid(row=0, column=0, padx=5, pady=8)
lbl_opponent_name.grid(row=1, column=0, padx=5, pady=8)
top_left_frame.pack(side=tk.LEFT, padx=(10, 10))
top_right_frame = tk.Frame(top_frame, highlightbackground='green', highlightcolor='green', highlightthickness=1)
lbl_game_round = tk.Label(top_right_frame, text='Game round (x) starts in', foreground='blue', font='Helvetica 14 bold')
lbl_timer = tk.Label(top_right_frame, text=' ', font='Helvetica 24 bold', foreground='blue')
lbl_game_round.grid(row=0, column=0, padx=5, pady=5)
lbl_timer.grid(row=1, column=0, padx=5, pady=5)
top_right_frame.pack(side=tk.RIGHT, padx=(10, 10))
top_frame.pack_forget()
middle_frame = tk.Frame(window_main)
lbl_line = tk.Label(middle_frame, text='***********************************************************').pack()
lbl_line = tk.Label(middle_frame, text='**** GAME LOG ****', font='Helvetica 13 bold', foreground='blue').pack()
lbl_line = tk.Label(middle_frame, text='***********************************************************').pack()
round_frame = tk.Frame(middle_frame)
lbl_round = tk.Label(round_frame, text='Round')
lbl_round.pack()
lbl_your_choice = tk.Label(round_frame, text='Your choice: None', font='Helvetica 13 bold')
lbl_your_choice.pack()
lbl_opponent_choice = tk.Label(round_frame, text='Opponent choice: ' + 'None')
lbl_opponent_choice.pack()
lbl_result = tk.Label(round_frame, text=' ', foreground='blue', font='Helvetica 14 bold')
lbl_result.pack()
round_frame.pack(side=tk.TOP)
final_frame = tk.Frame(middle_frame)
lbl_line = tk.Label(final_frame, text='***********************************************************').pack()
lbl_final_result = tk.Label(final_frame, text=' ', font='Helvetica 13 bold', foreground='blue')
lbl_final_result.pack()
lbl_line = tk.Label(final_frame, text='***********************************************************').pack()
final_frame.pack(side=tk.TOP)
middle_frame.pack_forget()
button_frame = tk.Frame(window_main)
photo_rock = tk.PhotoImage(file='rock.gif')
photo_paper = tk.PhotoImage(file='paper.gif')
photo_scissors = tk.PhotoImage(file='scissors.gif')
btn_rock = tk.Button(button_frame, text='Rock', command=lambda : choice('rock'), state=tk.DISABLED, image=photo_rock)
btn_paper = tk.Button(button_frame, text='Paper', command=lambda : choice('paper'), state=tk.DISABLED, image=photo_paper)
btn_scissors = tk.Button(button_frame, text='Scissors', command=lambda : choice('scissors'), state=tk.DISABLED, image=photo_scissors)
btn_rock.grid(row=0, column=0)
btn_paper.grid(row=0, column=1)
btn_scissors.grid(row=0, column=2)
button_frame.pack(side=tk.BOTTOM)

def game_logic(you, opponent):
    winner = ''
    rock = 'rock'
    paper = 'paper'
    scissors = 'scissors'
    player0 = 'you'
    player1 = 'opponent'
    if you == opponent:
        winner = 'draw'
    elif you == rock:
        if opponent == paper:
            winner = player1
        else:
            winner = player0
    elif you == scissors:
        if opponent == rock:
            winner = player1
        else:
            winner = player0
    elif you == paper:
        if opponent == scissors:
            winner = player1
        else:
            winner = player0
    return winner


def enable_disable_buttons(todo):
    if todo == 'disable':
        btn_rock.config(state=tk.DISABLED)
        btn_paper.config(state=tk.DISABLED)
        btn_scissors.config(state=tk.DISABLED)
    else:
        btn_rock.config(state=tk.NORMAL)
        btn_paper.config(state=tk.NORMAL)
        btn_scissors.config(state=tk.NORMAL)


def connect():
    global HOST_ADDR
    global your_name
    global HOST_PORT
    HOST_ADDR = entHost.get()
    HOST_PORT = int(entPort.get())
    if len(ent_name.get()) < 1:
        tkMessageBox.showerror(title='ERROR!!!', message='You MUST enter your first name <e.g. John>')
    else:
        your_name = ent_name.get()
        lbl_your_name['text'] = 'Your name: ' + your_name
        connect_to_server(your_name, HOST_ADDR, HOST_PORT)


def count_down(my_timer, nothing):
    global game_round
    if game_round <= TOTAL_NO_OF_ROUNDS:
        game_round = game_round + 1
    lbl_game_round['text'] = 'Game round ' + str(game_round) + ' starts in'
    while my_timer > 0:
        my_timer = my_timer - 1
        print 'game timer is: ' + str(my_timer)
        lbl_timer['text'] = my_timer
        sleep(1)

    enable_disable_buttons('enable')
    lbl_round['text'] = 'Round - ' + str(game_round)
    lbl_final_result['text'] = ''


def choice(arg):
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
    else:
        game_round = 0
        lbl_result['text'] = 'Result: DRAW'
        lbl_final_result['text'] = 'Game Out'
        lbl_final_result.config(foreground=color)
        client.close()
    if game_round == TOTAL_NO_OF_ROUNDS:
        final_result = ''
        color = ''
        enable_disable_buttons('disable')
        game_round = 0
    return


def connect_to_server(name, HOST_ADDR, HOST_PORT):
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
    except Exception as e:
        tkMessageBox.showerror(title='ERROR!!!', message='Cannot connect to host: ' + HOST_ADDR + ' on port: ' + str(HOST_PORT) + ' Server may be Unavailable. Try again later')


def receive_message_from_server(sck, m):
    global opponent_choice
    global opponent_name
    global flag
    while True:
        from_server = sck.recv(4096)
        if not from_server:
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


def on_closing():
    if tkMessageBox.askokcancel('Quit', 'Do you want to quit?'):
        if client:
            try:
                client.send('close$close')
                window_main.destroy()
                client.close()
            except:
                window_main.destroy()

        else:
            window_main.destroy()


window_main.protocol('WM_DELETE_WINDOW', on_closing)
window_main.mainloop()