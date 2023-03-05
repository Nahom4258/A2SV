class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            elif stack[-1] == '(':
                stack.pop()
                stack.append(1)
            else:
                curr = 0
                while stack[-1] != '(':
                    curr += stack.pop()

                stack.pop()
                stack.append(2 * curr)

        return sum(stack)