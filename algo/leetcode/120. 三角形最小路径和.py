class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        m = len(triangle[-1])
        old = [0] * m

        for i in range(n):
            k = len(triangle[i])
            new = old.copy()
            for j in range(k):
                if j == 0:
                    new[j] = old[j]
                elif j == k - 1:
                    new[j] = old[j - 1]
                else:
                    new[j] = min(old[j], old[j - 1])
                
                new[j] += triangle[i][j] 

            old = new.copy()

        return min(old)

