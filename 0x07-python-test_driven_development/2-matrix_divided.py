#!/usr/bin/python3
""" matrix deviding """


def matrix_divided(matrix, div):
    """ divides all elements of the matrix

    Args:
        matrix: matrix containing the elements
        div: divisor

    Returns:
        new matrix containing the results
    """
    new_matrix = []
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats)")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        new_row = []
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats)")
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats)")
            res = round(i / div, 2)
            new_row.append(res)
        new_matrix.append(new_row)
    return new_matrix
