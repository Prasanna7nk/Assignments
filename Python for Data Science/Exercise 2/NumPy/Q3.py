"""
Write a NumPy program to compute the cross product
of two given vectors.
"""
import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[2, 3, 4], [4, 5, 6]])

cross_product = np.cross(arr1, arr2)
print(cross_product)
