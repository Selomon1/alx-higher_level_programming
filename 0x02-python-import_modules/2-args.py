#!/usr/bin/python3
if  __name__ == '__main__':
    import sys
    argc = len(sys.argv)
    if argc == 1:
        print('0 arguments.')
    else:
        print('{:d} argument'.format(argc - 1, end=''))
        if argc > argc + 1:
            print('s', end='')
        for n in range(1, argc):
            print('{:d}: {:s}'.format(n, sys.argv[n]))

