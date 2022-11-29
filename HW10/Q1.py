# Hsuan-You Lin Module 10 Problem Set Question 1.
def counting_Sort(arr):
    # creat the hashmap for array and count the elements
    HashMap = dict()
    output = [None] * len(arr)
    for i in range(len(arr)):
        num = arr[i]
        # if any element repeats itself, 
        # simply increase its count
        if num not in HashMap:
            HashMap[num] = 0
        HashMap[num] += 1
    
    # sorted the hashmap by keys
    HashMap = dict(sorted(HashMap.items(), key = lambda item: item[0]))
    sorted_num = list(HashMap.keys())

    # cumulative count
    for i in range(1, len(sorted_num)):
        HashMap[sorted_num[i]] += HashMap[sorted_num[i - 1]]

    # Build the output array
    for num in arr:
        output[HashMap[num] - 1] = num
        HashMap[num] -= 1

    # Copy the output array to arr, 
    # so that arr now contains sorted characters
    for i in range(0, len(arr)):
        arr[i] = output[i]
    return arr

if __name__ == "__main__" :
    arr = [4, 2, 2, 8, 3, 3, 1]
    print("Before sorted array is: ", arr)
    ans = counting_Sort(arr)
    print("After counting sorted array is: ", ans)