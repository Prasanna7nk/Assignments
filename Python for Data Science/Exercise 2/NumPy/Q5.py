"""
Write a NumPy program to compute the eigenvalues and
right eigenvectors of a given square array.
"""
import numpy as np

sq_arr = np.array([[1, 2], [6, 9]])

eigen_vals, eigen_vectors = np.linalg.eig(sq_arr)
print(f"Eigen Values: {eigen_vals}")
print(f"Eigen Vectors: {eigen_vectors}")
