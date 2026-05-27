# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        if root == None:
            return ""

        if self.is_leaf(root):
            return str(root.val)

        left = self.tree2str(root.left)
        right = self.tree2str(root.right)

        if root.right is None:
            return f"{root.val}({left})"
        else:
            return f"{root.val}({left})({right})"

    def is_leaf(self, root):
        return root.left is None and root.right is None

