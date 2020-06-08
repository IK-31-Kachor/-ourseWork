import socket, time

host = socket.gethostbyname(socket.gethostname())
port = 9090

clients = []

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))

quit = False
print(" Server Started! Welcome")
print(" _____________________________")

while not quit:
	try:
		data, addr = s.recvfrom(1024)

		if addr not in clients:
			clients.append(addr)

		itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

		print("["+addr[0]+"]=["+str(addr[1])+"]=["+itsatime+"]/",end="")
		print(data.decode("utf-8"))

		for client in clients:
			if addr != client:
				s.sendto(data,client)
	except:	
		print("\n Server Stopped! ")
		quit = True
		

s.close()


def run_script():
    # 
    handle = open("script2.py", "r")
    script = handle.read()
    handle.close()
    # -----------------------------------------------
    exec(script)


def handling_InputEvents(readList, serverSocket, list_of_lists):
    requestData = ''
    for client in readList:
        IP, port = getClientIP(client)
        if client is serverSocket:
            # Подія від серверного сокета - нове підключеня
            connection, client_address = client.accept()
            connection.setblocking(0)
            INPUTS.append(connection)
        else:
            # parsing:
            requestData = getRequest(client)
            sender = requestData[0]
            command = requestData[1]
            #------------------------------------------------------------------

           
            if command == "script2.py":
                save_file(command)

                server_file = "exit.txt"
                run_script()


            # append lists:
            if (command != '_new') and (command != '_all'):
                list_of_lists = WriteInList(list_of_lists, requestData)
            #------------------------------------------------------------------
            # form back msg:
            compare, msg =  createMessage(sender, command)
            #------------------------------------------------------------------
            # 'send' msg:
            if compare == 0:
                messageForSocket[port] = 'No messages for you.'
            else:
                messageForSocket[port] = msg
            print("Повідомлення для відповіді сформовано :", messageForSocket[port])
            #------------------------------------------------------------------
            print()
            print(list_sender)
            print(list_command)
            print(list_message)
            print(list_time)
            print(list_mark)
            print()

    return list_of_lists



