class StockSpanner:

    def __init__(self):
        self.monotonic = [(float('inf'), 0)]

    def next(self, price: int) -> int:
        today = self.monotonic[-1]
        
        while self.monotonic and price >= self.monotonic[-1][0]:
            self.monotonic.pop()

        ans = today[1] - self.monotonic[-1][1] + 1

        self.monotonic.append((price, today[1]+1))

        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)