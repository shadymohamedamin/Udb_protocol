import socket
serverName='localhost'
serverPort=12000
clientSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
nickName=input('enter the nickName ')
message12=nickName+"#"+"server"+"#"+" joined the chat room"
clientSocket.sendto(message12.encode('UTF-8'),(serverName,serverPort))
while 1:
	print(nickName,end=' ')
	message=input(': ')
	serv=input('send this message to server or client? ')
	if message=="exit":break
	if serv=="server":message=nickName+"#"+"server"+"#"+message
	else:
		namee=input('enter the nickname ')
		message=nickName+"#"+namee+"#"+message
	clientSocket.sendto(message.encode('UTF-8'),(serverName,serverPort))
	data,clientAddress=clientSocket.recvfrom(2048)
	message1=data.decode("UTF-8")
	temp = message1
	arr = temp.split("#")
	print(arr[0],end=' : ')
	print(arr[2])


message12=nickName+"#"+"server"+"exit"
clientSocket.sendto(message12.encode('UTF-8'),(serverName,serverPort))
clientSocket.close()