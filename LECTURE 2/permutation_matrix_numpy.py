import numpy as np

A = np.array([[1, 2, 1],
     [3, 8, 1],
     [0, 4, 1]], dtype=float)

A_origin = A.copy()
L_total = np.eye(3)
P = np.eye(3)
L = np.eye(3)

for i in range(len(A)):
    max_row_index = np.argmax(np.abs(A[i:,i])) + i
    A[[i, max_row_index]] = A[[max_row_index, i]]
    P[[i, max_row_index]] = P[[max_row_index, i]]
    if i > 0:
        L[[i, max_row_index], :i] = L[[max_row_index, i], :i]
    for j in range(i+1, len(A)):
        multiplier = A[j][i] / A[i][i]
        
        E = np.eye(3)
        E[j, i] = -multiplier

        L[j, i] = multiplier
        L_total = L_total@np.linalg.inv(E)

        A[j][i:] -= multiplier * A[i][i:]

print(P)
print(np.allclose(L@A, P@A_origin))