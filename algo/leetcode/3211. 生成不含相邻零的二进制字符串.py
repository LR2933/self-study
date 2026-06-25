class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []

        def dfs(i, path):
            if i == n:
                ans.append(path)
                return

            if i == 0 or (i > 0 and path[-1] != '0'):
                dfs(i + 1, path + '0')

            dfs(i + 1, path + '1')

        dfs(0, '')

        return ans

