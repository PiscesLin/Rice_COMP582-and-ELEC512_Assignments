# Hsuan-You Lin
# Midterm exam: Question 7

def Find_Two_Largest(arr):
    max_1 = 0
    max_2 = 0
    for i in range(len(arr)):
        if arr[i] > max_1:
            max_1, max_2 = arr[i], max_1
        elif arr[i] > max_2:
            max_2 = arr[i]
    return max_1, max_2
    
if __name__ == "__main__":
    arr = [0, 1, 2, 3, 3, 5, 7, 10, 21]
    L1, L2 = Find_Two_Largest(arr)
    print(L1, L2)
