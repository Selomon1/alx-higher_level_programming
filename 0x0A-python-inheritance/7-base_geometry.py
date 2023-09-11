#!/usr/bin/python3
"""Class BaseGeometry """


class BaseGeometry():
    """class BaseGeometry """
    def area(self):
        """ area that raise exception with message """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ value validator """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
