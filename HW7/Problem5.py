# Hsuan-You Lin_Module 7 Problem Set - Problem5
def Heapify(arr, start, end):
    for i in range(end//2 - 1, start - 1, -1):
        Left = 2 * i + 1 # left = 2*i + 1
        Right = 2 * i + 2 # right = 2*i + 2
        root = i # Initialize largest as root
        
        if arr[root] < arr[Left]:
            root = Left
        if Right < end and arr[root] < arr[Right]:
            root = Right
        
        arr[i], arr[root] = arr[root], arr[i]
        if root != i:
            Heapify(arr, root, end)

def HeapSort(arr):
    for i in range(len(arr) -1, -1, -1):
        Heapify(arr, 0, i+1)
        arr[i], arr[0] = arr[0], arr[i]

#/-----main function------------------------

if __name__ == '__main__':
    arr = [4, 2, 7, 9, 12, 1, 3, 0, 10, 11]
    print("Unsorted array is:", arr)
    HeapSort(arr)
    print("Sorted array is:", arr)
