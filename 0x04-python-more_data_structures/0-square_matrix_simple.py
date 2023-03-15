#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        matrix = []
    new_matrix = matrix.copy()
    for i in range(len(matrix)):
        new_matrix[i] = list(map(lambda x: x**2, new_matrix[i]))
    return new_matrix
