#!/usr/bin/python3
"""The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard."""

import sys


if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)


number = sys.argv[1]

if type(number) is int:
    print('N must be a number')
    exit(1)

number = int(number)

if number < 4:
    print('N must be at least 4')
    exit(1)



def nqueens(n, y, board):
    """
    Method: nqueens - place n queens
            on an n by n board so that
            no queens are attacking any
            others.
    Parameters: n is an int that sets
                board size and # of queens
    Return: All possible solutions to
            placement, in list of lists form
    """
    for x in range(n):
        h = 0
        for q in board:
            if x == q[1]:
                h = 1
                break
            if y - x == q[0] - q[1]:
                h = 1
                break
            if x - q[1] == q[0] - y:
                h = 1
                break
        if h == 0:
            board.append([y, x])
            if y != n - 1:
                nqueens(n, y + 1, board)
            else:
                print(board)
            del board[-1]

if __name__ == '__main__':
    nqueens(number, 0, [])
