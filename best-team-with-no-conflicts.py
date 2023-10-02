class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        players = [[scores[i], ages[i]] for i in range(n)]
        players.sort()
        
        dp = [players[i][0] for i in range(n)]

        for i in range(n):
            min_score, min_age = players[i]
            for j in range(i):
                curr_score, curr_age = players[j]
                if min_age >= curr_age:
                    dp[i] = max(min_score+dp[j], dp[i])

        return max(dp)