class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        ans = 0
        for price in prices[1:]:
            min_price = min(min_price, price)
            ans = max(price - min_price, ans)

        return ans
