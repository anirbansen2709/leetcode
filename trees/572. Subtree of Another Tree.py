# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Level-by-Level Search (isSubtree): It uses a queue (Breadth-First Search) to traverse the main root tree, visiting every node one by
# one.
# Identical Tree Check (traverse): For every node it visits, it calls a helper function to recursively check if the tree starting at 
# that node is exactly identical (both in structure and values) to the subRoot.
# Conclusion: If a perfect match is found at any node, it immediately returns True. If it searches the entire root tree and finds no 
# match, it returns False.

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, p, q):
        if not p and not q:
            return True
        if (p and not q) or (q and not p) or (p.val != q.val):
            return False
        left = self.traverse(p.left, q.left)
        right = self.traverse(p.right, q.right)
        return left and right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if self.traverse(node, subRoot):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

# TC - O(nxm)
# SC - O(n+m)
