#!/usr/bin/python3
""" Square that inherits from Rectangle """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square that inherit from Rectangle class as sub """

    def __init__(self, size):
        """Initialize the Square """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """represent the set of string in the rectangle"""
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                        self.__size, self.__size)
