class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        costs.sort(key=lambda x: x[0]-x[1])

        ans = 0
        for i in range(n//2):
            a, b = costs[i]
            ans += a
        for i in range(n//2, n):
            a, b = costs[i]
            ans += b

        return ans