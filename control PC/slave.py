import time
import socket
import sys
import os

# Initialize s to socket
s = socket.socket()

# Initialize the host
host = "127.0.0.1"

# Initialize the port
port = 8080

# bind the socket with port and host
s.connect((host, port))


def main():
    print("Connected to Server.")

    # receive the command from master program
    command = s.recv(1024)
    command = command.decode()

    # match the command and execute it on slave system
    if command == "open":
        print("Command is :", command)
        s.send("Command received".encode())

        # you can give batch file as input here
        os.system('ls')


if __name__ == '__main__':
    main()
