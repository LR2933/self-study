class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        n = len(nums)
        t = s - abs(target)
        if t < 0 or t % 2 == 1:
            return  0
        t //= 2
        f = [[0] * (t + 1) for _ in range(n + 1)]
        f[0][0] = 1

        for i, x in enumerate(nums):
            for j in range(t + 1):
                if j < x:
                    f[i + 1][j] = f[i][j]
                else:
                    f[i + 1][j] = f[i][j] + f[i][j - x]

        return f[-1][-1]
