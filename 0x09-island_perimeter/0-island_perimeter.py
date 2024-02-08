#!/usr/bin/python3
"""
   Create a function def island_perimeter(grid): that returns
   the perimeter of the island described in grid:

    grid is a list of list of integers:
        0 represents water
        1 represents land
        Each cell is square, with a side length of 1
        Cells are connected horizontally/vertically (not diagonally).
        grid is rectangular, with its width and height not exceeding 100
    The grid is completely surrounded by water
    There is only one island (or nothing).
    The island doesn’t have “lakes” (water inside that isn’t connected to
    the water surrounding the island).
"""
def island_perimeter(grid):
    """function implementation for module"""
    grid_length = len(grid)
    grid_width = len(grid[0])

    perimeter = 0

    for i in range(0, grid_length):
        for j in range(0, grid_width):
            cell = grid[i][j]
            if cell == 1:
                # check the left
                if j == 0: # if we are at the far left
                    perimeter += 1
                elif grid[i][j - 1] == 0:
                    perimeter += 1

                # check the top
                if i == 0: # if we are at the far top
                    perimeter += 1
                elif grid[i - 1][j] == 0:
                    perimeter += 1

                # check the right
                if j == grid_width - 1: # if we are at the far right
                    perimeter += 1
                elif grid[i][j + 1] == 0:
                    perimeter += 1

                # check the bottom
                if i == grid_length - 1: # if we are at the far bottom
                    perimeter += 1
                elif grid[i + 1][j] == 0:
                    perimeter += 1
    return perimeter
