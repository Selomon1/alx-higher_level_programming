#!/usr/bin/python3
'''A class that define a square'''


class Square():
    '''square class'''

    def __init__(self, size=0):
        '''Initialize the argument (square)
        Args:
            size (int): the size of argument
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        '''calculate and return the current area of the square'''
        return (self.__size ** 2)
