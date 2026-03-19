# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# Depth-First Search (DFS)
# Initialization (cloneGraph): It first checks for the edge case of an empty graph. If the input node is None, it returns None. 
# Otherwise, it initializes an empty dictionary called old_to_new to keep track of the original nodes and their corresponding new clones.
# Then, it triggers the DFS traversal.
# DFS Traversal (get_clone): This helper function takes the current node and the old_to_new dictionary.
# Checking for Existing Clones: It first checks if the current node is already in old_to_new.
# If it is (the else block), it means this node has already been cloned during the traversal (which happens when there are cycles in the
# graph). It simply returns the existing clone to prevent an infinite loop.
# Creating a New Clone: If the node is not in old_to_new, it has not been visited yet:
# It creates a new clone node with the same value as the original.
# Crucial Step: It immediately adds the mapping old_to_new[node] = clone before exploring neighbors. This ensures that if a cycle leads
# back to this node while its neighbors are still being processed, the algorithm will recognize it has already been visited.
# Cloning Neighbors: It iterates through all the neighbors of the original node. For each neighbor, it recursively calls get_clone 
# to get the cloned version of that neighbor, and appends it to the clone.neighbors list.
# Return: Finally, it returns the fully constructed clone node.

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
