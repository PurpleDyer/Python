import socket 


# making the host and port
host = socket.gethostbyname(socket.gethostname())
port = 12345


# making the socket and binding the host and the port together
s = socket.socket()
s.bind((host, port))


# making the host ready to listen
s.listen(1)
print("socket is listening...")


while True:
    try:
        # getting the connection and address from the connected user
        conn, addr = s.accept()
        print(f"got connection from: {addr}")


        # sending a message to the connected user
        conn.send("Connection Established".encode('ascii'))
        print('----------------------')


        # reciving messages from the connected client
        while True:
            message = conn.recv(1024).decode('ascii')
            
            if message == 'close':
                print(f"User [{addr[0]}] left the connection")
                break
            else:
                print(f"[{addr[0]}]: {message}")


        # closing the connection to the server
        conn.close()
        print("Connection Closed")


    # exception handling
    except ConnectionResetError:
        print("CONNECTION LOST")
        conn.close()