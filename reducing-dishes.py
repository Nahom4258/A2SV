class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        maxim = -inf

        satisfaction.sort()

        for i in range(len(satisfaction)):
            sum = 0
            count = 1
            for j in range(i, len(satisfaction)):
                sum += (count * satisfaction[j])
                count += 1

            maxim = max(maxim, sum)

        # print('ans; ', maxim)

        return 0 if maxim < 0 else maxim