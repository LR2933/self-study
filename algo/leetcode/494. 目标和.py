class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def dfs(i, t):
            if i == n:
                return 1 if t == 0 else 0

            return dfs(i + 1, t + nums[i]) + dfs(i + 1, t - nums[i])

        return 0 if sum(nums) < abs(target) else dfs(0, target)
