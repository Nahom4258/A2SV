class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss = defaultdict(int)

        for winner, loser in matches:
            loss[loser] += 1

        ans = [set(), set()]
        
        for winner, loser in matches:
            if loss[winner] == 0:
                ans[0].add(winner)
            elif loss[winner] == 1:
                ans[1].add(winner)

            if loss[loser] == 0:
                ans[0].add(loser)
            elif loss[loser] == 1:
                ans[1].add(loser)

        ans[0] = sorted(ans[0])
        ans[1] = sorted(ans[1])

        return ans