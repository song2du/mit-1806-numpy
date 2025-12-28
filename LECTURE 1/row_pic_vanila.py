A = [[0, 1, 2],
     [3, 4, 5],
     [6, 7, 8]]

x = [1, 2, 3]

b = []

for i in range(len(A)):
    dot_product = 0
    for j in range(len(A[0])):
        dot_product += A[i][j] * x[j]
    b.append(dot_product)
print(b)

