#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    rel_no = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            rel_no = rel_no + i
        except IndexError:
            break
    print("")
    return rel_no
