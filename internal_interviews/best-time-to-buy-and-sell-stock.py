class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        future_max = [0] * n
        future_max[n-1] = prices[-1]

        for i in range(n-2, -1, -1):
            future_max[i] = max(future_max[i+1], prices[i])

        return max([future_max[i]-prices[i] for i in range(n)])