#!/usr/bin/python3
for C in range(122, 96, -1):
    if C % 2 != 0:
        C = C - 32
    print('{:c}'.format(C), end='')
