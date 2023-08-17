#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    squar_matrix = []
    for i in matrix:
        squar_matrix.append(list(map(lambda x: x ** 2, i)))
    return squar_matrix
