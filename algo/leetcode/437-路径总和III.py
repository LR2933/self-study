# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0

        def dfs(node):
            if not node:
                return

            helper(node, 0)
            dfs(node.left)
            dfs(node.right)

        def helper(node, total):
            nonlocal count
            if not node:
                return
            total += node.val
            if total == targetSum:
                count += 1
            helper(node.left, total)
            helper(node.right, total)

        dfs(root)
        return count
