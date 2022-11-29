def max_heapify(arr, k):
    l = left(k)
    r = right(k)
    if l < len(arr) and arr[l] > arr[k]:
        largest = l
    else:
        largest = k
    if r < len(arr) and arr[r] > arr[largest]:
        largest = r
    if largest != k:
        arr[k], arr[largest] = arr[largest], arr[k]
        max_heapify(arr, largest)

def left(k):
    return 2 * k + 1

def right(i):
    return 2 * i + 2

def build_heap(arr):
    n = int((len(arr)//2)-1)
    for k in range(n, -1, -1):
        max_heapify(arr,k)

# Binary Tree Representation of input array
#             4
#           /    \
#         2        7
#       /  \     /  \
#      9    12  1    3
#    / \    /
#   0  10  11
arr = [4, 2, 7, 9, 12, 1, 3, 0, 10, 11]
build_heap(arr)
print(arr)
 
# Final Heap:
#             12
#           /    \
#         11      7
#        /  \     / \
#       10   4   1   3
#      / \   /
#     0   9 2
