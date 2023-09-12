#!/usr/bin/python3
""" write string to text file """


def write_file(filename="", text=""):
    """ write string to textfile
    Args:
        filename: the string file name
        text: written text 
    Return:
        the number of characters written
    """
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
