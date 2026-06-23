class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        total_product = math.prod(nums)
        current = 1
        ret = False

        if target * target != total_product:
            return False

        def dfs(i):
            nonlocal ret
            nonlocal current

            if i == n:
                if current == target and total_product // current == target:
                    ret = True
                return 

            if current > target:
                return

            current *= nums[i]
            dfs(i + 1)
            current //= nums[i]
            dfs(i + 1)

        dfs(0)
        return ret
