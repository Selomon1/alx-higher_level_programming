#!/usr/bin/python3
def roman_to_int(roman_string):
    nu = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    sum = 0
    pre = 0
    if type(roman_string) is str and roman_string:
        for i in range(len(roman_string) -1, -1, -1):
            value = nu[roman_string[i]]
            if value >= pre:
                sum += value
            else:
                sum -= value
            pre = value
    return sum
