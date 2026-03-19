# Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys strictly less than the node's key.
# The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Instead of just checking immediate children, the algorithm passes down a valid range (min, max) to ensure every node is correctly 
# positioned relative to all its ancestors.
# Start: The root node can be any value: (-∞, ∞).
# Validate: If a node's value falls outside its allowed (min, max) range, the tree is invalid (return False).
# Branch Left: All left descendants must be strictly smaller than the current node. The max boundary updates to the current node's 
# value.
# Branch Right: All right descendants must be strictly larger than the current node. The min boundary updates to the current node's 
# value.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def validate(self, node, left, right):
        if not node:
            return True
        if node.val <= left or node.val >= right:
            return False
        left = self.validate(node.left, left, node.val)
        right = self.validate(node.right, node.val, right)
        return left and right

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, float('-inf'), float('inf'))

# TC - O(n)
# SC - O(logn)
