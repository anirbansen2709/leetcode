# Question - Given the root of a binary tree, invert the tree, and return its root.

# Logic - 
# The code uses a recursive Depth-First Search (DFS) approach, implemented in the traverse method.
# Base Case: If the current node is None (empty subtree), return None.
# Recursive Step:
# Recursively call traverse on the left child (node.left).
# Recursively call traverse on the right child (node.right).
# Swap: After the recursive calls return (meaning both left and right subtrees are inverted), swap the node.left 
# and node.right children of the current node.
# Return: Return the current node.
# The invertTree method simply initiates the process by calling traverse on the root of the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node):
        if not node:
            return None
        left = self.traverse(node.left)
        right = self.traverse(node.right)
        node.left = right
        node.right = left
        return node

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.traverse(root)

# TC - O(n)
# SC - O(logn)
