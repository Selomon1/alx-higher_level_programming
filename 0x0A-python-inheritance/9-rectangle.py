#!/usr/bin/python3
""" Rectangle that inherits from BaseGeometry """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class of Rectangle that inherit from BaseGeometry """

    def __init__(self, width, height):
        """Initialize the rectangle height and width """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Represent the set of the string of the rectangle """
        return ("[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                          self.__width, self.__height))
