from random import *
import string
from time import sleep
import os
import errno


# simple program to write to files randomly to be picked up by Spark Streaming
def write_to_file(path, n_lines, max_length):
    with open(path, "w") as file:
        for i in range(n_lines):
            rand_string = "".join(choice(string.ascii_letters) for _ in range(randint(1, max_length)))
            file.write(rand_string)
            file.write("\n")
            sleep(random() / 3)


def write_random_files(dir_path, n_files, n_lines, max_length):
    if not os.path.exists(dir_path):
        try:
            os.makedirs(dir_path)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

    for i in range(n_files):
        write_to_file(dir_path + "/file_" + str(i) + ".txt", n_lines, max_length)
        sleep(random())


if __name__ == '__main__':
    write_random_files("../dumped-data/watched-files", 5, 2, 20)
