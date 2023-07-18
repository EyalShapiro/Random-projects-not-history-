import time
import socket
import sys
import os
# server
s = socket.socket()

# Initialize the host
host = socket.gethostname()

port = 8080


def main():

    # Bind the socket with port and host
    s.bind(('', port))

    print("waiting for connections...")

    s.listen()

    conn, addr = s.accept()

    print(addr, "is connected to server")

    command = input(str("Enter Command :"))

    conn.send(command.encode())

    print("Command has been sent successfully.")

    data = conn.recv(1024)

    if data:
        print("command received and executed successfully.")


if __name__ == '__main__':
    main()
