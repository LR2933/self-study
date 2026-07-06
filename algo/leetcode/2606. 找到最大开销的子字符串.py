class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        dic = {v:i for i, v in enumerate(chars)}
        n = len(s)
        ans = 0
        last = 0

        for i in range(n):
            val = vals[dic[s[i]]] if s[i] in chars else (ord(s[i]) - ord('a') + 1)
            last = max(last, 0) + val
            ans = max(ans, last)

        return ans
