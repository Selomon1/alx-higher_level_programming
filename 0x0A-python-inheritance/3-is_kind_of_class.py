#!/usr/bin/python3
"""
Compare if classes are the same or not, module
"""


def is_kind_of_class(obj, a_class):
    """Function that check object class
    Args:
        obj: object in question to be checked
        a_class: class to compare with
    Return:
        True if obj is instance of a_class specified or inherited, else False
    """
    return isinstance(obj, a_class)
