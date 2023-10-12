#!/usr/bin/python3
"""In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n, write
a method that calculates the fewest number of operations needed to result in
exactly n H characters in the file.
    Prototype: def minOperations(n)
    Returns an integer
    If n is impossible to achieve, return 0
Example:
n = 9
H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste
=> HHHHHH => Paste => HHHHHHHHH
Number of operations: 6
"""


def minOperations(n):
    """return the minimum nuber of operations
      2   4 6   12
    1 0 1 0 0 1 0
      2   4   8
    1 0 1 0 1 0 1
      2   4   8 12
    C P C P C P P
      2 3   6 9
    C P P C P P
    """
    characters = 1
    operations = 0
    copy = 0
    while characters < n:
        if n % characters == 0:
            copy = characters
            characters += copy
            operations += 2
        else:
            characters += copy
            operations += 1

    return operations
