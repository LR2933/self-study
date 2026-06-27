class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        @cache
        def dfs(rest):
            if rest == 0:
                return 1
            if rest < 0:
                return 0

            count = 0
            for v in nums:
                count += dfs(rest - v)
            return count

        return dfs(target)
