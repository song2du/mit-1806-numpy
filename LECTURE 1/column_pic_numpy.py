import numpy as np

A = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
x = np.array([1, 2, 3])

b = np.zeros(3)

for i in range(len(x)):
    b += A[:, i] * x[i]

print(b)