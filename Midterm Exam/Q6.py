# Hsuan-You Lin
# Midterm exam: Question 6.3
import heapq

def bmerge_min(arr_sizes):
    heap = []
    for i in range(len(arr_sizes)):
        heapq.heappush(heap, (arr[i], i))
    
    L = len(arr_sizes)
    while len(heap) > 1:
        number_1, index_1 = heapq.heappop(heap)
        number_2, index_2 = heapq.heappop(heap)
        print(f"{L} = bmerge({index_1}, {index_2})")
        heapq.heappush(heap, (number_1 + number_2, L))
        L += 1
    
if __name__ == "__main__":
    arr = [0, 1, 2]
    bmerge_min(arr)
