#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    Ele_a = list(tuple_a)
    Ele_b = list(tuple_b)
    if len(Ele_a) <  2:
        for i in range(len(Ele_a), 2):
            Ele_a.append(0)
    if len(Ele_b) < 2:
        for i in range(len(Ele_b), 2):
            Ele_b.append(0)
    add_tuple = (Ele_a[0] + Ele_b[0] + Ele_a[1] + Ele_b[1])
    return tuple(add_tuple)
