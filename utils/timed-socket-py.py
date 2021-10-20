import socket

HOST = "localhost"
PORT = 9998


# a small application that programmatically sends data over a socket
# (for Spark Streaming)
def example1(sock):
    sock.send("7,blue\n".encode())
    # TODO examples in the training


if __name__ == '__main__':
    with socket.socket() as s:
        s.bind((HOST, PORT))
        print("Socket successfully created. Start Spark!")
        s.listen(5)
        sock, _ = s.accept()
        print("Accepted, sending...")
        example1(sock)
        print("Done!")
