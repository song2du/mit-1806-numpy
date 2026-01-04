import numpy as np

A = np.array([[1, 2, 1],
     [3, 8, 1],
     [0, 4, 1]], dtype=float)
A_origin = A.copy()
L_total = np.eye(3)
L = np.eye(3)
for i in range(len(A)):
    for j in range(i+1, len(A)):
        multiplier = A[j][i] / A[i][i]
        
        E = np.eye(3)
        E[j, i] = -multiplier

        L[j, i] = multiplier
        L_total = L_total@np.linalg.inv(E)

        A[j][i:] -= multiplier * A[i][i:]


print(L_total)
print(L)
print(np.allclose(L_total@A, A_origin))
print(np.allclose(L@A, A_origin))