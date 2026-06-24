class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def helper(i, path):
            if len(path) == k:
                ans.append(path[:])
                return
            if i > n:
                return

            helper(i + 1, path)
            path.append(i)
            helper(i + 1, path)
            path.pop()

        helper(1, [])
        return ans
