#!/usr/bin/python3
'''A class that define a square'''


class Square():
    '''square class type'''

    def __init__(self, size=0):
        '''initialize the argument (square)
        Args:
            size (int): size of the argument
        '''

        if not instance(size, int):
            raise TypeError('size must be an integer')
        elif  size < 0:
            raise ValueError('size must be >=0')
