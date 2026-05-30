# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        self.ans = []
        self.sum = 0
        self.path = []

        def dfs(node):
            self.sum += node.val
            self.path.append(node.val)
            if not node.left and not node.right:
                if self.sum == targetSum:
                    self.ans.append(self.path[:])

            if node.left:
                dfs(node.left)

            if node.right:
                dfs(node.right)

            self.sum -= node.val
            self.path.pop()

        dfs(root)
        return self.ans

