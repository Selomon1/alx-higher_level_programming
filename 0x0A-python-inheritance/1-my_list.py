#!/usr/bin/python3
"""
Class MyList that inherits from list 
"""


class MyList(list):
    """Function class MyList that inherits from list """
    def print_sorted(self):
        """ print list in ascending order """
        sorted_list = sorted(self)
        print(sorted_list)
