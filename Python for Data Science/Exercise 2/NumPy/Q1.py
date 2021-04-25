"""
Write a NumPy program to find the number of elements
of an array, length of one array element in bytes and total
bytes consumed by the elements.
"""
import numpy as np

array = np.array([2, 1, 1, 0, 9, 7, 3, 6, 9, 4, 2])

print(f"Number of elements in the array: {array.size}")
print(f"Length of one array element: {array.itemsize} bytes")
print(f"Total Bytes conusmed: {array.nbytes} bytes")
