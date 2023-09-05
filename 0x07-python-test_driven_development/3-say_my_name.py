#!/usr/bin/python3
""" prints first name and last name module """


def say_my_name(first_name, last_name=""):
    """ Function that print first and last name
    Args:
        first_name: first name parameter
        last_name: last name parameter of a person
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
