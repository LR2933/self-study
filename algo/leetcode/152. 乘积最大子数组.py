class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        f_min = f_max = 1
        ans = -float('inf')

        for n in nums:
            if n > 0:
                f_max, f_min = max(f_max * n, n), min(f_min * n, n)
            else:
                f_max, f_min = max(f_min * n, n), min(f_max * n, n)

            ans = max(ans, f_max)

        return ans
