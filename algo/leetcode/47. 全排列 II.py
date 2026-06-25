class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        path = [0] * n
        used = [0] * n
        ans = []

        def helper(i):
            if i == n:
                ans.append(path[:])
                return

            for j in range(n):
                if used[j] == 1:
                    continue

                if j > 0 and nums[j] == nums[j - 1] and used[j - 1] == 0:
                    continue

                path[i] = nums[j]
                used[j] = 1
                helper(i + 1)
                used[j] = 0

        helper(0)

        return ans

