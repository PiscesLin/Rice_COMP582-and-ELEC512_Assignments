# Hsuan-You Lin Final Exam Question 9.
def pow3x3(M, n):
    # initialize the result to be the identity matrix
    result = [[1, 0, 0], 
              [0, 1, 0], 
              [0, 0, 1]]
    
    # iterate n times
    for i in range(n):
        # compute the product of the result and M, and update the result
        result = [[sum(a * b for a, b in zip(result_row, M_col)) for M_col in zip(*M)] for result_row in result]
    
    return result

if __name__ == "__main__" :
    # test the pow3x3 function
    M = [[1, 2, 3], 
         [4, 5, 6], 
         [7, 8, 9]]
    n = 2
    print(pow3x3(M, n)) 
    # should print [[30, 36, 42], [66, 81, 96], [102, 126, 150]]