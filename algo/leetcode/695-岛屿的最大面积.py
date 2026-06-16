class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(row, col) -> int:
            if not (0 <= row < m and 0 <= col < n) or grid[row][col] == 0:
                return 0

            grid[row][col] = 0

            return 1 + sum(dfs(row + dx, col + dy) for dx, dy in direction)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i, j))

        return ans

