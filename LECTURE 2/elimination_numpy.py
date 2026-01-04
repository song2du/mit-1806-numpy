import numpy as np

A = np.array([[1, 2, 1],
     [3, 8, 1],
     [0, 4, 1]], dtype=float)

for i in range(len(A)):
    pivot = A[i][i]
    for j in range(i+1, len(A)):
        multiplier = A[j][i] / A[i][i]
        A[j][i:] -= multiplier * A[i][i:]

print(A)