# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def f(left, right):
            if left > right:
                return None

            mid = (left + right) // 2

            return TreeNode(nums[mid], f(left, mid - 1), f(mid + 1, right))

        return f(0, len(nums) - 1)
