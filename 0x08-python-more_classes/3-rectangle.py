#!/usr/bin/python3
""" Define a rectangle """


class Rectangle():
    """ Rectangle class """
    def __init__(self, width=0, height=0):
        """ initialize the width and height of the rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        self.__height = value

    def area(self):
        """ calculate and return the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ calculate and return the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """ returns the set of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return ""
        rec = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rec = rec + "#"
            rec = rec + "\n"
        return rec[:-1]
