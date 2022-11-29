class quickFind(object):
    def __init__(self, n):
        self.nodes = n
        self.idx = list(range(n))
        self.parts = n

    def union(self, edge):
        p, q = edge[0], edge[1]
        idxp, idxq = self.idx[p], self.idx[q]
        if idxp == idxq:
            return

        for i in range(n):
            if self.idx[i] == idxp:
                self.idx[i] == idxq
        self.parts -= 1

    def find(self, p, q):
        return self.idx[p] == self.idx[q]
#------------------------------------------------
class quickUnion(object):
    def __init__(self, n):
        self.nodes = n
        self.idx = list(range(n))
        self.parts = n

    def root(self, node):
        while node != self.idx[node]:
            node = self.idx[node]
        return node

    def union(self, edge):
        p, q = edge[0], edge[1]
        rootp, rootq = self.root(p), self.root(q)
        if rootp == rootq:
            return
        else:
            self.idx[rootp] = rootq
            self.parts -= 1

    def find(self, p, q):
        return self.root(p) == self.root(q)
#------------------------------------------------
class weightedQuickUnion(object):
    def __init__(self, n):
        self.nodes = n
        self.idx = list(range(n))
        self.size = [1] * n
        self.parts = n

    def root(self, node):
        while node != self.idx[node]:
            node = self.idx[node]
        return node

    def union(self, edge):
        p, q = edge[0], edge[1]
        rootp, rootq = self.root(p), self.root(q)
        if rootp == rootq:
            return
        elif self.size[rootp] > self.size[rootq]:
            self.idx[rootq] = rootp
            self.size[rootp] += self.size[rootq]
        else:
            self.idx[rootp] = rootq
            self.size[rootq] += self.size[rootp]
        self.parts -= 1

    def find(self, p, q):
        return self.root(p) == self.root(q)
#------------------------------------------------
class weightedQuickUnionWithCompression(object):
    def __init__(self, n):
        self.nodes = n
        self.idx = list(range(n))
        self.size = [1] * n
        self.parts = n

    def root(self, node):
        while node != self.idx[node]:
            node = self.idx[node]
        return node

    def union(self, edge):
        p, q = edge[0], edge[1]
        rootp, rootq = self.root(p), self.root(q)
        if rootp == rootq:
            return
        elif self.size[rootp] > self.size[rootq]:
            self.idx[rootq] = rootp
            self.size[rootp] += self.size[rootq]
        else:
            self.idx[rootp] = rootq
            self.size[rootq] += self.size[rootp]
        self.parts -= 1

    def find(self, p, q):
        return self.root(p) == self.root(q)
        
    def root(self, node):
        while node != self.idx[node]:
            # 将祖父节点变成父节点
            self.idx[node] = self.idx[self.idx[node]]
            node = self.idx[node]
        return node
        
#------------------------------------------------
class DisjointSet:
    parent = [0,1,2]
    def Find_parent(self, a):
        if a == self.parent[a]:
            return a
        if a != self.parent[a]:
            return self.Find_parent(self.parent[a])
    def Union(self, x, y):
        self.parent[x] = y
    
if __name__ == '__main__':
    ds = DisjointSet()
    graph = {
        0:[1,2],
        1:[2],
        2:[]
    }
    for i in graph:
        for j in graph[i]:
            x = ds.Find_parent(i)
            y = ds.Find_parent(j)
            if x == y:
                print("Cyclic Graph")
            ds.Union(x,y)
