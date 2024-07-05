class DisjointSet:
    def __init__(self, nodes):
        self.parent = [idx for idx in range(nodes + 1)]
        self.size = [1 for idx in range(nodes + 1)]

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
        return

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        ds = DisjointSet(n)
        for src, dest in edges:
            ds.union_by_size(src, dest)
        if ds.find_parent(source) == ds.find_parent(destination):
            return True
        else:
            return False

# TC - O(V + E)
# SC - O(V)
