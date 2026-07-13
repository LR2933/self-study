class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        m = len(matrix[0])

        last = matrix[0]

        for i in range(1, n):
            curr = matrix[i]
            for j in range(m):
                if j == 0:
                    curr[j] += min(last[j], last[j + 1])
                elif j == m - 1:
                    curr[j] += min(last[j - 1], last[j])
                else:
                    curr[j] += min(last[j - 1], last[j], last[j + 1])
            last = curr

        return min(last)
