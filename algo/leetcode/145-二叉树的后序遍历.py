# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        self.ans = []
        def dfs(r):
            if r.left:
                dfs(r.left)
            if r.right:
                dfs(r.right)
            self.ans.append(r.val)

        dfs(root)
        return self.ans

