# Hsuan-You Lin Module 9 Problem Set Question 5.

def heapify(arr, start, end, name_to_idx):
    for i in range(end // 2 - 1, start - 1, -1):
        l, r = 2 * i + 1, 2 * i + 2
        max_id = i
        if arr[max_id][0] > arr[1][0]:
            max_id = l
        if r < end and arr[max_id][0] > arr[r][0]:
            max_id = r
    name1, name2 = arr[i][1], arr[max_id][1]
    name_to_idx[name1] = max_id
    name_to_idx[name2] = i
    
    arr[i], arr[max_id] = arr[max_id], arr[i]
    if max_id != i:
        heapify(arr, max_id, end, name_to_idx)

def update_priority(arr, name, val, name_to_idx):
    idx = name_to_idx[name]
    arr[idx][0] = val
    heapify(arr, 0, len(arr), name_to_idx)

if __name__ == "__main__":
    arr = [[1, "A"], [0, "B"], [3, "C"], [2, "D"], [5, "E"]]
    name_to_idx = {arr[i][1]: i for i in range(len(arr))}
    heapify(arr, 0, len(arr), name_to_idx)
    
    print(arr)
    print(name_to_idx)
    print("-------------------------------------------------------------------")
    
    update_priority(arr, "A", 6, name_to_idx)
    print(arr)
    print(name_to_idx)
