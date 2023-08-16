#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    return ((x, y) for x in set_1 for y in set_2 if x != y)
