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
