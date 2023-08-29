#!/usr/bin/python3
'''A class that define a square'''


class Square():
    '''square class type'''

    def __init__(self, size=0):
        '''Initialize the argument (square)'''
        self.size = size

    @property
    def size(self):
        '''retrieve the size of square'''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''update the size of the currrent square'''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        '''retrieve the position of the square'''
        return (self.__position)

    @position.setter
    def position(self, value):
        '''update the position of the square'''
        if type(value) != tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not all(isinstance(x, int) for x in value) or not all(x >= 0 for x in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        '''calculate and return the current size of the square'''
        return (self.__size ** 2)

    def my_print(self):
        '''prints in stdout the square with character #'''
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
