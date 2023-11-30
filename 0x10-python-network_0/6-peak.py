#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    if not list_of_integers or list_of_integers == []:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid_point = (left + right) // 2

        if list_of_integers[mid_point] > list_of_integers[mid_point + 1] and \
           list_of_integers[mid_point] > list_of_integers[mid_point - 1]:
               return list_of_integers[mid_point]
        elif list_of_integers[mid_point] < list_of_integers[mid_point + 1]:
            left = mid_point + 1
        else:
            right = mid_point - 1

    return list_of_integers[left]
