class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        reached = [[False] * m for _ in range(n)]
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ans = 0
        val = 0

        def dfs(i, j):
            nonlocal ans, val
            if not (0 <= i < n) or not (0 <= j < m) or reached[i][j] == True or grid[i][j] == 0:
                ans = max(val, ans)
                return

            reached[i][j] = True
            val += grid[i][j]

            for dx, dy in direction:
                dfs(i + dx, j + dy)

            reached[i][j] = False
            val -= grid[i][j]

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    dfs(i, j)

        return ans

