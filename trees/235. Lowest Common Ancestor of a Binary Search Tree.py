# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node
# in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Logic
# Leverage BST Properties: In a BST, all left descendants are smaller than the current node, and all right descendants are larger.
# Go Left: If both p and q are smaller than the current node, the LCA must be in the left subtree.
# Go Right: If both p and q are larger than the current node, the LCA must be in the right subtree.
# Found It: The moment p and q "split" paths (one is smaller, one is larger) or one of them equals the current node, 
# that current node is your Lowest Common Ancestor.

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

# TC - Best case O(logn) Worst case - O(n)
# SC - Best case O(logn) Worst case - O(n)
