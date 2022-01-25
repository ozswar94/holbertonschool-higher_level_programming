#!/usr/bin/python3
def matrix_divided(matrix, div):
    """ return a + b

    Args:
        matrix (list): list of list
        div (int): integer > 0

    Raises:
        TypeError: matrix
        ZeroDivisionError: div
    """
    error_msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    error_msg2 = "Each row of the matrix must have the same size"
    error_msg3 = "div must be a number"
    error_msg4 = "division by zero"

    row_len = 0

    if not isinstance(matrix, list):
        raise TypeError(error_msg1)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(error_msg1)
        for i in row:
            if not isinstance(i, float) and not isinstance(i, int):
                raise TypeError(error_msg1)
            if len(row) is not row_len and row_len != 0:
                raise TypeError(error_msg2)
            row_len = len(row)

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError(error_msg3)
    if div == 0:
        raise ZeroDivisionError(error_msg4)

    return [[round(n / div, 2) for n in row] for row in matrix]
