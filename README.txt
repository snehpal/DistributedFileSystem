The objective of this programming assignment is to create a distributed	file system for	reliable and secure file storage. A Distributed	File System is a client/server-based application that
allows client to store and retrieve files on multiple servers. One of the features of Distributed file system is that each file	can be divided in to pieces and	stored on different servers.
In this	assignment one client DFC (Distributed File Client) is uploading and downloading files onto and	from 4 servers DFS1, DFS2, DFS3 and DFS4 (DFS means Distributed	File Server.) In order
to be able to run this	assignment in a	single	machine. The DFS servers are all running locally with different	port numbers from 10001	to 10004.When DFC want to upload a file	to the 4 DFS servers,
it first split the file	in to 4	equal length pieces P1,	P2, P3,	P4 (a small length difference is acceptable if the total length	can not	be divided by 4). Then the DFC groups the 4 pieces in to 4 pairs
(P1, P2),(P2, P3),(P3, P4),(P4,	P1). At	last the DFC uploads them onto	4 DFS servers.So now the file has redundancy, 1	failed server will not	affect	the integrity of the file.
First, we make 4 server.py files in different folders and 1 client.py file in a different folder. Then, on the client side, we make a config file which contains the port numbers and the host name of the
4 servers and the username, password of the person it wants it to access. Then, on the server side, we make a config file, in which we have the details of the usernames and passwords of different persons.
The communication will only take place if the authentication is done properly. First of all, we make four sockets on the client side and connect them to the individual socket in the server code. The client
goes through its config file and checks the username, password and transmits to the servers. These servers check their config files and see if the username, password matches or not. If the username and password
from one server doesnt match, it wont proceed forward. So, the user authentication is done before hand.
If the user authentication returns true, then the user is prompted for his choice of commands. The user can choose between GET, PUT and LIST. In PUT command, the client uploads the original file onto	DFS using 
the scheme that	is mentioned in the problem.The file is divided into 4 parts by taking the md5 value of the file and then, mod 4 the file to assign the pattern.	
GET command downloads all available pieces of a file from all available DFS, if	the file is reconstructable then write	the file into your working folder. If the file is not reconstructable, then print “File	is incomplete".
What happens in GET is, that the client requests the server to send its files back to the client which have uploaded during the PUT command. The request is received and acknowledged by the server. It sends the 
files to the client who compiles them into one file and compares it to the original file and decides whether it is complete or not. LIST command inquires what file is stored on DFS servers, and print	file names stored
under Username	on DFS servers (e.g., ./DFS1/Alice, ./DFS2/Alice.). LIST command should	also be	able to	identify if file pieces	on DFSs are enough to reconstruct the original	file. 
If pieces are not enough (means	some servers are not available)	then “[incomplete]” will be added to the end of the file.
