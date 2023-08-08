#!/usr/bin/python3
def uppercase(str):
    for c in str:
        lett = ord(str[c])
        if lett >= 97 and lett <= 122:
            lett = lett - 32
        print('{:c}'.format(lett), end='')
