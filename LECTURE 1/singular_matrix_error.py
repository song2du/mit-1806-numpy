import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 9],
              [7, 8, 15]])

b = np.array([1, 1, 1])

try:
    x = np.linalg.solve(A, b)
    print(x)
except np.linalg.LinAlgError as e:
    print(e)