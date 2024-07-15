# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_height(self, node):
        if not node:
            return 0
        left = self.get_height(node.left)
        right = self.get_height(node.right)
        return 1 + max(left, right)

    def print_tree(self, node, tree, row, start, end):
        if row == self.rows:
            return
        mid = (start + end) // 2
        tree[row][mid] = str(node.val)
        if node.left:
            self.print_tree(node.left, tree, row + 1, start, mid - 1)
        if node.right:
            self.print_tree(node.right, tree, row + 1, mid + 1, end)

    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        self.rows = self.get_height(root)
        self.cols = (2 ** self.rows) - 1
        tree = [["" for _ in range(self.cols)] for _ in range(self.rows)]
        self.print_tree(root, tree, 0, 0, self.cols - 1)
        return tree
