#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    po = 0
    for k, weight in my_list:
        po += k * weight
        average = po / sum(weight)
    return average
