import socket
from time import sleep
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('1.209.148.228',2021))
client.send(b'snwo')
f=client.recv(4096)
sleep(2)
client.send(b'0')
client.send(b'state$Yes')
f=client.recv(4096)
f=client.recv(4096)
for i in range(1,1002):
    print(i)
    client.send(f'round${i}'.encode())
    client.send(b'state$Yes')
    f=client.recv(4096)
    print(f)

