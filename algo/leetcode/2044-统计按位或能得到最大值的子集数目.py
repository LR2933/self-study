class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        mx = 0
        count = 0 

        def dfs(i, c):
            nonlocal mx, count
            if i == n:
                if c == mx:
                    count += 1
                elif c > mx:
                    mx = c
                    count = 1
                return

            dfs(i + 1, c | nums[i])
            dfs(i + 1, c)

        dfs(0, 0)

        return count

