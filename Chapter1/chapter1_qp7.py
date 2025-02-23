import unittest

from copy import deepcopy


def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(len(matrix) // 2):
        first, last = layer, len(matrix) - 1 - layer

        for i in range(first, last):
            temp = matrix[layer][i]

            matrix[layer][i] = matrix[n - 1- i][layer]

            matrix[n - 1 - i][layer] = matrix[n - 1 - layer] [n- 1 - i]

            matrix[n - 1 - layer] [n- 1 - i] = matrix[i][n- 1 - layer]

            matrix[i][n - 1 - layer] = temp
    return matrix


class Test(unittest.TestCase):

    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ],
        ),
    ]
    testable_functions = [
        rotate_matrix
    ]

    def test_rotate_matrix(self):
        for f in self.testable_functions:
            for [test_matrix, expected] in self.test_cases:
                test_matrix = deepcopy(test_matrix)
                assert f(test_matrix) == expected


if __name__ == "__main__":
    unittest.main()