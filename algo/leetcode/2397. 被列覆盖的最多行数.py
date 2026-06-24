class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        n = len(matrix[0])
        mx = 0

        def dfs(i, col):
            nonlocal mx
            if i == n or col == 0:
                c = 0
                for line in matrix:
                    if sum(line) == 0:
                        c += 1
                mx = max(mx, c)
                return

            dfs(i + 1, col)

            backup = []
            for line in matrix:
                backup.append(line[i])
                line[i] = 0
            dfs(i + 1, col - 1)

            backup = iter(backup)
            for line in matrix:
                line[i] = next(backup)

        dfs(0, numSelect)
        return mx

