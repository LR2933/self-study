class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        mid = sum(nums) // 2

        def dfs(i, left, right):
            if i == n:
                return True

            if left > mid or right > mid:
                return False

            return dfs(i + 1, left + nums[i], right) or dfs(i + 1, left,  right + nums[i])

        return dfs(0, 0, 0)
