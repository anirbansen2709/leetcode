from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_width = 0
        queue = deque([(root, 0)])
        while queue:
            length = len(queue)
            min_val = queue[0][1]
            for idx in range(length):
                node, val = queue.popleft()
                val = val - min_val
                if idx == 0:
                    min_idx = val
                if idx == length - 1:
                    max_idx = val
                max_width = max(max_width, max_idx - min_idx + 1)
                if node.left:
                    queue.append((node.left, 2 * val + 1))
                if node.right:
                    queue.append((node.right, 2 * val + 2))
        return max_width
