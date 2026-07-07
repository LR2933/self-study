class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    last = 0
                elif i == 0:
                    last = dp[i][j - 1]
                elif j == 0:
                    last = dp[i - 1][j]
                else:
                    last = min(dp[i - 1][j], dp[i][j - 1])

                dp[i][j] = last + grid[i][j]

        return dp[-1][-1]
