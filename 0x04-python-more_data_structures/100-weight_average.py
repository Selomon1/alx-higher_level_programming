#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    po = 0
    nat = 0
    for k, weight in my_list:
        po += k * weight
        nat += weight
    return po / nat
