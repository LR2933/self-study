class Solution:
    def perfectMenu(self, materials: List[int], cookbooks: List[List[int]], attribute: List[List[int]], limit: int) -> int:
        n = len(cookbooks)
        mx = -1

        def dfs(i, x, y):
            nonlocal mx, materials
            if i == n:
                if y >= limit:
                    mx = max(x, mx)
                return

            # 不制作第i份料理
            dfs(i + 1, x ,y)

            temp = materials[:] # 备份材料以便待会回溯

            # 制作i份料理
            for j in range(5):
                materials[j] -= cookbooks[i][j]
                if materials[j] < 0:
                    materials = temp
                    return

            dfs(i + 1, x + attribute[i][0], y + attribute[i][1])

            materials = temp

        dfs(0, 0, 0)

        return mx


