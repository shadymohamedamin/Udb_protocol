import socket
serverPort=12000
serverSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSocket.bind(('',serverPort))
res=[]
mp={}
#mp['s']=(2,3)
#print(mp['s'])
nickName="admin"
while 1:
	data,clientAddress=serverSocket.recvfrom(2048)
	message1=data.decode("UTF-8")
	value=clientAddress
	if value not in res:
		res.append(clientAddress)
	
	temp=message1
	arr=temp.split("#")
	if arr[1]=="server":
		print(arr[0],end=' : ')
		print(arr[2])
	else:
		serverSocket.sendto(message1.encode("UTF-8"),mp[arr[1]])
		continue
	mp[arr[0]]=clientAddress
	if arr[2]=="exit":res.remove(clientAddress)
	print(nickName,end=' ')
	message2=input(': ')
	message2="server"+"#"+nickName+"#"+message2

	choise=input('choose which client you want to send this data ')
	
	if choise=="all":
		for x in res:
			serverSocket.sendto(message2.encode("UTF-8"),x)
	else:
		serverSocket.sendto(message2.encode("UTF-8"),mp[choise])

    #message=data.decode("UTF-8")
    #print(clientAddress)
    #print('    ')
    #print(message)
    #modifiedMessage=message.upper()
    #serverSocket.sendto(modifiedMessage.encode("UTF-8"),clientAddress) 