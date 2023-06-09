class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = dict()
        visited = set()
        ans = 0

        def dp(index):
            if index >= len(questions):
                return 0
            
            visited.add(index)

            if index not in memo:
                maxim = 0
                # for i in range(index+questions[index][1]+1, len(questions)):
                #     maxim = max(maxim, dp(i))
                taken = questions[index][0] + dp(index+questions[index][1]+1)
                not_taken = dp(index+1)

                memo[index] = max(taken, not_taken)
                nonlocal ans
                ans = max(memo[index], ans)

            return memo[index]

        # ans = 0
        # for i in range(len(questions)):
        #     if i not in visited:
        #         ans = max(ans, dp(i))
        dp(0)
        return ans