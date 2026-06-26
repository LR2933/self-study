class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0, 0]

        for i in range(2, n + 1):
            curr = min(dp[0] + cost[i - 2], dp[1] + cost[i - 1])
            dp[0], dp[1] = dp[1], curr

        return dp[-1]
