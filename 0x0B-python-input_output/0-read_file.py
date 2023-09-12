#!/usr/bin/python3
"""Read a text file and print it to stdout """


def read_file(filename=""):
    """ Function that read textfile and print it to stdout """
    with open(filename, "r", encoding="UTF-8") as f:
        for line in f:
            print(line, end="")
