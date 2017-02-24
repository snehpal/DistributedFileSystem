import socket
import os.path
import hashlib
import os
import re
import base64
size=1024

if os.path.isfile('dfc.conf'):
    f=open("dfc.conf",'rb')
    file=f.read()
    print(file)
    data=file.split()
    print(data)
    data1=data[2].split(":")
    #print (data1)
    host=data1[0]
    port=data1[1]
    print ("Host ip of "+ data[1]+ " is: "+host+" and port number of "+ data[1]+ " is: "+port)
    #print ("Port number of "+ data[1]+ " is: "+port)
    data2=data[5].split(":")
    #print(data2)
    host1=data2[0]
    port1=data2[1]
    print ("Host ip of "+ data[4]+ " is: "+host1+" and port number of "+ data[4]+ " is: "+port1 )
    #print ("Port number of "+ data[4]+ " is: "+port1)
    data3=data[8].split(":")
    #print(data3)
    host2=data3[0]
    port2=data3[1]
    print ("Host ip of "+ data[7]+ " is: "+host2+" and port number of "+ data[7]+ " is: "+port2)
    #print ("Port number of "+ data[7]+ " is: "+port2)
    data4=data[11].split(":")
    #print(data4)
    host3=data4[0]
    port3=data4[1]
    print ("Host ip of "+ data[10]+ " is: "+host3+" and port number of "+ data[10]+ " is: "+port3)
    user=data[12].split(':')
    userid=user[1]
    print(userid)
   
    passwd=data[13].split(':')
    rpasswd=passwd[1]
    print(rpasswd)
    auth=(userid+" "+ rpasswd)
    print (auth)
else:
    print ("File Not Found")
try:
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client.connect((host,int(port)))
except:
    print ("Couldn't initalize the socket")

try:
    client1=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client1.connect((host1,int(port1)))
    #client1.send(auth)
except:
    print ("Couldn't initalize the socket")
try:
    client2=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client2.connect((host2,int(port2)))
except:
    print ("Couldn't initalize the socket")
try:
    client3=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client3.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client3.connect((host3,int(port3)))
except:
    print ("Couldn't initalize the socket")
client.send(auth)
client1.send(auth)
client2.send(auth)
client3.send(auth)
x=client.recv(size)
x1=client1.recv(size)
x2=client2.recv(size)
x3=client3.recv(size)
print(x)
if x==("Invalid Username/Password.Please try again."):
    print ("Data can't be transmitted due to invalid user/password. Closing socket")
    client.close()

if x1==("Invalid Username/Password.Please try again."):
    print ("Data can't be transmitted due to invalid user/password. Closing socket")
    client1.close()
if x2==("Invalid Username/Password.Please try again."):
    print ("Data can't be transmitted due to invalid user/password. Closing socket")
    client2.close()
if x3==("Invalid Username/Password.Please try again."):
    print ("Data can't be transmitted due to invalid user/password. Closing socket")
    client3.close()
if x and x1 and x2 and x3=="User has been authenticated":
    i=input("Give the command along with the filename")
    y=i.split()
    print (y)
    if y[0]=="PUT":
        if os.path.isfile("Message.txt")==True:
            fh=open("Message.txt",'rb')
            r_fh=fh.read()
            size_getter=os.path.getsize("Message.txt")
            print("File size: "+ str(size_getter))
            div_sizegetter=int(size_getter/4)
            divarray=str(div_sizegetter).split('.')
            if len(divarray)!=1:
                kyl=int(div_sizegetter)+1
            else:
                kyl=int(div_sizegetter)
            print("Chunk size: "+ str(kyl))
            i=0
            u=size_getter
            #print("Rchunks:",str(r_chunks))
            ch_no=1
            list=[]
            while i!=u:
                fh.seek(i)
                chunk=fh.read((kyl))
                i=fh.tell()
                enc=base64.b64encode(chunk).decode()
                encrypt=str(ch_no)+'|||'+str(enc)
                enc_encrypt=encrypt.encode('utf8')
                list.append(enc_encrypt)
                #r_chunks=fh.read(kyl)
                ch_no=ch_no+1
            print(len(list))
            print(list)
            hash=hashlib.md5()
            hash.update(r_fh)
            htc=hash.hexdigest()
            int_htc=int(htc,16)
            print(int_htc)
            mod_htc=int_htc%4
            print (mod_htc)
            if mod_htc==0:
                dfs11=list[0]
                dfs12=list[1]
                dfs21=list[1]
                dfs22=list[2]        
                dfs31=list[2]
                dfs32=list[3]        
                dfs41=list[3]
                dfs42=list[0]
                client.send(dfs11)
                client1.send(dfs21)
                client2.send(dfs31)
                client3.send(dfs41)
                ack=client.recv(65538)
                a1=ack.decode('ascii')
                b1=a1.split('|||')[0]
                print("Ack for file: "+b1+ " received from Server 1")
                client.send(dfs12)
                ack1=client1.recv(65538)
                a2=ack1.decode('ascii')
                b2=a2.split('|||')[0]
                print("Ack for file: "+b2+ " received from Server 2")
                client1.send(dfs22)
                ack2=client2.recv(65538)
                a3=ack2.decode('ascii')
                b3=a3.split('|||')[0]
                print("Ack for file: "+b3+ " received from Server 3")
                client2.send(dfs32)
                ack3=client3.recv(65538)
                a4=ack3.decode('ascii')
                b4=a4.split('|||')[0]
                print("Ack for file: "+b4+ " received from Server 4")
                client3.send(dfs42)
                
            elif mod_htc==1:
                dfs11=list[3]
                dfs12=list[0]
                dfs21=list[0]
                dfs22=list[1]        
                dfs31=list[1]
                dfs32=list[2]        
                dfs41=list[2]
                dfs42=list[3]
                client.send(dfs11)
                client1.send(dfs21)
                client2.send(dfs31)
                client3.send(dfs41)
                ack=client.recv(65538)
                a1=ack.decode('ascii')
                b1=a1.split('|||')[0]
                print("Ack for file: "+b1+ " received from Server 1")
                client.send(dfs12)
                ack1=client1.recv(65538)
                a2=ack1.decode('ascii')
                b2=a2.split('|||')[0]
                print("Ack for file: "+b2+ " received from Server 2")
                client1.send(dfs22)
                ack2=client2.recv(65538)
                a3=ack2.decode('ascii')
                b3=a3.split('|||')[0]
                print("Ack for file: "+b3+ " received from Server 3")
                client2.send(dfs32)
                ack3=client3.recv(65538)
                a4=ack3.decode('ascii')
                b4=a4.split('|||')[0]
                print("Ack for file: "+b4+ " received from Server 4")
                client3.send(dfs42)
                
            elif mod_htc==2:
                dfs11=list[2]
                dfs12=list[3]
                dfs21=list[3]
                dfs22=list[0]        
                dfs31=list[0]
                dfs32=list[1]        
                dfs41=list[1]
                dfs42=list[2]
                client.send(dfs11)
                client1.send(dfs21)
                client2.send(dfs31)
                client3.send(dfs41)
                ack=client.recv(65538)
                a1=ack.decode('ascii')
                b1=a1.split('|||')[0]
                print("Ack for file: "+b1+ " received from Server 1")
                client.send(dfs12)
                ack1=client1.recv(65538)
                a2=ack1.decode('ascii')
                b2=a2.split('|||')[0]
                print("Ack for file: "+b2+ " received from Server 2")
                client1.send(dfs22)
                ack2=client2.recv(65538)
                a3=ack2.decode('ascii')
                b3=a3.split('|||')[0]
                print("Ack for file: "+b3+ " received from Server 3")
                client2.send(dfs32)
                ack3=client3.recv(65538)
                a4=ack3.decode('ascii')
                b4=a4.split('|||')[0]
                print("Ack for file: "+b4+ " received from Server 4")
                client3.send(dfs42)
                
            elif mod_htc==3:
                dfs11=list[1]
                dfs12=list[2]
                dfs21=list[2]
                dfs22=list[3]        
                dfs31=list[3]
                dfs32=list[0]        
                dfs41=list[0]
                dfs42=list[1]
                client.send(dfs11)
                client1.send(dfs21)
                client2.send(dfs31)
                client3.send(dfs41)
                ack=client.recv(65538)
                a1=ack.decode('ascii')
                b1=a1.split('|||')[0]
                print("Ack for file: "+b1+ " received from Server 1")
                client.send(dfs12)
                ack1=client1.recv(65538)
                a2=ack1.decode('ascii')
                b2=a2.split('|||')[0]
                print("Ack for file: "+b2+ " received from Server 2")
                client1.send(dfs22)
                ack2=client2.recv(65538)
                a3=ack2.decode('ascii')
                b3=a3.split('|||')[0]
                print("Ack for file: "+b3+ " received from Server 3")
                client2.send(dfs32)
                ack3=client3.recv(65538)
                a4=ack3.decode('ascii')
                b4=a4.split('|||')[0]
                print("Ack for file: "+b4+ " received from Server 4")
                client3.send(dfs42)
    if y[0]=="GET":
        client.send("Requesting files from server")
        client1.send("Requesting files from server")
        client2.send("Requesting files from server")    
        client3.send("Requesting files from server")
        while True:
            get=client.recv(66538)
            get1=client1.recv(66538)
            get2=client2.recv(66538)
            get3=client3.recv(66538)
            print ("Data coming from Server1: "+get)
            print("Data coming from Server2: "+get1)
            print("Data coming from Server3: "+get2)
            print("Data coming from Server4 :"+get3)

        
        
    