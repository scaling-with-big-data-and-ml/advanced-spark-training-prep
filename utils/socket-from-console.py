import socket

HOST = "localhost"
PORT = 12345

# simple application that sends stdin through a socket
if __name__ == '__main__':
    with socket.socket() as s:
        s.bind((HOST, PORT))
        print("Socket successfully created. Start Spark!")
        s.listen(5)
        sock, _ = s.accept()
        print("Accepted, sending...")
        while True:
            print(sock.send(input().encode()))
