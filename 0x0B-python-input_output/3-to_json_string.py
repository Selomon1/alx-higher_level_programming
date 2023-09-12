#!/usr/bin/python3
""" JSON representation """


import json


def to_json_string(my_obj):
    """ Function that represent JSON of an object
    Args:
        my_obj: the object
    Return:
        Json representation of an object
    """
    return json.dumps(my_obj)
