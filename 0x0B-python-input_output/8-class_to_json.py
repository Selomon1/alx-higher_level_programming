#!/usr/bin/python3
"""
Dictionary description with simple data structure
"""


def class_to_json(obj):
    """ Function that return dictionary description with simple data Stru """
    return obj.__dict__
