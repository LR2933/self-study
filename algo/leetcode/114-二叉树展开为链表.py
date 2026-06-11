# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, left, right):
        if not left or not right:
            return

        if left.right:
            self.helper(left.right, right)
        else:
            left.right = right


    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        if root.left:
            self.helper(root.left, root.right)
            root.right = root.left
            root.left = None

        self.flatten(root.right)


