class Solution:
    def rob(self, nums: List[int]) -> int:
        p1, p2 = 0, 0

        for num in nums:
            curr = max(num + p1, p2)
            p1, p2 = p2, curr

        return p2
