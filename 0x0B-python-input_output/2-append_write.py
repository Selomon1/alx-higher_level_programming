#!/usr/bin/python3
"""
append a string
"""


def append_write(filename="", text=""):
    """ Function that append a string at the end of text file
    Args:
        filename: the name of the file
        text: the appended text to the file
    Return:
        the number of characters added
    """
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
