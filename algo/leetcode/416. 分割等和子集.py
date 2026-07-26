class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def dfs(i, rest):
            if i < 0:
                return rest == 0

            if rest < nums[i]:
                return dfs(i - 1, rest)

            return dfs(i - 1, rest - nums[i]) or dfs(i - 1, rest)

        s = sum(nums)
        return s % 2 == 0 and dfs(len(nums) - 1, s // 2)

