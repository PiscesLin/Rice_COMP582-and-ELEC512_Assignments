def Lx_solver(L, b):
    n = len(L)

    for i in range(n):
        b[i] /= L[i][i]
        L[i][i] = 1

        for j in range(i+1, n):
            b[j] -= L[j][i] * b[i]
            L[j][i] = 0

        print(f"[Iteration {i}]")
        print(f"L = {L}")
        print(f"b = {b}")

    return b
        

L = [
    [1, 0, 0],
    [4, 1, 0],
    [-6, 5, 1]
]
b = [3, 14, -7]
print(Lx_solver(L, b)) # [3, 2, 15]


# def Ux_solver(U, b):
#     n = len(U)

#     for i in range(n-1, -1, -1):
#         b[i] /= U[i][i]
#         U[i][i] = 1

#         for j in range(i):
#             b[j] -= U[j][i] * b[i]
#             U[j][i] = 0

#     return b


# U = [
#     [1, 2, 1],
#     [0, 1, 4],
#     [0, 0, 3]
# ]
# b = [5, 5, 3]
# print(Ux_solver(U, b)) # [2, 1, 1]


# def LU_decomposition(A):
#     n = len(A)
#
#     for k in range(n):
#         for i in range(k+1, n):
#             A[i][k] = A[i][k] / A[k][k]
#
#         for i in range(k+1, n):
#             for j in range(k+1, n):
#                 A[i][j] = A[i][j] - A[i][k] * A[k][j]
#
#         print(f"Iteration {k}")
#         print(f"Current compact A matrix is {A}")
#
#     L = [[0 for _ in range(n)] for _ in range(n)]
#     U = [[0 for _ in range(n)] for _ in range(n)]
#
#     for i in range(n):
#         L[i][i] = 1
#
#     for i in range(n):
#         for j in range(i):
#             L[i][j] = A[i][j]
#         for j in range(i, n):
#             U[i][j] = A[i][j]
#
#     return L, U
#
# A = [
#     [4, -5, 6],
#     [8, -6, 7],
#     [12, -7, 12]
# ]
# print(LU_decomposition(A))


# def karatsuba_multiplication(x, y):
#     a, b = x // 100, x % 100
#     c, d = y // 100, y % 100

#     # Karatsuba's algorithm
#     t1 = a * c
#     t2 = b * d
#     t3 = (a+b) * (c+d)
#     t4 = t3 - t1 - t2
    
#     print(t1, t2, t3, t4)
#     return t1 * 10000 + t4 * 100 + t2

# x = 5822
# y = 4104
# print(x*y)
# print(karatsuba_multiplication(x, y))