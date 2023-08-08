#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    for c in str:
        if c == n:
            str = str[:i - 1] + str[i + 1:]
            i += 1
        return str

