# Hsuan-You Lin Module 9 Problem Set Question 4.
from collections import defaultdict as DefDict
from collections import deque

def BFS(adjacency_list, start_idx, results):
    queue = deque([start_idx])
    mark = set([start_idx])
    while queue:
        idx = queue.popleft()
        results.append(idx)
        for neighbor in adjacency_list[idx]:
            if neighbor not in mark:
                queue.append(neighbor)
                mark.add(neighbor)

if __name__ == "__main__" :
    adjacency_list = [[1, 2, 3],
                      [0, 2, 3],
                      [0, 1, 3],
                      [0, 1, 2, 5],
                      [5, 6, 7],
                      [3, 4, 6],
                      [4, 5, 7],
                      [4, 6]]
    results = []
    BFS(adjacency_list, 0, results)
    print(results)
