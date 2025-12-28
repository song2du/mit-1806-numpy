import numpy as np

A = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
x = np.array([1, 2, 3])

b = []

for i in range(len(A)):
    row_result = np.dot(A[i], x)
    b.add(row_result)

print(b)