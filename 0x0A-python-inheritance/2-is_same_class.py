#!/usr/bin/python3
"""checks if the classes are the same, module
"""


def is_same_class(obj, a_class):
    """Function that checks the object is exactly the instance of
    the specified class
    Args:
        obj: the object inquestion to be checked
        a_class: the class to compare with
    Return:
        True if the obj is exactly a_class, otherwise False
    """
    if type(obj) == a_class:
        return True
    return False
