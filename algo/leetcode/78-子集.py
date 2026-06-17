class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        current = []
        n = len(nums)

        def dfs(i):
            if i == n:
                ret.append(current[:])
                return

            current.append(nums[i])
            dfs(i + 1)
            current.pop()
            dfs(i + 1)

        dfs(0)
        return ret
