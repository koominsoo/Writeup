from multiprocessing import Process, Queue

def work(id,start,end,data):
    f=open(f"out.{id}","wb")
    out=b''
    for i in range(start,end):
        temp=(((data[i]+25^149)^1)-18)&0xff
        if i % 10000==0:
            print(f'{id}: {i} : {temp}')
        out+=bytes([temp])
    f.write(out)
    f.close()


if __name__=="__main__":
    f=open("Encrypted_3번.exe","rb")
    byte=f.read()
    f.close()
    th1 = Process(target=work, args=(1, 0,1000000,byte))
    th2 = Process(target=work, args=(2, 1000000,2000000,byte))
    th3 = Process(target=work, args=(3, 2000000,3000000,byte))
    th4 = Process(target=work, args=(4, 3000000,len(byte),byte))
    th1.start()
    th2.start()
    th3.start()
    th4.start()
    th1.join()
    th2.join()
    th3.join()
    th4.join()
    print("endendendend")
    f1=open("out.1","rb")
    f2=open("out.2","rb")
    f3=open("out.3","rb")
    f4=open("out.4","rb")
    f5=open("out.exe","wb")
    f5.write(f1.read()+f2.read()+f3.read()+f4.read())
