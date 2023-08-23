import socket as s
import keyboard

# =====================================================================================================================

so = s.socket(s.AF_INET, s.SOCK_STREAM)

host = s.gethostbyname(s.gethostname())
port = 12345

# =====================================================================================================================

try:
    so.connect((host, port))

except ConnectionRefusedError:
    print("NO CONNECTION FOUND")

else:
    while True:
        board = so.recv(1024).decode('ascii')
        print(board)

        direction = keyboard.read_key()
        so.send(direction.encode('ascii'))
        if direction == 'esc':
            so.close()
            break

# this is the client program for 10_host.py