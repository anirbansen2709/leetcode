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
        if (not p and q) or (p and not q) or (p.val != q.val):
            return False
        
        left = self.traverse(p.left, q.left)
        right = self.traverse(p.right, q.right)

        return left and right

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.traverse(p, q)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if self.isSameTree(node, subRoot):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return False

# TC - O(n)
# SC - O(logm)
