import numpy as np
def lower_triangular_system(Lower_Matrix, b_Matrix):
    for i in range(len(Lower_Matrix)):
        b_Matrix[i] = b_Matrix[i] / Lower_Matrix[i][i]
        Lower_Matrix[i][i] = 1
        for j in range(i + 1, len(Lower_Matrix)):
            b_Matrix[j] -= Lower_Matrix[j][i] * b_Matrix[i]
            Lower_Matrix[j][i] = 0
            x_Matrix = b_Matrix
    return x_Matrix

Lower_Matrix = np.array([[1, 0, 0],
                     [4, 1, 0],
                     [-6, 5, 1]])
b_Matrix = np.array([3, 14, -7])
print("Q1: Solve the lower triangular system: Lx = b.")
print("L = \n", Lower_Matrix)
print("b = ", b_Matrix)
ans = lower_triangular_system(Lower_Matrix, b_Matrix)
print("x = ", ans) # [3, 2, 1]


def upper_triangular_system(Upper_Matrix, b_Matrix):
    for i in range(len(Upper_Matrix)-1, -1, -1):
        b_Matrix[i] = b_Matrix[i] / Upper_Matrix[i][i]
        Upper_Matrix[i][i] = 1
        for j in range(i):
            b_Matrix[j] -= Upper_Matrix[j][i] * b_Matrix[i]
            Upper_Matrix[j][i] = 0
            x_Matrix = b_Matrix
    return x_Matrix

Upper_Matrix = np.array([[1, 2, 1],
                        [0, 1, 4],
                        [0, 0, 3]])
b_Matrix = np.array([5, 5, 3])
print("Q2: Solve the upper triangular system: Ux = b.")
print("U = \n", Upper_Matrix)
print("b = ", b_Matrix)
ans = upper_triangular_system(Upper_Matrix, b_Matrix)
print("x = ", ans) # [2, 1, 1]

#/////////////////////////////////////////////////////

import scipy as sci
from scipy import linalg

# A = sci.array([[7, 3, -1, 2], [3, 8, 1, -4], [-1, 1, 4, -1], [2, -4, -1, 6]])
# A = sci.array([[4, -5, 6],
#                [8, -6, 7],
#                [12, -7, 12]])
# P, L, U = sci.linalg.lu(A)
#
# print("A: \n", A)
# print("P: \n", P)
# print("L: \n", L)
# print("U: \n", U)

#/////////////////////////////////////////////////////

MAX = 100
def LU_decomposition(mat, n):
    lower = [[0 for x in range(n)]
             for y in range(n)]
    upper = [[0 for x in range(n)]
             for y in range(n)]

    # Decomposing matrix into Upper
    # and Lower triangular matrix
    for i in range(n):

        # Upper Triangular
        for k in range(i, n):

            # Summation of L(i, j) * U(j, k)
            sum = 0
            for j in range(i):
                sum += (lower[i][j] * upper[j][k])

            # Evaluating U(i, k)
            upper[i][k] = mat[i][k] - sum

        # Lower Triangular
        for k in range(i, n):
            if (i == k):
                lower[i][i] = 1  # Diagonal as 1
            else:

                # Summation of L(k, j) * U(j, i)
                sum = 0
                for j in range(i):
                    sum += (lower[k][j] * upper[j][i])

                # Evaluating L(k, i)
                lower[k][i] = int((mat[k][i] - sum) /
                                  upper[i][i])

    # setw is for displaying nicely
    print("Lower Triangular\t\tUpper Triangular")

    # Displaying the result :
    for i in range(n):

        # Lower
        for j in range(n):
            print(lower[i][j], end="\t")
        print("", end="\t")

        # Upper
        for j in range(n):
            print(upper[i][j], end="\t")
        print("")
    return lower, upper


# Driver code
# mat = [[2, -1, -2],
#        [-4, 6, 3],
#        [-4, -2, 8]]
mat = [[4, -5, 6],
       [8, -6, 7],
       [12, -7, 12]]

LU_decomposition(mat, 3)
ans = LU_decomposition(mat, 3)
print("L&U: \n", ans)

#/////////////////////////////////////////////////////

def karatsuba(x, y):
    a, b = x // 100, x % 100
    c, d = y // 100, y % 100

    ac = a * c
    print("a * c = ", ac)
    bd = b * d
    print("b * d = ", bd)
    abcd = (a+b) * (c+d)
    print("(a + b) * (c + d) = ", abcd)
    result = ac * 10000 + (abcd - ac - bd) * 100 + bd

    return result

x = 5822
y = 4104
print(x*y)
print(karatsuba(x, y))