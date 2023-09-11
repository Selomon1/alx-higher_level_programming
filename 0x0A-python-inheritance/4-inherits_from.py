#!/usr/bin/python3
"""
Compares class 
"""


def inherits_from(obj, a_class):
    """Function that cecks obj is instance of specified class
    directly or indirectly
    Args:
        obj: the object in question
        a_class: class to compare with
    Return:
        True if obj is instance of specified class inheried, else False
    """
    if  issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
