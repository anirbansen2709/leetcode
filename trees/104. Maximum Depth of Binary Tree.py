# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Base Case: If the node is empty, return 0.
# Explore: Recursively calculate the maximum depth of the left and right subtrees.
# Calculate: Return 1 (to count the current node) plus the greater of the two subtree depths.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node):
        if not node:
            return 0
        left = self.traverse(node.left)
        right = self.traverse(node.right)
        return 1 + max(left, right)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root)

# TC - O(n)
# SC - Worst case - O(n) Best Case - O(logn)
