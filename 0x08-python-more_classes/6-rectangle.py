#!/usr/bin/python3
""" Define rectangle """


class Rectangle():
    """ Rectangle class """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Initialize the width and height of the rectangle """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter to value """
        if not isinstance(value, int):
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
        """ height setter to value """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ calculateand return the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ calculate and return the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """ string set of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return ""
        rec = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rec = rec + "#"
            rec = rec + "\n"
        return rec[:-1]

    def __repr__(self):
        """ string representing the rectangle """
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """ delete the instance of the rectangle """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
