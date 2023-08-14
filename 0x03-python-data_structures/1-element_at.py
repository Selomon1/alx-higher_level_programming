#!/usr/bin/python3
def element_at(my_list, idx):
    n_list = len(my_list)
    if idx < 0:
        return None
    elif idx >= n_list:
        return None
    else:
        return my_list[idx]
