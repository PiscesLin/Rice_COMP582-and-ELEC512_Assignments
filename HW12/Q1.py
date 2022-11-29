# Hsuan-You Lin Module 10 Problem Set Question 1.
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

if __name__ == "__main__" :
    Lower_Matrix = np.array([[1, 0, 0],
                             [4, 1, 0],
                             [-6, 5, 1]])
    b_Matrix = np.array([3, 14, -7])
    print("Q1: Solve the lower triangular system: Lx = b.")
    print("L = \n", Lower_Matrix)
    print("b = ", b_Matrix)
    ans = lower_triangular_system(Lower_Matrix, b_Matrix)
    print("x = ", ans)
