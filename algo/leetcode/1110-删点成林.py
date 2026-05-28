# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []

        result = []

        def dfs(root):
            if not root:
                return None

            root.left = dfs(root.left)
            root.right = dfs(root.right)

            if self.is_leaf(root) and root.val in to_delete:
                return None

            if root.val in to_delete:
                if root.left:
                    result.append(root.left)
                if root.right:
                    result.append(root.right)
                return None

            return root

        ans = dfs(root)
        if ans:
            result.append(ans)
        return result

    def is_leaf(self, root):
        return root.left is None and root.right is None

