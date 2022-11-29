# Hsuan-You Lin
# Midterm exam: Question 5
import heapq

def Largest_M(arr, m):
    root = []
    for i in range(len(arr)):
        heapq.heappush(root, arr[i])
        if len(root) > m:
            heapq.heappop(root)
    return root
    
if __name__ == "__main__":
    arr = [3, 6, 1, 8, 10, 14, 21, 42, 61, 52]
    print(Largest_M(arr, 5))

#       14
#      /   \
#     21    52
#    / \
#   61  42
