#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newma = []
    for nu in matrix:
        newma.append(list(map(lambda x: pow(x, 2), nu)))
    return newma
