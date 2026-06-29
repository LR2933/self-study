class Solution:
    def countHousePlacements(self, n: int) -> int:
        p2, p1 = 1, 1
        MOD = 10 ** 9 + 7

        for _ in range(n):
            curr = p2 + p1
            p2, p1 = p1, curr

        return pow(p1, 2, MOD)
