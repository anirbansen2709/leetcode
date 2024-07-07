# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, value, answer):
        if not node:
            return 
        if not node.left and not node.right:
            answer[0] += value
            return
        if node.left:
            self.traverse(node.left, value * 10 + node.left.val, answer)
        if node.right:
            self.traverse(node.right, value * 10 + node.right.val, answer)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        answer = [0]
        self.traverse(root, root.val, answer)
        return answer[0]

# TC - O(n)
# SC - O(logn)
