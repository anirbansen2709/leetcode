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
