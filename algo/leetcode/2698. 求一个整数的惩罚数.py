def helper(num):
    s = str(num * num)
    n = len(s)

    def dfs(i, curr_sum):
        if i == n:
            return curr_sum == num

        x = 0
        for j in range(i, n):
            x = x * 10 + int(s[j])
            if dfs(j + 1, curr_sum + x):
                return True
        return False

    return dfs(0, 0)

pre = [0] * 1001
for i in range(1, 1001):
    if helper(i):
        pre[i] = pre[i - 1] + i * i
    else:
        pre[i] = pre[i - 1]

class Solution:

    def punishmentNumber(self, n: int) -> int:
        return pre[n]
