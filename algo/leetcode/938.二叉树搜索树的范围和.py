# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans = 0

        def dfs(node):
            if node is None:
                return

            if node.val > low:
                dfs(node.left)

            if low <= node.val <= high:
                self.ans += node.val

            if node.val < high:
                dfs(node.right)

        dfs(root)
        return self.ans
