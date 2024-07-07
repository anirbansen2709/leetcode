from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([[root, 0]])
        answer = []
        while queue:
            node, level = queue.popleft()
            if level == len(answer):
                answer.append(node.val)
            if node.right:
                queue.append([node.right, level + 1])
            if node.left:
                queue.append([node.left, level + 1])
        return answer  

# TC - O(n)
# SC - O(n)
