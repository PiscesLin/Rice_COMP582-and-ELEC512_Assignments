# Hsuan-You Lin Module 9 Problem Set Question 9.
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_matrix = [[0 for i in range(vertices)]
                                    for j in range(vertices)]
 
    def insert(self, s, destination):
        self.adjacency_matrix[s - 1][destination - 1] = 1
 
    def issink(self, i):
        for j in range(self.vertices):
            if self.adjacency_matrix[i][j] == 1:
                return False
            if self.adjacency_matrix[j][i] == 0 and j != i:
                return False
        return True
 
    def eliminate(self):
        i, j = 0, 0
        while i < self.vertices and j < self.vertices:
            if self.adjacency_matrix[i][j] == 1:
                i += 1
            else:
                j += 1
        if i > self.vertices:
            return -1
        elif self.issink(i) is False:
            return -1
        else:
            return i
 
if __name__ == "__main__":
 
    number_of_vertices = 6
    number_of_edges = 5
    g = Graph(number_of_vertices)
 
    # input set 1
    g.insert(1, 6)
    g.insert(2, 6)
    g.insert(3, 6)
    g.insert(4, 6)
    g.insert(5, 6)
     
    # input set 2
#    g.insert(1, 6)
#    g.insert(2, 3)
#    g.insert(2, 4)
#    g.insert(4, 3)
#    g.insert(5, 3)
 
    vertex = g.eliminate()
 
    if vertex >= 0:
        print("Sink found at vertex %d" % (vertex + 1))
    else:
        print("No Sink")
