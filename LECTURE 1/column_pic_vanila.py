A = [[0, 1, 2],
     [3, 4, 5],
     [6, 7, 8]]

x = [1, 2, 3]

b = [0] * len(A)

for i in range(len(x)):
    scalar = x[i]
    for j in range(len(A)):
        b[j] += A[j][i] * scalar
print(b)