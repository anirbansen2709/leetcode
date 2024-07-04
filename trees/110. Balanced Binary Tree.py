# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node):
        if not node:
            return [0, True]
        left = self.traverse(node.left)
        right = self.traverse(node.right)
        balanced = left[1] and right[1] and abs(left[0] - right[0]) <= 1
        depth = 1 + max(left[0], right[0])
        return [depth, balanced]

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.traverse(root)[1]

# TC - O(n)
# SC - O(logn)
