#!/usr/bin/python3
def new_in_list(my_list, idx, elements):
    n_list = len(my_list)
    new_list = my_list.copy()
    if idx < 0:
        return my_list
    elif idx >= n_list:
        return my_list
    else:
        new_list[idx] = elements
        return new_list
