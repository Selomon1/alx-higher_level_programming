#!/usr/bin/python3
""" Define a rectangle """


class Rectangle():
    """ Rectangle class """
    def __init__(self, width=0, height=0):
        """ Initialize width and height of rectangle """
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
            raise ValueError("height must be an integer")
        elif value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        """ calulate and return the the area of the rectangle """
        return (self.__width * self.__height)
    def perimeter(self):
        """ calculate and return the preimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2
