#!/usr/bin/python3
"""a function to divide all elements of a matrix by a value"""


def matrix_divided(matrix, div):
    """Returns the matrix of the division"""
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    size = None
    for m in matrix:
        if type(m) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(m)
        elif size != len(m):
            raise TypeError("Each row of the matrix must have the same size")
        for i in m:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in m] for m in matrix]
