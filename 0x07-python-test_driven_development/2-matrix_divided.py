#!/usr/bin/python3
"""Creating a function that divides elements of a matrix"""


def matrix_divided(matrix, div):
    """Takes a matrix and div as arguments
    
    Divides elements of a matrix

    Args:
        Matrix
        Div
    Returns:
        new matrix of divided elements
    """
    rws = len(matrix)
    clmns = len(matrix[0])

    for elements in matrix:
        if not isinstance(elements, int) and not isinstance(elements, float):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in rws:
        if i < rws - 1 and matrix[i] != matrix[i + 1]:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    for i in rws:
        for j in clmns:
            result = [[round(matrix[i][j] / div, 2) for j in clmns] for i in rws]

    return result
