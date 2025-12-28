import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[10, 11], [12, 13], [14, 15]])

C = A @ B
C_func = np.dot(A, B)

print(C)
print(C_func)