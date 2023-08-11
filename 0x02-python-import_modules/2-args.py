#!/usr/bin/python3
if  __name__ == '__main__':
    import sys
    argc = len(sys.argv)
    if argc == 1:
        print('0 arguments.')
    elif argc - 1 == 1:
        print('1 argument:')
    else:
        print('{} {:s}:'.format(argc - 1, 'arguments'))
    for n in range(1, argc):
        print('{}: {:s}'.format(n, sys.argv[n]))
