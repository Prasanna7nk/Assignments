"""
Write a NumPy program to find the set difference of two
arrays. The set difference will return the sorted, unique
values in array1 that are not in array2.
"""
import numpy as np

array1 = np.array([1, 2, 3, 4, 5, 2, 1, 1, 0, 9, 7, 3, 6, 9, 4, 2])
array2 = np.array([8, 5, 4, 2, 3, 6, 7, 8, 2])

set_difference = np.setdiff1d(array1, array2)
print(set_difference)
