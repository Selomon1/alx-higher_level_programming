#!/usr/bin/python3
"""
divide every part of matrix by divider
"""


def matrix_divided(matrix, div):
    """
    Function that return division of every elemnts of matrix by div
    Args:
        matrix: the atrix parameter
        div: divider (number)
    """

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    curr = []

    for i in range(len(matrix)):
        if len(matrix[0]) != len(matrix[i]):
            raise TypeError(
                    'Each row of the matrix must have the same size')

        now = []

        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError('matrix must be matrix of number')

            now.append(round(matrix[i][j] / div, 2))

        curr.append(now)

    return curr
