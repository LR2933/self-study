class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ret = []
        path = []

        def dfs(i:int, start:int):
            if i == n:
                ret.append(path[:])
                return

            if i < n - 1:
                dfs(i + 1, start)

            t = s[start:i + 1]
            if t == t[::-1]:
                path.append(t)
                dfs(i + 1, i + 1)
                path.pop()

        dfs(0, 0)
        return ret
