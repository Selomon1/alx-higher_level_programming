#!/usr/bin/python3
""" rectangle class module """
from .base import Base


class Rectangle(Base):
    """ Rectangle class inherited from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ intialization of height, width, y, x, id """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ get width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter of width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ sets height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """ x coordinates """
        return self.__x

    @x.setter
    def x(self, value):
        """ sets x coordinates """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Y coordinates """
        return self.__y

    @y.setter
    def y(self, value):
        """ set y coordinates """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ print in stdout """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """ height, width, x, y and id of the rec """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """ dictionary representation of the rec """
        args_l = ["id", "width", "height", "x", "y"]
        args_len = len(args_l)
        if len(args) > 0:
            for i, argv in enumerate(args):
                if i < args_len:
                    self.__setattr__(args_l[i], argv)
        else:
            for e, f in kwargs.items():
                self.__setattr__(e, f)

    def to_dictionary(self):
        """ dictionary representation of a rectangle """
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
