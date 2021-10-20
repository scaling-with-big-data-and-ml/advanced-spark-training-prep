import socket
import time
import random

HOST = "localhost"
PORT = 9999


# simple program to read a file and send its contents through a socket
# (for Spark Streaming)
def send_simple_string(sock):
    sock.send("Writing from a socket app!".encode())


def read_file_random_speed(filename, sock):
    with open(filename) as f:
        for line in f.readlines():
            time.sleep(random.random())
            print(line)
            sock.send(line.encode())


if __name__ == "__main__":
    with socket.socket() as s:
        s.bind((HOST, PORT))
        print("Socket successfully created. Start Spark!")
        s.listen(5)
        c, _ = s.accept()
        print("Accepted, sending...")
        read_file_random_speed("../data/people-1m/people-1m.txt", c)

