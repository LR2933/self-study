class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        remain_count = Counter(s)
        stack = []
        in_stack = set()

        for i in s:
            remain_count[i] -= 1

            if i in in_stack:
                continue

            while stack and i < stack[-1] and remain_count[stack[-1]] > 0:
                in_stack.remove(stack.pop())

            stack.append(i)
            in_ans.add(i)

        return ''.join(stack)

