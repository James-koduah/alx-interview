#!/usr/bin/python3
"""An implementation of the pascal Triangle"""
from math import factorial


def pascal_triangle(n):
    """An implementation of the pascal Triangle"""
    final = []
    if n <= 0:
        return final

    for i in range(n):
        final.append([])
        for j in range(i+1):
            final[i].append(factorial(i)//(factorial(j)*factorial(i-j)))

    return final



