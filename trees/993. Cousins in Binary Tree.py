from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        depth = None
        parent = None
        queue = deque([[root, 0, -1]])
        while queue:
            node, node_depth, node_parent = queue.popleft()
            if (node.val == x) or (node.val == y):
                if depth == None:
                    depth = node_depth
                    parent = node_parent
                else:
                    if depth == node_depth and parent != node_parent:
                        return True
                    else:
                        return False
            if node.left:
                queue.append([node.left, node_depth + 1, node])
            if node.right:
                queue.append([node.right, node_depth + 1, node])
        return False
      
# TC - O(n)
# SC - O(n)
