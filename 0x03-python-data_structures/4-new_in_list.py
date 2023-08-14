#!/usr/bin/python3
def new_in_list(my_list, idx, elements):
    n_list = len(my_list)
    new_list = my_list.copy()
    if idx < 0:
        return new_list
    elif idx >= n_list:
        return new_list
    else:
        my_list[idx] = new_elements
        return new_list
