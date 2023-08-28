#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        resu = fct(*args)
    except Exception as err:
        print('Exception: {}'.format(err), file=sys.stderr)
        return None
    return resu
