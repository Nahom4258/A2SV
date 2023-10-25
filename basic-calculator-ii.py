class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        s = ''.join([ch for ch in s if ch != ' '])
        # print(s)
        temp = []
        add = []
        for i in range(len(s)):
            if s[i].isdigit():
                add.append(s[i])
            else:
                temp.append(''.join(add))
                temp.append(s[i])
                add = []

        temp.append(''.join(add))

        # print('te: ', temp)
        s = temp

        i = 0
        while i < len(s):
            ch = s[i]
            if ch == ' ':
                i += 1
                continue

            if ch == '*' or ch == '/':
                last_val = stack.pop()
                next_val = s[i+1]
                ans = 0
                if ch == '*':
                    ans = int(last_val) * int(next_val)
                else:
                    ans = int(last_val) // int(next_val)

                stack.append(ans)
                i += 2
            else:
                stack.append(ch)
                i += 1

        ans = 0
        op = '+'
        for ch in stack:
            ch = str(ch)
            if ch.isdigit():
                if op == '+':
                    ans += int(ch)
                else:
                    ans -= int(ch)
            else:
                op = ch

        # print('ans: ', stack, ans)

        return ans