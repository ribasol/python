A = [[1, 2],
     [3, 4]]

B = [[2, 0],
     [1, 2]]

filas_A = len(A)
columnas_B = len(B[0])
columnas_A = len(A[0])

C = [[0 for _ in range(columnas_B)] for _ in range(filas_A)]

for i in range(filas_A):
    for j in range(columnas_B):
        for k in range(columnas_A):
            C[i][j] += A[i][k] * B[k][j]

print("Matriz resultado:")
for fila in C:
    print(fila)
