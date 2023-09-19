#!/usr/bin/python3
""" Square class module """
from .rectangle import Rectangle


class Square(Rectangle):
    """ class of square """
    def __init__(self, size, x=0, y=0, id=None):
        """ initialize size, x, y and id """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ string representation of square """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y
                                                  self.width)

    @property
    def size(self):
        """ getting the size """
        return self.width

    @size.setter
    def size(self, value):
        """ set the size value """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update the square """
        args_li = ["id", "size", "x", "y"]
        args_len = len(args)

        if len(args) > 0:
            for i, argv in enumerate(args):
                if i < args_len:
                    self.setattr__(args_li[i], argv)
        else:
            for e, f in kwargs.items():
                self.__setattr__(e, f)

    def to_dictionary(self):
        """ DICTIONARY REPRESENTATION OF THE SQUARE """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
