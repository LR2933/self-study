# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        count = 0
        memo = [0] * 10

        def dfs(node):
            nonlocal count
            memo[node.val] ^= 1

            if not node.left and not node.right:
                if sum(memo) <= 1:
                    count += 1

            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            
            memo[node.val] ^= 1
        
        dfs(root)
        return count
