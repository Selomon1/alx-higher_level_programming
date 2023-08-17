#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    m = []
    m.append(list(map(lambda i: list(map(lambda x: pow(x, 2), i)), matrix)))
    return m
