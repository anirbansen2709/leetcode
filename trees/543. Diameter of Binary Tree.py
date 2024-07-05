# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, diam):
        if not node:
            return 0
        left = self.traverse(node.left, diam)
        right = self.traverse(node.right, diam)
        temp = max(left, right)
        diam[0] = max(diam[0], temp, left + right + 1)
        return 1 + temp

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam = [0]
        self.traverse(root, diam)
        return diam[0] - 1


# TC - O(n)
# SC - O(logn)
