#!/usr/bin/python3
'''A  class thta define a square'''


class Square():
    '''square class type'''

    def __init__(self, size=0):
        '''Initialize the argument (square)'''
        self.size = size

    @property
    def size(self):
        '''retrive the curerent size of the square'''
        self.__size = size

    @size.setter
    def size(self, value):
        '''update the size of the square'''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        '''calculate and return the current size of the square'''
        return (self.__size ** 2)

    def my_print(self):
        '''print in stdout the square with the character #'''
        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end='')
            print()
