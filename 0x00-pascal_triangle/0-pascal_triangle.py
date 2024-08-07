#!/usr/bin/python3

""" Pascal's Triangle. """


def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of n levels.

    Args:
        n (int): Number of levels of the triangle.

    Returns:
        List[List[int]]: Pascal's triangle of n levels.
    """
    if n <= 0:
        return []

    triangle = []

    for a in range(n):
        # Start with a row filled with 1s
        row = [1] * (a + 1)

        # Calculate the values for the interior of the row
        for b in range(1, a):
            row[b] = triangle[a - 1][b - 1] + triangle[a - 1][b]

        triangle.append(row)

    return triangle
