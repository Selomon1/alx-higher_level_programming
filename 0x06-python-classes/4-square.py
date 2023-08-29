#!/usr/bin/python3
'''A class that define a square'''


class Square():
    '''square class type'''

    def __init__(self, size=0):
        '''Initialize the argument (square)
        Args:
            size (int): size of the argument
        '''
        self.size = size

    @property
    def size(self):
        '''retrieve the size of the square'''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''updat the size of the square'''

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        '''calculate and return the current area of the square'''
        return (self.__size ** 2)
