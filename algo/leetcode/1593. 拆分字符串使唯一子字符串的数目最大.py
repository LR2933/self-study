class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        count = []
        mx = 0

        def helper(i):
            nonlocal mx
            if i == n:
                mx = max(mx, len(count))
                print(count)
                return

            x = ''
            for j in range(i, n):
                x = s[i:j + 1]
                if x not in count:
                    count.append(x)
                    helper(j + 1)
                    count.pop()

        helper(0)

        return mx
