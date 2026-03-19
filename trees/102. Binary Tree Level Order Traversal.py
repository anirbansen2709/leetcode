# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Breadth-First Search (BFS): It uses a deque (queue) to process nodes layer by layer, starting from the root.
# Track Levels: The queue stores pairs of (node, current_level) to keep track of the depth of each node.
# Group by Level: As it pops a node, it checks if a sublist for its level exists in the answer array (using len(answer) == level). 
# If not, it creates a new empty sublist. It then appends the node's value to the latest sublist.
# Enqueue Children: It adds the left and right children (if they exist) to the queue, incrementing their level by 1.

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        queue = deque([(root, 0)])
        answer = []
        while queue:
            node, level = queue.popleft()
            if len(answer) == level:
                answer.append([])
            answer[-1].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return answer

# TC - O(n)
# SC - O(logn)
