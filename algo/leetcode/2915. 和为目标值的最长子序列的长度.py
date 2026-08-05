class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def dfs(i, t):
            if i == n:
                if t == 0:
                    return 0
                else:
                    return -float("inf")

            return max(1 + dfs(i + 1, t - nums[i]), dfs(i + 1, t))
        
        ret = dfs(0, target)
        return -1 if ret == -float("inf") else ret

