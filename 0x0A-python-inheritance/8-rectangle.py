#!/usr/bin/python3
"""
Rectangle that inhertits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class rectangle that inherits from the BaseGeometry """

    def __init__(self, width, height):
        """ Initialize the rectangle """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
