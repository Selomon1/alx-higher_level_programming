#!/usr/bin/python3
"""
Defines student class
"""


class Student():
    """ a class Stdent that defines student class
    Args:
        first_name: first name of student
        last_name: last name of student
        age: the age of the student
    """
    def __init__(self, first_name, last_name, age):
        """ Initialize student name and age """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ get representation of student from dictionary """
        return self.__dict__
