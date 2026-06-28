class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper( nums: List[int]) -> int:
            p1, p2 = 0, 0

            for num in nums:
                curr = max(num + p1, p2)
                p1, p2 = p2, curr

            return p2
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[1:]), helper(nums[:-1]))
