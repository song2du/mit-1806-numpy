A = [[1, 2, 1],
     [3, 8, 1],
     [0, 4, 1]]

for i in range(len(A)):
    pivot = A[i][i]
    for j in range(i+1, len(A)):
        multiplier = A[j][i] / A[i][i]
        for k in range(i, len(A[0])):
            A[j][k] -= multiplier * A[i][k]

print(A)