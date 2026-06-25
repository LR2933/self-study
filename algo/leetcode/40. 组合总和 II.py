class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        curr_sum = 0
        nums = defaultdict(int)
        candidates.sort()
        nums = list(Counter(candidates).items())
        n = len(nums)

        def dfs(i, path):
            nonlocal curr_sum

            if curr_sum > target:
                return
            elif curr_sum == target:
                ans.append(path)
                return

            if i == n:
                return

            for t in range(0, nums[i][1] + 1):
                curr_sum += nums[i][0] * t
                dfs(i + 1, path + [nums[i][0]] * t)
                curr_sum -= nums[i][0] * t

        dfs(0, [])

        return ans

