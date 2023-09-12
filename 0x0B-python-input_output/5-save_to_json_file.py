#!/usr/bin/python3
"""
write object to text using JSON
"""


import json


def save_to_json_file(my_obj, filename):
    """ Function  that writes an object to text file using JSON repre
    Args:
        my_obj: object to be written to text
        filename: the nam of the file
    """
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
