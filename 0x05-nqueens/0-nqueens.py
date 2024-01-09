#!/usr/bin/python3
"""The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard."""

import sys


if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)

number = sys.argv[1]

if type(number) != int:
    print('N must be a number')
    exit(1)

if number < 4:
    print('N must be at least 4')
    exit(1)


