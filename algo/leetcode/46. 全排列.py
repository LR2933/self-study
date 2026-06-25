class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path = [0] * n
        flag = [False] * n
        ans = []

        def helper(i):
            if i == n:
                ans.append(path[:])
                return

            for j in range(n):
                if not flag[j]:
                    path[i] = nums[j]
                    flag[j] = True
                    helper(i + 1)
                    flag[j] = False

        helper(0)
        return ans
