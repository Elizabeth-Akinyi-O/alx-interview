#!/usr/bin/python3

"""calculates the fewest number of operations needed to result
    in exactly n H characters in the file
"""


def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        # Check if factor divides n
        while n % factor == 0:
            operations += factor  # Add the factor to the operation count
            n //= factor  # Divide n by the factor
        factor += 1  # Increment the factor to check the next possible factor

    return operations
