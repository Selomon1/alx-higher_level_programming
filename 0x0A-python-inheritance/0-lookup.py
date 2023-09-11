#!/usr/bin/python3
"""
Function of look up that return the lists
"""


def lookup(obj):
    """Function that return the list of attributes and method of obj
    Args:
        obj: the object to be returned
    Return:
        the list of objects
    """
    return dir(obj)
