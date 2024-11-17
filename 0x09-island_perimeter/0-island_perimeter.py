#!/usr/bin/python3
'''an algorithm to calculate the parimeter of an island'''


def island_perimeter(grid):
    '''a function that calculates the parimeter of a island
    args: grid: a 2d array'''
    rows = len(grid)
    parimeter = 0
    for i in range(rows):
        cols = len(grid[i])
        for j in range(cols):
            if grid[i][j]:
                parimeter += 4
                try:
                    if grid[i + 1][j]:
                        parimeter -= 2
                except IndexError:
                    pass
                try:
                    if grid[i][j + 1]:
                        parimeter -= 2
                except IndexError:
                    pass
    return parimeter
