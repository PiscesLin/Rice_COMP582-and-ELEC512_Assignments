# Hsuan-You Lin_Module 7 Problem Set - Problem7
import operator

def Heapify(arr, start, end, op = operator.lt):
    for i in range(end//2 - 1, start - 1, -1):
        Left = 2 * i + 1 # left = 2*i + 1
        Right = 2 * i + 2 # right = 2*i + 2
        target_root = i # Initialize largest as root
        
        if op(arr[target_root], arr[Left]):
            target_root = Left
        if Right < end and op(arr[target_root], arr[Right]):
            target_root = Right
        
        arr[i], arr[target_root] = arr[target_root], arr[i]
        if target_root != i:
            Heapify(arr, target_root, end)
        
class LMedianHeap:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        
    def insert(self, val):
        if not self.max_heap or val <= self.max_heap[0]:
            self.max_heap.append(val)
            Heapify(self.max_heap, 0, len(self.max_heap), op = operator.lt)
        else:
            self.min_heap.append(val)
            Heapify(self.min_heap, 0, len(self.min_heap), op = operator.gt)
            
        if len(self.max_heap) - len(self.min_heap) > 1:
            self.max_heap[0], self.max_heap[-1] = self.max_heap[-1], self.max_heap[0]
            val = self.max_heap.pop()
            Heapify(self.max_heap, 0, len(self.max_heap), op = operator.lt)
            self.min_heap.append(val)
            Heapify(self.min_heap, 0, len(self.min_heap), op = operator.gt)
        elif len(self.max_heap) - len(self.min_heap) < 0:
            self.min_heap[0], self.min_heap[-1] = self.min_heap[-1], self.min_heap[0]
            val = self.min_heap.pop()
            Heapify(self.min_heap, 0, len(self.min_heap), op = operator.gt)
            self.max_heap.append(val)
            Heapify(self.max_heap, 0, len(self.max_heap), op = operator.lt)
            
    def show_lmedian(self):
        print(self.max_heap[0] if self.max_heap else -1)

#/-----main function------------------------

if __name__ == '__main__':
    arr = [2, 9, -1, 7, 55]
    obj = LMedianHeap()
    for i in range(len(arr)):
        obj.insert(arr[i])
        print("Median = ", obj.show_lmedian())
