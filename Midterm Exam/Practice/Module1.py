def binary_search_recursive_method(arr, low, high, target):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search_recursive_method(arr, low, mid - 1 ,target)
        else:
            return binary_search_recursive_method(arr, mid + 1, high, target)
    else:
        return -1
    
def binary_search_iteration_method(arr, target):
    min = 0
    max = len(arr) - 1
    while min <= max:
        mid = (max + min) // 2
        if arr[mid] < target:
            min = mid + 1
        elif arr[mid] > target:
            max = mid - 1
        else:
            return mid
    return -1

if __name__ == "__main__":
    arr_1 = [ 2, 3, 4, 10, 40 ]
    target_1 = 10
    result_1 = binary_search_recursive_method(arr_1, 0, len(arr_1) - 1, target_1)
    if result_1 != -1:
        print("\nUsing Recursive Method:")
        print("--> The element at index", str(result_1), "is", arr_1[result_1])
    else:
        print("\nElement is not present in array")

    arr_2 = [ 1, 3, 5, 7, 30, 21, 23, 56, 98 ]
    target_2 = 56
    result_2 = binary_search_iteration_method(arr_2, target_2)
    if result_2 != -1:
        print("\nUsing Iteration Method:")
        print("--> The element at index", str(result_2), "is", arr_2[result_2])
    else:
        print("\nElement is not present in array")
# The complexity of Binary Search is O(log(n))
