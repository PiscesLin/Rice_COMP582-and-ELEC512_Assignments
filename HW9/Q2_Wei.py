# Hsuan-You Lin Module 9 Problem Set Question 2.
from collections import defaultdict as DefDict
from collections import deque

def topological_sort(graph, result):
    queue = deque()
    pre_queue = set()
    node = DefDict(set)
    
    for C1, C0_list in graph.items():
        for C0 in C0_list:
            node[C0].add(C1)
        if len(C0_list) == 0:
            queue.append(C1)
        while queue:
            C = queue.popleft()
            pre_queue.add(C)
            result.append(C)
            for C1 in node[C]:
                graph[C1].remove(C)
                if len(graph[C1]) == 0:
                    queue.append(C1)
    return result
    
if __name__ == "__main__":
    graph = { "LA15": {},
                "LA16": {"LA15"},
                "LA22": {},
                "LA31": {"LA15"},
                "LA32": {"LA16", "LA31"},
                "LA126": {"LA22", "LA32"},
                "LA127": {"LA16"},
                "LA141": {"LA22", "LA16"},
                "LA169": {"LA32"}
                }
    results =[]
    topological_sort(graph, results)
    ans = topological_sort(graph, results)
    print(result)
