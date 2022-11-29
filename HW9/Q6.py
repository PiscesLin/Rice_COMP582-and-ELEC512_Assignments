# Hsuan-You Lin Module 9 Problem Set Question 6.
import sys
import heapq

def dijkstra(graph, start, end):
    # Assign to all nodes a distance value of ‘inf’, except for the start node which has a distance of zero, and initialize a predecessor dictionary.
    inf = sys.maxsize
    pred = {i:i for i in graph}
    dist = {i:inf for i in graph}
    dist[start] = 0
    # initialize a priority queue and insert the tuple
    PQ = []
    heapq.heappush(PQ, [dist[start], start])
 
    while(PQ):
        # find the next node with the smallest distance value.
        u = heapq.heappop(PQ)
        u_dist = u[0]
        u_id = u[1]
        if u_dist == dist[u_id]:
            for v in graph[u_id]:
               v_id = v[0]
               w_uv = v[1]
               if dist[u_id] +  w_uv < dist[v_id]:
                   dist[v_id] = dist[u_id] + w_uv
                   heapq.heappush(PQ, [dist[v_id], v_id])
                   pred[v_id] = u_id
    # reconstruct the shortest path with the help of the predecessor dictionary.
    else:
        st = []
        # follow the shortest path backwards from the target to the start
        node = end
        while(True):
            st.append(str(node))
            if(node == pred[node]):
                break
            node = pred[node]
        path = st[::-1]
        print("The distance from " + start + " to " + end + " is: " + str(dist[end]) + "\n")
        print("The shortest path is: " + " ".join(path))

if __name__ == "__main__":
#    graph = {"A": [("B",2), ("C",4)],
#             "B": [("C",3), ("D",8)],
#             "C": [("D",2), ("E",5)],
#             "D": [("E",11), ("F",22)],
#             "E": [("F",1)],
#             "F": [("D",22), ("E",1)]
#            }
    graph = {"A": [("B",4), ("C",1)],
             "B": [("E",4)],
             "C": [("B",2), ("D",4)],
             "D": [("E",4)],
             "E": []
            }
#    graph = {"A": [("B",5), ("C",6)],
#             "B": [],
#             "C": [("B",-3)]
#            }
    start = "A"
    end = "E"
    dijkstra(graph, start, end)
