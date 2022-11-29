# Hsuan-You Lin Module 11 Problem Set Question 7.
def Q7(str1, str2, i, j):
    if i == 0:
        return j
 
    if j == 0:
        return i
 
    if str1[i-1] == str2[j-1]:
        return Q7(str1, str2, i-1, j-1)
 
    return 1 + min(Q7(str1, str2, i, j-1),    # Insert a char
                   Q7(str1, str2, i-1, j),    # Delete a char
                   Q7(str1, str2, i-1, j-1)    # Change 1 char into another char
                   )

if __name__ == "__main__" :
    str1 = "cast"
    str2 = "cats"
    ans = Q7(str1, str2, len(str1), len(str2))
    print("Answer is: ", ans)
