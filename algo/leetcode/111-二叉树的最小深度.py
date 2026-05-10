# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_height = self.minDepth(root.left)
        right_height = self.minDepth(root.right)

        if not root.left:
            return right_height + 1
        if not root.right:
            return left_height + 1

        return min(left_height, right_height) + 1

