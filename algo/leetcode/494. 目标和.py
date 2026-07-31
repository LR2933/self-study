class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        n = len(nums)
        of = s
        f = [[0] * (s * 2 + 1) for _ in range(n)]
        f[0][nums[0] + of] += 1
        f[0][-nums[0] + of] += 1

        j_max = s * 2 + 1
        for i in range(n - 1):
            for j in range(j_max):
                if j - nums[i + 1] >= 0:
                    f[i + 1][j - nums[i + 1]] += f[i][j]
                if j + nums[i + 1] < j_max:
                    f[i + 1][j + nums[i + 1]] += f[i][j]

        return 0 if s < abs(target) else f[-1][target + of]
