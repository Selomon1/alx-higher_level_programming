#!/usr/bin/python3
""" print square with character """


def print_square(size):
    """ Function that print square with character
    args:
        size: thenumber of the character and their size
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
