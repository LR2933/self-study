class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        dp = m * [0]
        for i in range(m):
            if obstacleGrid[0][i] == 1:
                break
            else:
                dp[i] = 1

        for i in range(1, n):
            for j in range(0, m):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] = dp[j] + dp[j - 1]

        return dp[-1]

