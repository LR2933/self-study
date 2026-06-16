class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def get_area(row, col):
            if not (0 <= row < m and 0 <= col < n) or grid[row][col] == 0 or visited[row][col]:
                return 0

            visited[row][col] = True

            total = grid[row][col]
            for dx, dy in direction:
                total += get_area(row + dx, col + dy)

            return total

        count = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] != 0 and not visited[row][col]:
                    if get_area(row, col) % k == 0:
                        count += 1

        return count

