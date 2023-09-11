#!/usr/bin/python3
"""
Square inhebits from rectangle as subclass
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """indicates square """

    def __init__(self, size):
        """ Initialize the square """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
