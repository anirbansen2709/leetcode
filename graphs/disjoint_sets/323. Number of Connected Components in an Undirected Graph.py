class DisjointSet:
    def __init__(self, nodes):
        self.size = [1 for _ in range(nodes + 1)]
        self.parent = [idx for idx in range(nodes + 1)]
    def find_parent(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]
    def union_by_size(self, u, v):
        par_u = self.find_parent(u)
        par_v = self.find_parent(v)
        if par_u == par_v:
            return 
        if self.size[par_u] > self.size[par_v]:
            self.parent[par_v] = par_u
            self.size[par_u] += self.size[par_v]
        else:
            self.parent[par_u] = par_v
            self.size[par_v] += self.size[par_u]

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ds = DisjointSet(n)
        for node1, node2 in edges:
            ds.union_by_size(node1, node2)
        
        count = 0
        for idx in range(n):
            if idx == ds.find_parent(idx):
                count += 1

        return count
