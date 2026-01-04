import numpy as np

A = np.array([[1, 2, 1],
     [3, 8, 1],
     [0, 4, 1]], dtype=float)
A_origin = A.copy()
E_total = np.eye(3)

for i in range(len(A)):
    for j in range(i+1, len(A)):
        multiplier = A[j][i] / A[i][i]
        E = np.eye(3)
        E[j, i] = -multiplier
        print(f"------------")
        print(f"E_{j}{i+1}")
        print(E)
        print(f"------------")
        E_total = E@E_total

        A[j][i:] -= multiplier * A[i][i:]

print(A_origin)
print(A)
print(E_total)
print(np.allclose(E_total@A_origin, A))