class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle[-1].copy()

        for i in range(n - 2, -1, -1):
            for k in range(len(triangle[i])):
                dp[k] = min(dp[k + 1], dp[k]) + triangle[i][k]

        return dp[0]
