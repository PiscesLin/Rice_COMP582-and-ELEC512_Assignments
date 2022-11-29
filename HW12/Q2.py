# Hsuan-You Lin Module 10 Problem Set Question 2.
import numpy as np

def upper_triangular_system(Upper_Matrix, b_Matrix):
    for i in range(len(Upper_Matrix)-1, -1, -1):
        b_Matrix[i] = b_Matrix[i] / Upper_Matrix[i][i]
        Upper_Matrix[i][i] = 1
        for j in range(i):
            b_Matrix[j] -= Upper_Matrix[j][i] * b_Matrix[i]
            Upper_Matrix[j][i] = 0
            x_Matrix = b_Matrix
    return x_Matrix

if __name__ == "__main__" :
    Upper_Matrix = np.array([[1, 2, 1],
                            [0, 1, 4],
                            [0, 0, 3]])
    b_Matrix = np.array([5, 5, 3])
    print("Q2: Solve the upper triangular system: Ux = b.")
    print("U = \n", Upper_Matrix)
    print("b = ", b_Matrix)
    ans = upper_triangular_system(Upper_Matrix, b_Matrix)
    print("x = ", ans)
