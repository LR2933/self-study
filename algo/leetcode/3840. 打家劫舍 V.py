class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        n = len(nums)
        p2, p1 = 0, nums[0]

        for i in range(1, n):
            if colors[i] == colors[i - 1]:
                p2, p1 = p1, max(p1, p2 + nums[i])
            else:
                p2, p1 = p1, p1 + nums[i]

        return p1

