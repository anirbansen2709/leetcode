# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def count_nodes(self, node):
        if not node:
            # num_nodes, sum, nodes_below
            return [0, 0, 0]

        left = self.count_nodes(node.left)
        right = self.count_nodes(node.right)

        total = left[1] + right[1] + node.val
        nodes_below = left[2] + right[2] + 1
        num_nodes = left[0] + right[0]
        if total // nodes_below == node.val:
            num_nodes += 1
        return [num_nodes, total, nodes_below] 

    def averageOfSubtree(self, root: TreeNode) -> int:
        return self.count_nodes(root)[0]
