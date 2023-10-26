#!/usr/bin/python3
"""Determine if a set of integers is valid UTF-8 encoding"""


def validUTF8(data):
    """Check if the integers constitue a valid utf-8 encoding"""
    successive_10 = 0
    for b in data:
        b = bin(b).replace('0b', '').rjust(8, '0')
        if successive_10 != 0:
            successive_10 -= 1
            if not b.startswith('10'):
                return False
        elif b[0] == '1':
            successive_10 = len(b.split('0')[0]) - 1
    return True
