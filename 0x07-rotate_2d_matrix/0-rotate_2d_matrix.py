#!/usr/bin/python3
"""Given an n x n 2D matrix, rotate it 90 degrees clockwise."""


def rotate_2d_matrix(matrix):
    """rotate the original matrix 90 degrees"""
    width = len(matrix[0])
    length = len(matrix)

    rotated = []

    """make a rotated version of matrix"""
    for i in range(0, width):
        group = []
        for j in range(length - 1, -1, -1):
            group.append(matrix[j][i])
        rotated.append(group)

    """make changes to the original list"""
    for i in range(0, length):
        for j in range(0, width):
            matrix[i][j] = rotated[i][j]
