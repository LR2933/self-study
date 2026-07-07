class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = m * [1]

        for _ in range(1, n):
            for i in range(1,m):
                dp[i] = dp[i - 1] + dp[i]

        return dp[-1]

