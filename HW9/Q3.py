# Hsuan-You Lin Module 9 Problem Set Question 3.
from collections import defaultdict as DefDict
from collections import deque

def DFS(adjacency_list, visited, idx, results):
    if idx in visited:
        return
    visited.add(idx)
    results.append(idx)
    for neighbor in adjacency_list[idx]:
        DFS(adjacency_list, visited, neighbor, results)

if __name__ == "__main__" :
    adjacency_list = [[1, 2, 3],
                      [0, 2, 3],
                      [0, 1, 3],
                      [0, 1, 2, 5],
                      [5, 6, 7],
                      [3, 4, 6],
                      [4, 5, 7],
                      [4, 6]]
    visited = set()
    results = []
    DFS(adjacency_list, visited, 0, results)
    print(results)
