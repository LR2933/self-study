# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        max_deepth = -1
        ans = None

        def dfs(node, deepth):
            nonlocal max_deepth, ans

            if not node:
                max_deepth = max(deepth, max_deepth)
                return deepth

            left = dfs(node.left, deepth + 1)
            right = dfs(node.right, deepth + 1)

            if left == right == max_deepth:
                ans = node

            return max(left, right)

        dfs(root, 1)

        return ans
