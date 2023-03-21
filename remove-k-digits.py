class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # num = list(map(int, list(num)))
        counter = 0
        stack = []

        for i in range(len(num)):
            curr = num[i]

            while stack and int(stack[-1]) > int(curr) and counter < k:
                counter += 1
                stack.pop()

            stack.append(curr)

        while stack and counter < k:
            stack.pop()
            counter += 1

        return str(int(''.join(stack))) if stack else '0'