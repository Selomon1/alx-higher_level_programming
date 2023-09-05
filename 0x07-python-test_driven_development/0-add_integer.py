#!/usr/bin/python3
"""
add_integer method module
example add_integer(1, 2)
3
"""


def add_integer(a, b=98):
    """ return the addition of the integer 
    Args:
        a: the first int/float para
        b: the second int/float para, default 98
    raise:
        TypeError if a or b is not int or float
    Return: the sum of a and b in
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
