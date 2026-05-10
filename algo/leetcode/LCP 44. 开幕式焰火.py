# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def numColor(self, root: TreeNode) -> int:
        s = set()
        stack = [root]
        while stack:
            curr = stack.pop()
            s.add(curr.val)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return len(s)

