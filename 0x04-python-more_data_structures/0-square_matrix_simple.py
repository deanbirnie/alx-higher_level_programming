#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = []
    i = 0
    for x in matrix:
        square.append([])
        for y in matrix[i]:
            square[i].append(y**2)
        i += 1
    return (square)
