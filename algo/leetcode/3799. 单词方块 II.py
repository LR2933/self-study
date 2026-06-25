class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        n = len(words)
        ans = []
        path = [""] * 4
        flag = [False] * n

        def dfs(i):
            if i == 4:
                ans.append(path[:])
                return

            for j, k in enumerate(flag):
                if not k:
                    path[i] = words[j]
                    if i == 1 and path[1][0] != path[0][0]:
                        continue
                    elif i == 2 and path[2][0] != path[0][3]:
                        continue
                    elif i == 3 and (path[3][0] != path[1][3] or path[3][3] != path[2][3]):
                         continue

                    flag[j] = True
                    dfs(i + 1)
                    flag[j] = False

        dfs(0)
        ans.sort()
        return ans
