# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        self.inserted = False

        def f(node):
            if self.inserted or not node:
                return None

            if node.val > val and not node.left:
                node.left = TreeNode(val)
                self.inserted = True
            elif node.val < val and not node.right:
                node.right = TreeNode(val)
                self.inserted = True
            else:
                f(node.left) if node.val > val else f(node.right)

        f(root)
        return root

