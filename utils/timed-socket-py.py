import socket
from time import sleep
import random

HOST = "localhost"
PORT = 9998


# a small application that programmatically sends data over a socket
# (for Spark Streaming)
def example1(sock):
    sock.send("7,blue\n".encode())
    # TODO examples in the training


# for the numbers aggregation exercise if netcat is unavailable/clunky to use
def send_numbers(sock):
    while True:
        sleep(random.random())
        sock.send(random.randint(0, 100))


if __name__ == '__main__':
    with socket.socket() as s:
        s.bind((HOST, PORT))
        print("Socket successfully created. Start Spark!")
        s.listen(5)
        sock, _ = s.accept()
        print("Accepted, sending...")
        example1(sock)
        print("Done!")
