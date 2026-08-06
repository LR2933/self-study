class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        if sum(nums) < target:
            return -1
        n = len(nums)
        f = [[-float("inf")] * (target + 1) for _ in range(n + 1)]
        f[0][0] = 0

        for i, x in enumerate(nums):
            for j in range(target + 1):
                if x > j:
                    f[i + 1][j] = f[i][j]
                else:
                    f[i + 1][j] = max(f[i][j - x] + 1, f[i][j])

        return f[-1][-1] if f[-1][-1] != -float("inf") else - 1
