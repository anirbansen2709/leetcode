"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def get_clone(self, node, old_to_new):
        if node not in old_to_new:
            clone = Node(node.val)
            old_to_new[node] = clone
            for nei in node.neighbors:
                clone.neighbors.append(self.get_clone(nei, old_to_new))
            return clone
        else:
            return old_to_new[node]

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old_to_new = dict()
        return self.get_clone(node, old_to_new)

# TC - O(V + E)
# SC - O(V)
