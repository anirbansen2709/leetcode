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
