# O(MxN)
import unittest
from copy import deepcopy


def zero_matrix(matrix):
    row = set()
    column = set()


    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                row.add(i)
                column.add(j)

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i in row or j in column:
                matrix[i][j] = 0
    return matrix


def check_if_matrix_rows_and_columns_are_not_zero(matrix, i, j):
    if matrix[i][j] != 0:
        return False

    if matrix[0][j] != 0:
        return False

    if matrix[-1][j] != 0:
        return False

    if matrix[-1][j] != 0:
        return False

    if matrix[i][0] != 0:
        return False

    if matrix[i][-1] != 0:
        return False

    return True


def zero_matrix_with_constant_space(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                if not check_if_matrix_rows_and_columns_are_not_zero(matrix, i, j):
                    set_row_col_zero(matrix, i, j)
    return matrix




def set_row_col_zero(matrix, i, j):
    for k in range(len(matrix[i])):
        matrix[i][k] = 0

    for k in range(len(matrix)):
        matrix[k][j] = 0

    return matrix


class Test(unittest.TestCase):

    test_cases = [
        (
            [
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [11, 0, 13, 14, 0],
                [0, 0, 0, 0, 0],
                [21, 0, 23, 24, 0],
            ],
        )
    ]
    testable_functions = [zero_matrix, zero_matrix_with_constant_space]

    def test_zero_matrix(self):
        for f in self.testable_functions:
            for [test_matrix, expected] in self.test_cases:
                test_matrix = deepcopy(test_matrix)
                assert f(test_matrix) == expected


if __name__ == "__main__":
    unittest.main()