# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        curr = root
        per = None

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack[-1]
            if not curr.right or curr.right == per:
                result.append(stack.pop().val)
                per = curr
            else:
                curr = curr.right
                stack.append(curr)

        return result

