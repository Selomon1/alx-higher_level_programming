#!/usr/bin/python3
"""
pascal's triangle printning up to n
"""


def pascal_triangle(n):
    """ returns a list of list of integers representing
    the Pascal's triangle of n
    """
    if n <= 0:
        return []

    triangles = [[1]]
    for i in range(1, n):
        l_rows = [1]
        for j in range(1, i):
            l_rows.append(triangles[i-1][j-1] + triangles[i-1][j])
        l_rows.append(1)
        triangles.append(l_rows)
    return triangles
