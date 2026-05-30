# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.ans = []

        def dfs(node, path: str):
            path += str(node.val)

            if not node.left and not node.right:
                self.ans.append(path)
                return

            if node.left:
                dfs(node.left, path + "->")

            if node.right:
                dfs(node.right, path + "->")

        dfs(root, "")
        return self.ans

