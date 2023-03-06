class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        for i in range(len(position)):
            position[i] = (position[i], speed[i])

        position.sort(key=lambda x: x[0])

        for i in range(len(position)):
            while stack and (target - position[i][0]) / position[i][1] >= (target - stack[-1][0]) / stack[-1][1]:
                stack.pop()
            stack.append(position[i])

        print('ans: ', position)

        return len(stack)