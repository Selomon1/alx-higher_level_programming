#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return None
    nu = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    pre = 0
    for i in range(len(roman_string) - 1, -1, -1):
        if nu[roman_string[i]] >= pre:
            sum += nu[roman_string[i]]
        else:
            sum -= nu[roman_string[i]]
        pre = nu[roman_string[i]]
    return sum
