#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in len(matrix):
        for j in len(matrix[i]):
            new_matrix.append(matrix[i][j] * matrix[i][j])

    return new_matrix
