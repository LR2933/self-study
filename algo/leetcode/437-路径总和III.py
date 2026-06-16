# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        memo = defaultdict(int)
        memo[0] = 1
        count = 0
        def dfs(node, total):
            nonlocal count
            if not node:
                return

            total += node.val

            target = total - targetSum
            if target in memo:
                count += memo[target]

            memo[total] += 1

            dfs(node.left, total)
            dfs(node.right, total)

            memo[total] -= 1

        dfs(root, 0)
        return count

