class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        path = []
        ret = []
        def helper(i):
            if i == n:
                ret.append(''.join(path))
                return

            if '0' <= s[i] <= '9':
                path.append(s[i])
                helper(i + 1)
                path.pop()
                return

            path.append(s[i].upper())
            helper(i + 1)
            path.pop()

            path.append(s[i].lower())
            helper(i + 1)
            path.pop()

        helper(0)
        return ret

