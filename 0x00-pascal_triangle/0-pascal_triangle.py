#!/usr/bin/env python3
'''this module contains a function(pascal_triangle)
that returns a paschals triangle'''


def pascal_triangle(n):
    '''this function returns the pascals triangle
    args:  n the number of rows of the triangle
    if n <= 0 return an empty list'''

    if n <= 0:
        return []
    expansion = [[1]]
    for i in range(1, n):
        prev_row = expansion[i - 1].copy()
        prev_row.insert(0, 0)
        prev_row.append(0)
        row = [prev_row[j] + prev_row[j + 1] for j in range(len(prev_row) - 1)]
        expansion.append(row)

    return expansion
