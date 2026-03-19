# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that
# the path does not need to pass through the root. The path sum of a path is the sum of the node's values in the path. Given the root of a binary tree, return the maximum path sum of any 
# non-empty path.

# Global Maximum Tracker: A mutable list max_sum = [float('-inf')] is used to keep track of the absolute maximum path sum found 
# anywhere in the tree. Using a list allows the helper function to update it by reference.
# Post-Order Traversal: The traverse function recursively calls itself on the left and right children first,
# meaning it processes the tree from the bottom up.
# Calculating temp (Single Branch Path): For any given node, the maximum path continuing upwards to its parent can only include the 
# node itself, or the node plus its most profitable child branch. temp = max(node.val, node.val + max(left, right)) calculates exactly 
# this. It inherently decides whether to include a subtree or abandon it (if both subtrees are highly negative, it just takes node.val).
# Checking the "Inverted V" Path: While temp is returned to the parent, the actual overall maximum path might peak at the current node
# and include both the left and right children. max_sum[0] is updated by comparing its current highest value against temp (a straight
# path) and left + right + node.val (a path that bridges across the left and right subtrees through the current node).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, max_sum):
        if not node:
            return 0
        left = self.traverse(node.left, max_sum)
        right = self.traverse(node.right, max_sum)
        temp = max(node.val, node.val + max(left, right))
        max_sum[0] = max(max_sum[0], temp, left + right + node.val)
        return temp

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [float('-inf')]
        self.traverse(root, max_sum)
        return max_sum[0]
        
# TC - O(N)
# SC - O(N)
