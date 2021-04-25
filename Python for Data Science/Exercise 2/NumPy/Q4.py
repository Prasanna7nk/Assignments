"""
Write a NumPy program to compute the determinant of
a given square array
"""
import numpy as np

sq_arr = np.array(
    [
        [
            [1, 2, 3],
            [2, 3, 4],
            [5, 6, 7]
        ],
        [
            [1, 2, 3],
            [4, 5, 6],
            [8, 4, 0]
        ],
        [
            [8, 9, 1],
            [5, 6, 3],
            [6, 2, 7]
        ]
    ]
)

det = np.linalg.det(sq_arr)

print(det)
