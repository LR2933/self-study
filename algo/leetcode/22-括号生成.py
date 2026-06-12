class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []

        def helper(current_s, left, right):
            if left == right == 0:
                ret.append(current_s)
                return

            if left > 0:
                helper(current_s + "(", left - 1, right)

            if right > left:
                helper(current_s + ")", left, right - 1)

        helper("", n, n)
        return ret

