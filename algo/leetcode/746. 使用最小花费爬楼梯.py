class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cost.append(0)
        memo = {}

        def dfs(i):
            if i == 0:
                return cost[0]
            elif i == 1:
                return cost[1]

            if i in memo:
                return memo[i]
            else:
                memo[i] = cost[i] + min(dfs(i - 1), dfs(i - 2))
                return memo[i]

        return dfs(n)
