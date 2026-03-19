# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [aᵢ, bᵢ] indicates that there is an edge 
# between aᵢ and bᵢ in the graph. Return the number of connected components in the graph.

# The goal is to find how many separate, unconnected clusters of nodes (components) exist in the graph. The code does this by initially 
# treating every node as its own independent component and then merging them as it reads the edges.
# Initialization (__init__) - When the DisjointSet is created for n nodes, it initializes two arrays: parent and size.
# Initially, every node is its own parent (representing n disconnected components), and the size of each component is 1.
# Find with Path Compression (find_parent)
# This function determines which component a node belongs to by finding its "root" or "parent" node.
# Optimization (Path Compression): As it recursively searches for the root, it updates the parent of every visited node directly to 
# the root (self.parent[node] = self.find_parent(...)). This flattens the tree, ensuring future lookups are almost instantaneous.
# Union by Size (union_by_size)
# This function takes two connected nodes (u and v) and merges their components. It first finds the root of both nodes. 
# If they share the same root, they are already in the same component, so it does nothing.
# Optimization (Union by Size): If they have different roots, it attaches the smaller component to the larger component. This keeps the
# resulting tree shallow, further speeding up the find_parent operations.
# Counting Components (countComponents)
# It loops through all the given edges and unions the nodes together.
# After processing all edges, it loops through every node from 0 to n-1. If a node's parent is itself (idx == ds.find_parent(idx)),
# it means this node is the root of a component. The number of unique roots equals the total number of connected components.

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

# TC - O(V + E)
# SC - O(V)
