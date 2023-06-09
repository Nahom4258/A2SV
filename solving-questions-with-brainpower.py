class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = dict()

        def dp(index):
            if index >= len(questions):
                return 0

            if index not in memo:
                taken = questions[index][0] + dp(index+questions[index][1]+1)
                not_taken = dp(index+1)

                memo[index] = max(taken, not_taken)

            return memo[index]

        return dp(0)