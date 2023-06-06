#!/usr/bin/python3

"""A module for matrix division operation."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a given divisor.

    Args:
    matrix (list): A matrix (list of lists) of integers/floats.
    div (int or float): The divisor.

    Raises:
    TypeError: If the matrix is not a matrix (list of lists) of
    integers/floats,
    each row of the matrix doesn't have the same size, or the divisor is not a
    number.
    ZeroDivisionError: If the divisor is zero.

    Returns:
    list: A new matrix with the divided values, rounded to two decimal
    places.
    """
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(ele, int) or isinstance(ele, float))
                for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
