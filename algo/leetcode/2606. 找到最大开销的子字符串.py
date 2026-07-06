class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        cost_map = {c:i + 1 for i, c in enumerate(alphabet)}

        for i, c in zip(chars, vals):
            cost_map[i] = c

        ans = 0
        last = 0

        for char in s:
            last = max(last, 0) + cost_map[char]
            ans = max(ans, last)

        return ans
