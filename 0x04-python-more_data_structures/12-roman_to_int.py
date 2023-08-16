#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) is not str and roman_string is None:
        return 0

    nu = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    sum = 0
    pre = 0

    for i in range(len(roman_string) -1, -1, -1):
        value = nu[roman_string[i]]
        if value >= pre:
            sum += value
        else:
            sum -= value
        pre = value
    return sum
