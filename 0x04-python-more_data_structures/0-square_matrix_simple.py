#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    New_matrix = []
    for row in matrix:
        New_matrix.append([elem**2 for elem in row])
    return New_matrix
