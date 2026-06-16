class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        data = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        n = len(digits)
        ans = []

        def dfs(i, s):
            if i >= n:
                ans.append(s)
                return 

            for d in data[digits[i]]:
                dfs(i + 1, s + d)

        dfs(0, "")
        return ans
