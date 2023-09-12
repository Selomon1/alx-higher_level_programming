#!/usr/bin/python3
"""
Defines a student class
"""


class Student():
    """ a class students that defines a student
    Args:
        first_name: first name of the student
        last_name: last name of the student
        age: the age of the student
    """
    def __init__(self, first_name, last_name, age):
        """ Initialize name and age of the student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ get representation of student from dictionary """
        if attrs is None:
            return self.__dict__
        cur_dict = {}

        for i in attrs:
            try:
                cur_dict[i] = self.__dict__[i]
            except Exception:
                pass
        return cur_dict
