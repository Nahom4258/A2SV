class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        minim = inf

        for num in nums:
            while stack and stack[-1][0] <= num:
                stack.pop()

            if stack and stack[-1][1] < num < stack[-1][0]:
                return True

            stack.append((num, minim))
            minim = min(minim, num)

        return False