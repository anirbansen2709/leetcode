# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build_tree(self, preorder, pre_start, pre_end, inorder, in_start, in_end, inorder_map):
        if pre_start > pre_end or in_start > in_end:
            return None
        root_val = preorder[pre_start]
        root = TreeNode(root_val)
        in_index = inorder_map[root_val]
        left = in_index - in_start
        root.left = self.build_tree(preorder, pre_start + 1, pre_start + left, inorder, in_start, in_index - 1, inorder_map)
        root.right = self.build_tree(preorder, pre_start + left + 1, pre_end, inorder, in_index + 1, in_end, inorder_map)
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = dict()
        length = len(preorder)
        for idx, val in enumerate(inorder):
            inorder_map[val] = idx
        return self.build_tree(preorder, 0, length - 1, inorder, 0, length - 1, inorder_map)

# TC - O(n)
# SC - O(n)
