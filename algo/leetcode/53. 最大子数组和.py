class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        p1 = 0
        ans = -float('inf')

        for i in range(n):
            p1 = max(p1, 0) + nums[i]
            ans = max(ans, p1)

        return ans
