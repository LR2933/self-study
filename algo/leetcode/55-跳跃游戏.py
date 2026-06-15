class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        target = len(nums) - 1

        for i, step in enumerate(nums):
            if i > max_reach:
                return False

            max_reach = max(max_reach, i + step)

            if max_reach >= target:
                return True
