#!/usr/bin/python3
def uppercase(str):
    for u in range(len(str)):
        lett = ord(str[u])
        if lett >= 97 and lett <= 122:
            lett = lett - 32
        print('{:c}'.format(lett), end='')
    print()
