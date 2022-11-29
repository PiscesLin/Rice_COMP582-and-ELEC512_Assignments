# Hsuan-You Lin Module 10 Problem Set Question 4.
import numpy as np

def LU_decomposition(A_Matrix, n):
    Lower_Matrix = [[0 for x in range(n)]
                    for y in range(n)]
    Upper_Matrix = [[0 for x in range(n)]
                    for y in range(n)]
                    
    for i in range(n):
        for k in range(i, n):
            LU = 0
            for j in range(i):
                LU += (Lower_Matrix[i][j] * Upper_Matrix[j][k])
            Upper_Matrix[i][k] = A_Matrix[i][k] - LU
        for k in range(i, n):
            if (i == k):
                Lower_Matrix[i][i] = 1
            else:
                LU = 0
                for j in range(i):
                    LU += (Lower_Matrix[k][j] * Upper_Matrix[j][i])
                    
                Lower_Matrix[k][i] = int((A_Matrix[k][i] - LU) /
                                  Upper_Matrix[i][i])
    print("Lower Triangular Matrix \tUpper Triangular Matrix")
    for i in range(n):
        for j in range(n):
            print(Lower_Matrix[i][j], end="\t")
        print("", end="\t")
        for j in range(n):
            print(Upper_Matrix[i][j], end="\t")
        print("")
    return Lower_Matrix, Upper_Matrix

if __name__ == "__main__" :
    A_Matrix = np.array([[4, -5, 6],
                         [8, -6, 7],
                         [12, -7, 12]])
    LU_decomposition(A_Matrix, 3)
