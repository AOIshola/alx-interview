#!/usr/bin/python3
"""Implements the Pascal's triangle"""

def pascal_triangle(n):
    """creates a pascal triangle of size n"""
    tri = [[1]]
    if n <= 0:
        return ([])
    elif n == 1:
        return (tri)
    else:
        for i in range(1, n):
            res = [1]
            last = tri[-1]
            for j in range(0, i):
                if j == i - 1:
                    res.append(1)
                    tri.append(res)
                else:
                    add = last[j] + last[j + 1]
                    res.append(add)
    return (tri)
