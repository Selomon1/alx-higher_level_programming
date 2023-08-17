#!/usr/bin/python3
def search_replace(my_list,search, replace):
    new_lists = my_list[:]
    for i in range(len(new_lists)):
        if new_lists[i] == search:
            return new_list.replace(i)
