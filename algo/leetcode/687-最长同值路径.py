# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node) -> int:
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.right and node.val == node.left.val == node.right.val:
                self.ans = max(self.ans, left + right)
                return max(left, right) + 1

            if node.left and node.val == node.left.val:
                self.ans = max(self.ans, left)
                return left + 1

            if node.right and node.val == node.right.val:
                self.ans = max(self.ans, right)
                return right + 1

            return 1

        dfs(root)
        return self.ans

