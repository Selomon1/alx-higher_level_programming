#!/usr/bin/python3
"""
Define a student class
"""


class Student():
    """ a class of student that defines student
    Args:
        first_name: first name of the student
        last_name: last name of the student
        age: age of the student
    """
    def __init__(self, first_name, last_name, age):
        """ initialize the name and age """
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

    def reload_from_json(self, json):
        """ replace all attributes of the student """
        for k, v in json.items():
            setattr(self, k, v)
