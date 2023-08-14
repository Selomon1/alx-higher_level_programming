#!/usr/bin/python3
def replace_in_list(my_list, idx, elements):
    n_list = len(my_list)
    if idx < 0:
        return my_list
    elif idx >= n_list:
        return my_list
    elif my_list[idx] == elements:
        return my_list
