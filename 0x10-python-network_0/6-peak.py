#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    function that finds the peak elements
    """

    if not list_of_integers or list_of_integers == []:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid_point = (left + right) // 2

        # checking if the middle element is the peak
        if list_of_integers[mid_point] > list_of_integers[mid_point + 1] and \
           list_of_integers[mid_point] > list_of_integers[mid_point - 1]:
               return list_of_integers[mid_point]
        # move right if right side is greater
        elif list_of_integers[mid_point] < list_of_integers[mid_point + 1]:
            left = mid_point + 1
        # move left if the left side is greater
        else:
            right = mid_point - 1
    # handle the case whether left or right attoned
    return list_of_integers[left]
