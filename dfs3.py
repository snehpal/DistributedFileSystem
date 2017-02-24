#!usr/bin/env Python

import socket
import os.path
import hashlib
import select
import thread
import sys
import base64
host='127.0.0.1'
port=10003
size=1024
if os.path.isfile("dfs.conf")==True:
    fh=open("dfs.conf",'rb')
    file=fh.read()
    data=file.split()
    user=data[0].split(':')
    userid=user[1]
    print (userid)
    passwd=data[1].split(':')
    rpasswd=passwd[1]
    print (rpasswd)
    auth=(userid+" "+rpasswd)
    print (auth)

dfs1=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#dfs1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
dfs1.bind((host,(port)))
dfs1.listen(1)
while 1:
    conn,address=dfs1.accept()
    print ("Data is: ",conn)
    print ("Address is: ",address)
        #while True:
#     while True:
    data=conn.recv(size)
    print ("Data: ",data)
    user=data.split()
    print(user)
    username=user[0]
    print(username)


    #dfs1.connect((host,port))
    if data == auth:
        print ("It matches")
        a = "User has been authenticated"
        conn.sendall(a)
        #dfs1.send(message)
    else:
        print("It doesn't match")
        conn.sendall("Invalid Username/Password.Please try again.")
        
    data1=conn.recv(size)
    print ("Data1: ",data1)
    if not os.path.exists(username):
        os.makedirs(username)
    if data1 == "Requesting files from server":
        xx=open("C:\Users\Snehpal\Desktop\ITP Semester 1\Data Communications 1\ProgramAssign4\Server3\Dennis\Recv_3.txt.1",'rb')
        r_xx=xx.read()
        print(r_xx)
        conn.send(r_xx)
        xy=open("C:\Users\Snehpal\Desktop\ITP Semester 1\Data Communications 1\ProgramAssign4\Server3\Dennis\Recv_3.txt.2",'rb')
        r_xy=xy.read()
        print (r_xy)
        conn.send(r_xy)
    else:    
        recv_file=data1.decode('utf8')
        print(recv_file)
        num=recv_file.split('|||')[0]
        bum=recv_file.split('|||')[1]
        print (bum)
        sum=base64.b64decode(bum)
        print(sum)
        with open("C:\Users\Snehpal\Desktop\ITP Semester 1\Data Communications 1\ProgramAssign4\Server3\Dennis\Recv_3.txt.1",'wb') as fh:
            wr=fh.write(sum)
        msg=str(num)+'|||ACK'
        print (msg)
        enc_msg=msg.encode('ascii')
        print(enc_msg)
        conn.send(enc_msg)
        
        data2=conn.recv(size)
        print ("Data2: ",data2)
        recv_file1=data2.decode('utf8')
        print(recv_file1)
        num1=recv_file1.split('|||')[0]
        bum1=recv_file1.split('|||')[1]
        print (bum1)
        sum1=base64.b64decode(bum1)
        print(sum1)
        with open("C:\Users\Snehpal\Desktop\ITP Semester 1\Data Communications 1\ProgramAssign4\Server3\Dennis\Recv_3.txt.2",'wb') as fh:
            wr=fh.write(sum1)
        
       