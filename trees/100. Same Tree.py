# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# The solution uses a recursive Depth-First Search (DFS) to traverse and compare both trees simultaneously.
# Here is the step-by-step logic:
# Check for End of Tree (Match): If both current nodes (p and q) are null, it means we've reached the end of the branches successfully. 
# Return True.
# Check for Mismatch: If one node is null but the other isn't, or if their values (p.val and q.val) are different, 
# the trees are not identical. Return False.
# Recursive Traversal: Recursively call the function to compare the left children of both nodes, and then the right children.
# Final Result: Return True only if both the left and right recursive checks return True.

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

# TC - O(n)
# SC - Best Case O(logn) Worst case O(n)
