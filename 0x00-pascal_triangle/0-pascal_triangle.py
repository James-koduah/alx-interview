#!/usr/bin/python3
"""An implementation of the pascal Triangle"""
from math import factorial


def pascal_triangle(n):
    """An implementation of the pascal Triangle"""
    final = []
    for i in range(1, n+1):
        final.append([])
        C = 1
        for j in range(1, i+1):
            final[i-1].append(C)
            C = C * (i-j) // j
    return final
