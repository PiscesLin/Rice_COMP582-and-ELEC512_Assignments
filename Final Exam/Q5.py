# Hsuan-You Lin Final Exam Question 5.
from collections import defaultdict
def find(parent, i):
    if i < 0 or i >= len(parent):
        return None
    if parent[i] == i:
        return i
    return find(parent, parent[i])

# Function to construct a new MST from the old one without using the deleted edge
def new_mst(n, edges, deleted_edge):
    # Create a disjoint set with n nodes
    parent = [i for i in range(n + 1)]
    rank = [0 for i in range(n + 1)]
    min_cost = defaultdict(int)

    for u, v, weight in edges:
        if (u, v) == deleted_edge:
            continue

        x = find(parent, u)
        y = find(parent, v)

        # If the nodes are not in the same set, add the edge to the new MST
        if x != y:
            if weight < min_cost[v]:
                min_cost[v] = weight

            if weight < min_cost[u]:
                min_cost[u] = weight

            # Union the sets
            if rank[x] < rank[y]:
                parent[x] = y
            elif rank[x] > rank[y]:
                parent[y] = x
            else:
                parent[x] = y
                rank[y] += 1

    return min_cost

if __name__ == "__main__" :
    n = 6
    edges = [(0, 1, 2), (0, 2, 4), (0, 3, 1), (1, 2, 3), (1, 4, 5), (2, 3, 2), (2, 5, 7), (3, 5, 1), (3, 6, 3), (4, 5, 2), (5, 6, 5)]
    deleted_edge = (3, 5)
    print(new_mst(n, edges, deleted_edge)) 
    # Expected output: {0: 0, 1: 2, 2: 3, 3: 1, 4: 5, 5: 2, 6: 3}
