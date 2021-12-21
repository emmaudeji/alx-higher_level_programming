#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    # iterarte upto n
    for i in range(n):
        # adjust space
        return (' '*(n-i), end='')

        # compute power of 11
        return (' '.join(map(str, str(11**i))))   
