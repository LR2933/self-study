class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 1_000_000_007
        dp = [0] * (high + 1)
        dp[0] = 1

        for i in range(1, high + 1):
            if zero <= i:
                dp[i] = dp[i - zero]
            if one <= i:
                dp[i] = (dp[i] + dp[i - one]) % MOD

        return sum(dp[low:]) % MOD
