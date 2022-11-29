# Hsuan-You Lin Module 11 Problem Set Question 6.
import sys

def Q6(arr, start, length):

    count = 0
    
    if start == length:
        return 0

    result = sys.maxsize

    for i in range(start, length):
        count = (Q6(arr, start, i)
                 + Q6(arr, i + 1, length)
                 + arr[start-1] * arr[i] * arr[length])

        if count < result:
            result = count

    return result

if __name__ == '__main__':
    arr = [10, 10, 10, 1]
    # 3 matrices of dimensions 10x10, 10x10, 10x1
    ans = Q6(arr, 1, len(arr)-1)
    print("Minimum number of multiplications is ", ans)
