A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[10, 11],
     [12, 13],
     [14, 15]]

C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

for i in range(len(B[0])):
    for j in range(len(B)):
        scalar = B[j][i]
        for k in range(len(A)):
                C[k][i] += A[k][j] * scalar

for row in C:
     print(row)

    