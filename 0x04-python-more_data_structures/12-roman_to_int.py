#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return None
    nu = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    sum = 0
    pre = 0
    for i in range(len(roman_string) - 1, -1, -1):
        if nu[roman_string[i]] >= pre:
            sum += nu[roman_string[i]]
        else:
            sum -= nu[roman_string[i]]
        pre = nu[roman_string[i]]
    return sum
