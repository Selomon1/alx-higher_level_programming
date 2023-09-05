#!/usr/bin/python3
""" Format and  print text module """


def text_indentation(text):
    """
    function that prints text
    Args:
        text: text written
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    new_line = True

    for s in text:
        if new_line and s == ' ':
            continue
        new_line = False

        print(s, end='')
        if s in ".?:":
            print("\n")
            new_line = True
