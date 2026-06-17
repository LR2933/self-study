class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        ret = 0

        def dfs(i, count):
            nonlocal ret
            if i == n:
                ret += count
                return

            dfs(i + 1, count)
            dfs(i + 1, count ^ nums[i])

        dfs(0, 0)
        return ret
