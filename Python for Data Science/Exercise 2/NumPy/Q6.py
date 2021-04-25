"""
Write a NumPy program to multiple three matrices each
of 3*3 dimensions.
"""
import numpy as np

A = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [5, 6, 7]
])

B = np.array([
    [5, 6, 7],
    [9, 8, 2],
    [6, 6, 6]
])

C = np.array([
    [5, 3, 2],
    [0, 0, 0],
    [6, 3, 4]
])

ABC = np.matmul(np.matmul(A, B), C)  # (A x B) x C

print(ABC)
