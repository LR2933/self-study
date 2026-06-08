# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def helper(left, right):
            if not right.left:
                right.left = left
                return
            else:
                helper(left, right.left)

        if not root:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                return None
            elif not root.left or not root.right:
                if root.left:
                    return root.left
                else:
                    return root.right
            else:
                helper(root.left, root.right)
                return root.right

        return root

