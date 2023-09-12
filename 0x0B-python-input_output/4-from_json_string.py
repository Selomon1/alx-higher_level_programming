#!/usr/bin/python3
"""
an object represented by a JSON
"""


import json


def from_json_string(my_str):
    """ Function that return an object represented by JSON
    Args:
        my_str: the string of an object
    Return:
        an object represented by JSON
    """
    return json.loads(my_str)
