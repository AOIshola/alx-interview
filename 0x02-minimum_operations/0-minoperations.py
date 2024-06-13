#!/usr/bin/python3
"""calculates the fewest number of operations needed
to result in exactly n H characters in a file"""


def minOperations(n):
    """finds the minimum operations using factorization approach"""
    if n <= 1:
        return 0

    factor = 2
    num_of_operations = 0

    while n > 1:
        while n % factor == 0:
            num_of_operations += factor
            n = n // factor
        factor += 1

    return num_of_operations
