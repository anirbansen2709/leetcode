# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverse(self, node, p, q):
        if not node:
            return None
        if p.val < node.val and q.val < node.val:
            return self.traverse(node.left, p, q)
        elif p.val > node.val and q.val > node.val:
            return self.traverse(node.right, p, q)
        else:
            return node

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.traverse(root, p, q)

# TC - O(logn)
# SC - O(logn)
