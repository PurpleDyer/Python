import socket


# making a socket connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# these have to be the same as the ones in host server
host = socket.gethostbyname(socket.gethostname())
port = 12345


try:
    # connecting to the host server
    s.connect((host, port))


    # reciving a message from the host server and decoding it to read it
    msg = s.recv(1024)
    print(msg.decode('ascii'))


    while True:
        # geting messages from the user
        message = input()


        # making a closing message 
        # sending the message to the server
        s.send(message.encode('ascii')) 
        
        
    # closing the connection to the server host
    s.close()


# exception handling
except ConnectionRefusedError:
    print("NO AVAILABLE CONNECTION FOUND")
    s.close()
