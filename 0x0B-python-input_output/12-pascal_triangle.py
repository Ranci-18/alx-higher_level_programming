#!/usr/bin/python3
"""defining a function"""


def pascal_triangle(n):
    """function that returns a list of integers
    representing the Pascal's triangle as a matrix"""
    if n <= 0:
        pascal_triangle = []
        return pascal_triangle

    if n == 1:
        pascal_triangle = [[1]]
        return pascal_triangle

    if n == 2:
        pascal_triangle = [[1], [1, 1]]
        return pascal_triangle

    pascal_triangle = [[1], [1, 1]]
    for i in range(2, n):
        pascal_triangle.append([1])
        for j in range(1, i):
            rslt = pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j]
            pascal_triangle[i].append(rslt)
        pascal_triangle[i].append(1)
    return pascal_triangle
