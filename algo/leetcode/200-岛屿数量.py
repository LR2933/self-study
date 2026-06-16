class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            if not (0 <= r < row and 0 <= c < col) or grid[r][c] == "0":
                return 
            grid[r][c] = "0"
            for dx, dy in direction:
                dfs(r + dx, c + dy)

        row = len(grid)
        col = len(grid[0])

        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1

        return count

