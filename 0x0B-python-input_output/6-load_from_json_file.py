#!/usr/bin/python3
""" Creating an object """


import json


def load_from_json_file(filename):
    """ Function that create an object from JSON file
    Args:
        filename: the name of the JSON file
    """
    with open(filename, "r") as f:
        return json.load(f)
